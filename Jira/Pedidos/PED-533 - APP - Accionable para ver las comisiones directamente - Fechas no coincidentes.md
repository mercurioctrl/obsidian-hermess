---
jira_key: "PED-533"
aliases: ["PED-533"]
summary: "APP - Accionable para ver las comisiones directamente - Fechas no coincidentes"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-02-06 12:55"
updated: "2024-02-08 19:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-533"
---

# PED-533: APP - Accionable para ver las comisiones directamente - Fechas no coincidentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-06 12:55 |
| Actualizado | 2024-02-08 19:47 |
| Etiquetas | ninguna |
| Jira | [PED-533](https://bluinc.atlassian.net/browse/PED-533) |

## Relaciones

- **Padre:** [[PED-6]] Comisiones
- **blocks:** [[PED-527]] APP - Feat - Agregar un accionable para ver las comisiones directamente
- **relates to:** [[PED-534]]  APP - Refactor - Listar comisiones - Selección automática de filtros
- **is blocked by:** [[PED-530]] APP - Feat - Agregar columas fecha de liquidacion y fecha de facturacion

## Descripcion

1. Cuando se consultan las comisiones por grupos de un vendedor desde el Dashboard, observo que muestra que tiene comisiones, pero al ejecutar el accionable, no se muestran datos de comisiones.

[adjunto]
Dato extra:
Esto ocurre cuando seleccionas por periodo de fecha en el dashboard. Al pasar a ver las comisiones, la fecha inicial se desplaza un día.

---

2. Al no seleccionar ningún vendedor en el dashboard y ejecutar el accionable aparece el vendedor como `undefined`

[adjunto]
Dato extra:
Al parecer esto sucede al cambiar desde cualquier otra pestaña y veo que al entrar a Comisiones no se realiza la petición automáticamente a `/v1/comissions`
