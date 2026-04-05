---
jira_key: "NBWEB-418"
aliases: ["NBWEB-418"]
summary: "API - Refactor - Alterar el metodo para generar un paquete para que el objeto se genere de manera interna"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-19 16:08"
updated: "2022-07-29 13:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-418"
---

# NBWEB-418: API - Refactor - Alterar el metodo para generar un paquete para que el objeto se genere de manera interna

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-19 16:08 |
| Actualizado | 2022-07-29 13:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-418](https://bluinc.atlassian.net/browse/NBWEB-418) |

## Relaciones

- **causes:** [[NBWEB-357 - API - Feat - Agregar un recurso para consumir el ms-envios para generar un|NBWEB-357]] API - Feat - Agregar un recurso para consumir el ms-envios para generar un nuevo paquete

## Descripcion

Para el recurso

```
POST {{API_URL}}/v1/miCuenta/ordenesDeCompra/0002/10217260/addTrackingOrder
```

Solo se deben enviar los datos branch y order en la URL.

La request que se genera como necesaria para el servicio de envíos, se debe generar de manera interna a modo tal de no tener que construirla par cada pedido, sino que sea suficiente con impactar contra '`/miCuenta/ordenesDeCompra/{branch}/{order}/addTrackingOrder`'.

Asi se habia pensado originalmente, pero se ve que como el ejemplo tenia la requiest interna, se presto a confusion.

Lo bueno es que ya estamos a mitad de camino!

Avisame si se entiende o necesitas que veamos en mas detalle
