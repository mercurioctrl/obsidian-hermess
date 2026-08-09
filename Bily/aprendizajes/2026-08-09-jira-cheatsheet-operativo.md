# 2026-08-09: Cheatsheet operativo de Jira (BLU / New Bytes)

Referencia viva para crear/consultar tickets rápido y sin errores vía el MCP de Atlassian.
Actualizar esta nota cuando aparezcan IDs, epics o gotchas nuevos.

## Conexión

- **cloudId:** `bluinc.atlassian.net` (equivalente UUID: `85590b1a-fa2f-42f4-a567-153cc8cffa2b`).
- Base web: `https://bluinc.atlassian.net/browse/{KEY}`.
- Descripciones: usar siempre `contentFormat: "markdown"`.

## Account IDs (assignee)

Confirmados en esta sesión:

| Persona | Alias | accountId |
|---------|-------|-----------|
| Emanuel Jesus Ferreyra | Ema | `624aea914fe01d006ba914ff` |
| Ezequiel manzano | Eze | `622f40a11dcf800070e80d77` |
| Marbe Moreno | Marbe | `60b6410d24eedc006d1a41c1` |

Para el resto (Guille, Franco Callipo, Alejandra Guidobono/"ale", etc.): resolver con `lookupJiraAccountId` antes de asignar. Ojo: "ale" ≈ **Alejandra Guidobono** (a confirmar cada vez).

## Proyectos y tipos de issue

- **PED** (Pedidos, classic): Tarea, Historia, Error, Subtarea.
- **LIO** (LibreOpción, classic): Epic, Tarea, Historia, Subtarea, Error.
- **GIGA** (team-managed / next-gen): Epic, Tarea, Subtarea, Idea, Elemento, Solicitud. **NO tiene "Historia"** → usar Tarea.
- **SNB** (Servicio de asistencia, service desk): **Error, Nueva función, Support** (no hay Tarea ni Historia). Un reporte de bug va como **Error**.
- Otros prefijos vistos: INV, NBWEB, COM, EXP, PEGA, NBE, POS, MKT, LOMKT, LOCAPP, etc. (24 proyectos). Verificar tipos con `getJiraProjectIssueTypesMetadata` si hay duda.

## Epics / padres conocidos

| Key | Qué es | Uso |
|-----|--------|-----|
| `GIGA-1` | Epic **ERP** | Colgar tareas del ERP (parent = GIGA-1). |
| `LIO-1` | Epic **Experiencia del Usuario (UX)** | Contenedor de Historias UX. |
| `LIO-709` | Historia **Tiendas oficiales** (bajo LIO-1) | Las tareas de tiendas oficiales cuelgan acá como **Subtareas**. |
| `LIO-737` | Tarea **"A+ Content 2"** | Padre de las **Subtareas de content A+** (asignadas a Marbe). Es donde vienen las fichas más recientes. |
| `LIO-742` | Epic **PartPicker** | — |

## Convención de títulos (summary)

`Área o flujo o sección: descripción de lo que se necesita o de lo que ocurre`.
Ej: *Precios y Stock: al tildar el checkbox, resaltar toda la línea en verde (ayuda visual)*.
Detalle en [[Bily/aprendizajes/2026-08-07-formato-titulos-jira|nota dedicada]].

## Patrones que funcionan

- **Content A+ (LIO):** Subtarea bajo `LIO-737`, assignee Marbe, summary `Elaborar content A+ de {Producto}`, descripción con URL del producto + URL de ficha de ejemplo.
- **Checklists por módulo (GIGA/ERP):** una Tarea por módulo bajo `GIGA-1` con los ítems como checklist markdown (`* [ ]`), en vez de una tarjeta por ítem.
- **Lotes:** al crear muchos tickets, mandar varias `createJiraIssue` en paralelo (batches de ~8) para acelerar.

## Estados (status categories)

- `new` → **Por hacer** (Abierta, Backlog, Tareas por hacer).
- `indeterminate` → **En curso** (incluye **"Ready for QA"** y "En curso" propiamente).
- `done` → **Listo** (Finalizada).

## Gotchas de JQL / MCP

- **Colisión de nombres de estado:** `status = "En curso"` matchea un único status ID y se pierde otros estados con el mismo nombre en otros workflows. Workaround: filtrar por `statusCategory` y después filtrar el `.fields.status.name` exacto en el JSON.
- **Resultados grandes:** `searchJiraIssuesUsingJql` puede exceder el máximo de tokens y se auto-guarda a archivo. Extraer sólo lo necesario con `jq -r '.issues.nodes[] | [.key, .fields.status.name, .fields.summary] | @tsv' <archivo>`.
- **Imágenes privadas de Slack** (`files.slack.com/files-pri/...`): no se pueden embeber en Jira; referenciar la URL en la descripción.
- Traer sólo los `fields` necesarios (`["summary","status","issuetype","parent","assignee"]`) para achicar la respuesta.

Ver también: [[Bily/MEMORIA|MEMORIA]] · [[Bily/aprendizajes/aprendizajes|Aprendizajes]] · [[Bily/aprendizajes/2026-08-07-formato-titulos-jira|Formato de títulos Jira]].
