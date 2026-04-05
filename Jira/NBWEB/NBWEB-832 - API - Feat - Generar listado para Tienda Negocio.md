---
jira_key: "NBWEB-832"
aliases: ["NBWEB-832"]
summary: "API - Feat - Generar listado para Tienda Negocio"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-08-16 08:00"
updated: "2024-08-25 22:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-832"
---

# NBWEB-832: API - Feat - Generar listado para Tienda Negocio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-16 08:00 |
| Actualizado | 2024-08-25 22:29 |
| Etiquetas | ninguna |
| Jira | [NBWEB-832](https://bluinc.atlassian.net/browse/NBWEB-832) |

## Relaciones

- **Padre:** [[NBWEB-602 - Sitio Web|NBWEB-602]] Sitio Web
- **blocks:** [[NBWEB-833 - APP - Feat - Agregar a Mis Listas el lsitado de Tienda negocio|NBWEB-833]] APP - Feat - Agregar a Mis Listas el lsitado de Tienda negocio
- **is blocked by:** [[NBWEB-845 - API - Generar listado para Tienda Negocio - Mi producto y categoría no visible|NBWEB-845]] API - Generar listado para Tienda Negocio - Mi producto y categoría no visible 

## Descripcion

Basándonos en la misma idea de cuando desarrollamos el listado CSV y XMLX [link](https://lioteam.atlassian.net/browse/NBWEB-657) [link](https://lioteam.atlassian.net/browse/NBWEB-655) generaremos un CSV especifico basado en el formato de tienda nube para importar productos (El ejemplo que te dan en el sitio esta adjuntado).

```
GET {{API_URL}}/v1/priceListTNegocio
```

Vamos a poner todos los mismos datos que tenemos en el CSV, pero vinculados (si el formato lo permite) a estas columnas.
