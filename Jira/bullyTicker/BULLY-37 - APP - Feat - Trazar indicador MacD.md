---
jira_key: "BULLY-37"
aliases: ["BULLY-37"]
summary: "APP - Feat - Trazar indicador MacD"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-08-21 21:05"
updated: "2023-09-05 09:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BULLY-37"
---

# BULLY-37: APP - Feat - Trazar indicador MacD

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-21 21:05 |
| Actualizado | 2023-09-05 09:26 |
| Etiquetas | ninguna |
| Jira | [BULLY-37](https://bluinc.atlassian.net/browse/BULLY-37) |

## Relaciones

- **Padre:** [[BULLY-9 - Grafico de velas movimientos de precios|BULLY-9]] Grafico de velas / movimientos de precios

## Descripcion

Imagina que estás en un un auto. Tenes dos velocímetros: uno muestra la velocidad actual y el otro muestra tu velocidad promedio de los últimos minutos. Si tu velocidad actual es más rápida que tu velocidad promedio, significa que estás acelerando. Si es más lenta, estás desacelerando.

El MACD (Moving Average Convergence Divergence) es similar a esos dos velocímetros. Es un indicador que muestra la relación entre dos medias móviles de precios.

- **Línea MACD**: Es como tu velocidad actual. Se calcula restando una media móvil larga (por ejemplo, de 26 días) de una media móvil corta (por ejemplo, de 12 días).


- **Línea de señal**: Es como tu velocidad promedio. Es una media móvil (generalmente de 9 días) de la línea MACD.



Cuando la línea MACD cruza por encima de la línea de señal, es como si estuvieras acelerando (podría ser una señal de compra). Cuando cruza por debajo, es como si estuvieras desacelerando (podría ser una señal de venta).

**¿que vamos a hacer?** 

Necesitamos integrar el indicador MACD para tener una idea de si nuestras acciones están "acelerando" o "desacelerando". 

[adjunto]
