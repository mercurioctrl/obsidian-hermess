---
jira_key: "EXP-158"
aliases: ["EXP-158"]
summary: "API - Review - Al serializar un pedido poniendo cualquier numero el error es incierto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-01-19 09:26"
updated: "2023-01-27 12:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-158"
---

# EXP-158: API - Review - Al serializar un pedido poniendo cualquier numero el error es incierto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-19 09:26 |
| Actualizado | 2023-01-27 12:01 |
| Etiquetas | ninguna |
| Jira | [EXP-158](https://bluinc.atlassian.net/browse/EXP-158) |

## Relaciones

- **Padre:** [[EXP-15]] Feat - Serializar salida

## Descripcion

No me dice cual es el problema, solo un error generico y por detras

```
{
    "message": "Slim Application Error",
    "exception": [
        {
            "type": "TypeError",
            "code": 0,
            "message": "array_column(): Argument #1 ($array) must be of type array, bool given",
            "file": "/var/www/app/src/Service/Order/ProcessSerialService.php",
            "line": 82
        }
    ]
}
```

[adjunto]
Estaría muy bueno que en ese caso puntual el error sea mas especifico.
