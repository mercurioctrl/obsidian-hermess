---
jira_key: "NBWEB-163"
summary: "API - CMS - Editar medios pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-02 09:51"
updated: "2022-07-26 08:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-163"
---

# NBWEB-163: API - CMS - Editar medios pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-02 09:51 |
| Actualizado | 2022-07-26 08:56 |
| Etiquetas | ninguna |
| Jira | [NBWEB-163](https://bluinc.atlassian.net/browse/NBWEB-163) |

## Descripción

*se podra agregar el parametro para el interes?

```
POST {{API_URL}}/v1/cms/paymethMethods
```

Request

```
[
  {
  'paymentMethodId': 3,
  'description': 'Transferencia bancaria',
  'show': true
  } 
]
```
