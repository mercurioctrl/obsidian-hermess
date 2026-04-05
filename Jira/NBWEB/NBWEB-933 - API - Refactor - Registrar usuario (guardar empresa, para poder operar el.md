---
jira_key: "NBWEB-933"
aliases: ["NBWEB-933"]
summary: "API - Refactor - Registrar usuario (guardar empresa, para poder operar el filtro companyCode en pedidos)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-06 09:58"
updated: "2024-12-13 07:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-933"
---

# NBWEB-933: API - Refactor - Registrar usuario (guardar empresa, para poder operar el filtro companyCode en pedidos)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-06 09:58 |
| Actualizado | 2024-12-13 07:54 |
| Etiquetas | ninguna |
| Jira | [NBWEB-933](https://bluinc.atlassian.net/browse/NBWEB-933) |

## Relaciones

- **Padre:** [[NBWEB-602 - Sitio Web|NBWEB-602]] Sitio Web

## Descripcion

Agregaremos a la solicitud en si, el filtrado por `companyCode` 

```
POST {API_URL}/v1/registrationRequest
```

De modo tal que sea posible filtrarlo en la aplicación de pedidos directamente en el recurso 

```
GET {API_PEDIDOS_URL}/v1/clientsRequests?full=true&companyCode={companyCode}
```

Para esto se puede agregar `[NB_WEB].[dbo].[usuarios_nb].companyCode` o en alguna tabla utilizada en `clientsRequests`

Se debe tener cuidado al agregar companyCode, para evitar errores en repositorios donde el parametro ya se use en otra tabla.
