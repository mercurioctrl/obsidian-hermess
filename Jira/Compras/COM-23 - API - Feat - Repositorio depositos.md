---
jira_key: "COM-23"
aliases: ["COM-23"]
summary: "API - Feat - Repositorio depositos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-13 17:03"
updated: "2024-02-14 09:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-23"
---

# COM-23: API - Feat - Repositorio depositos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-13 17:03 |
| Actualizado | 2024-02-14 09:49 |
| Etiquetas | ninguna |
| Jira | [COM-23](https://bluinc.atlassian.net/browse/COM-23) |

## Relaciones

- **Padre:** [[COM-14 - Repositorios|COM-14]] Repositorios
- **blocks:** [[COM-21 - APP - Feat - Listar ordenes de compra|COM-21]] APP - Feat - Listar ordenes de compra

## Descripcion

```
{API_URL}/v1/warehouse
```

```
[
  {
    "warehouse": "DE1",
    "description": "DEPOSITO 1",
    "addres": null,
    "id": 1,
    "Predeterminado": 1,
    "defaultSet": 2,
    "provinceId": null,
    "counttryId": 1
  },
  {
    "warehouse": "SAF",
    "description": "SAFcom",
    "addres": "Jujuy 1039",
    "id": 2,
    "Predeterminado": null,
    "defaultSet": 2,
    "provinceId": null,
    "counttryId": 1
  ...
```

```
SELECT TOP (1000) [CCODALM]
      ,[CNOMBRE]
      ,[CDIRECC]
      ,[CCODPOBL]
      ,[NCODPROV]
      ,[CTFNO]
      ,[ID_ALMACEN]
      ,[Predeterminado]
      ,[ID_CIUDAD]
      ,[ID_Provincia]
  FROM [NewBytes_DBF].[dbo].[FP_Almacen]
```
