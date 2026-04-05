---
jira_key: "NBWEB-184"
summary: "APP - Medio de pago - Componente para el carrito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-05-13 10:49"
updated: "2022-06-26 21:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-184"
---

# NBWEB-184: APP - Medio de pago - Componente para el carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-13 10:49 |
| Actualizado | 2022-06-26 21:33 |
| Etiquetas | ninguna |
| Jira | [NBWEB-184](https://bluinc.atlassian.net/browse/NBWEB-184) |

## Descripción

```
GET {{API_URL}}/v1/carrito/mediosDePago
```

Retorna

```json
[
  {
    "payMethodId": 1,
    "description": "Cta. Cte Cliente"
  },
  {
    "payMethodId": 2,
    "description": "Efectivo Moto"
  },
  {
    "payMethodId": 3,
    "description": "Depósito en Banco"
  },
  {
    "payMethodId": 4,
    "description": "Efectivo Camioneta"
  },
  {
    "payMethodId": 5,
    "description": "Efectivo Caja"
  }
```
