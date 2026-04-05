---
jira_key: "EXP-184"
aliases: ["EXP-184"]
summary: "API - Feat - Agregar posibilidad de serial izar en intervalos, como se hizo para la entrada, pero para la salida"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-01-26 10:00"
updated: "2024-02-07 15:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-184"
---

# EXP-184: API - Feat - Agregar posibilidad de serial izar en intervalos, como se hizo para la entrada, pero para la salida

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-26 10:00 |
| Actualizado | 2024-02-07 15:22 |
| Etiquetas | ninguna |
| Jira | [EXP-184](https://bluinc.atlassian.net/browse/EXP-184) |

## Relaciones

- **Padre:** [[EXP-15 - Feat - Serializar salida|EXP-15]] Feat - Serializar salida
- **blocks:** [[EXP-186 - APP - Feat - Serializar salida por intervalos|EXP-186]] APP - Feat - Serializar salida por intervalos

## Descripcion

Lo que haremos es usar el metodo [link](https://lioteam.atlassian.net/browse/EXP-66)  pero en lugar de usar el parametro `mode:list` usaremos `mode:interval` como hacemos en [link](https://lioteam.atlassian.net/browse/EXP-45) 

```
[
  {
    mode:interval, //indica el modo para la lista
    "serials": [
        'MMFE8YT000095',
        'MMFE8YT000105'
    ]
}
]
```
