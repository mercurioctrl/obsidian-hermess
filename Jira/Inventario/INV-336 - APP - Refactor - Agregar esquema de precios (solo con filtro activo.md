---
jira_key: "INV-336"
aliases: ["INV-336"]
summary: "APP - Refactor - Agregar esquema de precios (solo con filtro activo controlPrices)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-02-09 08:42"
updated: "2026-02-25 14:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-336"
---

# INV-336: APP - Refactor - Agregar esquema de precios (solo con filtro activo controlPrices)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-09 08:42 |
| Actualizado | 2026-02-25 14:15 |
| Etiquetas | ninguna |
| Jira | [INV-336](https://bluinc.atlassian.net/browse/INV-336) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios

## Descripcion

Agregaremos nuevas columnas a la derecha si `controlPrices=true` según [link](https://bluinc.atlassian.net/browse/INV-335) 

Las ordenaremos de la siguiente manera 

| #  orden | JSON | Nombre Visible HTML |
| --- | --- | --- |
| 1 | itemId | ID_NB |
| 2 | IVA | IVA |
| 3 | fob | FOB |
| 4 | cost | COSTO |
| 5 | unitPrice | UNIT |
| 6 | mayPrice | MAY |
| 7 | loCost | LO |
| 8 | mlPrice | ML |
| 9 | PL | PL1 |
| 10 | PLI | PL2 |
| 11 | MAY1 | MAY1 |
| 12 | MAY2 | MAY2 |
| 13 | DT2 | DT2 |
| 14 | DT3 | DT3 |
| 15 | LO1 | LO1 |
| 16 | LO2 | LO2 |
| 17 | PML | PML |
| 18 | PCAM | PCAM |
| 19 | MK1 | MK1 |
| 20 | priceLoReseller | LO Reseller |
| 21 | PVP | PVP |
| 22 | IINT | IINT |
