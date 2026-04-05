---
jira_key: "COB-579"
aliases: ["COB-579"]
summary: "API - Feat - Agregar repositorio de empresas"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-26 15:15"
updated: "2025-10-02 15:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-579"
---

# COB-579: API - Feat - Agregar repositorio de empresas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-26 15:15 |
| Actualizado | 2025-10-02 15:15 |
| Etiquetas | ninguna |
| Jira | [COB-579](https://bluinc.atlassian.net/browse/COB-579) |

## Relaciones

- **Padre:** [[COB-21 - Base del proyecto y formularios|COB-21]] Base del proyecto y formularios
- **has action item:** [[COB-580 - APP - Refctor - MVP - Agregar filtro empresas al repositorio de clientes|COB-580]] APP - Refctor - MVP - Agregar filtro empresas al repositorio de clientes
- **relates to:** [[COB-584 - APP - Refactor - MVP - Agregar filtro empresas al repositorio de clientes -|COB-584]] APP - Refactor - MVP - Agregar filtro empresas al repositorio de clientes -> Solo visualizar empresas activas

## Descripcion

Así como se hizo en otras aplicaciones agregaremos el filtro de companies 

```
GET {API_URL}/v1/companies?show=1
```

El repositorio esta basado en `[NewBytes_DBF].[dbo].[FP_Empresas]` y devuelve una respuesta consistente a los demás servicios

```
[
    {
        "id": 2,
        "description": "OXXEN SRL"
    },
    {
        "id": 3,
        "description": "NBGLOBAL"
    },
    {
        "id": 4,
        "description": "NB DISTRIBUIDORA MAYORISTA SRL"
    },
    {
        "id": 5,
        "description": "DIGITO BINARIO SRL"
    },
    {
        "id": 7,
        "description": "SUC 10"
    },
    {
        "id": 9,
        "description": "NBElectric"
    },
    {
        "id": 8,
        "description": "MUGELLO SRL"
    },
    {
        "id": 10,
        "description": "PISOS Y REVESTIMIENTOS"
    },
    {
        "id": 11,
        "description": "LASET"
    },
    {
        "id": 6,
        "description": "CONSORCIO DE COOPERACION RED DE TECNOLOGIA"
    }
]
```
