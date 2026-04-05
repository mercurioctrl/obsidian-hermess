---
jira_key: "COB-9"
aliases: ["COB-9"]
summary: "API - Feat - Listar bancos"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-15 08:50"
updated: "2022-10-20 17:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-9"
---

# COB-9: API - Feat - Listar bancos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-15 08:50 |
| Actualizado | 2022-10-20 17:08 |
| Etiquetas | ninguna |
| Jira | [COB-9](https://bluinc.atlassian.net/browse/COB-9) |

## Relaciones

- **Padre:** [[COB-16]] Cuentas bancarias
- **Subtarea:** [[COB-163]] API - Feat - Refactor - Agregar saldo a el recurso
- **Subtarea:** [[COB-164]] Bancos
- **Subtarea:** [[COB-196]] API - Refactor - Agregar filtro "con saldo"
- **Subtarea:** [[COB-606]] API - Refactor - Refactorizar el repositorio de  movimientos de bancos para agregar atributos y filtros referidos a companyCode
- **Subtarea:** [[COB-607]] APP - Refactor - Agregar Filtro Empresa a el repositorio de movimientos de bancos y mostrarlo en el listado
- **Subtarea:** [[COB-608]] API - Feat - Listar / Agregar / Editar nuevo banco 
- **Subtarea:** [[COB-609]] APP - Feat - Listar  Agregar / Editar nuevo banco
- **Subtarea:** [[COB-610]] .
- **Subtarea:** [[COB-611]] .
- **Subtarea:** [[COB-612]] API - Feat - Agregar recurso para crear banco con cuenta bancaria asociada automáticamente   
- **blocks:** [[COB-40]] APP - Feat - Listar movimientos caja
- **blocks:** [[COB-163]] API - Feat - Refactor - Agregar saldo a el recurso
- **blocks:** [[COB-165]] APP - Feat - Listar bancos

## Descripcion

Se trata del recurso que lista los bancos disponibles para hacer operaciones.

```
GET {{API_URL}}/v1/banks
```

```
[
  {
    "id": 34,
    "description": "BANCO PATAGONIA S.A.",
    "oldId": 9
  },
  {
    "id": 16,
    "description": "CITIBANK N.A.",
    "oldId": 6
  },
  {
    "id": 389,
    "description": "BANCO COLUMBIA S.A.",
    "oldId": 5
  },
  {
    "id": 17,
    "description": "BBVA BANCO FRANCES S.A.",
    "oldId": 3
  },
  {
    "id": 7,
    "description": "BANCO DE GALICIA Y BUENOS AIRES S.A.",
    "oldId": 2
  },
  {
    "id": 72,
    "description": "BANCO SANTANDER RIO S.A.",
    "oldId": 1
  },
  {
    "id": 27,
    "description": "BANCO SUPERVIELLE S.A.",
    "oldId": null
  },
  {
    "id": 312,
    "description": "BANCO VOII S.A.",
    "oldId": null
  },
  {
    "id": 262,
    "description": "BANK OF AMERICA, NATIONAL ASSOCIATION",
    "oldId": null
  },
  {
    "id": 301,
    "description": "BANCO PIANO S.A.",
    "oldId": null
  },
  {
    "id": 268,
    "description": "BANCO PROVINCIA DE TIERRA DEL FUEGO",
    "oldId": null
  },
  {
    "id": 97,
    "description": "BANCO PROVINCIA DEL NEUQUÉN SOCIEDAD ANÓ",
    "oldId": null
  },
  {
    "id": 309,
    "description": "BANCO RIOJA SOCIEDAD ANONIMA UNIPERSONAL",
    "oldId": null
  },
  {
    "id": 247,
    "description": "BANCO ROELA S.A.",
    "oldId": null
  }
]
```

```
SELECT TOP (1000) [ID_BANCO]
      ,[DESCRIPCION]
      ,[idbcoold]
  FROM [NEW_BYTES].[dbo].[BANCOS]
```

Research: Al final las query se parecen mas a esto:

```
SELECT 
isnull((SELECT top(1) IMPORTE
FROM [NEW_BYTES].[dbo].[MC_SALDOS_BANCOS] where Id_Caja_Cuenta = B.Id_Caja_Cuenta and ID_MONEDA = 1 order by FECHA_SALDO desc),0),
isnull((SELECT  top(1)  IMPORTE
FROM [NEW_BYTES].[dbo].[MC_SALDOS_BANCOS] where Id_Caja_Cuenta = B.Id_Caja_Cuenta and ID_MONEDA = 2  order by FECHA_SALDO desc),0),
*
FROM [NEW_BYTES].[dbo].[BA_BP_BANCOS] A
LEFT JOIN NEW_BYTES.dbo.BA_BP_CAJA_CBANCARIAS B ON A.Id_Banco = B.Id_Banco
```
