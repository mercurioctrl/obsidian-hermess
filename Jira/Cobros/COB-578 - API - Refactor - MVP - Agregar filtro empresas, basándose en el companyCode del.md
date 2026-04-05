---
jira_key: "COB-578"
aliases: ["COB-578"]
summary: "API - Refactor - MVP - Agregar filtro empresas, basándose en el companyCode del cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-26 15:06"
updated: "2025-10-08 10:51"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/COB-578"
---

# COB-578: API - Refactor - MVP - Agregar filtro empresas, basándose en el companyCode del cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-26 15:06 |
| Actualizado | 2025-10-08 10:51 |
| Etiquetas | MVPLaset |
| Jira | [COB-578](https://bluinc.atlassian.net/browse/COB-578) |

## Relaciones

- **Padre:** [[COB-573]] Clientes
- **has action item:** [[COB-580]] APP - Refctor - MVP - Agregar filtro empresas al repositorio de clientes

## Descripcion

Agregaremos el filtro `companyCode` para poder filtrar los clientes según la clave `[NewBytes_DBF].[dbo].[clientes].companyCode`

```
GET {API_URL}/v1/clients?companyCode={companyCode}
```

```
{
    "response": [
        {
            "clientId": 93255,
            "clientName": "NU\u00d1EZ MARIA FABIANA",
            "clientBusinessName": "NU\u00d1EZ MARIA FABIANA",
            "clientTaxNumber": "27209466827",
            "clientPerception": 0,
            "limitCheckBalanceAmount": 0,
            "usedCheckBalanceAmount": 0,
            "limitBalanceAmount": 0,
            "usedBalanceAmount": 0,
            "desactive": false,
            "salespersonName": "Altamiranda Andrea",
            "sellerId": 8
        },
        {
            "clientId": 93177,
            "clientName": "LUXYT TRADE",
            "clientBusinessName": "LUXYT TRADE",
            "clientTaxNumber": "30717442144",
            "clientPerception": 0,
            "limitCheckBalanceAmount": 0,
            "usedCheckBalanceAmount": 0,
            "limitBalanceAmount": 0,
            "usedBalanceAmount": 1.2999999967178155e-5,
            "desactive": false,
            "salespersonName": "Altamiranda Andrea",
            "sellerId": 8
        },
        {
            "clientId": 93160,
            "clientName": "TARAMARCAZ NORA LIA",
            "clientBusinessName": "TARAMARCAZ NORA LIA",
            "clientTaxNumber": "27272288637",
            "clientPerception": 0,
            "limitCheckBalanceAmount": 0,
            
            ....
```
