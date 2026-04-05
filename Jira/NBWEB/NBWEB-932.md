---
jira_key: "NBWEB-932"
summary: "EXTENSIÓN - Posibles conflictos con tareas programadas en WordPress"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-12-03 14:42"
updated: "2024-12-05 11:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-932"
---

# NBWEB-932: EXTENSIÓN - Posibles conflictos con tareas programadas en WordPress

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-12-03 14:42 |
| Actualizado | 2024-12-05 11:04 |
| Etiquetas | ninguna |
| Jira | [NBWEB-932](https://bluinc.atlassian.net/browse/NBWEB-932) |

## Descripción

Se recibió por medio del correo de integraciones un problema con tareas programadas fallidas en WordPress y posibles conflictos con el plugin NewBytes. 

Te comparto el reporte:

```
Hola, ¿cómo están?

Me comunico porque estoy teniendo problemas en mi tienda virtual en WordPress y estoy descartando opciones sobre cuál puede ser el problema que genera conflictos. Les describo brevemente lo que me pasa.

El error principal que tengo es la cantidad de tareas programadas pendientes o fallidas que tiene el sitio, que pueden llegar hasta más de 7000. Los ganchos principales que se acumulan (por encima de 3000 cuando genera errores) son:
 - woocommerce_deliver_webhook_async
 - gla/jobs/update_products/process_item
El primero entiendo que está relacionado con WooCommerce, pero el segundo no sé de qué puede ser y se me ocurrió que podía ser de ustedes porque parecería encargarse de actualizar productos en masa.

La falla que genera es que el sitio deja de poder ejecutar tareas, por ejemplo, no puedo desactivar plugins o temas, editar páginas o productos e incluso a veces deja de cargar bien los archivos CSS.

Mi teoría principal es que las actualizaciones periódicas del plugin llenan la base de datos hasta llenar su capacidad máxima, lo que genera la falla que mencioné.

De momento recuperé una copia de seguridad de la página a un momento anterior a la falla y desactivé el Conector NewBytes para comprobar si eso es lo que generaba el problema.

Anticipándome a que esa sea la razón, quería, primero, acercarles el problema por si tienen otros usuarios con el mismo conflicto y, segundo, consultarles los nombres de las tablas en la base de datos para poder hacer una limpieza manual (en el caso de que el plugin no lo haga por su cuenta) y poder retomar el uso del plugin. Cualquier otra ayuda o comentario podría servir.

Ante todo, muchas gracias.

Quedo atenta a la respuesta.

Saludos,
Diana 
```
