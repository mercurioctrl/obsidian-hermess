---
jira_key: "NBWEB-221"
aliases: ["NBWEB-221"]
summary: "APP - Formulario para pagos MP tarjeta y plata en cuenta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-06-02 16:17"
updated: "2022-06-26 21:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-221"
---

# NBWEB-221: APP - Formulario para pagos MP tarjeta y plata en cuenta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-02 16:17 |
| Actualizado | 2022-06-26 21:08 |
| Etiquetas | ninguna |
| Jira | [NBWEB-221](https://bluinc.atlassian.net/browse/NBWEB-221) |

## Relaciones

- **Padre:** [[NBWEB-77]] Implementar Pagos
- **relates to:** [[NBWEB-219]] API - Procesar pagos con plata en cuenta de mercadopago

## Descripcion

```
POST {{API_URL}}/mercadopago?branch={numeroDeBranch}&orderNumber={numero de orden}
```

Se debe levantar un modal, para el caso de dinero en cuenta

[https://www.mercadopago.com.ar/developers/es/docs/checkout-api/wallet-integration/wallet-addto-website](https://www.mercadopago.com.ar/developers/es/docs/checkout-api/wallet-integration/wallet-addto-website)

[en desarrollo]
