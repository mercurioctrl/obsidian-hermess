---
jira_key: "EXP-53"
summary: "API - Feat - Armar paqueteria"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-09 09:01"
updated: "2023-05-29 06:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-53"
---

# EXP-53: API - Feat - Armar paqueteria

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-09 09:01 |
| Actualizado | 2023-05-29 06:34 |
| Etiquetas | ninguna |
| Jira | [EXP-53](https://bluinc.atlassian.net/browse/EXP-53) |

## Descripción

```
POST {{API_URL}}/v1/shipments/addTrackingOrder
```

Basándonos en el siguiente recurso, se debe poder armar paquetes, evitar rescribir código.

```
Esta basado en {{MS_ENVIOS}}/addTrackingOrder/nb
```

Que envia la siguiente carga util.

```
{
    "branch": "0002",
    "order": "10286794",
    "packageGroup": 2
}
```

[https://liodev.postman.co/workspace/Team-LO~75849ccd-cf9d-4bd6-8a70-d240478268d8/request/16026277-96c3abd3-c769-469b-be35-72dacae2dc06](https://liodev.postman.co/workspace/Team-LO~75849ccd-cf9d-4bd6-8a70-d240478268d8/request/16026277-96c3abd3-c769-469b-be35-72dacae2dc06)

Si es necesario el login, en ms envios integrarlo para que ya quede disponible.
