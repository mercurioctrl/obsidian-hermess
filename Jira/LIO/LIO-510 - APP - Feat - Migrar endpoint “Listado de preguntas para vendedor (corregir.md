---
jira_key: "LIO-510"
aliases: ["LIO-510"]
summary: "APP - Feat - Migrar endpoint “Listado de preguntas para vendedor (corregir paginado)” actualemente en Legacy"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-12 08:02"
updated: "2026-02-12 22:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-510"
---

# LIO-510: APP - Feat - Migrar endpoint “Listado de preguntas para vendedor (corregir paginado)” actualemente en Legacy

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-12 08:02 |
| Actualizado | 2026-02-12 22:55 |
| Etiquetas | ninguna |
| Jira | [LIO-510](https://bluinc.atlassian.net/browse/LIO-510) |

## Relaciones

- **Padre:** [[LIO-498 - Listado de preguntas|LIO-498]] Listado de preguntas
- **action item from:** [[LIO-534 - API - Feat - Responder preguntas|LIO-534]] API - Feat - Responder preguntas

## Descripcion

Hoy en Legacy el listado paginado se implementa mal: primero trae **todos** los IDs que matchean filtros y recién después pagina en PHP.

## Problema a corregir (obligatorio en la migración desde [link](https://bluinc.atlassian.net/browse/LIO-534) )

- Si un vendedor tiene 10.000 preguntas, la API trae 10.000 IDs desde la BD


-  Carga 10.000 IDs en memoria PHP


-  Desperdicia procesamiento de BD y red


-  Paginación en aplicación en vez de en SQL Server



## Objetivo

Migrar el endpoint a API v4 **sin cambiar el contrato funcional** (misma URL, mismos parámetros, mismos filtros, mismos errores y misma respuesta), **pero** corrigiendo la paginación para que sea en SQL Server usando `OFFSET / FETCH NEXT`.

---

## Endpoint a migrar (contrato congelado)

```
GET {API_URL}/productos/preguntas/vendedor?estado={opcional}&p={opcional}
```

Query params:

- `estado` opcional: `pendientes | respondidas | (vacío => todas)`


- `p` opcional: página (default `1`)


- `itemsPorPagina`: fijo `10`



Seguridad:

- JWT Bearer


- Solo perfil `vendedor`


- Filtra por `vendedor_id` del usuario autenticado


- Si no tiene permisos → **403** `"No tenés permisos para ver las preguntas"`



---

## Criterios de aceptación (DoD)

- Cambiando solo el dominio/baseURL, el front funciona igual (mismo contrato).


- Paginación se hace en SQL Server con `OFFSET/FETCH NEXT` (no hay fetch masivo de IDs).


- `total` refleja la cantidad real con filtros.


- 10 items por página, orden `id DESC`.


- Permisos y errores idénticos (incluye 403 con el texto exacto).


-  Tests cubren paridad funcional y aseguran query paginada.
