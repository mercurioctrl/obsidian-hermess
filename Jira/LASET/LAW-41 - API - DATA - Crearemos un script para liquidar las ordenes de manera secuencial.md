---
jira_key: "LAW-41"
aliases: ["LAW-41"]
summary: "API - DATA - Crearemos un script para liquidar las ordenes de manera secuencial"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-04 07:54"
updated: "2025-12-05 04:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-41"
---

# LAW-41: API - DATA - Crearemos un script para liquidar las ordenes de manera secuencial

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-04 07:54 |
| Actualizado | 2025-12-05 04:13 |
| Etiquetas | ninguna |
| Jira | [LAW-41](https://bluinc.atlassian.net/browse/LAW-41) |

## Relaciones

- **Padre:** [[LAW-30 - Onboarding de la nueva empresa en los sistemas del grupo NB|LAW-30]] Onboarding de la nueva empresa en los sistemas del grupo NB

## Descripcion

Según lo conversado crearemos un pequeño script que pueda golpear el recurso

```
POST {API_URL}/v1/closeSale
```

de menera secuencial, de modo tal de que se puedan procesar todos los pedidos importados de laset, generando todos los registros como si hubiesen sido procesados por una persona

Para esto los liquidaremos como Pago con Cuenta Corriente (`"paymentMethod":1`) y retiro en persona (`"shippingMethod":3999`)
