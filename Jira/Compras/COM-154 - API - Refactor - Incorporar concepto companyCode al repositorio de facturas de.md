---
jira_key: "COM-154"
aliases: ["COM-154"]
summary: "API - Refactor - Incorporar concepto companyCode al repositorio de facturas de COMPRA"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-09 08:10"
updated: "2024-12-26 10:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-154"
---

# COM-154: API - Refactor - Incorporar concepto companyCode al repositorio de facturas de COMPRA

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-09 08:10 |
| Actualizado | 2024-12-26 10:44 |
| Etiquetas | ninguna |
| Jira | [COM-154](https://bluinc.atlassian.net/browse/COM-154) |

## Relaciones

- **Padre:** [[COM-27 - Listar facturas de compras|COM-27]] Listar facturas de compras 
- **has action item:** [[COM-159 - APP - Refactor - Agregar filtro empresa global|COM-159]] APP - Refactor - Agregar filtro empresa global

## Descripcion

Al igual que lo realizado en ventas, incorporaremos el concepto `companyCode` a la parte de compras

Para esto lo agregaremos en la tabla `[NewBytes_DBF].[dbo].[facprot].companyCode`

Y de esta forma lo filtraremos en el recurso

```
GET {API_URL}/v1/providerVoucher?companyCode={companyCode}
```

A su vez, tambien lo agregaremos en el objeto de respuesta del recurso

```
{
    "response": [
        {
            "voucherCode": 34621,
            "voucherNumber": "A-0003-00090234",
            "providerId": "001171",
            "providerName": "SIGNIFY ARGENTINA S.A.",
            "voucherDataDate": "2024-12-06 17:19:54",
            "voucherDate": "2024-11-27 00:00:00",
            "currencyPrefix": "PSO",
            "currencyAmount": 1,
            "fob": "0.0",
            "providerOrderInbound": "15645",
            "statusId": null,
            "id": 103258,
            "companyCode": 4 <<-- SE AGREGA
        },
```

Para evitar concurrencias indeseadas dado que somos tres tirando codigo a este repo, se aconseja trabajar una rama aparte por feature a partir de development
