---
jira_key: "INV-84"
summary: "API - Refactor - Incorporar codigo para autogenerar descripciones con IA"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-12 09:44"
updated: "2025-12-29 15:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-84"
---

# INV-84: API - Refactor - Incorporar codigo para autogenerar descripciones con IA

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-12 09:44 |
| Actualizado | 2025-12-29 15:22 |
| Etiquetas | ninguna |
| Jira | [INV-84](https://bluinc.atlassian.net/browse/INV-84) |

## Descripción

Pedir token por privado

```
POST {API_URL}/v1/suggestDescription
```

```
 {
    "characteristics": informacion copiada asi nomas de lo sitios oficiales,
    "itemId": 118865,
    "temperature": 0.2
  },
```

La idea es obtener una sugerencia para una descripción. 

Las caracteristicas pueden existir o no.

Temperatura es un valor de 0 a 1 que ajuste el nivl de determinismo del agente
