---
jira_key: "LAW-61"
aliases: ["LAW-61"]
summary: "Bug: Al agregar un cliente en Pedidos, aparecen fechas en el selector de País"
status: "POR HACER"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-04-04 21:15"
updated: "2026-04-04 21:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-61"
---

# LAW-61: Bug: Al agregar un cliente en Pedidos, aparecen fechas en el selector de País

| Campo | Valor |
|-------|-------|
| Estado | POR HACER (Por hacer) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-04-04 21:15 |
| Actualizado | 2026-04-04 21:15 |
| Etiquetas | ninguna |
| Jira | [LAW-61](https://bluinc.atlassian.net/browse/LAW-61) |

## Relaciones

- **Padre:** [[LAW-43 - Onboarding producción|LAW-43]] Onboarding producción

## Descripcion

En la aplicación de Pedidos, al intentar agregar un nuevo cliente, el dropdown de "País" muestra valores incorrectos: además de los países válidos (Francia, Austria, Singapur, Alemania, etc.) aparecen fechas como opciones (ej: 2025-11-24 00:00:00, 2026-02-10 00:00:00, 2025-10-17 00:00:00, 2025-12-19 00:00:00).

**Pasos para reproducir:**

- Ir a la sección Pedidos


- Hacer clic en "Agregar Nuevo Cliente"


- Abrir el selector de "País"


- Se observan fechas mezcladas con los países



**Comportamiento esperado:** El selector de País solo debería mostrar nombres de países válidos.

**Comportamiento actual:** Se muestran fechas (formato datetime) junto a los países, probablemente por datos incorrectos en la tabla de países o en la query que alimenta el combo.
