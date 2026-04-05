---
jira_key: "LAW-62"
aliases: ["LAW-62"]
summary: "Seleccionar automáticamente categoría \"Import / Export\" cuando el país no es Argentina"
status: "POR HACER"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-04-04 21:15"
updated: "2026-04-04 21:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-62"
---

# LAW-62: Seleccionar automáticamente categoría "Import / Export" cuando el país no es Argentina

| Campo | Valor |
|-------|-------|
| Estado | POR HACER (Por hacer) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-04-04 21:15 |
| Actualizado | 2026-04-04 21:15 |
| Etiquetas | ninguna |
| Jira | [LAW-62](https://bluinc.atlassian.net/browse/LAW-62) |

## Relaciones

- **Padre:** [[LAW-43]] Onboarding producción

## Descripcion

En el formulario de "Agregar Nuevo Cliente" de la aplicación de Pedidos, cuando se selecciona un país distinto a Argentina, el campo "Categoría" debería seleccionarse automáticamente en **Import / Export**.

**Comportamiento esperado:**

- Si el usuario selecciona cualquier país que NO sea Argentina (ej: Estados Unidos, Francia, Alemania, etc.), la categoría debe cambiar automáticamente a "Import / Export".


- Si el usuario selecciona Argentina, la categoría debe permanecer en su valor por defecto o permitir elegir libremente.



**Referencia visual:** Ver captura adjunta donde se muestra el formulario con país "Estados Unidos De America" y categoría "Import / Export".
