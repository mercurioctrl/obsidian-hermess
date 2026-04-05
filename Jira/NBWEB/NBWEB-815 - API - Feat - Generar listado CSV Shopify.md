---
jira_key: "NBWEB-815"
aliases: ["NBWEB-815"]
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

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web
- **blocks:** [[NBWEB-816]] APP - Agregar a Mis Listados el listado de Shopify
- **is blocked by:** [[NBWEB-824]] API - Generar listado CSV Shopify - Datos no coincidentes
- **is blocked by:** [[NBWEB-822]] API - Errorres al subir el xlsx de empretienda a "empretienda" y csv de shopify  a "shopify"

## Descripcion

Basándonos en la misma idea de cuando desarrollamos el listado CSV y XMLX [link](https://lioteam.atlassian.net/browse/NBWEB-657) [link](https://lioteam.atlassian.net/browse/NBWEB-655) generaremos un CSV especifico basado en el formato de tienda nube para importar productos (El ejemplo que te dan en el sitio esta adjuntado).

```
GET {{API_URL}}/v1/priceListCsvShopify
```

Vamos a poner todos los mismos datos que tenemos en el CSV, pero vinculados (si el formato lo permite) a estas columnas.

Recorda que si tiene utilidad en la categoria, el precio es el que surge de ese calculo y sino, del precio normal para nuestra cliente.
