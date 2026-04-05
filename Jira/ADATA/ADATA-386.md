---
jira_key: "ADATA-386"
summary: "API - Feat - Procesar compras mediante el reporte del cliente"
status: "Revisión"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-03-29 21:48"
updated: "2026-03-30 11:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ADATA-386"
---

# ADATA-386: API - Feat - Procesar compras mediante el reporte del cliente

| Campo | Valor |
|-------|-------|
| Estado | Revisión (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-29 21:48 |
| Actualizado | 2026-03-30 11:52 |
| Etiquetas | ninguna |
| Jira | [ADATA-386](https://bluinc.atlassian.net/browse/ADATA-386) |

## Descripción

[attachment]
Se requiere implementar una función en la API que permita a los administradores adjudicar compras a los clientes. Esto se hará utilizando un sistema de coincidencia de palabras clave basado en el total o parcial del nombre del cliente.

### Contexto

El cliente proporcionó una planilla que se utilizará para procesar las compras. Los administradores deben poder asignar estas compras a los clientes desde su cuenta.

### Criterios de aceptación

- Implementar un sistema de coincidencia de palabras clave para adjudicar compras.


- Permitir coincidencias totales o parciales con el nombre del cliente.


- Registrar quién genera el registro (cliente o marca como admin).



### Otra información

[attachment]
