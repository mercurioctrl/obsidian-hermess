---
jira_key: "COB-553"
aliases: ["COB-553"]
summary: "API - Refactor - Mejorar velocidad de carga para \"cobrables\" sin afectar resultados"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-03 06:34"
updated: "2025-02-03 20:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-553"
---

# COB-553: API - Refactor - Mejorar velocidad de carga para "cobrables" sin afectar resultados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-03 06:34 |
| Actualizado | 2025-02-03 20:12 |
| Etiquetas | ninguna |
| Jira | [COB-553](https://bluinc.atlassian.net/browse/COB-553) |

## Relaciones

- **Padre:** [[COB-33 - Cobrar|COB-33]] Cobrar

## Descripcion

```
GET {API_URL}/v1/tradable
```

Al igual que realizamos en otros repositorios, se busca mejorar el tiempo de carga de este, pero sin afectar los datos que muestra y los totales.
