---
jira_key: "NBWEB-616"
aliases: ["NBWEB-616"]
summary: "API  - Feat - Regenerar hard token"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-22 09:08"
updated: "2024-01-26 05:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-616"
---

# NBWEB-616: API  - Feat - Regenerar hard token

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-22 09:08 |
| Actualizado | 2024-01-26 05:29 |
| Etiquetas | ninguna |
| Jira | [NBWEB-616](https://bluinc.atlassian.net/browse/NBWEB-616) |

## Relaciones

- **Padre:** [[NBWEB-610]] API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta
- **blocks:** [[NBWEB-617]] APP - Feat - Mi cuenta - Credenciales
- **blocks:** [[NBWEB-618]] API - Feat - Leer hard token -> Agregar fecha de creacion

## Descripcion

Crearemos un recurso para regenerar el hardToken que se encuentra en `[NB_WEB].[dbo].[usuarios_nb].handedToken`

```
PATCH {API_URL}/v1/miCuenta/hardToken
```

Agregaremos adicionalmente una columna para poder guardar la fecha de regeneración.

Solo la cuenta principal puede hacer esto.
