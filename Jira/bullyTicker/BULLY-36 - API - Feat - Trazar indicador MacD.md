---
jira_key: "BULLY-36"
aliases: ["BULLY-36"]
summary: "API - Feat - Trazar indicador MacD"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-08-21 21:03"
updated: "2023-08-23 16:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BULLY-36"
---

# BULLY-36: API - Feat - Trazar indicador MacD

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-21 21:03 |
| Actualizado | 2023-08-23 16:12 |
| Etiquetas | ninguna |
| Jira | [BULLY-36](https://bluinc.atlassian.net/browse/BULLY-36) |

## Relaciones

- **Padre:** [[BULLY-9]] Grafico de velas / movimientos de precios

## Descripcion

Imagina que estás en un un auto. Tenes dos velocímetros: uno muestra la velocidad actual y el otro muestra tu velocidad promedio de los últimos minutos. Si tu velocidad actual es más rápida que tu velocidad promedio, significa que estás acelerando. Si es más lenta, estás desacelerando.

El MACD (Moving Average Convergence Divergence) es similar a esos dos velocímetros. Es un indicador que muestra la relación entre dos medias móviles de precios.

- **Línea MACD**: Es como tu velocidad actual. Se calcula restando una media móvil larga (por ejemplo, de 26 días) de una media móvil corta (por ejemplo, de 12 días).


- **Línea de señal**: Es como tu velocidad promedio. Es una media móvil (generalmente de 9 días) de la línea MACD.



Cuando la línea MACD cruza por encima de la línea de señal, es como si estuvieras acelerando (podría ser una señal de compra). Cuando cruza por debajo, es como si estuvieras desacelerando (podría ser una señal de venta).

**¿que vamos a hacer?**

Se debe cumplir con los parametros necesarios para poder dibujar el grafico MACD de la historia [link](https://lioteam.atlassian.net/browse/BULLY-37)  en caso de que sea necesario
