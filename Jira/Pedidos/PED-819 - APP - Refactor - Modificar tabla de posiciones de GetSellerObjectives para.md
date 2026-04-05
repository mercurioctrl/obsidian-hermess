---
jira_key: "PED-819"
aliases: ["PED-819"]
summary: "APP - Refactor - Modificar tabla de posiciones de GetSellerObjectives para cumplir un nuevo requerimiento"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-09-16 07:32"
updated: "2024-09-17 01:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-819"
---

# PED-819: APP - Refactor - Modificar tabla de posiciones de GetSellerObjectives para cumplir un nuevo requerimiento

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-16 07:32 |
| Actualizado | 2024-09-17 01:40 |
| Etiquetas | ninguna |
| Jira | [PED-819](https://bluinc.atlassian.net/browse/PED-819) |

## Relaciones

- **Padre:** [[PED-242]] Pestaña Estadisticas
- **is blocked by:** [[PED-818]] API - Refactor - Modificar GetSellerObjectives para cumplir un nuevo requerimiento
- **is blocked by:** [[MKT-215]] NB_ FLOR DE INCENTIVO

## Descripcion

Usando el recurso

```
GET {API_URL}/v1/objectives/capillarityIncentive/sellers
```

Agregaremos la nueva columna para la cantidad de `UniqueClients` 

[adjunto]
Adicionalmente marcaremos con algún destaque el valor mas alto de `UniqueClients` y el valor mas alto de `TotalSales` para poder reflejar los dos ganadores descritos en [link](https://lioteam.atlassian.net/browse/MKT-215) 

También estaría bueno que arriba de la tablita se explique brevemente el objetivo con algo como “El vendedor que acumule mas clientes que compren las marcas AUREOX, RAIDMAX, F&D FENDA y DUCKY gana u$s 100. Tambien gana u$s 100 quien acumule mayor facturación para estas bancas. Un solo vendedor no puede ganar ambas competencias, en caso de suceder, el segundo puesto gana el segundo premio”
