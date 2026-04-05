---
jira_key: "NBWEB-322"
summary: "Agregar limite de seguro para los envios en camioneta"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-06-29 15:59"
updated: "2022-07-11 15:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-322"
---

# NBWEB-322: Agregar limite de seguro para los envios en camioneta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-29 15:59 |
| Actualizado | 2022-07-11 15:14 |
| Etiquetas | ninguna |
| Jira | [NBWEB-322](https://bluinc.atlassian.net/browse/NBWEB-322) |

## Descripción

Deberíamos agregarle al recurso para cotizar 

```
{{API_URL}}/v1/carrito/calcularEnvioPara/
```

Un limite que puede o no ser null (no considerado) que debería estar asociado en la tabla mediosDeEnvio a cada tipo de envío.

Se trata de un monto total máximo que el flete considera que asegura la mercadería. Si se excede ese limite no debe mostrarse.
