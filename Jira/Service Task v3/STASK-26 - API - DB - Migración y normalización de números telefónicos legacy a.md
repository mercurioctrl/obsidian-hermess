---
jira_key: "STASK-26"
aliases: ["STASK-26"]
summary: "API - DB - Migración y normalización de números telefónicos legacy a repositorio unificado de usuarios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-13 17:47"
updated: "2026-03-02 16:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-26"
---

# STASK-26: API - DB - Migración y normalización de números telefónicos legacy a repositorio unificado de usuarios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-13 17:47 |
| Actualizado | 2026-03-02 16:14 |
| Etiquetas | ninguna |
| Jira | [STASK-26](https://bluinc.atlassian.net/browse/STASK-26) |

## Relaciones

- **Padre:** [[STASK-20 - API - Workers - Preparación para SMS y WhatsApp (sin ejecución)|STASK-20]] API - Workers - Preparación para SMS y WhatsApp (sin ejecución)

## Descripcion

Se requiere centralizar y normalizar los números telefónicos de usuarios actualmente dispersos en tablas legacy (`vendor_verification`, `clientes`, `legacy_notification_users`) hacia una nueva tabla `UserPhoneNumbers`.

La migración debe:.

- Evitar duplicados por `(UserId, Phone)`.


- Priorizar fuentes confiables (`vendor_verification`) como número primario.


- Importar solo el **último número válido por usuario** desde tablas legacy con alto volumen histórico.


- Mantener trazabilidad mediante campos `Source` y `SourceRefId`.



Este repositorio será la **fuente única** para SMS y WhatsApp (Twilio), desacoplado de dispositivos.
