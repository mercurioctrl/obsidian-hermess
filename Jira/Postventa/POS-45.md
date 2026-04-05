---
jira_key: "POS-45"
summary: "API - Feat - Enviar mensaje al cliente"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-29 09:19"
updated: "2022-10-14 09:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-45"
---

# POS-45: API - Feat - Enviar mensaje al cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-29 09:19 |
| Actualizado | 2022-10-14 09:34 |
| Etiquetas | ninguna |
| Jira | [POS-45](https://bluinc.atlassian.net/browse/POS-45) |

## Descripción

Este recurso se trata sobre consumir el servicie de messageChannel de la API de nb

```
POST {API_URL}/v1/preAftersales/{preAftersalesId}/sendMessage
```

Lo que se busca es poder entablar una conversación fluida con el cliente antes de que traiga la mercadería. O incluso posteriormente.

Cada vez que enviamos un mensaje, se debe enviar un correo.
