---
jira_key: ADATA-437
status: Revisión
assignee: Ezequiel manzano
assignee_email: null
reporter: Catriel Mercurio
priority: High
issuetype: Subtarea
project: ADATA
updated: "2026-06-02T15:14:19.346-0300"
created: "2026-06-02T09:07:56.483-0300"
url: "https://bluinc.atlassian.net/browse/ADATA-437"
tags: [jira, ADATA, revisión]
---

# ADATA-437 · API - Feat - Envio de correo periodicos de posiciones y aceleradores

[ADATA-437 en Jira](https://bluinc.atlassian.net/browse/ADATA-437)

## Descripción

### Resumen

Implementar un sistema de envío de correos para informar a los usuarios su posición actual en el ranking y sus puntos acumulados.

Los envíos podrán ejecutarse de manera semanal automática o manual cuando se requiera.

El sistema debe usar una cola de envío con persistencia en base de datos para controlar el estado de cada correo enviado y evitar duplicados.

Cada usuario debe recibir una única vez el correo correspondiente a un envío determinado, incluso si el proceso se ejecuta nuevamente por error.

El contenido del correo debe incluir:

- Posición actual del usuario en el ranking.
- Cantidad de puntos acumulados.
- Competidores cercanos en la tabla de posiciones.
- Botón para ingresar al sitio.
- Plantilla o banner diferente según el tier o liga del usuario.

El contenido deberá enviarse en formato simple y estructurado para que frontend o marketing puedan aplicar luego el diseño visual final.

### Contexto

Feature: Correos de ranking por puntos.

### Criterios de aceptación

1. El sistema genera un registro de envío individual por cada usuario incluido en una campaña o envío de ranking.
2. Un mismo usuario no puede recibir dos veces el mismo correo para un mismo envío.
3. El sistema registra el estado del envío, los intentos realizados y los errores en caso de falla.
4. El correo muestra correctamente la posición, los puntos y los competidores cercanos del usuario.
5. El banner o plantilla utilizada cambia según el tier, liga o confederación del usuario.
6. El correo incluye un acceso directo al sitio mediante un botón o enlace.

###

---
_Sincronizado por jira-sidecar el 2026-06-07 22:24:24 UTC._
