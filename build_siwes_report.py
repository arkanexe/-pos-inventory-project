from __future__ import annotations

import html
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.table import WD_ROW_HEIGHT_RULE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "INDUSTRIAL_TRAINING_TECHNICAL_REPORT.md"
DOCX = ROOT / "INDUSTRIAL_TRAINING_TECHNICAL_REPORT.docx"
PDF = ROOT / "INDUSTRIAL_TRAINING_TECHNICAL_REPORT.pdf"


def plain(value: str) -> str:
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"\\text\{([^}]+)\}", r"\1", value)
    value = value.replace("\\phi", "φ").replace("\\ge", "≥").replace("\\le", "≤")
    value = value.replace("\\approx", "≈").replace("\\pm", "±").replace("\\times", "×")
    value = value.replace("\\cdot", "·").replace("\\mu", "μ").replace("\\Omega", "Ω")
    value = re.sub(r"\*\*|`|\$", "", value)
    # clean any non-printable ASCII
    cleaned = []
    for c in value:
        if ord(c) < 32 and c not in "\t\n\r":
            cleaned.append(" ")
        else:
            cleaned.append(c)
    return "".join(cleaned).strip()


def figure_from_fence(lines: list[str]):
    caption = None
    description = []
    reading_description = False
    for line in lines:
        content = re.sub(r"^\|\s*|\s*\|$", "", line).strip()
        if not content or content.startswith("+---") or "SPACE RESERVED" in content:
            continue
        match = re.search(r"Figure\s+[\d.]+[A-Z]?:\s*(.*)", content)
        if match:
            caption = f"Figure {content.split('Figure ', 1)[1]}"
            reading_description = False
        elif content.startswith("Description:"):
            description.append(content.removeprefix("Description:").strip())
            reading_description = True
        elif reading_description:
            description.append(content)
    if caption:
        return "figure", plain(caption), plain(" ".join(description))
    return "paragraph", plain(" ".join(lines))


def parse_source():
    text = SOURCE.read_text(encoding="utf-8")
    lines = text.splitlines()
    blocks = []
    paragraph = []
    fence = []
    table_lines = []
    in_fence = False
    in_body = False
    skip_contents = False

    def flush_paragraph():
        if paragraph:
            p_text = plain(" ".join(paragraph))
            if p_text:
                blocks.append(("paragraph", p_text))
            paragraph.clear()

    def flush_table():
        if table_lines:
            header_raw = table_lines[0]
            headers = [plain(c) for c in header_raw.split("|")[1:-1]]
            rows = []
            start_idx = 1
            if len(table_lines) > 1 and "---" in table_lines[1]:
                start_idx = 2
            for row_line in table_lines[start_idx:]:
                cells = [plain(c) for c in row_line.split("|")[1:-1]]
                if any(cells):
                    rows.append(cells)
            if headers and rows:
                blocks.append(("table", headers, rows))
            table_lines.clear()

    for line in lines:
        stripped = line.strip()
        if not in_body:
            if stripped == "## CERTIFICATION":
                in_body = True
            else:
                continue

        # Handle code fences
        if stripped.startswith("```"):
            flush_paragraph()
            flush_table()
            if in_fence:
                blocks.append(figure_from_fence(fence))
                fence = []
            in_fence = not in_fence
            continue

        if in_fence:
            fence.append(line)
            continue

        # Handle Markdown Tables
        if stripped.startswith("|") and stripped.endswith("|"):
            flush_paragraph()
            table_lines.append(stripped)
            continue
        else:
            flush_table()

        if stripped == "## TABLE OF CONTENTS":
            flush_paragraph()
            blocks.append(("contents",))
            skip_contents = True
            continue

        if stripped == "## LIST OF FIGURES":
            flush_paragraph()
            blocks.append(("figures",))
            skip_contents = True
            continue

        if skip_contents:
            if stripped.startswith("## CHAPTER ONE"):
                skip_contents = False
            else:
                continue

        if not stripped or stripped == "---":
            flush_paragraph()
            continue

        if stripped.startswith("#"):
            flush_paragraph()
            level = len(stripped) - len(stripped.lstrip("#"))
            blocks.append(("heading", level, plain(stripped[level:].strip())))
            continue

        match = re.match(r"\*\*(Figure\s+[\d.]+[A-Z]?\s*—\s*[^*]+)\*\*\s*(.*)", stripped)
        if match:
            flush_paragraph()
            blocks.append(("figure", plain(match.group(1)), plain(match.group(2))))
            continue

        if re.match(r"^(?:[-*]|\d+\.)\s+", stripped):
            flush_paragraph()
            blocks.append(("list", plain(re.sub(r"^(?:[-*]|\d+\.)\s+", "", stripped))))
            continue

        paragraph.append(stripped)

    flush_paragraph()
    flush_table()
    return blocks


def add_docx_page_number(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    paragraph._p.append(field)


def build_docx(blocks):
    document = Document()
    section = document.sections[0]
    section.page_height, section.page_width = Inches(11.69), Inches(8.27)
    section.different_first_page_header_footer = True
    section.top_margin = section.bottom_margin = Inches(0.85)
    section.left_margin = section.right_margin = Inches(1)

    normal = document.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(11)
    normal.paragraph_format.line_spacing = 1.35
    normal.paragraph_format.space_after = Pt(7)

    for style_name, size in [("Heading 1", 15), ("Heading 2", 13), ("Heading 3", 11.5)]:
        style = document.styles[style_name]
        style.font.name = "Times New Roman"
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        style.paragraph_format.space_before = Pt(14)
        style.paragraph_format.space_after = Pt(6)

    # Title Page
    for text, size in [
        ("TECHNICAL REPORT ON STUDENTS' INDUSTRIAL WORK EXPERIENCE SCHEME (SIWES)", 16),
        ("UNDERTAKEN AT COMPUTER WAREHOUSE GROUP (CWG) PLC, LAGOS", 14),
        ("BY", 12),
        ("AYANBISI ABDULRAHMAN\nCPE/22/9996", 14),
        ("DEPARTMENT OF COMPUTER ENGINEERING\nSCHOOL OF ELECTRICAL SYSTEMS ENGINEERING\nFEDERAL UNIVERSITY OF TECHNOLOGY, AKURE", 12),
        ("IN PARTIAL FULFILMENT OF THE REQUIREMENTS FOR THE AWARD OF THE B.ENG. DEGREE IN COMPUTER ENGINEERING", 11),
        ("DECEMBER 2026", 12),
    ]:
        paragraph = document.add_paragraph()
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        paragraph.paragraph_format.space_after = Pt(22)
        run = paragraph.add_run(text)
        run.bold = True
        run.font.size = Pt(size)
    document.add_page_break()

    chapters = [entry[2] for entry in blocks if entry[0] == "heading" and entry[1] == 2 and (entry[2].startswith("CHAPTER") or entry[2] == "REFERENCES")]
    figures = [entry[1] for entry in blocks if entry[0] == "figure"]

    for entry in blocks:
        kind = entry[0]
        if kind == "heading":
            level, title = entry[1:]
            if level == 2 and (title.startswith("CHAPTER") or title in {"DEDICATION", "ACKNOWLEDGMENTS", "ABSTRACT"}):
                document.add_page_break()
            document.add_heading(title, level=min(max(level - 1, 1), 3))
        elif kind == "paragraph":
            document.add_paragraph(entry[1])
        elif kind == "list":
            document.add_paragraph(entry[1], style="List Bullet")
        elif kind in {"contents", "figures"}:
            document.add_page_break()
            document.add_heading("TABLE OF CONTENTS" if kind == "contents" else "LIST OF FIGURES", level=1)
            for title in (chapters if kind == "contents" else figures):
                document.add_paragraph(title)
        elif kind == "figure":
            table = document.add_table(rows=1, cols=1)
            table.style = "Table Grid"
            table.rows[0].height = Inches(1.8)
            table.rows[0].height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
            cell = table.cell(0, 0)
            shading = parse_xml(r'<w:shd {} w:fill="F1F5F9"/>'.format(nsdecls('w')))
            cell._tc.get_or_add_tcPr().append(shading)
            p = cell.paragraphs[0]
            run1 = p.add_run(f"FIGURE PLACEHOLDER — {entry[1]}\n")
            run1.bold = True
            run1.font.size = Pt(9.5)
            run2 = p.add_run(f"Technical Diagram / Photographic Evidence: {entry[2]}")
            run2.italic = True
            run2.font.size = Pt(9)
            document.add_paragraph("")
        elif kind == "table":
            headers, rows = entry[1], entry[2]
            table = document.add_table(rows=len(rows) + 1, cols=len(headers))
            table.style = "Table Grid"
            # format headers
            for col_idx, h_text in enumerate(headers):
                cell = table.cell(0, col_idx)
                shading = parse_xml(r'<w:shd {} w:fill="1E3A8A"/>'.format(nsdecls('w')))
                cell._tc.get_or_add_tcPr().append(shading)
                p = cell.paragraphs[0]
                run = p.add_run(h_text)
                run.bold = True
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            # format rows
            for row_idx, row_cells in enumerate(rows):
                for col_idx, c_text in enumerate(row_cells):
                    if col_idx < len(headers):
                        cell = table.cell(row_idx + 1, col_idx)
                        if row_idx % 2 == 1:
                            shading = parse_xml(r'<w:shd {} w:fill="F8FAFC"/>'.format(nsdecls('w')))
                            cell._tc.get_or_add_tcPr().append(shading)
                        p = cell.paragraphs[0]
                        run = p.add_run(c_text)
                        run.font.size = Pt(8.5)
            document.add_paragraph("")

    add_docx_page_number(section.footer.paragraphs[0])
    document.save(DOCX)


def build_pdf(blocks):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    font_path = Path("C:/Windows/Fonts/arial.ttf")
    bold_path = Path("C:/Windows/Fonts/arialbd.ttf")
    italic_path = Path("C:/Windows/Fonts/ariali.ttf")
    if font_path.exists():
        pdfmetrics.registerFont(TTFont("Report", str(font_path)))
        pdfmetrics.registerFont(TTFont("Report-Bold", str(bold_path)))
        if italic_path.exists():
            pdfmetrics.registerFont(TTFont("Report-Italic", str(italic_path)))
        else:
            pdfmetrics.registerFont(TTFont("Report-Italic", str(font_path)))
    else:
        raise FileNotFoundError("Windows Arial font is required to build the PDF")

    normal = ParagraphStyle("Normal", fontName="Report", fontSize=9.5, leading=14, alignment=TA_JUSTIFY, spaceAfter=8)
    heading1 = ParagraphStyle("H1", parent=normal, fontName="Report-Bold", fontSize=13, leading=17, spaceBefore=14, spaceAfter=7, textColor=colors.HexColor("#1e3a8a"))
    heading2 = ParagraphStyle("H2", parent=normal, fontName="Report-Bold", fontSize=11, leading=15, spaceBefore=10, spaceAfter=5, textColor=colors.HexColor("#1e3a8a"))
    heading3 = ParagraphStyle("H3", parent=normal, fontName="Report-Bold", fontSize=9.5, leading=13, spaceBefore=8, spaceAfter=4, textColor=colors.HexColor("#334155"))
    small = ParagraphStyle("Small", parent=normal, fontSize=8, leading=11)
    center = ParagraphStyle("Center", parent=heading1, alignment=TA_CENTER, spaceAfter=20)
    story = []

    # Title Page
    for title in [
        "TECHNICAL REPORT ON STUDENTS' INDUSTRIAL WORK EXPERIENCE SCHEME (SIWES)",
        "UNDERTAKEN AT COMPUTER WAREHOUSE GROUP (CWG) PLC, LAGOS",
        "BY AYANBISI ABDULRAHMAN — CPE/22/9996",
        "DEPARTMENT OF COMPUTER ENGINEERING, SCHOOL OF ELECTRICAL SYSTEMS ENGINEERING",
        "FEDERAL UNIVERSITY OF TECHNOLOGY, AKURE",
        "IN PARTIAL FULFILMENT OF THE REQUIREMENTS FOR THE AWARD OF THE B.ENG. DEGREE IN COMPUTER ENGINEERING",
        "DECEMBER 2026",
    ]:
        story.extend([Spacer(1, 20), Paragraph(html.escape(title), center)])
    story.append(PageBreak())

    chapters = [entry[2] for entry in blocks if entry[0] == "heading" and entry[1] == 2 and (entry[2].startswith("CHAPTER") or entry[2] == "REFERENCES")]
    figures = [entry[1] for entry in blocks if entry[0] == "figure"]

    for entry in blocks:
        kind = entry[0]
        if kind == "heading":
            level, title = entry[1:]
            if level == 2 and (title.startswith("CHAPTER") or title in {"DEDICATION", "ACKNOWLEDGMENTS", "ABSTRACT"}):
                story.append(PageBreak())
            if level <= 2:
                story.append(Paragraph(html.escape(title), heading1))
            elif level == 3:
                story.append(Paragraph(html.escape(title), heading2))
            else:
                story.append(Paragraph(html.escape(title), heading3))
        elif kind == "paragraph":
            story.append(Paragraph(html.escape(entry[1]), normal))
        elif kind == "list":
            story.append(Paragraph("• " + html.escape(entry[1]), normal))
        elif kind in {"contents", "figures"}:
            story.append(PageBreak())
            story.append(Paragraph("TABLE OF CONTENTS" if kind == "contents" else "LIST OF FIGURES", heading1))
            for title in (chapters if kind == "contents" else figures):
                story.append(Paragraph(html.escape(title), small))
        elif kind == "figure":
            content = Paragraph(
                f"<b>FIGURE PLACEHOLDER — {html.escape(entry[1])}</b><br/><br/><i>Technical Diagram / Photographic Evidence:</i> {html.escape(entry[2])}",
                small,
            )
            table = Table([[content]], colWidths=[465], rowHeights=[125])
            table.setStyle(TableStyle([
                ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#475569")),
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ]))
            story.extend([table, Spacer(1, 10)])
        elif kind == "table":
            headers, rows = entry[1], entry[2]
            total_width = 465
            num_cols = len(headers)
            col_width = total_width / max(num_cols, 1)

            t_headers = [Paragraph(f"<b>{html.escape(h)}</b>", ParagraphStyle("TH", parent=small, textColor=colors.white)) for h in headers]
            t_data = [t_headers]
            for row in rows:
                t_row = []
                for cell_idx, cell_text in enumerate(row):
                    if cell_idx < num_cols:
                        t_row.append(Paragraph(html.escape(cell_text), small))
                # Pad row if incomplete
                while len(t_row) < num_cols:
                    t_row.append(Paragraph("", small))
                t_data.append(t_row)

            table = Table(t_data, colWidths=[col_width] * num_cols)
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1e3a8a")),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#94a3b8")),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ]))
            story.extend([table, Spacer(1, 8)])

    def page_decorations(canvas, document):
        canvas.saveState()
        canvas.setFont("Report", 7.5)
        canvas.setFillColor(colors.HexColor("#64748b"))
        # Running header (on pages > 1)
        if document.page > 1:
            canvas.drawString(65, 800, "SIWES Technical Report | Ayanbisi AbdulRahman (CPE/22/9996) | CWG Plc")
            canvas.setStrokeColor(colors.HexColor("#cbd5e1"))
            canvas.setLineWidth(0.5)
            canvas.line(65, 794, 530, 794)
        # Running footer
        canvas.drawCentredString(A4[0] / 2, 30, str(document.page))
        canvas.restoreState()

    SimpleDocTemplate(
        str(PDF), pagesize=A4, leftMargin=65, rightMargin=65,
        topMargin=55, bottomMargin=50, title="Ayanbisi AbdulRahman SIWES Technical Report",
        author="Ayanbisi AbdulRahman",
    ).build(story, onLaterPages=page_decorations)


if __name__ == "__main__":
    report_blocks = parse_source()
    build_docx(report_blocks)
    if "--docx-only" not in sys.argv:
        build_pdf(report_blocks)
        print(f"Created {DOCX.name} and {PDF.name}")
    else:
        print(f"Created {DOCX.name}")
