---
jira_key: "COM-99"
aliases: ["COM-99"]
summary: "API - Feat - Listar repositorio de impuestos para posiciones arancelarias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-05-23 13:22"
updated: "2025-11-20 15:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-99"
---

# COM-99: API - Feat - Listar repositorio de impuestos para posiciones arancelarias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-05-23 13:22 |
| Actualizado | 2025-11-20 15:10 |
| Etiquetas | ninguna |
| Jira | [COM-99](https://bluinc.atlassian.net/browse/COM-99) |

## Relaciones

- **Padre:** [[COM-98]] Repositorio de impuestos por posicionar arancelaria
- **blocks:** [[COM-113]] APP - Feat -Pestaña "Impuestos"
- **relates to:** [[COM-254]] API - MVP - Refactor - Listar repositorio de impuestos/gastos -> Agregar companyCode y companyDescription

## Descripcion

Según lo conversado, agregaremos un repositorio para poder listar los impuestos que figuran en los item.



Se reutilizara la siguiente tabla: `NewBytes_DBF.[dbo].[FP_IMPUESTOS]`



Ej de respuesta:

GET {API_URL`/v1/tariffTax`

Filter: 

`acronym`: `true/false` --en caso de ser tru retorna todos aquellos que tiene un tax asociado a posiciones arancelarias. en caso de ser false los que se utilizan en otras partes del ecosistema de la empresa.

`id`: 8 – busca por id de impuesto.

`orderBy: asc/desc  `ordena por id

```
[
    {
        "id": 3,
        "acronym": "IVA",
        "description": "IVA"
    },
    {
        "id": 7,
        "acronym": "TE",
        "description": "TASA ESTADISTICA"
    }
    ...
]
```
