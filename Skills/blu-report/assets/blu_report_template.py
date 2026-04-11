"""
Blu Report Template — sistema visual minimalista de Blu Studio Inc.

Copiá este archivo al scratchpad de la sesión, editá las constantes del top y
reescribí `build_story()` con el contenido del informe. No toques el resto:
el header, footer y estilos ya están calibrados.

Uso:
    cp /sessions/<id>/mnt/.claude/skills/blu-report/assets/blu_report_template.py \
       /sessions/<id>/generate_report.py
    # editá generate_report.py
    python /sessions/<id>/generate_report.py
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, PageBreak, KeepTogether, NextPageTemplate
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY

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
COMPARE_PERIOD = "12/02/2026 — 11/03/2026"    # Período de comparación (opcional, dejar "" si no aplica)
FOOTER_TEXT    = "Reporte semanal de SEO y performance del período indicado."

# ============================================================================
# SISTEMA VISUAL — no modificar salvo para ajustes finos
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

PAGE_W, PAGE_H = A4
MARGIN_L = 22 * mm
MARGIN_R = 22 * mm
MARGIN_T = 70 * mm    # Espacio para el header grande de la primera página
MARGIN_B = 30 * mm
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

styles = getSampleStyleSheet()

H1 = ParagraphStyle('H1', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=14, textColor=BLACK,
    spaceBefore=18, spaceAfter=10, leading=18)

H2 = ParagraphStyle('H2', parent=styles['Normal'],
    fontName='Helvetica-Bold', fontSize=10, textColor=MUTED,
    spaceBefore=14, spaceAfter=6, leading=12)

BODY = ParagraphStyle('BODY', parent=styles['Normal'],
    fontName='Helvetica', fontSize=9.5, textColor=TEXT,
    leading=14, spaceAfter=6, alignment=TA_JUSTIFY)

BODY_LEFT = ParagraphStyle('BODY_LEFT', parent=BODY, alignment=TA_LEFT)

SMALL = ParagraphStyle('SMALL', parent=styles['Normal'],
    fontName='Helvetica', fontSize=8, textColor=MUTED, leading=11)

LABEL = ParagraphStyle('LABEL', parent=styles['Normal'],
    fontName='Helvetica', fontSize=7.5, textColor=MUTED, leading=10)

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
    """Helper: envolvé texto de celda en Paragraph para que haga wrap."""
    return Paragraph(text, style)


# ============================================================================
# HEADER / FOOTER (canvas drawing)
# ============================================================================
def draw_first_page(canv, doc):
    canv.saveState()

    # Logo "Blu." grande arriba a la izquierda
    canv.setFillColor(BLACK)
    canv.setFont("Helvetica-Bold", 36)
    canv.drawString(MARGIN_L, PAGE_H - 32 * mm, "Blu.")

    # "DOCUMENTO" label gris arriba a la derecha
    canv.setFont("Helvetica", 8)
    canv.setFillColor(MUTED)
    canv.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 22 * mm, "DOCUMENTO")

    # Título del documento (grande, bold)
    canv.setFont("Helvetica-Bold", 22)
    canv.setFillColor(BLACK)
    canv.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 30 * mm, DOC_TITLE)

    # N° documento
    canv.setFont("Helvetica", 8)
    canv.setFillColor(MUTED)
    canv.drawRightString(PAGE_W - MARGIN_R - 12, PAGE_H - 36 * mm, "N°  ")
    canv.setFont("Helvetica-Bold", 9)
    canv.setFillColor(BLACK)
    canv.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 36 * mm, DOC_NUMBER)

    # Bloque de metadata alineado a la derecha
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

    # Línea separadora antes del contenido
    canv.setStrokeColor(LIGHT_LINE)
    canv.setLineWidth(0.5)
    canv.line(MARGIN_L, PAGE_H - MARGIN_T + 4 * mm,
              PAGE_W - MARGIN_R, PAGE_H - MARGIN_T + 4 * mm)

    draw_footer(canv)
    canv.restoreState()


def draw_later_page(canv, doc):
    canv.saveState()
    # Mini-logo arriba a la izquierda
    canv.setFillColor(BLACK)
    canv.setFont("Helvetica-Bold", 16)
    canv.drawString(MARGIN_L, PAGE_H - 18 * mm, "Blu.")

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

    # Footer text
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

    # Logo grande gris abajo a la derecha
    canv.setFillColor(colors.HexColor("#d4d4d4"))
    canv.setFont("Helvetica-Bold", 24)
    canv.drawRightString(PAGE_W - MARGIN_R, fy - 4 * mm, "Blu.")

    # Número de página
    canv.setFillColor(MUTED)
    canv.setFont("Helvetica", 7)
    canv.drawCentredString(PAGE_W / 2, 10 * mm, f"Página {canv.getPageNumber()}")


# ============================================================================
# COMPONENTES REUTILIZABLES
# ============================================================================
def section_header(text):
    """Header de sección: uppercase gris chico (el estilo clave del look Blu)."""
    return Paragraph(text.upper(), H2)


def kpi_cards(cards):
    """
    Grid de 4 KPI cards. `cards` es una lista de tuplas:
        (label, value, delta_text, delta_positive)
    Ejemplo:
        [("CONVERSIONES", "906", "+110,7 %", True),
         ("INGRESOS", "$291,5 M", "+1.287 %", True),
         ("TASA", "0,43 %", "+233 %", True),
         ("ENGAGEMENT", "35 s", "+48 %", True)]
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
    """
    Tabla de comparación antes / hoy / Δ.
    `headers`: lista de strings (ej: ["MÉTRICA", "ANTES", "HOY", "Δ"])
    `rows`: lista de listas con los datos
    `delta_col_index`: índice de la columna Δ para colorear (default: última)
    `positive_rows`: lista de índices de filas donde el delta es positivo (verde).
                     Si es None, todas se pintan verde.
                     Si es una lista, las que no están se pintan rojo.
    """
    data = [headers] + rows
    col_count = len(headers)
    # Repartir anchos: primera columna más ancha
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
        # Delta column en bold
        ('FONT', (delta_col_index, 1), (delta_col_index, -1), 'Helvetica-Bold', 9),
    ]
    # Colorear deltas
    for i, _ in enumerate(rows):
        row_idx = i + 1
        is_positive = positive_rows is None or i in positive_rows
        color = GREEN_OK_TEXT if is_positive else RED_TEXT
        style.append(('TEXTCOLOR', (delta_col_index, row_idx),
                      (delta_col_index, row_idx), color))

    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle(style))
    return t


def status_table(headers, rows, status_col_index=-1):
    """
    Tabla con chips de estado en la última columna.
    `rows`: cada fila tiene strings o Paragraphs. La última celda es el estado
            ("Verificado", "Pendiente", "En proceso", etc.)
    Pintar la columna de estado en verde.
    """
    data = [headers] + rows
    col_count = len(headers)

    # Anchos balanceados con última columna fija
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
        ('TEXTCOLOR', (0, 1), (0, -1), MUTED),  # Columna de índice en gris
        ('LINEBELOW', (0, 0), (-1, 0), 0.6, BLACK),
        ('LINEBELOW', (0, 1), (-1, -2), 0.3, LIGHT_LINE),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (status_col_index, 0), (status_col_index, -1), 'CENTER'),
        # Chip de estado
        ('BACKGROUND', (status_col_index, 1), (status_col_index, -1), GREEN_OK),
        ('TEXTCOLOR', (status_col_index, 1), (status_col_index, -1), GREEN_OK_TEXT),
        ('FONT', (status_col_index, 1), (status_col_index, -1), 'Helvetica-Bold', 8),
    ]))
    return t


# ============================================================================
# CONTENIDO — reescribí esta función para cada informe
# ============================================================================
def build_story():
    story = []
    story.append(NextPageTemplate('later'))

    # ---------- RESUMEN EJECUTIVO ----------
    story.append(Paragraph("Resumen ejecutivo", H1))
    story.append(Paragraph(
        "Párrafo corto (2-4 líneas) con el mensaje principal del informe. "
        "Resaltá con <b>bold</b> lo más importante.",
        BODY))

    story.append(Spacer(1, 4))
    story.append(kpi_cards([
        ("MÉTRICA 1", "906", "+110,7 %", True),
        ("MÉTRICA 2", "$291,5 M", "+1.287 %", True),
        ("MÉTRICA 3", "0,43 %", "+233 %", True),
        ("MÉTRICA 4", "35 s", "+48,8 %", True),
    ]))

    # ---------- SECCIÓN DE DATOS ----------
    story.append(section_header("Nombre de la sección"))
    story.append(Paragraph(
        "Párrafo de contexto que explica qué muestra la tabla siguiente.",
        BODY))

    story.append(comparison_table(
        headers=["INDICADOR", "ANTES", "HOY", "VARIACIÓN"],
        rows=[
            ["Sesiones", "296.786", "185.338", "−37,55 %"],
            ["Conversiones", "430", "906", "+110,70 %"],
            ["Ingresos", "$21,0 M", "$291,5 M", "+1.287,8 %"],
        ],
        positive_rows=[1, 2],  # filas 1 y 2 son positivas; 0 es negativa
    ))

    # ---------- TABLA DE ESTADO (fixes / acciones) ----------
    story.append(section_header("Acciones desplegadas"))
    story.append(status_table(
        headers=["#", "ACCIÓN", "DESCRIPCIÓN", "ESTADO"],
        rows=[
            ["1",
             P("Título de la acción en bold", CELL_BOLD),
             P("Descripción que puede ser larga y hacer wrap dentro de la celda.", CELL),
             "Verificado"],
            ["2",
             P("Otra acción", CELL_BOLD),
             P("Descripción.", CELL),
             "Verificado"],
        ],
    ))

    # ---------- OPORTUNIDADES ----------
    story.append(section_header("Oportunidades para el próximo período"))
    opps = [
        ("1. Título de la oportunidad.",
         "Explicación breve en 1-2 líneas de qué hacer y por qué."),
        ("2. Otra oportunidad.",
         "Otra explicación."),
    ]
    for title, desc in opps:
        story.append(Paragraph(f"<b>{title}</b>", BODY))
        story.append(Paragraph(desc, BODY))
        story.append(Spacer(1, 4))

    # ---------- CONCLUSIÓN (envuelta en KeepTogether para evitar viudas) ----------
    story.append(KeepTogether([
        section_header("Conclusión"),
        Paragraph(
            "Párrafo de cierre con el mensaje clave. Idealmente 3-5 líneas.",
            BODY),
    ]))

    return story


# ============================================================================
# BUILD
# ============================================================================
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
