# -*- coding: utf-8 -*-
"""
Generates publication-grade UI screenshot mockups for CWG Retail Suite POS & Inventory System.
Matches the exact colors, layout, and seeded database records of the application.
"""

from pathlib import Path
import shutil
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
IMG_DIR = ROOT / "report_images"
IMG_DIR.mkdir(exist_ok=True)
ARTIFACT_DIR = Path(r"C:\Users\Dell\.gemini\antigravity\brain\2971304b-d5bb-46d6-8d46-b89e93c72bee\report_samples")
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

# Font configurations
FONT_DIR = Path(r"C:\Windows\Fonts")
font_reg = lambda sz: ImageFont.truetype(str(FONT_DIR / "arial.ttf"), sz)
font_bold = lambda sz: ImageFont.truetype(str(FONT_DIR / "arialbd.ttf"), sz)
font_mono = lambda sz: ImageFont.truetype(str(FONT_DIR / "consola.ttf"), sz)

# Color Palette (Tailwind CSS matching the project)
BG_MAIN = "#f8fafc"      # slate-50
SIDEBAR_BG = "#0f172a"   # slate-900
SIDEBAR_HOVER = "#1e293b"# slate-800
SIDEBAR_ACTIVE = "#2563eb"# blue-600
TEXT_WHITE = "#ffffff"
TEXT_MUTED = "#94a3b8"   # slate-400
TEXT_DARK = "#0f172a"    # slate-900
TEXT_BODY = "#334155"    # slate-700
BORDER_COLOR = "#e2e8f0" # slate-200
PRIMARY = "#2563eb"      # blue-600
PRIMARY_HOVER = "#1d4ed8"# blue-700
SUCCESS = "#10b981"      # emerald-500
SUCCESS_BG = "#ecfdf5"   # emerald-50
SUCCESS_TEXT = "#047857" # emerald-700
WARNING_BG = "#fffbeb"   # amber-50
WARNING_TEXT = "#b45309" # amber-700
CARD_BG = "#ffffff"

W, H = 1400, 880
SIDEBAR_W = 240
TOPBAR_H = 64

def create_base(active_item="POS"):
    img = Image.new("RGB", (W, H), BG_MAIN)
    draw = ImageDraw.Draw(img)

    # Sidebar background
    draw.rectangle([0, 0, SIDEBAR_W, H], fill=SIDEBAR_BG)

    # Logo / Brand
    draw.rectangle([20, 20, 48, 48], fill=PRIMARY)
    draw.text((27, 24), "CWG", fill=TEXT_WHITE, font=font_bold(15))
    draw.text((58, 20), "CWG RETAIL", fill=TEXT_WHITE, font=font_bold(16))
    draw.text((58, 38), "SUITE POS v2.4", fill="#38bdf8", font=font_bold(10))

    draw.line([0, 64, SIDEBAR_W, 64], fill="#1e293b", width=1)

    # Menu items
    items = [
        ("Dashboard", 80),
        ("Point of Sale", 125),
        ("Products", 170),
        ("Inventory", 215),
        ("Sales Ledger", 260),
        ("Reports", 305),
        ("Settings", 350)
    ]

    for label, y in items:
        is_active = (label.lower() in active_item.lower()) or (active_item.lower() in label.lower())
        if is_active:
            draw.rounded_rectangle([12, y, SIDEBAR_W - 12, y + 36], radius=6, fill=PRIMARY)
            draw.text((36, y + 9), label, fill=TEXT_WHITE, font=font_bold(13))
            # active indicator bullet
            draw.ellipse([22, y + 14, 30, y + 22], fill="#93c5fd")
        else:
            draw.text((36, y + 9), label, fill=TEXT_MUTED, font=font_reg(13))
            draw.ellipse([24, y + 16, 28, y + 20], fill="#475569")

    # Bottom User Profile Card
    draw.line([0, H - 75, SIDEBAR_W, H - 75], fill="#1e293b", width=1)
    draw.ellipse([16, H - 60, 52, H - 24], fill="#3b82f6")
    draw.text((25, H - 54), "CO", fill=TEXT_WHITE, font=font_bold(14))
    draw.text((60, H - 58), "Chinedu Okafor", fill=TEXT_WHITE, font=font_bold(12))
    draw.text((60, H - 42), "Role: Owner / Admin", fill=TEXT_MUTED, font=font_reg(10))
    draw.ellipse([SIDEBAR_W - 25, H - 45, SIDEBAR_W - 17, H - 37], fill="#22c55e") # online

    # Topbar
    draw.rectangle([SIDEBAR_W, 0, W, TOPBAR_H], fill="#ffffff")
    draw.line([SIDEBAR_W, TOPBAR_H, W, TOPBAR_H], fill=BORDER_COLOR, width=1)

    # Live Status Badges
    draw.rounded_rectangle([W - 380, 16, W - 200, 48], radius=6, fill="#f1f5f9", outline="#cbd5e1")
    draw.ellipse([W - 368, 28, W - 360, 36], fill="#10b981")
    draw.text((W - 352, 24), "Server: Online (Sync 100%)", fill="#334155", font=font_bold(11))

    # Topbar profile pill
    draw.rounded_rectangle([W - 180, 16, W - 20, 48], radius=6, fill=PRIMARY, outline=PRIMARY)
    draw.text((W - 165, 24), "Terminal #01 (Lagos)", fill=TEXT_WHITE, font=font_bold(11))

    return img, draw

# ==============================================================================
# Screen 1: Figure 3.32 - POS Checkout Interface & Cart Processing
# ==============================================================================
def render_fig_3_32():
    img, draw = create_base("Point of Sale")

    # Breadcrumb / Page Title
    draw.text((SIDEBAR_W + 24, 20), "POS Cashier Checkout", fill=TEXT_DARK, font=font_bold(18))
    draw.text((SIDEBAR_W + 240, 24), "• Shift Session: Morning Active", fill="#64748b", font=font_reg(12))

    # Left Catalog Area (width 740px)
    left_x = SIDEBAR_W + 24
    top_y = TOPBAR_H + 20

    # Search Bar
    draw.rounded_rectangle([left_x, top_y, left_x + 720, top_y + 44], radius=6, fill="#ffffff", outline="#cbd5e1")
    draw.text((left_x + 16, top_y + 12), "🔍  Scan barcode with laser scanner or search product (Press '/' to focus)...", fill="#94a3b8", font=font_reg(13))
    draw.rounded_rectangle([left_x + 590, top_y + 6, left_x + 712, top_y + 38], radius=4, fill="#f1f5f9", outline="#cbd5e1")
    draw.text((left_x + 605, top_y + 13), "Scanner Active", fill="#047857", font=font_bold(11))

    # Category Filter Pills
    cat_y = top_y + 54
    cats = [("All Items (14)", True), ("Beverages (4)", False), ("Dairy & Breakfast (3)", False), ("Groceries (4)", False), ("Household (3)", False)]
    curr_cx = left_x
    for c_text, active in cats:
        tw = len(c_text) * 8 + 24
        bg = PRIMARY if active else "#ffffff"
        fg = TEXT_WHITE if active else "#475569"
        border = PRIMARY if active else "#cbd5e1"
        draw.rounded_rectangle([curr_cx, cat_y, curr_cx + tw, cat_y + 32], radius=16, fill=bg, outline=border)
        draw.text((curr_cx + 12, cat_y + 8), c_text, fill=fg, font=font_bold(11))
        curr_cx += tw + 10

    # Product Cards Grid (2 columns x 3 rows = 6 visible items)
    grid_y = cat_y + 44
    products = [
        ("Nestlé Milo 500g Tin", "SKU: NES-MILO-500", "48 in stock", "₦4,200.00", "#14532d", "#facc15"),
        ("Peak Evaporated Milk 160g", "SKU: PEK-EVAP-160", "120 in stock", "₦650.00", "#1e3a8a", "#93c5fd"),
        ("Indomie Onion Chicken 70g (Ctn 40)", "SKU: IND-ONC-CTN", "32 in stock", "₦9,800.00", "#991b1b", "#fde047"),
        ("Golden Penny Semovita 2kg", "SKU: GLD-SEM-2KG", "42 in stock", "₦3,100.00", "#78350f", "#fef08a"),
        ("Dangote Granulated Sugar 1kg", "SKU: DAN-SUG-1KG", "65 in stock", "₦1,850.00", "#1e293b", "#38bdf8"),
        ("Dano Full Cream Milk Powder 800g", "SKU: DAN-MLK-800", "28 in stock", "₦5,400.00", "#0369a1", "#bae6fd"),
    ]

    card_w = 350
    card_h = 175

    for idx, (pname, psku, pstock, pprice, cbg, cfg) in enumerate(products):
        row = idx // 2
        col = idx % 2
        px = left_x + col * (card_w + 20)
        py = grid_y + row * (card_h + 16)

        # Card container
        draw.rounded_rectangle([px, py, px + card_w, py + card_h], radius=8, fill="#ffffff", outline="#e2e8f0")

        # Color banner / Thumbnail
        draw.rounded_rectangle([px + 12, py + 12, px + 80, py + 80], radius=6, fill=cbg)
        draw.text((px + 22, py + 38), "CWG", fill=cfg, font=font_bold(15))

        # Title & SKU
        draw.text((px + 92, py + 14), pname[:24], fill=TEXT_DARK, font=font_bold(13))
        draw.text((px + 92, py + 34), psku, fill="#64748b", font=font_mono(11))
        # Stock pill
        draw.rounded_rectangle([px + 92, py + 54, px + 180, py + 74], radius=4, fill="#f1f5f9")
        draw.text((px + 100, py + 57), pstock, fill="#047857", font=font_bold(10))

        # Price and Add to Cart button
        draw.text((px + 16, py + 128), pprice, fill="#0f172a", font=font_bold(17))

        draw.rounded_rectangle([px + card_w - 110, py + 120, px + card_w - 12, py + 158], radius=6, fill=PRIMARY)
        draw.text((px + card_w - 92, py + 130), "+ Add to Cart", fill=TEXT_WHITE, font=font_bold(11))

    # ================= Right Cart Panel (370px width) =================
    cart_x = left_x + 745
    cart_y = top_y
    cart_w = 365
    cart_h = 760

    draw.rounded_rectangle([cart_x, cart_y, cart_x + cart_w, cart_y + cart_h], radius=8, fill="#ffffff", outline="#cbd5e1")

    # Cart Header
    draw.rectangle([cart_x, cart_y, cart_x + cart_w, cart_y + 50], fill="#f8fafc")
    draw.text((cart_x + 16, cart_y + 16), "Active Order Cart", fill=TEXT_DARK, font=font_bold(15))
    draw.rounded_rectangle([cart_x + cart_w - 95, cart_y + 12, cart_x + cart_w - 12, cart_y + 38], radius=4, fill="#fee2e2")
    draw.text((cart_x + cart_w - 82, cart_y + 18), "Clear Cart", fill="#b91c1c", font=font_bold(11))
    draw.line([cart_x, cart_y + 50, cart_x + cart_w, cart_y + 50], fill="#e2e8f0", width=1)

    # Cart Lines
    cart_items = [
        ("Nestlé Milo 500g Tin", 2, "₦4,200.00", "₦8,400.00"),
        ("Peak Evaporated Milk 160g", 4, "₦650.00", "₦2,600.00"),
        ("Golden Penny Semovita 2kg", 1, "₦3,100.00", "₦3,100.00"),
    ]

    item_y = cart_y + 60
    for title, qty, unit_p, total_p in cart_items:
        draw.rounded_rectangle([cart_x + 10, item_y, cart_x + cart_w - 10, item_y + 70], radius=6, fill="#f8fafc", outline="#f1f5f9")
        draw.text((cart_x + 20, item_y + 8), title, fill=TEXT_DARK, font=font_bold(12))
        draw.text((cart_x + 20, item_y + 30), f"{qty} × {unit_p}", fill="#64748b", font=font_reg(11))

        # Quantity stepper controls
        draw.rounded_rectangle([cart_x + cart_w - 145, item_y + 26, cart_x + cart_w - 95, item_y + 52], radius=4, fill="#ffffff", outline="#cbd5e1")
        draw.text((cart_x + cart_w - 140, item_y + 30), "-", fill="#0f172a", font=font_bold(14))
        draw.text((cart_x + cart_w - 124, item_y + 32), str(qty), fill="#0f172a", font=font_bold(12))
        draw.text((cart_x + cart_w - 108, item_y + 30), "+", fill="#0f172a", font=font_bold(14))

        # Line total
        draw.text((cart_x + cart_w - 85, item_y + 32), total_p, fill="#0f172a", font=font_bold(12))
        item_y += 78

    # Payment & Summary section
    summary_y = cart_y + 360
    draw.line([cart_x + 10, summary_y, cart_x + cart_w - 10, summary_y], fill="#e2e8f0", width=1)

    draw.text((cart_x + 20, summary_y + 15), "Subtotal:", fill="#64748b", font=font_reg(13))
    draw.text((cart_x + cart_w - 110, summary_y + 15), "₦14,100.00", fill="#0f172a", font=font_bold(13))

    draw.text((cart_x + 20, summary_y + 40), "Tax / VAT (Retail Exempt):", fill="#64748b", font=font_reg(13))
    draw.text((cart_x + cart_w - 70, summary_y + 40), "₦0.00", fill="#047857", font=font_bold(13))

    draw.text((cart_x + 20, summary_y + 65), "Discount applied:", fill="#64748b", font=font_reg(13))
    draw.text((cart_x + cart_w - 70, summary_y + 65), "₦0.00", fill="#64748b", font=font_reg(13))

    # Total payable card
    draw.rounded_rectangle([cart_x + 12, summary_y + 100, cart_x + cart_w - 12, summary_y + 160], radius=8, fill="#ecfdf5", outline="#a7f3d0")
    draw.text((cart_x + 24, summary_y + 112), "Total Amount Payable", fill="#065f46", font=font_reg(12))
    draw.text((cart_x + 24, summary_y + 130), "₦14,100.00", fill="#047857", font=font_bold(22))

    # Payment Method Selector
    draw.text((cart_x + 20, summary_y + 175), "Payment Method:", fill=TEXT_DARK, font=font_bold(12))
    p_methods = [("Cash", True), ("POS Card", False), ("Bank Transfer", False)]
    mx = cart_x + 20
    for m_label, selected in p_methods:
        mbg = PRIMARY if selected else "#f1f5f9"
        mfg = TEXT_WHITE if selected else "#334155"
        draw.rounded_rectangle([mx, summary_y + 195, mx + 95, summary_y + 228], radius=6, fill=mbg)
        draw.text((mx + 18, summary_y + 204), m_label, fill=mfg, font=font_bold(11))
        mx += 105

    # Cash Tendered & Change
    draw.text((cart_x + 20, summary_y + 245), "Amount Tendered (NGN):", fill="#64748b", font=font_reg(11))
    draw.rounded_rectangle([cart_x + 20, summary_y + 265, cart_x + 190, summary_y + 300], radius=6, fill="#ffffff", outline="#cbd5e1")
    draw.text((cart_x + 30, summary_y + 274), "15,000.00", fill="#0f172a", font=font_bold(14))

    draw.text((cart_x + 210, summary_y + 245), "Change Due:", fill="#64748b", font=font_reg(11))
    draw.rounded_rectangle([cart_x + 210, summary_y + 265, cart_x + cart_w - 20, summary_y + 300], radius=6, fill="#f8fafc", outline="#cbd5e1")
    draw.text((cart_x + 222, summary_y + 274), "₦900.00", fill="#047857", font=font_bold(14))

    # Checkout Action Button
    draw.rounded_rectangle([cart_x + 16, summary_y + 325, cart_x + cart_w - 16, summary_y + 380], radius=8, fill="#10b981")
    draw.text((cart_x + 38, summary_y + 342), "✓ COMPLETE SALE & PRINT RECEIPT", fill=TEXT_WHITE, font=font_bold(13))

    out_file = IMG_DIR / "fig_3_32_pos_checkout.png"
    img.save(out_file)
    shutil.copy(out_file, ARTIFACT_DIR / "fig_3_32_pos_checkout.png")
    print(f"Generated {out_file}")

# ==============================================================================
# Screen 2: Figure 3.32B - Product Catalog Management with Live Search & Filtering
# ==============================================================================
def render_fig_3_32b():
    img, draw = create_base("Products")

    # Title & Controls
    draw.text((SIDEBAR_W + 24, 20), "Products Catalogue & Pricing", fill=TEXT_DARK, font=font_bold(18))

    # Action buttons top-right
    draw.rounded_rectangle([W - 360, 16, W - 220, 48], radius=6, fill="#ffffff", outline="#cbd5e1")
    draw.text((W - 340, 24), "⭳ Export CSV", fill="#334155", font=font_bold(12))

    draw.rounded_rectangle([W - 200, 16, W - 24, 48], radius=6, fill=PRIMARY)
    draw.text((W - 180, 24), "+ Add New Product", fill=TEXT_WHITE, font=font_bold(12))

    # Filters Bar Card
    top_y = TOPBAR_H + 20
    draw.rounded_rectangle([SIDEBAR_W + 24, top_y, W - 24, top_y + 60], radius=8, fill="#ffffff", outline="#e2e8f0")

    # Search Input
    draw.rounded_rectangle([SIDEBAR_W + 40, top_y + 10, SIDEBAR_W + 420, top_y + 50], radius=6, fill="#f8fafc", outline="#cbd5e1")
    draw.text((SIDEBAR_W + 55, top_y + 20), "🔍  Search by product name, SKU or barcode...", fill="#94a3b8", font=font_reg(12))

    # Category dropdown
    draw.rounded_rectangle([SIDEBAR_W + 440, top_y + 10, SIDEBAR_W + 650, top_y + 50], radius=6, fill="#f8fafc", outline="#cbd5e1")
    draw.text((SIDEBAR_W + 455, top_y + 20), "Category: All Categories  ▼", fill="#334155", font=font_bold(12))

    # Stock Status dropdown
    draw.rounded_rectangle([SIDEBAR_W + 670, top_y + 10, SIDEBAR_W + 860, top_y + 50], radius=6, fill="#f8fafc", outline="#cbd5e1")
    draw.text((SIDEBAR_W + 685, top_y + 20), "Stock: In Stock (13)  ▼", fill="#334155", font=font_bold(12))

    # Count badge
    draw.text((W - 220, top_y + 20), "Showing 14 Active Products", fill="#64748b", font=font_bold(12))

    # Data Table Container
    table_y = top_y + 75
    draw.rounded_rectangle([SIDEBAR_W + 24, table_y, W - 24, H - 70], radius=8, fill="#ffffff", outline="#e2e8f0")

    # Table Header Row
    draw.rectangle([SIDEBAR_W + 24, table_y, W - 24, table_y + 45], fill="#f1f5f9")
    draw.line([SIDEBAR_W + 24, table_y + 45, W - 24, table_y + 45], fill="#cbd5e1", width=1)

    headers = [
        ("PRODUCT DETAILS & SKU", SIDEBAR_W + 44),
        ("CATEGORY", SIDEBAR_W + 360),
        ("COST PRICE", SIDEBAR_W + 500),
        ("SELLING PRICE", SIDEBAR_W + 640),
        ("MARGIN", SIDEBAR_W + 770),
        ("STOCK LEVEL", SIDEBAR_W + 890),
        ("STATUS", SIDEBAR_W + 1020),
        ("ACTIONS", SIDEBAR_W + 1120)
    ]
    for h_text, h_x in headers:
        draw.text((h_x, table_y + 15), h_text, fill="#475569", font=font_bold(11))

    # Table Rows
    rows = [
        ("Nestlé Milo Energy Drink 500g", "NES-MILO-500", "Beverages", "₦3,200.00", "₦4,200.00", "+31.25%", "48 tins", "In Stock", True),
        ("Peak Evaporated Milk 160g Tin", "PEK-EVAP-160", "Dairy", "₦510.00", "₦650.00", "+27.45%", "120 tins", "In Stock", True),
        ("Indomie Onion Chicken (Ctn 40)", "IND-ONC-CTN", "Groceries", "₦8,100.00", "₦9,800.00", "+20.99%", "32 ctns", "In Stock", True),
        ("Golden Penny Semovita 2kg Pack", "GLD-SEM-2KG", "Staples", "₦2,400.00", "₦3,100.00", "+29.17%", "42 packs", "In Stock", True),
        ("Dangote Granulated Sugar 50kg Bag", "DAN-SUG-50KG", "Wholesale", "₦38,500.00", "₦44,000.00", "+14.29%", "8 bags", "Low Stock", False),
        ("Dano Full Cream Milk Powder 800g", "DAN-MLK-800", "Dairy", "₦4,250.00", "₦5,400.00", "+27.06%", "28 pouches", "In Stock", True),
        ("Mamador Pure Vegetable Oil 3.8L", "MAM-OIL-38L", "Groceries", "₦7,500.00", "₦9,200.00", "+22.67%", "19 kegs", "In Stock", True),
        ("Gala Sausage Roll (Pack of 20)", "GAL-SAU-PK20", "Snacks", "₦2,800.00", "₦3,600.00", "+28.57%", "55 packs", "In Stock", True),
    ]

    row_y = table_y + 46
    for title, sku, cat, cost, sell, margin, stock, status, is_ok in rows:
        # Alternating background
        draw.line([SIDEBAR_W + 24, row_y + 60, W - 24, row_y + 60], fill="#f1f5f9", width=1)

        # Product Title & SKU
        draw.text((SIDEBAR_W + 44, row_y + 12), title, fill=TEXT_DARK, font=font_bold(13))
        draw.text((SIDEBAR_W + 44, row_y + 34), sku, fill="#64748b", font=font_mono(11))

        # Category pill
        draw.rounded_rectangle([SIDEBAR_W + 360, row_y + 16, SIDEBAR_W + 450, row_y + 40], radius=4, fill="#f1f5f9")
        draw.text((SIDEBAR_W + 372, row_y + 22), cat, fill="#334155", font=font_bold(11))

        # Prices
        draw.text((SIDEBAR_W + 500, row_y + 20), cost, fill="#64748b", font=font_reg(13))
        draw.text((SIDEBAR_W + 640, row_y + 20), sell, fill=TEXT_DARK, font=font_bold(13))

        # Margin pill (green)
        draw.rounded_rectangle([SIDEBAR_W + 770, row_y + 16, SIDEBAR_W + 845, row_y + 40], radius=12, fill="#ecfdf5", outline="#a7f3d0")
        draw.text((SIDEBAR_W + 780, row_y + 22), margin, fill="#047857", font=font_bold(11))

        # Stock count
        draw.text((SIDEBAR_W + 890, row_y + 20), stock, fill=TEXT_DARK, font=font_bold(13))

        # Status badge
        s_bg = "#ecfdf5" if is_ok else "#fffbeb"
        s_fg = "#047857" if is_ok else "#b45309"
        draw.rounded_rectangle([SIDEBAR_W + 1020, row_y + 16, SIDEBAR_W + 1095, row_y + 40], radius=12, fill=s_bg)
        draw.text((SIDEBAR_W + 1030, row_y + 22), status, fill=s_fg, font=font_bold(11))

        # Action Buttons
        draw.rounded_rectangle([SIDEBAR_W + 1120, row_y + 16, SIDEBAR_W + 1165, row_y + 40], radius=4, fill="#eff6ff", outline="#bfdbfe")
        draw.text((SIDEBAR_W + 1130, row_y + 22), "Edit", fill=PRIMARY, font=font_bold(11))

        draw.rounded_rectangle([SIDEBAR_W + 1175, row_y + 16, SIDEBAR_W + 1230, row_y + 40], radius=4, fill="#f0fdf4", outline="#bbf7d0")
        draw.text((SIDEBAR_W + 1182, row_y + 22), "Restock", fill="#15803d", font=font_bold(11))

        row_y += 62

    # Bottom Pagination
    p_y = H - 55
    draw.text((SIDEBAR_W + 30, p_y), "Showing 1 to 8 of 14 products (Page 1 of 2)", fill="#64748b", font=font_reg(12))

    draw.rounded_rectangle([W - 250, p_y - 8, W - 180, p_y + 24], radius=4, fill="#ffffff", outline="#cbd5e1")
    draw.text((W - 240, p_y), "Previous", fill="#94a3b8", font=font_bold(11))

    draw.rounded_rectangle([W - 170, p_y - 8, W - 135, p_y + 24], radius=4, fill=PRIMARY)
    draw.text((W - 157, p_y), "1", fill=TEXT_WHITE, font=font_bold(11))

    draw.rounded_rectangle([W - 125, p_y - 8, W - 90, p_y + 24], radius=4, fill="#ffffff", outline="#cbd5e1")
    draw.text((W - 112, p_y), "2", fill="#334155", font=font_bold(11))

    draw.rounded_rectangle([W - 80, p_y - 8, W - 24, p_y + 24], radius=4, fill="#ffffff", outline="#cbd5e1")
    draw.text((W - 68, p_y), "Next", fill="#334155", font=font_bold(11))

    out_file = IMG_DIR / "fig_3_32b_pos_product_catalog.png"
    img.save(out_file)
    shutil.copy(out_file, ARTIFACT_DIR / "fig_3_32b_pos_product_catalog.png")
    print(f"Generated {out_file}")

# ==============================================================================
# Screen 3: Figure 3.33 - ESC/POS 80mm Thermal Receipt Layout & Modal Preview
# ==============================================================================
def render_fig_3_33():
    # Base is the POS interface slightly darkened to simulate modal backdrop
    img, draw = create_base("Point of Sale")

    # Dark modal overlay
    overlay = Image.new("RGBA", (W, H), (15, 23, 42, 160))
    img.paste(overlay, (0, 0), overlay)
    draw = ImageDraw.Draw(img)

    # Modal Dialog Window (520px x 780px) centered
    mw, mh = 500, 780
    mx = (W - mw) // 2
    my = (H - mh) // 2

    # Modal Window Container
    draw.rounded_rectangle([mx, my, mx + mw, my + mh], radius=12, fill="#ffffff", outline="#cbd5e1")

    # Modal Header
    draw.rectangle([mx, my, mx + mw, my + 50], fill="#f8fafc")
    draw.text((mx + 20, my + 16), "Transaction Completed Successfully", fill="#047857", font=font_bold(14))
    draw.text((mx + mw - 35, my + 14), "✖", fill="#94a3b8", font=font_bold(16))
    draw.line([mx, my + 50, mx + mw, my + 50], fill="#e2e8f0", width=1)

    # Simulated Thermal Receipt Paper Roll (420px wide)
    rx = mx + 40
    ry = my + 65
    rw = 420
    rh = 630

    # Receipt paper container with drop shadow and serrated paper edges
    draw.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=4, fill="#fafafa", outline="#d1d5db")

    # Receipt text in Monospace
    lines = [
        ("================================================", False, 10, "center"),
        ("COMPUTER WAREHOUSE GROUP PLC", True, 13, "center"),
        ("CWG RETAIL SUITE - VI BRANCH", True, 11, "center"),
        ("Plot 5, Commercial Block West, Victoria Island", False, 10, "center"),
        ("Lagos State, Nigeria | Tel: +234 1 270 0000", False, 10, "center"),
        ("TIN / VAT REG: 10482910-0001", False, 10, "center"),
        ("------------------------------------------------", False, 10, "center"),
        ("INVOICE NO:  CWG-TXN-20261026-0084", True, 11, "left"),
        ("DATE / TIME: 2026-10-26 14:32:18", False, 10, "left"),
        ("CASHIER:     Chinedu Okafor (ID: USR-001)", False, 10, "left"),
        ("TERMINAL:    POS-STATION-01", False, 10, "left"),
        ("------------------------------------------------", False, 10, "center"),
        ("ITEM DESCRIPTION        QTY   UNIT(NGN)   TOTAL", True, 10, "left"),
        ("------------------------------------------------", False, 10, "center"),
        ("Nestle Milo 500g Tin     2    4,200.00  8,400.00", False, 10, "left"),
        ("Peak Evap Milk 160g      4      650.00  2,600.00", False, 10, "left"),
        ("Golden Penny Semo 2kg    1    3,100.00  3,100.00", False, 10, "left"),
        ("------------------------------------------------", False, 10, "center"),
        ("SUBTOTAL:                            ₦14,100.00", False, 11, "left"),
        ("VAT (0% Retail Exempt):                   ₦0.00", False, 11, "left"),
        ("TOTAL DUE:                           ₦14,100.00", True, 13, "left"),
        ("------------------------------------------------", False, 10, "center"),
        ("PAYMENT METHOD:      CASH", True, 11, "left"),
        ("AMOUNT TENDERED:                     ₦15,000.00", False, 11, "left"),
        ("CHANGE RETURNED:                        ₦900.00", True, 12, "left"),
        ("------------------------------------------------", False, 10, "center"),
        ("          THANK YOU FOR YOUR PATRONAGE!         ", True, 10, "center"),
        ("   Goods sold in good condition cannot be       ", False, 9, "center"),
        ("   refunded without original print receipt.     ", False, 9, "center"),
        ("================================================", False, 10, "center"),
    ]

    ty = ry + 12
    for l_text, is_bold, sz, align in lines:
        font = font_mono(sz)
        if align == "center":
            draw.text((rx + 25, ty), l_text, fill="#1e293b", font=font)
        else:
            draw.text((rx + 20, ty), l_text, fill="#1e293b", font=font)
        ty += 16

    # Barcode representation
    bar_y = ty + 10
    draw.rectangle([rx + 60, bar_y, rx + rw - 60, bar_y + 40], fill="#0f172a")
    for bx in range(rx + 65, rx + rw - 65, 8):
        draw.line([bx, bar_y, bx, bar_y + 40], fill="#ffffff", width=2)
    draw.text((rx + 115, bar_y + 45), "*CWG-20261026-0084*", fill="#334155", font=font_mono(10))

    # Modal Action Buttons
    btn_y = my + mh - 60
    draw.rounded_rectangle([mx + 20, btn_y, mx + 160, btn_y + 42], radius=6, fill="#f1f5f9", outline="#cbd5e1")
    draw.text((mx + 45, btn_y + 12), "Close (Esc)", fill="#475569", font=font_bold(12))

    draw.rounded_rectangle([mx + 175, btn_y, mx + 310, btn_y + 42], radius=6, fill="#eff6ff", outline="#93c5fd")
    draw.text((mx + 195, btn_y + 12), "✉ Email Receipt", fill=PRIMARY, font=font_bold(12))

    draw.rounded_rectangle([mx + 325, btn_y, mx + mw - 20, btn_y + 42], radius=6, fill="#10b981")
    draw.text((mx + 342, btn_y + 12), "🖨 Print ESC/POS 80mm", fill=TEXT_WHITE, font=font_bold(12))

    out_file = IMG_DIR / "fig_3_33_pos_receipt.png"
    img.save(out_file)
    shutil.copy(out_file, ARTIFACT_DIR / "fig_3_33_pos_receipt.png")
    print(f"Generated {out_file}")

# ==============================================================================
# Screen 4: Figure 3.34 - Inventory Adjustment & Restocking Modal Workflow
# ==============================================================================
def render_fig_3_34():
    # Base is Inventory screen with darkened overlay
    img, draw = create_base("Inventory")

    # Dark overlay
    overlay = Image.new("RGBA", (W, H), (15, 23, 42, 160))
    img.paste(overlay, (0, 0), overlay)
    draw = ImageDraw.Draw(img)

    # Active Modal Dialog (640px x 680px)
    mw, mh = 640, 680
    mx = (W - mw) // 2
    my = (H - mh) // 2

    draw.rounded_rectangle([mx, my, mx + mw, my + mh], radius=10, fill="#ffffff", outline="#cbd5e1")

    # Header
    draw.rectangle([mx, my, mx + mw, my + 54], fill="#f8fafc")
    draw.text((mx + 24, my + 16), "Record Stock Inflow / Inventory Adjustment", fill=TEXT_DARK, font=font_bold(16))
    draw.text((mx + mw - 35, my + 16), "✖", fill="#94a3b8", font=font_bold(16))
    draw.line([mx, my + 54, mx + mw, my + 54], fill="#e2e8f0", width=1)

    # Form Content
    fy = my + 75

    # 1. Product Selection
    draw.text((mx + 30, fy), "Target Product *", fill=TEXT_DARK, font=font_bold(12))
    draw.rounded_rectangle([mx + 30, fy + 22, mx + mw - 30, fy + 62], radius=6, fill="#f8fafc", outline="#cbd5e1")
    draw.text((mx + 45, fy + 33), "Dangote Granulated Sugar 50kg Bag (SKU: DAN-SUG-50KG)", fill=TEXT_DARK, font=font_bold(13))

    # Current stock indicator
    fy += 80
    draw.rounded_rectangle([mx + 30, fy, mx + 300, fy + 50], radius=6, fill="#fffbeb", outline="#fde68a")
    draw.text((mx + 42, fy + 10), "Current On-Hand Stock:", fill="#92400e", font=font_reg(11))
    draw.text((mx + 42, fy + 26), "8 bags (Low-Stock Alert Triggered)", fill="#b45309", font=font_bold(12))

    draw.rounded_rectangle([mx + 330, fy, mx + mw - 30, fy + 50], radius=6, fill="#ecfdf5", outline="#a7f3d0")
    draw.text((mx + 342, fy + 10), "Calculated New Balance:", fill="#065f46", font=font_reg(11))
    draw.text((mx + 342, fy + 26), "33 bags (Safe Level)", fill="#047857", font=font_bold(12))

    # 2. Adjustment Type & Quantity Row
    fy += 68
    draw.text((mx + 30, fy), "Adjustment Movement Type *", fill=TEXT_DARK, font=font_bold(12))
    draw.rounded_rectangle([mx + 30, fy + 22, mx + 300, fy + 62], radius=6, fill="#ffffff", outline="#cbd5e1")
    draw.text((mx + 45, fy + 33), "Stock Inflow (Restock Delivery)  ▼", fill="#047857", font=font_bold(12))

    draw.text((mx + 330, fy), "Quantity Received (Units) *", fill=TEXT_DARK, font=font_bold(12))
    draw.rounded_rectangle([mx + 330, fy + 22, mx + mw - 30, fy + 62], radius=6, fill="#ffffff", outline="#2563eb")
    draw.text((mx + 345, fy + 33), "+ 25 bags", fill="#2563eb", font=font_bold(14))

    # 3. Unit Purchase Cost & Batch Valuation
    fy += 80
    draw.text((mx + 30, fy), "Unit Purchase Cost (NGN) *", fill=TEXT_DARK, font=font_bold(12))
    draw.rounded_rectangle([mx + 30, fy + 22, mx + 300, fy + 62], radius=6, fill="#ffffff", outline="#cbd5e1")
    draw.text((mx + 45, fy + 33), "₦38,500.00", fill=TEXT_DARK, font=font_bold(13))

    draw.text((mx + 330, fy), "Total Inflow Valuation (NGN)", fill=TEXT_DARK, font=font_bold(12))
    draw.rounded_rectangle([mx + 330, fy + 22, mx + mw - 30, fy + 62], radius=6, fill="#f8fafc", outline="#cbd5e1")
    draw.text((mx + 345, fy + 33), "₦962,500.00", fill="#047857", font=font_bold(14))

    # 4. Supplier Waybill & Reference
    fy += 80
    draw.text((mx + 30, fy), "Supplier / Waybill Reference No.", fill=TEXT_DARK, font=font_bold(12))
    draw.rounded_rectangle([mx + 30, fy + 22, mx + mw - 30, fy + 62], radius=6, fill="#ffffff", outline="#cbd5e1")
    draw.text((mx + 45, fy + 33), "WB-DAN-2026-0942 (Dangote Sugar Refinery)", fill=TEXT_DARK, font=font_reg(13))

    # 5. Audit Trail Reason Note
    fy += 80
    draw.text((mx + 30, fy), "Audit Trail Justification / Reason *", fill=TEXT_DARK, font=font_bold(12))
    draw.rounded_rectangle([mx + 30, fy + 22, mx + mw - 30, fy + 90], radius=6, fill="#ffffff", outline="#cbd5e1")
    draw.text((mx + 42, fy + 32), "Q4 inventory restock batch delivered via Dangote Apapa Depot truck.", fill="#334155", font=font_reg(12))
    draw.text((mx + 42, fy + 52), "Physical count verified by Aisha Bello (Store Manager). Zero damages recorded.", fill="#64748b", font=font_reg(11))

    # Modal Action Buttons Footer
    btn_y = my + mh - 70
    draw.line([mx, btn_y - 15, mx + mw, btn_y - 15], fill="#e2e8f0", width=1)

    draw.rounded_rectangle([mx + mw - 310, btn_y, mx + mw - 200, btn_y + 44], radius=6, fill="#f1f5f9", outline="#cbd5e1")
    draw.text((mx + mw - 280, btn_y + 14), "Cancel", fill="#475569", font=font_bold(12))

    draw.rounded_rectangle([mx + mw - 185, btn_y, mx + mw - 30, btn_y + 44], radius=6, fill="#10b981")
    draw.text((mx + mw - 170, btn_y + 14), "✓ Commit Stock Intake", fill=TEXT_WHITE, font=font_bold(12))

    out_file = IMG_DIR / "fig_3_34_pos_inventory_adjustment.png"
    img.save(out_file)
    shutil.copy(out_file, ARTIFACT_DIR / "fig_3_34_pos_inventory_adjustment.png")
    print(f"Generated {out_file}")

# ==============================================================================
# Screen 5: Figure 3.35 - Real-Time Business Intelligence & Financial Reports Dashboard
# ==============================================================================
def render_fig_3_35():
    img, draw = create_base("Reports")

    # Header & Date Filter
    draw.text((SIDEBAR_W + 24, 20), "Financial & Inventory Analytics", fill=TEXT_DARK, font=font_bold(18))

    draw.rounded_rectangle([W - 380, 16, W - 180, 48], radius=6, fill="#ffffff", outline="#cbd5e1")
    draw.text((W - 365, 24), "📅  Oct 18, 2026 - Nov 16, 2026  ▼", fill="#334155", font=font_bold(11))

    draw.rounded_rectangle([W - 165, 16, W - 24, 48], radius=6, fill=PRIMARY)
    draw.text((W - 150, 24), "⭳ Download PDF", fill=TEXT_WHITE, font=font_bold(11))

    # Reports Tabs Bar
    top_y = TOPBAR_H + 20
    draw.rounded_rectangle([SIDEBAR_W + 24, top_y, W - 24, top_y + 50], radius=8, fill="#ffffff", outline="#e2e8f0")

    tabs = [
        ("Sales Analytics (Active)", True),
        ("Product Performance", False),
        ("Inventory Valuation", False),
        ("Cashier Audits", False),
        ("Security Activity Logs", False)
    ]
    curr_tx = SIDEBAR_W + 36
    for t_name, is_act in tabs:
        tw = len(t_name) * 8 + 20
        if is_act:
            draw.rounded_rectangle([curr_tx, top_y + 8, curr_tx + tw, top_y + 42], radius=6, fill=PRIMARY)
            draw.text((curr_tx + 12, top_y + 16), t_name, fill=TEXT_WHITE, font=font_bold(11))
        else:
            draw.text((curr_tx + 12, top_y + 16), t_name, fill="#64748b", font=font_bold(11))
        curr_tx += tw + 16

    # 4 KPI Stat Metric Cards
    cards_y = top_y + 65
    card_w = (W - SIDEBAR_W - 48 - 60) // 4
    card_h = 115

    kpis = [
        ("TOTAL REVENUE", "₦4,825,400.00", "+14.8% vs last month", "#047857", "#ecfdf5", "342 completed sales"),
        ("COST OF GOODS (COGS)", "₦3,704,750.00", "76.8% of turnover", "#475569", "#f1f5f9", "Inventory replenishment"),
        ("GROSS PROFIT", "₦1,120,650.00", "23.2% Net Margin", "#047857", "#ecfdf5", "Positive retail cashflow"),
        ("AVERAGE ORDER (AOV)", "₦14,109.35", "+3.4% basket growth", "#1d4ed8", "#eff6ff", "14 items catalogue")
    ]

    for idx, (label, val, badge, bfg, bbg, sub) in enumerate(kpis):
        cx = SIDEBAR_W + 24 + idx * (card_w + 20)
        draw.rounded_rectangle([cx, cards_y, cx + card_w, cards_y + card_h], radius=8, fill="#ffffff", outline="#e2e8f0")

        draw.text((cx + 16, cards_y + 14), label, fill="#64748b", font=font_bold(11))
        draw.text((cx + 16, cards_y + 36), val, fill=TEXT_DARK, font=font_bold(18))

        draw.rounded_rectangle([cx + 16, cards_y + 70, cx + 16 + len(badge) * 7 + 10, cards_y + 92], radius=10, fill=bbg)
        draw.text((cx + 22, cards_y + 74), badge, fill=bfg, font=font_bold(10))
        draw.text((cx + 16 + len(badge) * 7 + 18, cards_y + 74), sub, fill="#94a3b8", font=font_reg(10))

    # Main Visual Analytics Split View
    chart_y = cards_y + card_h + 20

    # Left Container: Revenue Bar / Trend Chart (60% width = 670px)
    left_w = 680
    draw.rounded_rectangle([SIDEBAR_W + 24, chart_y, SIDEBAR_W + 24 + left_w, H - 24], radius=8, fill="#ffffff", outline="#e2e8f0")

    draw.text((SIDEBAR_W + 44, chart_y + 20), "Weekly Revenue & Turnout Trends (October - November 2026)", fill=TEXT_DARK, font=font_bold(14))
    draw.text((SIDEBAR_W + 44, chart_y + 40), "Daily gross turnover across all cashier stations", fill="#64748b", font=font_reg(11))

    # Draw Bar Chart Grid & Bars
    chart_base_y = H - 80
    chart_top_y = chart_y + 80
    draw.line([SIDEBAR_W + 80, chart_base_y, SIDEBAR_W + 24 + left_w - 40, chart_base_y], fill="#cbd5e1", width=1)

    # Gridlines
    for gy, glabel in [(chart_base_y - 60, "₦200k"), (chart_base_y - 120, "₦400k"), (chart_base_y - 180, "₦600k"), (chart_base_y - 240, "₦800k")]:
        draw.line([SIDEBAR_W + 80, gy, SIDEBAR_W + 24 + left_w - 40, gy], fill="#f1f5f9", width=1)
        draw.text((SIDEBAR_W + 35, gy - 7), glabel, fill="#94a3b8", font=font_reg(10))

    # Daily Bars (Mon - Sun for 2 weeks)
    days_data = [
        ("Mon", 140, "₦340k"),
        ("Tue", 175, "₦420k"),
        ("Wed", 155, "₦380k"),
        ("Thu", 195, "₦480k"),
        ("Fri", 270, "₦680k"),
        ("Sat", 310, "₦790k"),
        ("Sun", 220, "₦540k"),
        ("Mon", 160, "₦390k"),
        ("Tue", 185, "₦450k"),
        ("Wed", 170, "₦410k"),
        ("Thu", 210, "₦520k"),
        ("Fri", 290, "₦720k"),
    ]

    bx = SIDEBAR_W + 95
    bar_width = 34
    for day_lbl, bar_h, rev_str in days_data:
        draw.rounded_rectangle([bx, chart_base_y - bar_h, bx + bar_width, chart_base_y], radius=4, fill="#3b82f6")
        draw.text((bx + 2, chart_base_y + 8), day_lbl, fill="#64748b", font=font_bold(10))
        draw.text((bx - 4, chart_base_y - bar_h - 18), rev_str, fill="#0f172a", font=font_bold(9))
        bx += 46

    # Right Container: Top Performing Products (40% width = 410px)
    right_x = SIDEBAR_W + 24 + left_w + 20
    right_w = W - right_x - 24
    draw.rounded_rectangle([right_x, chart_y, right_x + right_w, H - 24], radius=8, fill="#ffffff", outline="#e2e8f0")

    draw.text((right_x + 20, chart_y + 20), "Top Selling Products", fill=TEXT_DARK, font=font_bold(14))
    draw.text((right_x + 20, chart_y + 40), "Ranked by total monthly sales revenue", fill="#64748b", font=font_reg(11))

    top_sellers = [
        ("Nestlé Milo 500g", "212 units sold", "₦890,400", "#14532d"),
        ("Dangote Sugar 50kg", "16 bags sold", "₦704,000", "#1e293b"),
        ("Indomie Onion Ctn", "60 ctns sold", "₦588,000", "#991b1b"),
        ("Golden Penny Semo", "140 packs sold", "₦434,000", "#78350f"),
        ("Peak Evap Milk", "600 tins sold", "₦390,000", "#1e3a8a"),
        ("Dano Milk 800g", "68 pouches sold", "₦367,200", "#0369a1"),
    ]

    ty = chart_y + 75
    for idx, (pname, units, rev, cbg) in enumerate(top_sellers):
        draw.rounded_rectangle([right_x + 16, ty, right_x + right_w - 16, ty + 50], radius=6, fill="#f8fafc", outline="#f1f5f9")
        # Rank pill
        draw.ellipse([right_x + 24, ty + 12, right_x + 50, ty + 38], fill=cbg)
        draw.text((right_x + 33, ty + 16), str(idx + 1), fill=TEXT_WHITE, font=font_bold(12))

        # Title & units
        draw.text((right_x + 60, ty + 8), pname, fill=TEXT_DARK, font=font_bold(12))
        draw.text((right_x + 60, ty + 26), units, fill="#64748b", font=font_reg(11))

        # Revenue
        draw.text((right_x + right_w - 110, ty + 16), rev, fill="#047857", font=font_bold(13))
        ty += 58

    out_file = IMG_DIR / "fig_3_35_pos_reports_dashboard.png"
    img.save(out_file)
    shutil.copy(out_file, ARTIFACT_DIR / "fig_3_35_pos_reports_dashboard.png")
    print(f"Generated {out_file}")

if __name__ == "__main__":
    render_fig_3_32()
    render_fig_3_32b()
    render_fig_3_33()
    render_fig_3_34()
    render_fig_3_35()
    print("All 5 publication-grade POS UI figures generated successfully!")
