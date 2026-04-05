---
jira_key: "NBWEB-648"
summary: "API - Feat - Listas de precio csv -> Agregar nueva utilidad y mascara de Categoria"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-15 08:51"
updated: "2025-08-27 09:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-648"
---

# NBWEB-648: API - Feat - Listas de precio csv -> Agregar nueva utilidad y mascara de Categoria

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-15 08:51 |
| Actualizado | 2025-08-27 09:34 |
| Etiquetas | ninguna |
| Jira | [NBWEB-648](https://bluinc.atlassian.net/browse/NBWEB-648) |

## Descripción

Agregaremos al CSV las ultimas columnas, quedando de la siguiente manera

```
CODIGO
ID FABRICANTE
CATEGORIA
DETALLE	IMAGEN
IVA	
STOCK
GARANTIA
MONEDA
PRECIO
PRECIO FINAL
COTIZACION DOLAR
PRECIO PESOS SIN IVA
PRECIO PESOS CON IVA
ATRIBUTOS
CATEGORIA USUARIO <-- NUEVA
PRECIO FINAL USUARIO <-- NUEVA
UTILIDAD USUARIO <-- NUEVA
```

Es importante que cada vez que agregamos una columna, lo hagamos al final para no romper el mapeo que puedan tener algunos clientes
