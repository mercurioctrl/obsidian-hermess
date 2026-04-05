---
jira_key: "INV-278"
aliases: ["INV-278"]
summary: "API - Review - Al ejecutar el syncUp no parece estar agregando el stock de mis nuevos kits"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-10 09:33"
updated: "2025-12-10 15:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-278"
---

# INV-278: API - Review - Al ejecutar el syncUp no parece estar agregando el stock de mis nuevos kits

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-10 09:33 |
| Actualizado | 2025-12-10 15:32 |
| Etiquetas | ninguna |
| Jira | [INV-278](https://bluinc.atlassian.net/browse/INV-278) |

## Relaciones

- **Padre:** [[INV-253]] Crear y modificar Kits

## Descripcion

Agregue un nuevo kit en `GAMMA` con un stock que parece cumplir como para agregar varios al stock del kit, pero al ejecutarlo este aparece en 0

```
{{API_URL}}/itemsKits/syncUp
```

[adjunto]
