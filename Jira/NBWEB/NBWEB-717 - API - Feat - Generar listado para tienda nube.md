---
jira_key: "NBWEB-717"
aliases: ["NBWEB-717"]
summary: "API - Feat - Generar listado para tienda nube"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-18 08:55"
updated: "2025-08-20 14:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-717"
---

# NBWEB-717: API - Feat - Generar listado para tienda nube

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-18 08:55 |
| Actualizado | 2025-08-20 14:52 |
| Etiquetas | ninguna |
| Jira | [NBWEB-717](https://bluinc.atlassian.net/browse/NBWEB-717) |

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web
- **Subtarea:** [[NBWEB-949]] API - Refactor - Generar listado para tienda nube - Adición de imagén principal
- **blocks:** [[NBWEB-718]] APP - Feat - Descargar listado para tienda nube
- **relates to:** [[NBWEB-723]] API - Generar listado para tienda nube - Cambio en nombre de columna SKU
- **relates to:** [[NBWEB-885]] API - Refactor - Generar listado para Tiendanube - Agregar medidas del artículo 
- **has action item:** [[NBWEB-949]] API - Refactor - Generar listado para tienda nube - Adición de imagén principal
- **relates to:** [[SNB-3308]] Integraciones - Generar listado para tienda nube - Error al intentar descargar
- **relates to:** [[SNB-3340]] Integraciones - Generar listado para tienda nube -> Articulos repetidos

## Descripcion

Basándonos en la misma idea de cuando desarrollamos el listado CSV y XMLX [link](https://lioteam.atlassian.net/browse/NBWEB-657)  [link](https://lioteam.atlassian.net/browse/NBWEB-655)  generaremos un CSV especifico basado en el formato de tienda nube para importar productos (El ejemplo que te dan en el sitio esta adjuntado).

```
GET {{API_URL}}/v1/priceListCsvTiendaNube
```

Vamos a poner todos los mismos datos que tenemos en el CSV, pero vinculados (si el formato lo permite) a estas columnas.

Recorda que si tiene utilidad en la categoria, el precio es el que surge de ese calculo y sino, del precio normal para nuestra cliente.
