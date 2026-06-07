---
jira_key: ADATA-367
status: PENDIENTE DE COMUNICAR
assignee: Marbe Moreno
assignee_email: null
reporter: Catriel Mercurio
priority: Medium
issuetype: Historia
project: ADATA
updated: "2026-04-09T12:25:11.631-0300"
created: "2026-02-19T11:24:50.406-0300"
url: "https://bluinc.atlassian.net/browse/ADATA-367"
tags: [jira, ADATA, pendiente-de-comunicar]
---

# ADATA-367 · APP - Feat - Dashboard XPG (puntos + ranking snippet + aceleradores)

[ADATA-367 en Jira](https://bluinc.atlassian.net/browse/ADATA-367)

## Descripción

Dashboard según mockup XPG:

- Puntos totales
- Ranking snippet (anterior/yo/siguiente)
- Aceleradores activos (y accesos a próximos/expirados)
- Banner/área de contenido

Consume repos:

- datos usuario (/me)
- aceleradores (/accelerators?status=)
- ranking snippet (/ranking/snippet)

### Acceptance Criteria

ACCriterioAC1Renderiza puntos totales y estado sin datos.AC2Renderiza ranking snippet correctamente (máx 3 filas).AC3Renderiza aceleradores con vigencia y multiplicador.

---
_Sincronizado por jira-sidecar el 2026-06-07 22:31:49 UTC._
