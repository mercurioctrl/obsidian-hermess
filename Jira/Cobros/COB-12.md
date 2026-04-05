---
jira_key: "COB-12"
summary: "Feat - Procesar pases de caja"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-15 12:25"
updated: "2022-12-14 16:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-12"
---

# COB-12: Feat - Procesar pases de caja

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-15 12:25 |
| Actualizado | 2022-12-14 16:27 |
| Etiquetas | ninguna |
| Jira | [COB-12](https://bluinc.atlassian.net/browse/COB-12) |

## Descripción

Este recurso se trata sobre como crear un pase desde la caja de origen, hasta la caja destino. Luego este debe ser aceptado por la caja de destino para (en ese momento impactamos el monto) finalizar la operación. También existe la posibilidad de que sea rechazado.

Para que la feauture este completa, deben ejecutarse las subtareas descritas mas abajo.

 

- Los saldos de cada pase deben descontarse de la caja de origen, pero no agregarse hasta ser aceptados.


- Una vez aceptado un pase, debe agregarse a la caja de destino.


- En el front, los saldos totales deben reflejarse y cambiar de manera dinamica cuando acepto un pase.


- En el front, los saldos totales deben reflejarse y cambiar de manera dinamica cuando realizo un pase.


- Debo poder anular un pase y los saldos de mi caja deben volver a la normalidad.


- No debo poder anular un pase que ya se encuentra aceptado.
