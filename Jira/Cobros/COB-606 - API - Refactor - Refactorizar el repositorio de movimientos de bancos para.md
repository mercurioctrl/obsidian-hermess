---
jira_key: "COB-606"
aliases: ["COB-606"]
summary: "API - Refactor - Refactorizar el repositorio de  movimientos de bancos para agregar atributos y filtros referidos a companyCode"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-02-03 13:38"
updated: "2026-02-12 23:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-606"
---

# COB-606: API - Refactor - Refactorizar el repositorio de  movimientos de bancos para agregar atributos y filtros referidos a companyCode

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-03 13:38 |
| Actualizado | 2026-02-12 23:21 |
| Etiquetas | ninguna |
| Jira | [COB-606](https://bluinc.atlassian.net/browse/COB-606) |

## Relaciones

- **Padre:** [[COB-9 - API - Feat - Listar bancos|COB-9]] API - Feat - Listar bancos
- **has action item:** [[COB-607 - APP - Refactor - Agregar Filtro Empresa a el repositorio de movimientos de|COB-607]] APP - Refactor - Agregar Filtro Empresa a el repositorio de movimientos de bancos y mostrarlo en el listado

## Descripcion

Se debe refactorizar  el recurso de cuentas bancarias para hacerlo sensible al filtro `companyCode`

```
{API_URL}/v1/currentBankAccount?currentPage=1&itemsPerPage=15&currency=2&agentId=12&companyCode={companyCode}
```

Adicionalmente agregaremos en la respuesta el id y nombre de la empresa

```
{
    "response": [
        {
            "orderBank": 20260202074954,
            "dateOperation": "2026-02-02 07:02:54",
            "amount": -1711,
            "subTotal": 0,
            "symbolCurrency": "$",
            "nameCurrency": "Pesos",
            "agent": "Seba",
            "observation": "",
            "voucherId": 118343,
            "balanceTotal": 0,
            "clientId": null,
            "clientDescription": null,
            "providerId": null,
            "providerDescription": null,
            "bankId": 15,
            "bankDescription": "MercadoPago",
            "originBankId": null,
            "originBankDescription": null,
            "destinyBankId": null,
            "destinyBankDescription": null,
            "companyCode": 4, < --- SE AGREGA
            "companyDescription": "NB DISTRIBUIDORA MAYORISTA S.R.L" < --- SE AGREGA
        },
        {
            "orderBank": 20260126174949,
            "dateOperation": "2026-01-26 17:01:49",
            "amount": -1899.5,
            "subTotal": 0,
            "symbolCurrency": "$",
            "nameCurrency": "Pesos",
            "agent": "Seba",
            "observation": "",
            "voucherId": 118336,
            "balanceTotal": 0,
            "clientId": null,
            "clientDescription": null,

            ...
```
