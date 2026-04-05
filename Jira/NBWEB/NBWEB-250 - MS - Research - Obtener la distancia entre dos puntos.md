---
jira_key: "NBWEB-250"
aliases: ["NBWEB-250"]
summary: "MS - Research - Obtener la distancia entre dos puntos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-06-09 16:27"
updated: "2022-06-26 20:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-250"
---

# NBWEB-250: MS - Research - Obtener la distancia entre dos puntos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-09 16:27 |
| Actualizado | 2022-06-26 20:18 |
| Etiquetas | ninguna |
| Jira | [NBWEB-250](https://bluinc.atlassian.net/browse/NBWEB-250) |

## Relaciones

- **Padre:** [[NBWEB-76]] API - Implementar MS envios
- **relates to:** [[NBWEB-256]] MS - Feat - Integrar transporte con precio por KM
- **is blocked by:** [[NBWEB-261]] API - Feat -  Agregar un porcentaje mínimo de exclusión en la cotización 

## Descripcion

Como comente la otra vez, tenemos que agregar un medio mas de envio, que son camionetas de la emrpesa.

Este tipo de cotización se hace aplicando una tarifa plana por km de distancia (Según me comentaron es lineal, no por ruta. Osea de punto a punto).

[adjunto]
Para eso me pasaron una planilla con los precios, pero al dividir el precio por la cantidad de km, parece dar el mismo valor.

Osea que como dijimos, es precio por km.

Tendríamos que buscar la forma de formalizar esto en un algoritmo, lo que es en principio sencillo.

Pero por ahí podríamos hacer la parte que es mas tediosa, si podemos consumir alguna API o herramienta como maps (o cualquier otra) que nos de la distancia entre dos puntos, dos codigos postales, dos direcciones, etc.

¿como se puede hacer esto?

 ¿que api o servicio podríamos integrar?

¿de ser posible, que datos se necesitan?
