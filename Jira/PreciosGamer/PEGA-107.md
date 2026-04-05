---
jira_key: "PEGA-107"
summary: "APP - Refactor - Cuando te deslizas para abajo y se acaban los resultados, desaparece todo el contenido"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-09-09 07:42"
updated: "2024-09-11 04:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-107"
---

# PEGA-107: APP - Refactor - Cuando te deslizas para abajo y se acaban los resultados, desaparece todo el contenido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-09 07:42 |
| Actualizado | 2024-09-11 04:15 |
| Etiquetas | ninguna |
| Jira | [PEGA-107](https://bluinc.atlassian.net/browse/PEGA-107) |

## Descripción

[attachment]
Parece ser que al terminarse los resultados, cuando total es `total`:0

```
{
    "response": [],
    "pagination": {
        "total": 0,
        "offset": 60,
        "limit": 30,
        "order": "asc_price"
    }
}
```

Se pierde lo que estas viendo. Si no es un problema de front, lo reasignamos al back.
