---
jira_key: "SNB-807"
aliases: ["SNB-807"]
summary: "mejoras para oca y andreani "
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "logistica@nb.com.ar"
created: "2023-05-30 13:23"
updated: "2023-07-18 14:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-807"
---

# SNB-807: mejoras para oca y andreani 

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | logistica@nb.com.ar |
| Creado | 2023-05-30 13:23 |
| Actualizado | 2023-07-18 14:44 |
| Etiquetas | ninguna |
| Jira | [SNB-807](https://bluinc.atlassian.net/browse/SNB-807) |

## Relaciones

- **is blocked by:** [[EXP-277 - Refactor - Modal Generar etiqueta, agregar comentarios, carga inicial de|EXP-277]] Refactor - Modal "Generar etiqueta", agregar comentarios, carga inicial de dirección, dirección completa
- **is blocked by:** [[EXP-307 - API - Refactor - Agregar numero de pedido (ex remito) y orden en algún lugar de|EXP-307]] API - Refactor - Agregar numero de pedido (ex remito) y orden en algún lugar de la etiqueta y comentarios
- **is blocked by:** [[EXP-311 - API - Feat - Contador de impresiones de etiqueta ZPL|EXP-311]] API - Feat - Contador de impresiones de etiqueta ZPL

## Descripcion

el tema es el siguente que se puede agregar para que no salga la misma etiqueta dias distintos. osea si yo scaneo en un excel planilla oca o andreani para que todos puedan ver que salio y que no cuando sale por error la misma etiqueta y se vuelva a serializar o a imprimir que tire un alerta diciendo ya se imprimio o ya salio esa etiqueta,. esto salto a raiz que una etiqueta salio 2 dias distintos y de casualidad era para el mismo cliente pero entendemos que oca no la puso en circulacion calculo porque le figuraba que ya existia, antes oca venia con scanner a retirar y el error se solucionaba en el momento ahora no trae mas scaner y paso esto. hay que buscarle la vuleta porque seguro va a volver a pasar.
