---
jira_key: "PED-23"
aliases: ["PED-23"]
summary: "API - Repository - Vendedores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-08 09:49"
updated: "2023-11-02 11:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-23"
---

# PED-23: API - Repository - Vendedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-08 09:49 |
| Actualizado | 2023-11-02 11:14 |
| Etiquetas | ninguna |
| Jira | [PED-23](https://bluinc.atlassian.net/browse/PED-23) |

## Relaciones

- **Padre:** [[PED-7 - Repositorios y base del proyecto|PED-7]] Repositorios y base del proyecto
- **blocks:** [[PED-25 - APP - Feat - Modal - Seteo de parámetros de cliente|PED-25]] APP - Feat - Modal - Seteo de parámetros de cliente 
- **blocks:** [[PED-210 - APP - Feat - Filtros de ordenes - Filtrar por Vendedores en pedido|PED-210]] APP - Feat - Filtros de ordenes -> Filtrar por Vendedores en pedido

## Descripcion

Basándose en `[LO].[dbo].[vendedores]` se debe generar el repositorio de vendedores del sitio

```
GET {API_URL}/v1/sellers
```

Devuelve:

```
  {
    "ccodage": "07 ",
    "description": "Blanco Insua    Galo",
    "id": 7
  },
  {
    "ccodage": "08 ",
    "description": "Altamiranda Andrea",
    "id": 8
  },
  {
    "ccodage": "10 ",
    "description": "Iannicelli                     Matias         ",
    "id": 10
  },
```

```
SELECT  
       [ccodage] as ccodage
      ,[capeage]+' '+[cnbrage] as description
      , id_vendedor as id
  FROM [NewBytes_DBF].[dbo].[agentes]
   
```
