---
jira_key: ADATA-386
status: Revisión
assignee: Ezequiel manzano
assignee_email: null
reporter: Catriel Mercurio
priority: Medium
issuetype: Subtarea
project: ADATA
updated: "2026-03-30T11:52:01.592-0300"
created: "2026-03-29T21:48:43.831-0300"
url: "https://bluinc.atlassian.net/browse/ADATA-386"
tags: [jira, ADATA, revisión]
---

# ADATA-386 · API - Feat - Procesar compras mediante el reporte del cliente

[ADATA-386 en Jira](https://bluinc.atlassian.net/browse/ADATA-386)

## Descripción

Se requiere implementar una función en la API que permita a los administradores adjudicar compras a los clientes. Esto se hará utilizando un sistema de coincidencia de palabras clave basado en el total o parcial del nombre del cliente.

### Contexto

El cliente proporcionó una planilla que se utilizará para procesar las compras. Los administradores deben poder asignar estas compras a los clientes desde su cuenta.

### Criterios de aceptación

- Implementar un sistema de coincidencia de palabras clave para adjudicar compras.
- Permitir coincidencias totales o parciales con el nombre del cliente.
- Registrar quién genera el registro (cliente o marca como admin).

### Otra información

---
_Sincronizado por jira-sidecar el 2026-06-07 22:31:44 UTC._
