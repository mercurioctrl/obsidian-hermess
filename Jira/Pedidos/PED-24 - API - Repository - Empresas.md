---
jira_key: "PED-24"
aliases: ["PED-24"]
summary: "API - Repository - Empresas "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-08 09:51"
updated: "2024-08-12 11:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-24"
---

# PED-24: API - Repository - Empresas 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-08 09:51 |
| Actualizado | 2024-08-12 11:59 |
| Etiquetas | ninguna |
| Jira | [PED-24](https://bluinc.atlassian.net/browse/PED-24) |

## Relaciones

- **Padre:** [[PED-7 - Repositorios y base del proyecto|PED-7]] Repositorios y base del proyecto
- **blocks:** [[PED-25 - APP - Feat - Modal - Seteo de parámetros de cliente|PED-25]] APP - Feat - Modal - Seteo de parámetros de cliente 
- **blocks:** [[PED-793 - API - Feat - Filtrar clientes por empresa|PED-793]] API - Feat - Filtrar clientes por empresa
- **blocks:** [[PED-794 - APP - Feat - Filtrar clientes por empresa|PED-794]] APP - Feat - Filtrar clientes por empresa

## Descripcion

Basandonos en `[NewBytes_DBF].[dbo].[FP_Empresas] crearemos el recurso `

```
{API_URL}/v1/cms/companies
```

```
[
  {
    "id": "02",
    "DESCRIPTION": "OXXEN SRL"
  },
  {
    "id": "03",
    "DESCRIPTION": "NBGLOBAL"
  },
  {
    "id": "04",
    "DESCRIPTION": "NB DISTRIBUIDORA MAYORISTA SRL"
  },
  {
    "id": "05",
    "DESCRIPTION": "DIGITO BINARIO SRL"
  },
  {
    "id": "07",
    "DESCRIPTION": "SUC 10"
  },
  {
    "id": "08",
    "DESCRIPTION": "MUGELLO SRL"
  },
  {
    "id": "06",
    "DESCRIPTION": "CONSORCIO DE COOPERACION RED DE TECNOLOGIA"
  }
]
```
