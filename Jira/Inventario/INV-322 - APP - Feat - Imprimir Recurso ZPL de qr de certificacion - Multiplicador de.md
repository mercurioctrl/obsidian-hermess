---
jira_key: "INV-322"
aliases: ["INV-322"]
summary: "APP - Feat - Imprimir Recurso ZPL de qr de certificacion -> Multiplicador de cantidad"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-09 09:23"
updated: "2026-01-22 11:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-322"
---

# INV-322: APP - Feat - Imprimir Recurso ZPL de qr de certificacion -> Multiplicador de cantidad

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-09 09:23 |
| Actualizado | 2026-01-22 11:21 |
| Etiquetas | ninguna |
| Jira | [INV-322](https://bluinc.atlassian.net/browse/INV-322) |

## Relaciones

- **Padre:** [[INV-260]] Certificados eléctricos por Qr
- **action item from:** [[INV-321]] API - Refactor - Recurso ZPL para imprimir qr de certificacion -> Multiplicador de cantidad

## Descripcion

Al hacer click se debe preguntar la cantidad y se debe enviar el parámetro `amount` el cual representa un numero entero que permite repetir la cantidad de etiquetas que se necesitan imprimir.

```
GET {API_URL}/electricalCertificate/{certificateId}/zpl?amount={amount}
```
