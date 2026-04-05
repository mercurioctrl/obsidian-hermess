---
jira_key: "NBWEB-718"
summary: "APP - Feat - Descargar listado para tienda nube"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-04-18 09:02"
updated: "2024-04-23 22:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-718"
---

# NBWEB-718: APP - Feat - Descargar listado para tienda nube

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-18 09:02 |
| Actualizado | 2024-04-23 22:53 |
| Etiquetas | ninguna |
| Jira | [NBWEB-718](https://bluinc.atlassian.net/browse/NBWEB-718) |

## Descripción

Basándonos en la misma idea de cuando desarrollamos el listado CSV y XMLX [https://lioteam.atlassian.net/browse/NBWEB-657](https://lioteam.atlassian.net/browse/NBWEB-657)  [https://lioteam.atlassian.net/browse/NBWEB-655](https://lioteam.atlassian.net/browse/NBWEB-655)  generaremos un CSV especifico basado en el formato de tienda nube para importar productos (

Agregaremos la opción a 

[attachment]
Usando el recurso [link](https://lioteam.atlassian.net/browse/NBWEB-717) 

```
GET {{API_URL}}/v1/priceListCsvTiendaNube
```

Vamos a poner todos los mismos datos que tenemos en el CSV, pero vinculados (si el formato lo permite) a estas columnas.

Recorda que si tiene utilidad en la categoria, el precio es el que surge de ese calculo y sino, del precio normal para nuestra cliente.
