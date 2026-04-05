---
jira_key: "PED-1139"
aliases: ["PED-1139"]
summary: "API - Refactor - Agregar al repositorio de clientes los balances de cuentas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-10-06 08:28"
updated: "2025-10-27 10:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1139"
---

# PED-1139: API - Refactor - Agregar al repositorio de clientes los balances de cuentas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-06 08:28 |
| Actualizado | 2025-10-27 10:51 |
| Etiquetas | ninguna |
| Jira | [PED-1139](https://bluinc.atlassian.net/browse/PED-1139) |

## Relaciones

- **Padre:** [[PED-54]] Cuenta corriente de clientes
- **blocks:** [[PED-1140]] APP - Refactor - Agregar al repositorio de clientes los balances de cuentas
- **has action item:** [[SNB-3398]] Agregar Caja a Pedidos

## Descripcion

Para que desde el área comercial tambien tengan presentes estos datos y puedan filtrar de manera mas sencilla agregaremos los parámetros

- `usedBalanceAmount`


- `limitBalanceAmount`


- `usedCheckBalanceAmount`


- `limitCheckBalanceAmount`



Agregaremos tambien el filtro `balanceState`para poder utilizarlo y filtrar quienes tienen saldo neutro, deuda o a favor

```
GET {API_URL}/v1/clients?balanceState=credit
```

 

```
{
    "list": [
        {
            "ccodcli": 93435,
            "businessName": "Leandro Deferrari",
            "name": "Leandro Deferrari",
            "clientTaxNumber": "37215700",
            "email": "deferrari.leandro@gmail.com",
            "phone": "1133052207",
            "salespersonName": "Opcion Libre",
            "address": "",
            "id": 93435,
            "date": "2025-10-06 03:09:22",
            "provinceDescription": "",
            "sellerId": 100,
            "provinceId": 0,
            "averagePurchaseValue": 0,
            "purchaseFrequency": 0,
            "relationshipDurationMonth": 0,
            "ltv": 0,
            "lastBuy": null,
            "lastBuyDays": null,
            "whaPhone": "",
            "companyCode": 4,
            "specialPrice": 0,
            "profile": 1,
            "mode": "",
            "limitCheckBalanceAmount": 0, <- SE AGREGA
            "usedCheckBalanceAmount": 2529928.8,  <- SE AGREGA
            "limitBalanceAmount": 0,  <- SE AGREGA
            "usedBalanceAmount": -0.0227162,  <- SE AGREGA
        },
        {
            "ccodcli": 93434,
            "businessName": "Leonel Moreno",
            "name": "Leonel Moreno",
            "clientTaxNumber": "40483330",
            "email": "leomoreno330@gmail.com",
            "phone": "3804261732",
            "salespersonName": "Opcion Libre",
            "address": "Soberan\u00eda Nacional 2035 1",
            "id": 93434,
            "date": "2025-10-05 23:23:51",
            "provinceDescription": "",
            "sellerId": 100,
            "provinceId": 0,
            "averagePurchaseValue": 0,
            "purchaseFrequency": 0,
            "relationshipDurationMonth": 0,
            "ltv": 0,
            "lastBuy": null,
            "lastBuyDays": null,
            "whaPhone": "",
            "companyCode": 4,
            "specialPrice": 0,
            "profile": 1,
            "mode": "",
            "limitCheckBalanceAmount": 0, <- SE AGREGA
            "usedCheckBalanceAmount": 2529928.8,  <- SE AGREGA
            "limitBalanceAmount": 0,  <- SE AGREGA
            "usedBalanceAmount": -0.0227162,  <- SE AGREGA
        },
        {
...        
```

Es importante mantener la performance del recurso de modo tal que el mismo no tarde mas de 1s al hacer una búsqueda con al menos 100 resultados
