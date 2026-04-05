---
jira_key: "PEGA-182"
aliases: ["PEGA-182"]
summary: "API - Refactor - Admitir búsquedas por términos por separado"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-04-25 08:45"
updated: "2025-04-29 10:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-182"
---

# PEGA-182: API - Refactor - Admitir búsquedas por términos por separado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-25 08:45 |
| Actualizado | 2025-04-29 10:42 |
| Etiquetas | ninguna |
| Jira | [PEGA-182](https://bluinc.atlassian.net/browse/PEGA-182) |

## Relaciones

- **Padre:** [[PEGA-6]] Feat - Listar productos

## Descripcion

Dado algunos casos puntuales que queremos trabajar (Se requiere trabajar sobre un apartado consolas (ps5,xbox,nitendo, etc) dentro de los mismos resultados de búsqueda se debe buscar una manera pero sin afectar las búsquedas tradicionales

Tal vez es posible detectar cuando los términos están separados por coma e incluir una condición LIKE especifica para cada termino y que al hacer algo como `search=XBOX,PS5,nintendo` me muestra prodcutos que pueden contener el termino xbox o ps5  o nintendo por igual.

```
https://api.preciosgamer.com/v1/items?rate=down&order=asc_price&search=XBOX,PS5,nintendo&changedate=10&priceLimit=150000-2919870&offset=0
```

Se aceptan otras ideas y sugerencias de como obtener la feature, avisame lo que se te ocurra y lo charlamos!
