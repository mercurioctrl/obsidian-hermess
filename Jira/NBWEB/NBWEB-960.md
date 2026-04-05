---
jira_key: "NBWEB-960"
summary: "API - Feat - Generar catálogo exclusivo para ReplyLatam con precio en pesos final y columnas adicionales"
status: "Finalizada"
type: "Tarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-01 11:50"
updated: "2025-04-21 08:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-960"
---

# NBWEB-960: API - Feat - Generar catálogo exclusivo para ReplyLatam con precio en pesos final y columnas adicionales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-01 11:50 |
| Actualizado | 2025-04-21 08:44 |
| Etiquetas | ninguna |
| Jira | [NBWEB-960](https://bluinc.atlassian.net/browse/NBWEB-960) |

## Descripción

Se requiere generar un nuevo catálogo específico para la empresa **ReplyLatam**, cuya estructura es idéntica al catálogo ya existente en la siguiente URL:

```
https://api.nbe.com.ar/v1/priceListExcel/4520348d5e5ab6d973b54aec33dcd3
```

El nuevo catálogo estará disponible en la siguiente ruta:

```
https://api.nbe.com.ar/v1/priceListReplyLatam/{token}
```

Solo que trae un precio diferente por lo cual queda de la siguiente manera

[attachment]
- **Precio**:
Este nuevo catálogo incluirá **solo un precio final en pesos argentinos**, que reemplazará los distintos precios en dólares que tiene el catálogo base. El precio que se mostrará es el valor conocido como **"PRECIO ML"**, calculado con la siguiente fórmula:

```
(npvp3 * (SELECT COTIZACION FROM NEW_BYTES.dbo.MS_COTIZACIONES WHERE ID=1 )*(ivaVenta/100+1)) AS mlPrice
```

Este valor se obtiene de la tabla `[NewBytes_DBF].[dbo].[articulo]`.


- **Columnas adicionales**:
 Se agregarán al catálogo las siguientes columnas provenientes también de la tabla `[NewBytes_DBF].[dbo].[articulo]`:

- `ean`


- `upc`


- `gtin`
