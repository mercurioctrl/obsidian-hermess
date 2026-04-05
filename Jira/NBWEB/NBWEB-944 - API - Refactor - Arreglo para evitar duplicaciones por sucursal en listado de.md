---
jira_key: "NBWEB-944"
aliases: ["NBWEB-944"]
summary: "API - Refactor - Arreglo para evitar duplicaciones por sucursal en listado de comprobantes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-29 11:48"
updated: "2025-02-04 10:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-944"
---

# NBWEB-944: API - Refactor - Arreglo para evitar duplicaciones por sucursal en listado de comprobantes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-29 11:48 |
| Actualizado | 2025-02-04 10:42 |
| Etiquetas | ninguna |
| Jira | [NBWEB-944](https://bluinc.atlassian.net/browse/NBWEB-944) |

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web

## Descripcion

```
GET {API_URL}/v1/miCuenta/comprobantes
```

Dado que hasta el momento no había pasado que dos empresas tuvieran el mismo numero de sucursal de facturación (hasta ahora), es necesario hacer un pequeño refactor en los repositorios de facturas para poder hacer que las mismas no dupliquen filas en el repositorio.

Esto ya se aplico en pedidos en el siguiente commit que dejo de ejemplo: [link](https://github.com/New-Bytes/api-rest-pedidos-laravel/commit/bf2934379b2c04d1da35c9cb24bb0a14b641f539)

## ¿Cuando se produce el problema?

El problema se produce cuando en la tabla `[NewBytes_DBF].[dbo].[FP_Empresas]` existe para el parámetro `CNUMSUC`un valor repetido.

Si por ejemplo para el `CODEMP`04 y el 09 ambos poseen el valor `[NewBytes_DBF].[dbo].[FP_Empresas].SUCFacturaPlus = 0003`

Esto genera automáticamente que todas las facturas se dupliquen.

## ¿Como se evita el problema?

Aplicando lo mismo que hicimos en [link](https://github.com/New-Bytes/api-rest-pedidos-laravel/commit/bf2934379b2c04d1da35c9cb24bb0a14b641f539) agregando en el nexo del join `AND E.CODEMP = C.CODEMP`
