---
jira_key: "PED-1233"
aliases: ["PED-1233"]
summary: "API - Refactor - Editar parametros de usuario de libre opcion para un cliente de NB (Capa 1) -> Mejora en el objeto de respuesta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Guillermo Avila"
created: "2026-01-06 10:47"
updated: "2026-01-20 18:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1233"
---

# PED-1233: API - Refactor - Editar parametros de usuario de libre opcion para un cliente de NB (Capa 1) -> Mejora en el objeto de respuesta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-06 10:47 |
| Actualizado | 2026-01-20 18:08 |
| Etiquetas | ninguna |
| Jira | [PED-1233](https://bluinc.atlassian.net/browse/PED-1233) |

## Relaciones

- **Padre:** [[PED-600 - EdicionAlta de cliente|PED-600]] Edicion/Alta de cliente
- **clones:** [[PED-1202 - API - Feat - Editar parametros de usuario de libre opcion para un cliente de NB|PED-1202]] API - Feat - Editar parametros de usuario de libre opcion para un cliente de NB (Capa 1)

## Descripcion

Realizaremos una refactorización al recurso para adecuarnos al siguiente objeto de respuesta:

```
PATCH /v1/loUser/{clientLo}
```

```
{
  "success": true,                    // true o false
  "message": "Operación exitosa"      // Descripción opcional
}
```

[adjunto]
