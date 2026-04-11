---
name: blu-report
description: Genera informes y reportes en PDF con el formato visual minimalista de Blu Studio Inc. (hoja membretada "Activación" / "Informe") para clientes. Usá esta skill SIEMPRE que el usuario pida un "informe", "reporte", "report", "weekly report", "entregable para cliente", "informe semanal", "informe mensual", o cualquier documento formal que vaya dirigido a un cliente de Blu Studio — incluso si no menciona explícitamente a Blu. El formato incluye logo Blu grande arriba a la izquierda, bloque "DOCUMENTO / [Título] / N° X" arriba a la derecha, metadata del proyecto, secciones con tablas de comparación, chips de estado verdes/rojos, y footer con logo Blu gris + email + CUIT. Usar SIEMPRE esta skill para entregables de cliente — no armar PDFs genéricos con reportlab SimpleDocTemplate.
---

# Blu Report — Informes en hoja membretada Blu

Esta skill genera informes/reportes en PDF siguiendo el sistema visual de Blu Studio Inc. Es el formato que el cliente espera recibir: minimalista, limpio, tipo "Activación N°X" pero adaptable a cualquier tipo de reporte (SEO, performance, analytics, branding, etc.).

## Cuándo usar esta skill

Usala siempre que el usuario pida un documento formal para uno de sus clientes:
- "hacemé el informe semanal / mensual / de X"
- "armame el reporte para el cliente"
- "generá el entregable en PDF"
- "informe de SEO / performance / campañas / auditoría"

Aunque el usuario no mencione "Blu" ni "membretada", asumí que todos los entregables formales van en este formato a menos que indique lo contrario.

**No uses esta skill** para cosas informales: resúmenes en chat, notas, READMEs, borradores que no son para cliente.

## Cómo funciona

El entregable se construye con un script Python basado en ReportLab que ya tiene todo el sistema visual resuelto: márgenes, tipografías, colores, header/footer, estilos de tabla, chips de estado. Vos solo adaptás el contenido.

El template base está en `assets/blu_report_template.py`. Es un script ejecutable y listo para copiar + modificar. **No reinventes el layout** — copiá el template y editá solamente la función `build_story()` con el contenido nuevo, más el número de documento y la metadata del header.

### Proceso

1. **Conversá con el usuario primero** si falta información clave (N° de documento, período, qué secciones incluir, etc.).
2. **Copiá** `assets/blu_report_template.py` al scratchpad (`/sessions/<id>/`) como por ejemplo `generate_report.py`.
3. **Editá** las constantes del top (OUTPUT, DOC_NUMBER, DOC_TITLE, PROJECT, CLIENT, CLIENT_EMAIL, PERIOD, COMPARE_PERIOD) y reescribí `build_story()` con el contenido del reporte.
4. **Ejecutá** el script. El PDF se guarda directamente en la carpeta del usuario.
5. **Verificá** renderizando las páginas con `pdf2image` antes de entregar, para detectar superposiciones o contenido cortado.
6. **Entregá** el PDF con un link `computer://` y un resumen de 2-3 líneas de lo que contiene.

## Sistema visual (para que entiendas las decisiones)

**Tipografía:** Helvetica en toda la pieza. No uses fuentes custom — mantener Helvetica garantiza que renderice igual en cualquier visor.

**Paleta:**
- Negro puro `#0a0a0a` para títulos y cifras
- Gris medio `#6b6b6b` para labels, headers de tabla, texto auxiliar (los headers de tabla siempre en uppercase, font-size chico, gris — esto le da el look "Blu")
- Gris muy claro `#e5e5e5` para líneas separadoras
- Fondo claro `#f7f7f5` para las KPI cards del resumen
- Verde OK `#dcfce7` / `#15803d` (bg / text) para chips de estado y deltas positivos
- Rojo `#fee2e2` / `#b91c1c` para deltas negativos / estados de error
- Ámbar `#fef3c7` / `#a16207` para estados intermedios ("En proceso")

**Primera página:**
- Logo "Blu." grande (Helvetica-Bold 36pt) arriba a la izquierda
- Arriba a la derecha: "DOCUMENTO" en gris 8pt + título del documento en 22pt bold + "N° X" debajo
- Metadata block alineada a la derecha con labels en gris regular y valores en negro bold (Proyecto, Para, email del cliente, Período, Comparado con)
- Línea separadora sutil antes del contenido

**Páginas siguientes:**
- Mini-logo "Blu." (16pt) arriba a la izquierda + título y N° pequeño arriba a la derecha
- Línea separadora
- Menos margen superior para aprovechar espacio

**Footer en TODAS las páginas:**
- Línea separadora
- "Reporte [tipo] del período indicado."
- "Para consultas: info@blustudioinc.com"
- "CUIT: 30-71909207-8"
- Logo "Blu." grande en gris claro `#d4d4d4` abajo a la derecha
- "Página N" centrado abajo

## Estructura de contenido recomendada

La mayoría de los reportes de cliente siguen este patrón. Adaptalo al contenido específico pero mantené el orden:

1. **Resumen ejecutivo** — 1 párrafo corto + grid de 4 KPI cards con las métricas clave y su delta (verde si mejoró, rojo si bajó).
2. **Secciones de datos** — una por tema, cada una con:
   - Header uppercase gris (estilo `H2`)
   - Párrafo breve de contexto
   - Tabla de comparación (antes / hoy / Δ) con deltas coloreados
3. **Acciones ejecutadas / fixes desplegados** — tabla con # + título + descripción + chip de estado
4. **Oportunidades para el próximo período** — lista de 3-5 items, cada uno con título en bold y 1-2 líneas de explicación
5. **Conclusión** — 1 párrafo cerrando el mensaje clave (envolvelo en `KeepTogether` para evitar que quede huérfano)

## Tips críticos (aprendidos a los golpes)

- **Texto en celdas que puede ser largo → siempre `Paragraph`**, nunca string pelado. Los strings pelados no hacen wrap y se superponen con la columna siguiente. Usá el helper `P(text, style)` del template.
- **Anchos de columna**: dejá margen extra en columnas con texto (mínimo 55-65mm para títulos de fix/acción). Si pintás "Verificado" o "OK" en una columna, reservale 28-30mm fijos.
- **Widows / huérfanos**: envolvé el título + párrafo de conclusión en `KeepTogether(...)` para que no quede una línea sola en la última página.
- **PageBreak vs flujo natural**: dejá que ReportLab flotee el contenido naturalmente. Solo forzá `PageBreak` si realmente querés que una sección grande empiece en página nueva. Forzar de más genera páginas con una sola línea al final.
- **Deltas**: hacelos bold y colorealos — verde para mejoras, rojo para bajas. Usá el símbolo `−` (U+2212) y no un guión normal para que el signo menos se vea bien.
- **Evitá ALL-CAPS innecesario** excepto en los headers de sección (que sí son uppercase por diseño). El resto en capitalización normal.
- **Verificá con pdf2image** antes de entregar. Siempre. Es barato y atrapa superposiciones que no ves en el código.
- **El nombre del archivo** debe ser descriptivo: `Informe-[Tipo]-[Cliente]-[YYYY-MM-DD].pdf`.
- **Guardá directamente** en la carpeta que seleccionó el usuario (`/sessions/<id>/mnt/<folder>/`) — no uses el scratchpad para el output final.

## El template

Revisá `assets/blu_report_template.py`. Tiene todo: setup de `BaseDocTemplate`, dos `PageTemplate` (first/later), callbacks `draw_first_page` / `draw_later_page` / `draw_footer`, estilos de párrafo, helpers para KPI cards y tablas de comparación con deltas coloreados, y un `build_story()` de ejemplo que podés usar como esqueleto.

**Copialo tal cual y editalo.** El sistema visual ya está resuelto — enfocá tu energía en el contenido.
