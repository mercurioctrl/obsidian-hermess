---
jira_key: "COB-552"
aliases: ["COB-552"]
summary: "API - Refactor - Mejorar performance para repositorio de movimientos de caja (regla de los 2s en produ)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-03 06:31"
updated: "2025-02-03 20:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-552"
---

# COB-552: API - Refactor - Mejorar performance para repositorio de movimientos de caja (regla de los 2s en produ)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-03 06:31 |
| Actualizado | 2025-02-03 20:11 |
| Etiquetas | ninguna |
| Jira | [COB-552](https://bluinc.atlassian.net/browse/COB-552) |

## Relaciones

- **Padre:** [[COB-15 - Cajas|COB-15]] Cajas

## Descripcion

```
GET {API_URL}/v1/box/{usuario}
```

Al igual que realizamos en otros repositorios, se busca mejorar el tiempo de carga de este, pero sin afectar los datos que muestra y los totales.



Actualmente tarda ~18s.



[adjunto]
