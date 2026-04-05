---
jira_key: "PED-1019"
aliases: ["PED-1019"]
summary: "API - MVP - Mejora de performance del repositorio de clientes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-13 08:17"
updated: "2025-07-07 08:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1019"
---

# PED-1019: API - MVP - Mejora de performance del repositorio de clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-13 08:17 |
| Actualizado | 2025-07-07 08:02 |
| Etiquetas | ninguna |
| Jira | [PED-1019](https://bluinc.atlassian.net/browse/PED-1019) |

## Relaciones

- **Padre:** [[PED-15 - Clientes|PED-15]] Clientes

## Descripcion

Actualmente al ejecutar el repositorio de clientes `EN PRODUCCION` de esta forma

```
GET {API_URL}/v1/clients
```

El recurso tiene una demora entre 6 y 10 segundos

Se deben buscar estrategias, configuraciones, creación de indices que permitan reducir la espera del repositorio ya sea filtrado como no filtrado a 2 segundos o menos
