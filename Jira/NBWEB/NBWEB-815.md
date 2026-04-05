---
jira_key: "NBWEB-815"
summary: "API - Feat - Generar listado CSV Shopify"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-08-07 16:12"
updated: "2024-08-27 04:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-815"
---

# NBWEB-815: API - Feat - Generar listado CSV Shopify

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-08-07 16:12 |
| Actualizado | 2024-08-27 04:18 |
| Etiquetas | ninguna |
| Jira | [NBWEB-815](https://bluinc.atlassian.net/browse/NBWEB-815) |

## Descripción

Basándonos en la misma idea de cuando desarrollamos el listado CSV y XMLX [link](https://lioteam.atlassian.net/browse/NBWEB-657) [link](https://lioteam.atlassian.net/browse/NBWEB-655) generaremos un CSV especifico basado en el formato de tienda nube para importar productos (El ejemplo que te dan en el sitio esta adjuntado).

```
GET {{API_URL}}/v1/priceListCsvShopify
```

Vamos a poner todos los mismos datos que tenemos en el CSV, pero vinculados (si el formato lo permite) a estas columnas.

Recorda que si tiene utilidad en la categoria, el precio es el que surge de ese calculo y sino, del precio normal para nuestra cliente.
