---
jira_key: "INV-321"
aliases: ["INV-321"]
summary: "API - Refactor - Recurso ZPL para imprimir qr de certificacion -> Multiplicador de cantidad"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-09 09:23"
updated: "2026-01-22 11:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-321"
---

# INV-321: API - Refactor - Recurso ZPL para imprimir qr de certificacion -> Multiplicador de cantidad

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-09 09:23 |
| Actualizado | 2026-01-22 11:21 |
| Etiquetas | ninguna |
| Jira | [INV-321](https://bluinc.atlassian.net/browse/INV-321) |

## Relaciones

- **Padre:** [[INV-260 - Certificados eléctricos por Qr|INV-260]] Certificados eléctricos por Qr
- **action item from:** [[INV-310 - API - Feat - Recurso ZPL para imprimir qr de certificacion|INV-310]] API - Feat - Recurso ZPL para imprimir qr de certificacion
- **has action item:** [[INV-322 - APP - Feat - Imprimir Recurso ZPL de qr de certificacion - Multiplicador de|INV-322]] APP - Feat - Imprimir Recurso ZPL de qr de certificacion -> Multiplicador de cantidad

## Descripcion

Se debe agregar el parámetro `amount` el cual representa un numero entero que permite repetir la cantidad de etiquetas que se necesitan imprimir.

```
GET {API_URL}/electricalCertificate/{certificateId}/zpl?amount={amount}
```
