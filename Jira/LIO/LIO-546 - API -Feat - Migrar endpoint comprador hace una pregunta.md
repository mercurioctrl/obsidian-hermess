---
jira_key: "LIO-546"
aliases: ["LIO-546"]
summary: "API -Feat - Migrar endpoint comprador hace una pregunta     "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-20 12:09"
updated: "2026-02-26 17:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-546"
---

# LIO-546: API -Feat - Migrar endpoint comprador hace una pregunta     

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-20 12:09 |
| Actualizado | 2026-02-26 17:05 |
| Etiquetas | ninguna |
| Jira | [LIO-546](https://bluinc.atlassian.net/browse/LIO-546) |

## Relaciones

- **Padre:** [[LIO-537]] Migración de repositorios previa deprecación de la api legacy

## Descripcion

Como usuario autenticado, quiero poder realizar una pregunta en la publicación de un producto para resolver mis dudas antes de realizar una compra.

```
POST /questions/product/{product_id}
```



`Payload:`

```json
{
    "producto_id": 688969,
    "pregunta": "Pregunta de prueba."
}
```



`Response:`

```json
{
    "id": 131173,
    "texto": "Pregunta de prueba 2",
    "fecha": "2026-02-20 15:55:43.747",
    "usuario": {
        "id": 274942,
        "nombre": "Emanuel Jesus",
        "avatar": 44,
        "bloqueado": false
    },
    "producto": {
        "id": 688969,
        "nombre": "DISCO SSD NETAC SA500 2.5 SATA3 240GB",
        "img": "eb086ab91688e6590b0ca9d3f11f62fd.jpeg"
    },
    "vendedor": {
        "id": 22,
        "usuarioId": 2,
        "nombre": "BsAsPC"
    },
    "respuesta": null
}
```





**Criterios de Aceptación (Business Rules)**
Para que la pregunta se cree exitosamente, el sistema debe validar lo siguiente:

- **Existencia**: El product_id debe ser válido y existir en la base de datos.


- **Visibilidad**: El producto no debe estar en estado "oculto".


- **Autoría**: El usuario que pregunta no puede ser el mismo dueño (vendedor) de la publicación.


- **Restricción de Bloqueo**: El usuario no debe haber sido bloqueado previamente por el vendedor para interactuar en esa publicación específica.


- **Autenticación**: Solo usuarios con un token JWT válido pueden acceder a este endpoint.





**Acciones Post-Creación (Asíncronas)**
Una vez creada la pregunta en la base de datos, se deben disparar las siguientes notificaciones al vendedor bajo un modelo fire-and-forget:

`Push Notification`**:** Al dispositivo del vendedor.

`Email`: Notificación formal con el contenido de la pregunta y link al producto.
