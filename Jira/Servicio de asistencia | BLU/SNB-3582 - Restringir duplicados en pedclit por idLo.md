---
jira_key: "SNB-3582"
aliases: ["SNB-3582"]
summary: "Restringir duplicados en pedclit por idLo"
status: "Abierta"
type: "Error"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Catriel Mercurio"
created: "2025-12-30 14:31"
updated: "2025-12-30 14:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3582"
---

# SNB-3582: Restringir duplicados en pedclit por idLo

| Campo | Valor |
|-------|-------|
| Estado | Abierta (Por hacer) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-30 14:31 |
| Actualizado | 2025-12-30 14:31 |
| Etiquetas | ninguna |
| Jira | [SNB-3582](https://bluinc.atlassian.net/browse/SNB-3582) |

## Relaciones

*Sin relaciones*

## Descripcion

```
SELECT idLo, COUNT(*) AS cantidad
FROM pedclit
WHERE idLo IS NOT NULL
GROUP BY idLo
HAVING COUNT(*) > 1;
```
