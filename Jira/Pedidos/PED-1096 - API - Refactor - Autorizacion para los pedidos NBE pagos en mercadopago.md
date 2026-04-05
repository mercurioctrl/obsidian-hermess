---
jira_key: "PED-1096"
aliases: ["PED-1096"]
summary: "API - Refactor - Autorizacion  para los pedidos NBE pagos en mercadopago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-09-09 09:17"
updated: "2025-09-16 20:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1096"
---

# PED-1096: API - Refactor - Autorizacion  para los pedidos NBE pagos en mercadopago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-09-09 09:17 |
| Actualizado | 2025-09-16 20:22 |
| Etiquetas | ninguna |
| Jira | [PED-1096](https://bluinc.atlassian.net/browse/PED-1096) |

## Relaciones

- **Padre:** [[PED-123]] Feat - Liquidar pedido
- **action item from:** [[SNB-3374]] Conector NB - Sincronización automática -> Actualización no reflejada

## Descripcion

Permite autorizar una compra origanada en NBE, teniendo como condicion que sea companyCode = 9 y su mla de pedclit no sea null.

De cumplir con esto, podria reutilizar la misma logica que se utiliza para autorizar un pedido de libreopcion.

Endpoint a utilizar.

```php
    # Payment For Bank
    Route::post('paymentForBank', PaymentForBank::class);
```
