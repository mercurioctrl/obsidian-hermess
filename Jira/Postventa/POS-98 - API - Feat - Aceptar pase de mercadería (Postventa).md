---
jira_key: "POS-98"
aliases: ["POS-98"]
summary: "API - Feat - Aceptar pase de mercadería (Postventa)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-09-05 15:29"
updated: "2022-10-18 14:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-98"
---

# POS-98: API - Feat - Aceptar pase de mercadería (Postventa)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-05 15:29 |
| Actualizado | 2022-10-18 14:20 |
| Etiquetas | ninguna |
| Jira | [POS-98](https://bluinc.atlassian.net/browse/POS-98) |

## Relaciones

- **Padre:** [[POS-95 - API - Feat - Pedir un pase de mercaderia|POS-95]] API - Feat - Pedir un pase de mercaderia
- **is blocked by:** [[POS-97 - API - Feat - Procesar pase de mercadería (Deposito)|POS-97]] API - Feat - Procesar pase de mercadería (Deposito)
- **blocks:** [[POS-154 - APP - Feat - Aceptar pase de mercadería (Postventa)|POS-154]] APP - Feat - Aceptar pase de mercadería (Postventa)

## Descripcion

Esta historia se trata sobre el momento cuando ya procesaron el pase en el deposito, y ya con la mercadería en la mano, los chicos de postventa aceptan el pase que acaban de hacerles, si todo esta correcto.

```
PATCH {{API_URL}}/v1/passes
```

Como ultimo paso, en este punto se cambia el estado de en `[NB_WEB].[dbo].[passesHeader]` de la columna `statusId` a Finalizado.

(posteriormente al finalizar este caso de postventa, y marcarse como entregado al cliente, se removera de la columna  nstock_postventa en newbytes_Dbf.dbo.stocks)



```
{
    "statusId":2, 
    "passId":11,
    "items": [
        {
            "productDescription": "MOTHER ASUS (LGA1200) PRIME Z590-A",
            "productId": "109344",
            "serial": "M6M0KC428971WTD"
        }
        ]
}
```
