---
jira_key: "NBWEB-531"
summary: "API - Editar - parametros del personal"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-04-18 10:28"
updated: "2023-05-08 07:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-531"
---

# NBWEB-531: API - Editar - parametros del personal

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-18 10:28 |
| Actualizado | 2023-05-08 07:24 |
| Etiquetas | ninguna |
| Jira | [NBWEB-531](https://bluinc.atlassian.net/browse/NBWEB-531) |

## Descripción

```
PATCH {API_URL}/v1/cms/staff
```

Enviaremos el objeto, que permite setear cualquier permiso y parámetro, menos el id que lo usamos en la carga útil.

Puede recibir uno o mas objetos

```
[
  {
    "id": 1,
    "clientes_remitos": 1,
    "dtoGral": -200.0,
    "dtoMax": 4500.0
}
]
```

Solo pueden editar queienes tengan previamente el permiso “gerencia”
