---
jira_key: "NBWEB-817"
summary: "API - Feat - Generar listado xlsx MercadoLibre"
status: "Tareas por hacer"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-08-08 09:56"
updated: "2024-09-02 17:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-817"
---

# NBWEB-817: API - Feat - Generar listado xlsx MercadoLibre

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-08-08 09:56 |
| Actualizado | 2024-09-02 17:24 |
| Etiquetas | ninguna |
| Jira | [NBWEB-817](https://bluinc.atlassian.net/browse/NBWEB-817) |

## Descripción

Basándonos en la misma idea de cuando desarrollamos el listado CSV y XMLX [link](https://lioteam.atlassian.net/browse/NBWEB-657) [link](https://lioteam.atlassian.net/browse/NBWEB-655) generaremos un CSV especifico basado en el formato de tienda nube para importar productos (El ejemplo que te dan en el sitio esta adjuntado).

```
GET {{API_URL}}/v1/priceListXlsxMercadoLibre
```

Vamos a poner todos los mismos datos que tenemos en el CSV, pero vinculados (si el formato lo permite) a estas columnas.

Recorda que si tiene utilidad en la categoria, el precio es el que surge de ese calculo y sino, del precio normal para nuestra cliente.
