---
jira_key: "NBWEB-235"
summary: "API -  Eliminar un medio de pago de mp"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-06-06 16:51"
updated: "2022-11-09 11:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-235"
---

# NBWEB-235: API -  Eliminar un medio de pago de mp

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-06 16:51 |
| Actualizado | 2022-11-09 11:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-235](https://bluinc.atlassian.net/browse/NBWEB-235) |

## Descripción

```
DELETE {{API_URL}}/v1/carrito/mpPaymentMethods
```

payload

```
{
  id : 47982343
  customer_id: 2345234
}
```

return

```
{
succes:true
}
```
