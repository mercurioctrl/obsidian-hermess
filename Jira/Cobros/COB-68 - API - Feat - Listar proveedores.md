---
jira_key: "COB-68"
aliases: ["COB-68"]
summary: "API - Feat - Listar proveedores"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-29 07:37"
updated: "2022-10-20 17:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-68"
---

# COB-68: API - Feat - Listar proveedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-29 07:37 |
| Actualizado | 2022-10-20 17:10 |
| Etiquetas | ninguna |
| Jira | [COB-68](https://bluinc.atlassian.net/browse/COB-68) |

## Relaciones

- **Padre:** [[COB-17 - Pagos a proveedores|COB-17]] Pagos a proveedores
- **Subtarea:** [[COB-69 - API - Feat - Filtros y paginado|COB-69]] API - Feat - Filtros y paginado
- **blocks:** [[COB-70 - APP - Feat - Listar proveedores|COB-70]] APP - Feat - Listar proveedores

## Descripcion

```
GET {{API_URL}}/v1/providers
```

```
[
  {
    "id": 14646,
    "providerCode": "001594",
    "name": "TRENDSETTERS - DA PALACE SRL",
    "businessName": "TRENDSETTERS - DA PALACE SRL",
    "Addres": "CARLOS TEJEDOR 890",
    "countryId": 7,
    "provicenId": 2,
    "localitieId": 14233,
    "Contact": "",
    "TotSaldosaFavor": null,
    "SaldoInicialCTA": null,
    "AgentePercIVA": 0,
    "ivaPercepction": false,
    "correo": "",
    "aliquotIbb": 1
  },
  {
    "id": 14645,
    "providerCode": "001593",
    "name": "FRUITLOSOPHY EMPRSAS SRL",
    "businessName": "FRUITLOSOPHY EMPRSAS SRL",
    "Addres": "",
    "countryId": 7,
    "provicenId": 2,
    "localitieId": 14233,
    "Contact": "",
    "TotSaldosaFavor": null,
    "SaldoInicialCTA": null,
    "AgentePercIVA": 0,
    "ivaPercepction": false,
    "correo": "",
    "aliquotIbb": 1
  }
  ]
```

```
SELECT [ID_PROVEEDOR]
      ,[CCODPRO]
      ,[cnompro]
      ,[NombreComercial]
      ,[Direccion]
      ,[Id_Pais]
      ,[Id_Provincia]
      ,[Id_Ciudad]
      ,[Contacto]
      ,[TotSaldosaFavor]
      ,[SaldoInicialCTA]
      ,[AgentePercIVA]
      ,[Id_CategoriaIVA]
      ,[InscripMunicipal]
      ,[correo]
      ,[alicuotaIbb]
  FROM [NewBytes_DBF].[dbo].[FP_Proveedores]
ORDER BY ccodpro desc
```
