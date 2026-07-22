---
jira_key: NBWEB-1028
status: Ready for QA
assignee: Emanuel Jesus Ferreyra
assignee_email: null
reporter: Emanuel Jesus Ferreyra
priority: Medium
issuetype: Subtarea
project: NBWEB
updated: "2026-06-05T19:07:12.126-0300"
created: "2026-06-05T17:33:10.957-0300"
url: "https://bluinc.atlassian.net/browse/NBWEB-1028"
tags: [jira, NBWEB, ready-for-qa]
sprint: Sprint 3 Q3 1/7
---

# NBWEB-1028 · API - ENV - feature - Registro de actividad en envíos con Entregar

[NBWEB-1028 en Jira](https://bluinc.atlassian.net/browse/NBWEB-1028)

## Descripción

Se implementó un sistema de registro automático que guarda en un archivo de log diario cada paso del proceso de creación de envíos y obtención de etiquetas con el transportista Entregar.

Se detectó un caso donde Entregar confirmaba la creación de un envío, pero el número de seguimiento (tracking) no existía en su sistema.  
Sin registro de la comunicación con su API, era imposible identificar cuándo y por qué sucede esto.

**Implementación.**

- Registra la solicitud enviada a Entregar y la respuesta recibida al crear un envío.
- Después de crear el envío, consulta a Entregar para confirmar que el número de tracking existe. Si no existe, lo marca con un símbolo visible (❌).
- Registra también las operaciones de obtención de etiquetas (PDF, ZPL, JPG).
- Los logs se guardan por día y permiten buscar cualquier pedido por número de orden.

El flujo de negocio es igual al anterior. Si falla el registro, el proceso de creación del envío continúa sin interrupciones. Esta implementación es transparente para el usuario final.

**Permite que, ante un reclamo ("el envío se creó pero no tiene tracking válido"), se pueda revisar el log del día y ver qué respondió la API de Entregar en ese momento.**

---
_Sincronizado por jira-sidecar el 2026-06-07 22:27:33 UTC._
