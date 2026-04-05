---
jira_key: "COB-30"
aliases: ["COB-30"]
summary: "APP - Feat - Ver movimientos de caja"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-07-17 20:25"
updated: "2022-10-27 08:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-30"
---

# COB-30: APP - Feat - Ver movimientos de caja

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-17 20:25 |
| Actualizado | 2022-10-27 08:06 |
| Etiquetas | ninguna |
| Jira | [COB-30](https://bluinc.atlassian.net/browse/COB-30) |

## Relaciones

- **Padre:** [[COB-15 - Cajas|COB-15]] Cajas
- **Subtarea:** [[COB-89 - APP - Review - Pequeño defecto al mostrar cuenta corriente|COB-89]] APP - Review - Pequeño defecto al mostrar cuenta corriente
- **Subtarea:** [[COB-99 - APP - Feat - Editar comentario en movimiento de caja|COB-99]] APP - Feat - Editar comentario en movimiento de caja
- **causes:** [[COB-3 - API - Feat - Listar movimiento por caja|COB-3]] API - Feat - Listar movimiento por caja

## Descripcion

Se trata de la pantalla/pestaña que muestra todos los movimientos de una caja determinada.

```
GET {APP_URL}/v1/box/{boxId}
```

Debe contener filtros para fechas, caja, tipo de movimiento, tipo saldo (cheque, dolares, etc)

Es muy parecida a estas pantallas.

[adjunto]
[adjunto]
