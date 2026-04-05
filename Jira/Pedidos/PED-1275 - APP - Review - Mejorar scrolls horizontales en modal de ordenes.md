---
jira_key: "PED-1275"
aliases: ["PED-1275"]
summary: "APP - Review - Mejorar scrolls horizontales en modal de ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-22 07:34"
updated: "2026-01-23 17:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1275"
---

# PED-1275: APP - Review - Mejorar scrolls horizontales en modal de ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-22 07:34 |
| Actualizado | 2026-01-23 17:23 |
| Etiquetas | ninguna |
| Jira | [PED-1275](https://bluinc.atlassian.net/browse/PED-1275) |

## Relaciones

- **Padre:** [[PED-1093 - Ver detalle de orden|PED-1093]] Ver detalle de orden

## Descripcion

[adjunto]
En este modal están apareciendo **scrolls horizontales innecesarios**. La idea es **evitarlos por defecto** y **aprovechar mejor el ancho disponible**.

**Concepto general:**

- El modal debería tener un **ancho base**.


- Si el contenido **desborda horizontalmente**, antes de mostrar scroll:

- **ensanchar el modal un poco más**, usando el espacio libre de pantalla.




- **No llevarlo directamente a full width**: solo crecer lo necesario.



**Objetivo:**
Mejorar legibilidad y evitar scrolls cuando el problema es solo que el modal está quedando más angosto de lo necesario.
