---
jira_key: "COB-584"
aliases: ["COB-584"]
summary: "APP - Refactor - MVP - Agregar filtro empresas al repositorio de clientes -> Solo visualizar empresas activas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2025-10-02 15:15"
updated: "2025-10-22 13:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-584"
---

# COB-584: APP - Refactor - MVP - Agregar filtro empresas al repositorio de clientes -> Solo visualizar empresas activas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2025-10-02 15:15 |
| Actualizado | 2025-10-22 13:17 |
| Etiquetas | ninguna |
| Jira | [COB-584](https://bluinc.atlassian.net/browse/COB-584) |

## Relaciones

- **Padre:** [[COB-573]] Clientes
- **relates to:** [[COB-580]] APP - Refctor - MVP - Agregar filtro empresas al repositorio de clientes
- **relates to:** [[COB-579]] API - Feat - Agregar repositorio de empresas

## Descripcion

Realizaremos un refactor para añadir el parámetro `show` al obtener el listado de empresas, con el objetivo de mostrar únicamente las que se encuentran activas.

```
GET {API_URL}/v1/companies?show=1
```

[adjunto]
