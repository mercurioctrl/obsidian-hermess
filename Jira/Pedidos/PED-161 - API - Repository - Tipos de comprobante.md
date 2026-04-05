---
jira_key: "PED-161"
aliases: ["PED-161"]
summary: "API - Repository - Tipos de comprobante"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-24 08:48"
updated: "2023-10-24 10:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-161"
---

# PED-161: API - Repository - Tipos de comprobante

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-24 08:48 |
| Actualizado | 2023-10-24 10:26 |
| Etiquetas | ninguna |
| Jira | [PED-161](https://bluinc.atlassian.net/browse/PED-161) |

## Relaciones

- **Padre:** [[PED-7 - Repositorios y base del proyecto|PED-7]] Repositorios y base del proyecto
- **blocks:** [[PED-162 - API - Feat - Filtrar por tipo de comprobante|PED-162]] API - Feat - Filtrar por tipo de comprobante

## Descripcion

Basados en la tabla `[NewBytes_DBF].[dbo].[FP_TiposDocumentosCobro] `

Crearemos un recurso para obtener facilmente que tipos de documentos podemos emitir. 

```
GET {API_URL}/v2/voucherTypes
```

retorna

```json
[
  {
    "id": 3,
    "description": "NOTA DE DEBITO",
    "order": 3,
    "signo": 1,
    "cod_A": "02",
    "cod_B": "07",
    "cod_C": "12",
    "cod_E": "20"
  },
  {
    "id": 1,
    "description": "FACTURA",
    "order": 1,
    "signo": 1,
    "cod_A": "01",
    "cod_B": "06",
    "cod_C": "11",
    "cod_E": "19"
  },
  {
    "id": 2,
    "description": "NOTA DE CREDITO",
    "order": 4,
    "signo": -1,
    "cod_A": "03",
    "cod_B": "08",
    "cod_C": "13",
    "cod_E": "21"
  },
  ...
  ]
```
