"""
Blu Report Template — sistema visual minimalista de Blu Studio Inc.

Copiá este archivo al scratchpad de la sesión, editá las constantes del top y
reescribí `build_story()` con el contenido del informe. No toques el resto:
el header, footer y estilos ya están calibrados.

El logo oficial viene embebido en base64 (constante BLU_LOGO_SVG_B64) y se
renderiza con svglib + reportlab.graphics. No uses texto "Blu." en Helvetica:
siempre invocá draw_blu_logo() para mantener el branding correcto.

Uso:
    cp /sessions/<id>/mnt/.claude/skills/blu-report/assets/blu_report_template.py \
       /sessions/<id>/generate_report.py
    # editá generate_report.py
    python /sessions/<id>/generate_report.py
"""
import base64
import io

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, PageBreak, KeepTogether, NextPageTemplate
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

# ============================================================================
# CONFIGURACIÓN DEL DOCUMENTO — editá solamente esto
# ============================================================================
OUTPUT         = "/sessions/<id>/mnt/<folder>/Informe-Ejemplo-YYYY-MM-DD.pdf"
DOC_TITLE      = "Informe Semanal SEO"       # Título grande arriba a la derecha
DOC_NUMBER     = "2"                          # N° de documento
PROJECT        = "Abr: Nombre del Proyecto"   # Proyecto
CLIENT         = "Nombre del Cliente"         # Cliente
CLIENT_EMAIL   = "<info@cliente.com>"         # Email del cliente (con <>)
PERIOD         = "12/03/2026 — 08/04/2026"    # Período del informe
COMPARE_PERIOD = "12/02/2026 — 11/03/2026"    # Período de comparación (vacío si no aplica)
FOOTER_TEXT    = "Reporte semanal de SEO y performance del período indicado."

# ============================================================================
# LOGO OFICIAL BLU (SVG embebido en base64)
# Bounding box ajustado al acrónimo "B." — aspect ratio ≈ 1.078 (casi cuadrado).
# No modificar. Si hace falta cambiar el logo, regenerar la constante con:
#     python3 -c "import base64; print(base64.b64encode(open('blu-logo.svg','rb').read()).decode())"
# ============================================================================
BLU_LOGO_SVG_B64 = (
    "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB4bWxucz0iaHR0"
    "cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NTQuMDAgNDIxLjA1Ij4K"
    "ICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNzMzLjAwLC0zMjYuODApIj4KICAgIDxwYXRo"
    "IGQ9Ik0xMDcwLjEyLDU4NC4zOGMtMy43OC0xMS41MS04Ljk0LTIxLjY0LTE1LjQ5LTMwLjM4"
    "LTYuNTUtOC43My0xNC4yLTE2LjA5LTIyLjk0LTIyLjA0LTguNzQtNS45Ni0xOC4wOC0xMC41"
    "Mi0yOC0xMy43LDEyLjcxLTYuNzUsMjIuOTQtMTYuNTgsMzAuNjgtMjkuNDksNy43NS0xMi45"
    "LDExLjYyLTI5LjQ5LDExLjYyLTQ5Ljc1LDAtMTYuMjgtMi41OS0zMS4wNy03Ljc1LTQ0LjM4"
    "LTUuMTctMTMuMzEtMTIuNTEtMjQuOTItMjIuMDQtMzQuODYtOS41My05LjkyLTIxLjE1LTE3"
    "LjU4LTM0Ljg1LTIyLjk0LTEzLjctNS4zNi0yOS4xLTguMDQtNDYuMTctOC4wNGgtMjAwLjE4"
    "djM0OC41Mmg3NC40NXY2OC41M2gxNDIuNDFjMTkuMDYsMCwzNi4yNC0yLjk4LDUxLjUzLTgu"
    "OTQsMTUuMjktNS45NiwyOC4zLTE0LjM5LDM5LjAyLTI1LjMyLDEwLjcyLTEwLjkyLDE4Ljk2"
    "LTIzLjgzLDI0LjcyLTM4LjczLDUuNzYtMTQuOSw4LjY0LTMxLjI4LDguNjQtNDkuMTUsMC0x"
    "NC42OS0xLjg5LTI3LjgtNS42Ni0zOS4zMlpNODA5LjQ2LDM5Ny4zMWgxMTYuMThjMTMuOSww"
    "LDI1LjAyLDQuMTcsMzMuMzYsMTIuNTEsOC4zNCw4LjM0LDEyLjUxLDE5LjY2LDEyLjUxLDMz"
    "Ljk2cy00LjE3LDI1LjAyLTEyLjUxLDMzLjM2Yy04LjM0LDguMzQtMTkuNDcsMTIuNTEtMzMu"
    "MzYsMTIuNTFoLTExNi4xOHYtOTIuMzRaTTk4NS4yMiw2NjEuMjRjLTEwLjcyLDEwLjcyLTI1"
    "LjAyLDE2LjA5LTQyLjksMTYuMDloLTEzMi44NnYtMTE5LjE1aDEzMi44NmMxNy44NywwLDMy"
    "LjE3LDUuNDYsNDIuOSwxNi4zOCwxMC43MiwxMC45MywxNi4wOSwyNS41MiwxNi4wOSw0My43"
    "OXMtNS4zNiwzMi4xNy0xNi4wOSw0Mi45WiIvPgogICAgPHJlY3QgeD0iMTExMy41MSIgeT0i"
    "NjczLjQ1IiB3aWR0aD0iNzEuNDkiIGhlaWdodD0iNjguNTEiLz4KICA8L2c+Cjwvc3ZnPgo="
)

_LOGO_CACHE = {}

def _load_logo():
    if "rlg" not in _LOGO_CACHE:
        svg_bytes = base64.b64decode(BLU_LOGO_SVG_B64)
        _LOGO_CACHE["rlg"] = svg2rlg(io.BytesIO(svg_bytes))
    return _LOGO_CACHE["rlg"]


def draw_blu_logo(canv, x, y, height, color=None):
    """
    Dibuja el logo oficial Blu sobre el canvas.
      x, y   — esquina inferior-izquierda del logo (en puntos).
      height — alto deseado en puntos. El ancho se calcula manteniendo el
               aspect ratio real del logo (≈1.078).
      color  — opcional: si se pasa un reportlab.lib.colors.Color, el logo
               se dibuja en ese color (útil para el logo gris del footer).
               Default: negro tal como viene en el SVG.
    """
    logo = _load_logo()
    scale = height / logo.height
    canv.saveState()
    canv.translate(x, y)
    canv.scale(scale, scale)
    if color is not None:
        # Aplicar color a todos los shapes del Drawing
        from reportlab.graphics.shapes import Path, Rect, Group
        def tint(node):
            if hasattr(node, "fillColor"):
                node.fillColor = color
            if hasattr(node, "strokeColor") and node.strokeColor is not None:
                node.strokeColor = color
            if hasattr(node, "contents"):
                for child in node.contents:
                    tint(child)
        tint(logo)
    renderPDF.draw(logo, canv, 0, 0)
    canv.restoreState()


def logo_width_for_height(height):
    """Devuelve el ancho (en puntos) que tendrá el logo a la altura dada."""
    logo = _load_logo()
    return height * (logo.width / logo.height)


# ============================================================================
# SISTEMA VISUAL — no modificar salvo ajustes finos
# ============================================================================
BLACK          = colors.HexColor("#0a0a0a")
TEXT           = colors.HexColor("#1a1a1a")
MUTED          = colors.HexColor("#6b6b6b")
LIGHT_LINE     = colors.HexColor("#e5e5e5")
BG_LIGHT       = colors.HexColor("#f7f7f5")
GREEN_OK       = colors.HexColor("#dcfce7")
GREEN_OK_TEXT  = colors.HexColor("#15803d")
AMBER          = colors.HexColor("#fef3c7")
AMBER_TEXT     = colors.HexColor("#a16207")
RED_BG         = colors.HexColor("#fee2e2")
RED_TEXT       = colors.HexColor("#b91c1c")
FOOTER_LOGO_GRAY = colors.HexColor("#d4d4d4")

PAGE_W, PAGE_H = A4
MARGIN_L = 22 * mm
MARGIN_R = 22 * mm
MARGIN_T = 70 * mm
MARGIN_B = 30 * mm
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

styles = getSampleStyleSheet()

H1 = ParagraphStyle('H1', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=14, textColor=BLACK,
    spaceBefore=14, spaceAfter=8, leading=18)

H2 = ParagraphStyle('H2', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=10, textColor=MUTED,
    spaceBefore=12, spaceAfter=6, leading=12)

BODY = ParagraphStyle('BODY', parent=styles['Normal'],
    fontName='Helvetica', fontSize=9.5, textColor=TEXT,
    leading=14, spaceAfter=6, alignment=TA_JUSTIFY)

BODY_LEFT = ParagraphStyle('BODY_LEFT', parent=BODY, alignment=TA_LEFT)

SMALL = ParagraphStyle('SMALL', parent=styles['Normal'],
    fontName='Helvetica', fontSize=8, textColor=MUTED, leading=11)

KPI_NUM = ParagraphStyle('KPI_NUM', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=15, textColor=BLACK, leading=18,
    alignment=TA_LEFT)

KPI_LABEL = ParagraphStyle('KPI_LABEL', parent=styles['Normal'],
    fontName='Helvetica', fontSize=7.5, textColor=MUTED, leading=10,
    alignment=TA_LEFT)

CELL = ParagraphStyle('CELL', parent=BODY_LEFT,
    fontName='Helvetica', fontSize=9, leading=12, spaceAfter=0)

CELL_BOLD = ParagraphStyle('CELL_BOLD', parent=CELL,
    fontName='Helvetica-Bold')


def P(text, style=CELL):
    return Paragraph(text, style)


# ============================================================================
# HEADER / FOOTER (canvas drawing)
# ============================================================================
HEADER_LOGO_H  = 18 * mm    # Alto del logo grande en la primera página
MINI_LOGO_H    = 7 * mm     # Alto del logo chico en las páginas siguientes
FOOTER_LOGO_H  = 11 * mm    # Alto del logo gris del footer

def draw_first_page(canv, doc):
    canv.saveState()

    # Logo Blu grande arriba a la izquierda
    draw_blu_logo(canv, MARGIN_L, PAGE_H - 14*mm - HEADER_LOGO_H, HEADER_LOGO_H)

    # "DOCUMENTO" label arriba a la derecha
    canv.setFont("Helvetica", 8)
    canv.setFillColor(MUTED)
    canv.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 22 * mm, "DOCUMENTO")

    canv.setFont("Helvetica-Bold", 22)
    canv.setFillColor(BLACK)
    canv.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 30 * mm, DOC_TITLE)

    canv.setFont("Helvetica", 8)
    canv.setFillColor(MUTED)
    canv.drawRightString(PAGE_W - MARGIN_R - 12, PAGE_H - 36 * mm, "N°  ")
    canv.setFont("Helvetica-Bold", 9)
    canv.setFillColor(BLACK)
    canv.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 36 * mm, DOC_NUMBER)

    meta_y = PAGE_H - 46 * mm
    line_h = 4.2 * mm
    metas = [
        ("Proyecto: ", PROJECT),
        ("Para: ", CLIENT),
        ("", CLIENT_EMAIL),
        ("Período: ", PERIOD),
    ]
    if COMPARE_PERIOD:
        metas.append(("Comparado con: ", COMPARE_PERIOD))

    for i, (label, value) in enumerate(metas):
        y = meta_y - i * line_h
        canv.setFont("Helvetica-Bold", 8.5)
        canv.setFillColor(BLACK)
        bold_w = canv.stringWidth(value, "Helvetica-Bold", 8.5)
        canv.drawString(PAGE_W - MARGIN_R - bold_w, y, value)
        canv.setFont("Helvetica", 8.5)
        canv.setFillColor(MUTED)
        label_w = canv.stringWidth(label, "Helvetica", 8.5)
        canv.drawString(PAGE_W - MARGIN_R - bold_w - label_w, y, label)

    canv.setStrokeColor(LIGHT_LINE)
    canv.setLineWidth(0.5)
    canv.line(MARGIN_L, PAGE_H - MARGIN_T + 4*mm,
              PAGE_W - MARGIN_R, PAGE_H - MARGIN_T + 4*mm)

    draw_footer(canv)
    canv.restoreState()


def draw_later_page(canv, doc):
    canv.saveState()

    # Mini-logo arriba a la izquierda
    draw_blu_logo(canv, MARGIN_L, PAGE_H - 14*mm - MINI_LOGO_H*0.2, MINI_LOGO_H)

    # Título corto arriba a la derecha
    canv.setFont("Helvetica", 8)
    canv.setFillColor(MUTED)
    canv.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 18 * mm,
                         f"{DOC_TITLE}  ·  N° {DOC_NUMBER}  ·  {CLIENT}")

    # Línea separadora
    canv.setStrokeColor(LIGHT_LINE)
    canv.setLineWidth(0.5)
    canv.line(MARGIN_L, PAGE_H - 22 * mm, PAGE_W - MARGIN_R, PAGE_H - 22 * mm)

    draw_footer(canv)
    canv.restoreState()


def draw_footer(canv):
    fy = 22 * mm
    canv.setStrokeColor(LIGHT_LINE)
    canv.setLineWidth(0.5)
    canv.line(MARGIN_L, fy + 4 * mm, PAGE_W - MARGIN_R, fy + 4 * mm)

    canv.setFillColor(MUTED)
    canv.setFont("Helvetica", 7.5)
    canv.drawString(MARGIN_L, fy, FOOTER_TEXT)
    canv.drawString(MARGIN_L, fy - 3.2 * mm, "Para consultas: ")
    canv.setFont("Helvetica-Bold", 7.5)
    canv.setFillColor(BLACK)
    canv.drawString(MARGIN_L + canv.stringWidth("Para consultas: ", "Helvetica", 7.5),
                    fy - 3.2 * mm, "info@blustudioinc.com")
    canv.setFont("Helvetica", 7.5)
    canv.setFillColor(MUTED)
    canv.drawString(MARGIN_L, fy - 6.4 * mm, "CUIT: 30-71909207-8")

    # Logo gris abajo a la derecha.
    # El borde superior del logo se alinea con la línea superior del texto
    # del footer (la de "Reporte semanal..."): la B "comienza" donde arranca
    # visualmente el texto de la izquierda.
    logo_w = logo_width_for_height(FOOTER_LOGO_H)
    draw_blu_logo(canv,
                  PAGE_W - MARGIN_R - logo_w,
                  fy - FOOTER_LOGO_H + 2 * mm,
                  FOOTER_LOGO_H,
                  color=FOOTER_LOGO_GRAY)

    canv.setFillColor(MUTED)
    canv.setFont("Helvetica", 7)
    canv.drawCentredString(PAGE_W / 2, 10 * mm, f"Página {canv.getPageNumber()}")


# ============================================================================
# COMPONENTES REUTILIZABLES
# ============================================================================
def section_header(text):
    return Paragraph(text.upper(), H2)


def kpi_cards(cards):
    """
    cards: lista de (label, value, delta_text, positive_bool)
    """
    labels, values, deltas = [], [], []
    for label, value, delta, positive in cards:
        color = "#15803d" if positive else "#b91c1c"
        labels.append(Paragraph(label, KPI_LABEL))
        values.append(Paragraph(value, KPI_NUM))
        deltas.append(Paragraph(
            f'<font color="{color}"><b>{delta}</b></font>', KPI_LABEL))

    col_w = CONTENT_W / len(cards)
    t = Table([labels, values, deltas],
              colWidths=[col_w] * len(cards),
              rowHeights=[5 * mm, 9 * mm, 5 * mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BG_LIGHT),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LINEAFTER', (0, 0), (-2, -1), 0.4, colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t


def comparison_table(headers, rows, delta_col_index=-1, positive_rows=None):
    data = [headers] + rows
    col_count = len(headers)
    first_w = CONTENT_W * 0.42
    rest_w = (CONTENT_W - first_w) / (col_count - 1)
    col_widths = [first_w] + [rest_w] * (col_count - 1)

    style = [
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 7.5),
        ('TEXTCOLOR', (0, 0), (-1, 0), MUTED),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 9),
        ('TEXTCOLOR', (0, 1), (-1, -1), TEXT),
        ('LINEBELOW', (0, 0), (-1, 0), 0.6, BLACK),
        ('LINEBELOW', (0, 1), (-1, -2), 0.3, LIGHT_LINE),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONT', (delta_col_index, 1), (delta_col_index, -1), 'Helvetica-Bold', 9),
    ]
    for i, _ in enumerate(rows):
        row_idx = i + 1
        is_positive = positive_rows is None or i in positive_rows
        color = GREEN_OK_TEXT if is_positive else RED_TEXT
        style.append(('TEXTCOLOR', (delta_col_index, row_idx),
                      (delta_col_index, row_idx), color))

    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle(style))
    return t


def status_table(headers, rows):
    data = [headers] + rows
    col_count = len(headers)
    status_w = 30 * mm
    index_w = 8 * mm if headers[0] in ("#", "Nº", "N°") else 0
    remaining = CONTENT_W - status_w - index_w
    text_cols = col_count - (2 if index_w else 1)
    text_w = remaining / text_cols

    widths = []
    if index_w:
        widths.append(index_w)
    widths += [text_w] * text_cols
    widths.append(status_w)

    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 7.5),
        ('TEXTCOLOR', (0, 0), (-1, 0), MUTED),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 9),
        ('TEXTCOLOR', (0, 1), (-1, -1), TEXT),
        ('TEXTCOLOR', (0, 1), (0, -1), MUTED),
        ('LINEBELOW', (0, 0), (-1, 0), 0.6, BLACK),
        ('LINEBELOW', (0, 1), (-1, -2), 0.3, LIGHT_LINE),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (-1, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (-1, 1), (-1, -1), GREEN_OK),
        ('TEXTCOLOR', (-1, 1), (-1, -1), GREEN_OK_TEXT),
        ('FONT', (-1, 1), (-1, -1), 'Helvetica-Bold', 8),
    ]))
    return t


# ============================================================================
# CONTENIDO — reescribí esta función para cada informe
# ============================================================================
def build_story():
    story = []
    story.append(NextPageTemplate('later'))

    story.append(Paragraph("Resumen ejecutivo", H1))
    story.append(Paragraph(
        "Párrafo corto con el mensaje principal del informe. Resaltá con "
        "<b>bold</b> lo más importante.",
        BODY))

    story.append(Spacer(1, 4))
    story.append(kpi_cards([
        ("MÉTRICA 1", "906", "+110,7 %", True),
        ("MÉTRICA 2", "$291,5 M", "+1.287 %", True),
        ("MÉTRICA 3", "0,43 %", "+233 %", True),
        ("MÉTRICA 4", "35 s", "+48,8 %", True),
    ]))

    story.append(section_header("Sección"))
    story.append(Paragraph("Párrafo de contexto.", BODY))
    story.append(comparison_table(
        headers=["INDICADOR", "ANTES", "HOY", "VARIACIÓN"],
        rows=[
            ["Sesiones", "296.786", "185.338", "−37,55 %"],
            ["Conversiones", "430", "906", "+110,70 %"],
            ["Ingresos", "$21,0 M", "$291,5 M", "+1.287,8 %"],
        ],
        positive_rows=[1, 2],
    ))

    story.append(KeepTogether([
        section_header("Conclusión"),
        Paragraph("Párrafo de cierre.", BODY),
    ]))

    return story


def main():
    doc = BaseDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=MARGIN_L, rightMargin=MARGIN_R,
        topMargin=MARGIN_T, bottomMargin=MARGIN_B,
        title=f"{DOC_TITLE} N°{DOC_NUMBER} - {CLIENT}",
        author="Blu Studio Inc.",
    )

    first_frame = Frame(MARGIN_L, MARGIN_B,
                        CONTENT_W, PAGE_H - MARGIN_T - MARGIN_B,
                        leftPadding=0, rightPadding=0,
                        topPadding=0, bottomPadding=0)
    later_frame = Frame(MARGIN_L, MARGIN_B,
                        CONTENT_W, PAGE_H - 30 * mm - MARGIN_B,
                        leftPadding=0, rightPadding=0,
                        topPadding=4, bottomPadding=0)

    doc.addPageTemplates([
        PageTemplate(id='first', frames=[first_frame], onPage=draw_first_page),
        PageTemplate(id='later', frames=[later_frame], onPage=draw_later_page),
    ])

    doc.build(build_story())
    print(f"OK: {OUTPUT}")


if __name__ == "__main__":
    main()
