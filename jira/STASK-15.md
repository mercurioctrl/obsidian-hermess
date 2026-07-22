---
jira_key: STASK-15
status: Tareas por hacer
assignee: null
assignee_email: null
reporter: Catriel Mercurio
priority: Medium
issuetype: Epic
project: STASK
updated: "2026-01-13T08:43:19.164-0300"
created: "2026-01-13T08:42:14.810-0300"
url: "https://bluinc.atlassian.net/browse/STASK-15"
tags: [jira, STASK, tareas-por-hacer]
---

# STASK-15 · Sistema de Notificaciones Multicanal (Queue + Workers)

[STASK-15 en Jira](https://bluinc.atlassian.net/browse/STASK-15)

## Descripción

Implementar un sistema centralizado para **encolar y enviar notificaciones** a usuarios por distintos canales.

  
El sistema desacopla la **intención de notificar** del **envío real**, utilizando colas y workers por canal.

  
En esta primera etapa se implementan **push notifications (Android + iPhone/APNs)** y **emails**, dejando el diseño preparado para **SMS y WhatsApp** sin romper contratos futuros.

  
El objetivo es garantizar escalabilidad, trazabilidad, control de duplicados opcional y estabilidad operativa.

---
_Sincronizado por jira-sidecar el 2026-06-07 22:26:33 UTC._
