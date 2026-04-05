---
jira_key: "LIO-199"
aliases: ["LIO-199"]
summary: "API CMS - Feat - Agregar cuotas diferenciadas"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-31 17:47"
updated: "2025-02-10 03:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-199"
---

# LIO-199: API CMS - Feat - Agregar cuotas diferenciadas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-31 17:47 |
| Actualizado | 2025-02-10 03:40 |
| Etiquetas | ninguna |
| Jira | [LIO-199](https://bluinc.atlassian.net/browse/LIO-199) |

## Relaciones

- **Padre:** [[LIO-198 - CMS|LIO-198]] CMS
- **blocks:** [[LIO-200 - APP CMS - Feat - Agregar cuotas diferenciadas|LIO-200]] APP CMS - Feat - Agregar cuotas diferenciadas

## Descripcion

Luego del refactor en [link](https://lioteam.atlassian.net/browse/LIO-182) 

Es necesario agregar los parámetros al CMS para que puedan ser editados de manera simple

```
PATCH /v1/paymentMethods
```

Se guarda en la tabla `[LO].[dbo].[mediosPago]` en los siguientes parámetros:

`[LO].[dbo].[mediosPago].interes1`

`[LO].[dbo].[mediosPago].interes3`

`[LO].[dbo].[mediosPago].interes6`

`[LO].[dbo].[mediosPago].interes9`

`[LO].[dbo].[mediosPago].interes12`

```
[
{
  "id":"5056",
  "activo":1,
  "destacado_home":"1",
  "cuotas":"1",
  "soloSucursal":"1",
  "stockPropio":"0",
  "stockVirtual":"0",
  "interesBruto":"-10.0100",
  "interes":"-8.27",
  "nombre":"Green Cash Efectivo",
  "descripcion":"Efectivo en dólares (Green Cash)"
  "interes1": 0, <-- Se agrega
  "interes3": 20,  <-- Se agrega
  "interes6": 30,  <-- Se agrega
  "interes9": 40,  <-- Se agrega
  "interes12": 50,  <-- Se agrega   
  }
  ]
```
