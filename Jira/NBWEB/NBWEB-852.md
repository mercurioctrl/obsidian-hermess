---
jira_key: "NBWEB-852"
summary: "API - Refactor - Los listados de productos deben mostrar solo aquellas empresas (companyCode) que están determinadas en la variable de entorno"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-28 17:14"
updated: "2024-08-30 00:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-852"
---

# NBWEB-852: API - Refactor - Los listados de productos deben mostrar solo aquellas empresas (companyCode) que están determinadas en la variable de entorno

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-28 17:14 |
| Actualizado | 2024-08-30 00:06 |
| Etiquetas | ninguna |
| Jira | [NBWEB-852](https://bluinc.atlassian.net/browse/NBWEB-852) |

## Descripción

Filtraremos todos los llamados a la tabla articulos de los listados (api pura, como listados descargables) para que solo se muestren aquellos productos que se encuentren en la tabla `NewBytes_DBF.dbo.articulos` dentro de ciertos valores enteros de `companyCode`

Esto quiere decir que puedo tener mas valores definidos en mis variables de entorno `.env`
Ejemplo: 

```
COMPANY_CODES=1,4,2
```

Podemos arrancar mostrando solo NB DISTRIBUIDORA MAYORISTA
