---
jira_key: "NBWEB-647"
aliases: ["NBWEB-647"]
summary: "API - Feat - Listas de precio xlmx -> Agregar nueva utilidad y mascara de Categoria"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-15 08:51"
updated: "2024-03-25 02:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-647"
---

# NBWEB-647: API - Feat - Listas de precio xlmx -> Agregar nueva utilidad y mascara de Categoria

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-15 08:51 |
| Actualizado | 2024-03-25 02:49 |
| Etiquetas | ninguna |
| Jira | [NBWEB-647](https://bluinc.atlassian.net/browse/NBWEB-647) |

## Relaciones

- **Padre:** [[NBWEB-641]] Listas de precio
- **is blocked by:** [[NBWEB-655]] API - Listas de precio xlsx -> Agregar nueva utilidad y mascara de Categoría - Filtrar categorías por usuario

## Descripcion

```
CODIGO	
ID FABRICANTE	
DETALLE	
IVA	
STOCK	
GARANTIA	
MONEDA	
PRECIO
PRECIO FINAL
COTIZACION DOLAR
PRECIO PESOS SIN IVA
PRECIO PESOS CON IVA
DETALLE	IMAGEN <--
CATEGORIA USUARIO <--
PRECIO FINAL USUARIO <--
UTILIDAD USUARIO <--

```

Es importante que cada vez que agregamos una columna, lo hagamos al final para no romper el mapeo que puedan tener algunos clientes

Fijate que en este agregue el de la imagen principal tambien
