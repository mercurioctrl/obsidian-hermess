---
jira_key: "STASK-15"
aliases: ["STASK-15"]
summary: "Sistema de Notificaciones Multicanal (Queue + Workers)"
status: "Tareas por hacer"
type: "Epic"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2026-01-13 08:42"
updated: "2026-01-13 08:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-15"
---

# STASK-15: Sistema de Notificaciones Multicanal (Queue + Workers)

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Epic |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-13 08:42 |
| Actualizado | 2026-01-13 08:43 |
| Etiquetas | ninguna |
| Jira | [STASK-15](https://bluinc.atlassian.net/browse/STASK-15) |

## Relaciones

*Sin relaciones*

## Descripcion

Implementar un sistema centralizado para **encolar y enviar notificaciones** a usuarios por distintos canales.


El sistema desacopla la **intención de notificar** del **envío real**, utilizando colas y workers por canal.


En esta primera etapa se implementan **push notifications (Android + iPhone/APNs)** y **emails**, dejando el diseño preparado para **SMS y WhatsApp** sin romper contratos futuros.


El objetivo es garantizar escalabilidad, trazabilidad, control de duplicados opcional y estabilidad operativa.
