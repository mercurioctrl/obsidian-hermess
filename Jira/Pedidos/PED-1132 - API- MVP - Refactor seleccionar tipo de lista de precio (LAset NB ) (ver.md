---
jira_key: "PED-1132"
aliases: ["PED-1132"]
summary: "API- MVP - Refactor seleccionar tipo de lista de precio (LAset / NB ) (ver adjunto lista de precio)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-10-02 09:40"
updated: "2025-10-27 10:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1132"
---

# PED-1132: API- MVP - Refactor seleccionar tipo de lista de precio (LAset / NB ) (ver adjunto lista de precio)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-02 09:40 |
| Actualizado | 2025-10-27 10:44 |
| Etiquetas | ninguna |
| Jira | [PED-1132](https://bluinc.atlassian.net/browse/PED-1132) |

## Relaciones

- **Padre:** [[PED-191 - Descargar Listado de precios|PED-191]] Descargar Listado de precios
- **action item from:** [[PED-1131 - APP- MVP - Refactor seleccionar tipo de lista de precio (Laset NB ) (ver|PED-1131]] APP- MVP - Refactor seleccionar tipo de lista de precio (Laset / NB ) (ver adjunto lista de precio)
- **has action item:** [[PED-1157 - API - MVP - Refactor - Agregar columna de reserva|PED-1157]] API - MVP - Refactor - Agregar columna de "reserva"

## Descripcion

Relacionada con tarea 19 [link](https://docs.google.com/spreadsheets/d/18TUSaVG3bY_lMLunZ3kDCRlLnKpQV-_BPfrtbL4pHNA/edit?gid=723483997#gid=723483997) 

```
GET {{API_URL}}/v1/download/priceList?clientId=19227&type=xlsxb&companyCode={companyCode}&warehouseid=x

```




Se debe obtener un archivo Excel en el **formato de plantilla adjuntado por LASET**, incluyendo la columna “Cantidad por caja” y el resto del formato

## Alcance

- Se agrega soporte al **parámetro **`type=xlsxb` al endpoint existente.


- La respuesta utiliza **la plantilla LASET** (archivo base) y se completa con los datos del cliente/compañía. (No remplaza la `xlsx`)


- La columna **“Cantidad por caja”** se calcula a partir de `[NewBytes_DBF].[dbo].[articulo].packagePerUnit`:

- `cantidadPorCaja = 1 / packagePerUnit`


- Ejemplo: si `packagePerUnit = 0.1` (10 unidades por caja) ⇒ `cantidadPorCaja = 10`.





> Nota: `packagePerUnit` “representa en cuántas unidades se divide un bulto”; por eso se usa el recíproco.
