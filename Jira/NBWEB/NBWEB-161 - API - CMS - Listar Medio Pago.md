---
jira_key: "NBWEB-161"
aliases: ["NBWEB-161"]
summary: "API - CMS - Listar Medio Pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-02 09:41"
updated: "2022-07-21 10:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-161"
---

# NBWEB-161: API - CMS - Listar Medio Pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-02 09:41 |
| Actualizado | 2022-07-21 10:42 |
| Etiquetas | ninguna |
| Jira | [NBWEB-161](https://bluinc.atlassian.net/browse/NBWEB-161) |

## Relaciones

- **Padre:** [[NBWEB-73 - API - CMS - ABMS|NBWEB-73]] API - CMS - ABMS

## Descripcion

Listar todos los medios de pago para poder editarlos

```
GET {{API_URL}}/v1/CMS/paymentMethods
```

Devuelve un array de objetos

Request

```json
[
  {
  'paymentMethodId': 3,
  'description': 'Transferencia bancaria',
  'show': true
  },
   {
  'paymentMethodId': 3,
  'description': 'Transferencia bancaria',
  'show': true
  }
]
```
