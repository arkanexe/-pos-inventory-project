from __future__ import annotations

import html
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.table import WD_ROW_HEIGHT_RULE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "INDUSTRIAL_TRAINING_TECHNICAL_REPORT.md"
DOCX = ROOT / "INDUSTRIAL_TRAINING_TECHNICAL_REPORT.docx"
PDF = ROOT / "INDUSTRIAL_TRAINING_TECHNICAL_REPORT.pdf"


def plain(value: str) -> str:
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"\\text\{([^}]+)\}", r"\1", value)
    value = value.replace("\\phi", "φ").replace("\\ge", "≥")
    value = re.sub(r"\*\*|`|\$", "", value)
    return value.strip()


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
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    blocks = []
    paragraph = []
    fence = []
    in_fence = False
    in_body = False
    skip_contents = False

    def flush():
        if paragraph:
            blocks.append(("paragraph", plain(" ".join(paragraph))))
            paragraph.clear()

    for line in lines:
        stripped = line.strip()
        if not in_body:
            if stripped == "## CERTIFICATION":
                in_body = True
            else:
                continue
        if stripped.startswith("```"):
            flush()
            if in_fence:
                blocks.append(figure_from_fence(fence))
                fence = []
            in_fence = not in_fence
            continue
        if in_fence:
            fence.append(line)
            continue
        if stripped == "## TABLE OF CONTENTS":
            flush()
            blocks.append(("contents",))
            skip_contents = True
            continue
        if stripped == "## LIST OF FIGURES":
            flush()
            blocks.append(("figures",))
            skip_contents = True
            continue
        if skip_contents:
            if stripped.startswith("## CHAPTER ONE"):
                skip_contents = False
            else:
                continue
        if not stripped or stripped == "---":
            flush()
            continue
        if stripped.startswith("#"):
            flush()
            level = len(stripped) - len(stripped.lstrip("#"))
            blocks.append(("heading", level, plain(stripped[level:].strip())))
            continue
        match = re.match(r"\*\*(Figure\s+[\d.]+[A-Z]?\s*—\s*[^*]+)\*\*\s*(.*)", stripped)
        if match:
            flush()
            blocks.append(("figure", plain(match.group(1)), plain(match.group(2))))
            continue
        if re.match(r"^(?:[-*]|\d+\.)\s+", stripped):
            flush()
            blocks.append(("list", plain(re.sub(r"^(?:[-*]|\d+\.)\s+", "", stripped))))
            continue
        paragraph.append(stripped)
    flush()
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
    normal.paragraph_format.space_after = Pt(8)
    for style_name, size in [("Heading 1", 15), ("Heading 2", 13), ("Heading 3", 12)]:
        style = document.styles[style_name]
        style.font.name = "Times New Roman"
        style.font.size = Pt(size)
        style.font.bold = True
        style.paragraph_format.space_before = Pt(14)
        style.paragraph_format.space_after = Pt(6)

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
        paragraph.paragraph_format.space_after = Pt(25)
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
            cell.text = f"IMAGE SPACE — {entry[1]}\nExpected image: {entry[2]}"
            document.add_paragraph("")
    add_docx_page_number(section.footer.paragraphs[0])
    document.save(DOCX)


def build_pdf(blocks):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    font_path = Path("C:/Windows/Fonts/arial.ttf")
    bold_path = Path("C:/Windows/Fonts/arialbd.ttf")
    if font_path.exists():
        pdfmetrics.registerFont(TTFont("Report", str(font_path)))
        pdfmetrics.registerFont(TTFont("Report-Bold", str(bold_path)))
    else:
        raise FileNotFoundError("Windows Arial font is required to build the PDF")

    normal = ParagraphStyle("Normal", fontName="Report", fontSize=9.5, leading=14, alignment=TA_JUSTIFY, spaceAfter=9)
    heading = ParagraphStyle("Heading", parent=normal, fontName="Report-Bold", fontSize=13, leading=18, spaceBefore=13, spaceAfter=8)
    subheading = ParagraphStyle("Subheading", parent=heading, fontSize=11, leading=15)
    small = ParagraphStyle("Small", parent=normal, fontSize=8, leading=11)
    center = ParagraphStyle("Center", parent=heading, alignment=TA_CENTER, spaceAfter=22)
    story = []

    for title in [
        "TECHNICAL REPORT ON STUDENTS' INDUSTRIAL WORK EXPERIENCE SCHEME (SIWES)",
        "UNDERTAKEN AT COMPUTER WAREHOUSE GROUP (CWG) PLC, LAGOS",
        "BY AYANBISI ABDULRAHMAN — CPE/22/9996",
        "DEPARTMENT OF COMPUTER ENGINEERING, SCHOOL OF ELECTRICAL SYSTEMS ENGINEERING",
        "FEDERAL UNIVERSITY OF TECHNOLOGY, AKURE",
        "IN PARTIAL FULFILMENT OF THE REQUIREMENTS FOR THE AWARD OF THE B.ENG. DEGREE IN COMPUTER ENGINEERING",
        "DECEMBER 2026",
    ]:
        story.extend([Spacer(1, 25), Paragraph(html.escape(title), center)])
    story.append(PageBreak())

    chapters = [entry[2] for entry in blocks if entry[0] == "heading" and entry[1] == 2 and (entry[2].startswith("CHAPTER") or entry[2] == "REFERENCES")]
    figures = [entry[1] for entry in blocks if entry[0] == "figure"]
    for entry in blocks:
        kind = entry[0]
        if kind == "heading":
            level, title = entry[1:]
            if level == 2 and (title.startswith("CHAPTER") or title in {"DEDICATION", "ACKNOWLEDGMENTS", "ABSTRACT"}):
                story.append(PageBreak())
            story.append(Paragraph(html.escape(title), heading if level <= 3 else subheading))
        elif kind == "paragraph":
            story.append(Paragraph(html.escape(entry[1]), normal))
        elif kind == "list":
            story.append(Paragraph("• " + html.escape(entry[1]), normal))
        elif kind in {"contents", "figures"}:
            story.append(PageBreak())
            story.append(Paragraph("TABLE OF CONTENTS" if kind == "contents" else "LIST OF FIGURES", heading))
            for title in (chapters if kind == "contents" else figures):
                story.append(Paragraph(html.escape(title), small))
        elif kind == "figure":
            content = Paragraph(
                html.escape("IMAGE SPACE — " + entry[1]) + "<br/>" + html.escape("Expected image: " + entry[2]),
                small,
            )
            table = Table([[content]], colWidths=[455], rowHeights=[130])
            table.setStyle(TableStyle([
                ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#4b5563")),
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f7f8fa")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 12),
            ]))
            story.extend([table, Spacer(1, 10)])

    def page_number(canvas, document):
        canvas.setFont("Report", 8)
        canvas.drawCentredString(A4[0] / 2, 30, str(document.page))

    SimpleDocTemplate(
        str(PDF), pagesize=A4, leftMargin=65, rightMargin=65,
        topMargin=60, bottomMargin=55, title="Ayanbisi AbdulRahman SIWES Technical Report",
        author="Ayanbisi AbdulRahman",
    ).build(story, onLaterPages=page_number)


if __name__ == "__main__":
    report_blocks = parse_source()
    build_docx(report_blocks)
    if "--docx-only" not in sys.argv:
        build_pdf(report_blocks)
        print(f"Created {DOCX.name} and {PDF.name}")
    else:
        print(f"Created {DOCX.name}")
