---
jira_key: "COB-383"
aliases: ["COB-383"]
summary: "API - Refactor - Agregar filtro por clientId, agentId y providerId en Listar movimientos bancarios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-03-23 09:04"
updated: "2023-04-28 08:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-383"
---

# COB-383: API - Refactor - Agregar filtro por clientId, agentId y providerId en Listar movimientos bancarios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-23 09:04 |
| Actualizado | 2023-04-28 08:59 |
| Etiquetas | ninguna |
| Jira | [COB-383](https://bluinc.atlassian.net/browse/COB-383) |

## Relaciones

- **Padre:** [[COB-218]] Feat - Movimientos bancarios
- **blocks:** [[COB-395]] APP - Refactor  - Agregar filtros de agente, proveedor y cliente

## Descripcion

Agregaremos los filtros de la siguiente forma

```
GET {API_RUL}/v1/currentBankAccount/{BankId}?clientId={clientId}&providerId={providerId}&agentId={agentId}
```
