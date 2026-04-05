---
jira_key: "LIO-294"
aliases: ["LIO-294"]
summary: "API - Feat - Recurso para permitir a usuarios sin login consultar el estado de su envío desde el Centro de Ayuda

"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-03-21 07:45"
updated: "2025-03-28 01:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-294"
---

# LIO-294: API - Feat - Recurso para permitir a usuarios sin login consultar el estado de su envío desde el Centro de Ayuda



| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-21 07:45 |
| Actualizado | 2025-03-28 01:58 |
| Etiquetas | ninguna |
| Jira | [LIO-294](https://bluinc.atlassian.net/browse/LIO-294) |

## Relaciones

- **Padre:** [[LIO-17 - Mejorar seguimientos de guia y agregar un seguimiento activo|LIO-17]] Mejorar seguimientos de guia y agregar un seguimiento activo
- **action item from:** [[LIO-93 - API - Refactor - Migrar recurso de seguimiento|LIO-93]] API - Refactor - Migrar recurso de seguimiento 
- **has action item:** [[LIO-295 - APP - Feat - Rastreo de envios|LIO-295]] APP - Feat - Rastreo de envios

## Descripcion

Vamos a crear un nuevo recurso público en el Centro de Ayuda que permita a los usuarios sin login consultar el estado de su envío, ingresando uno de los siguientes datos:

- Número de pedido de LO


- Número de tracking


- Número de pedido de NB



Para esto vamos a apoyarnos en un endpoint existente de la API v4 ([link](https://lioteam.atlassian.net/browse/LIO-93) )

Pero generaremos uno nuevo

```
GET {API_V4}/v4/findShipments
```

Este recurso ya devuelve el historial de estados de un envío, pero actualmente requiere login o más información de la que generalmente tiene el comprador.
Vamos a hacer los ajustes necesarios para permitir su uso sin autenticación, validando solo con uno de los identificadores mencionados.

**Ejemplo de respuesta actual del endpoint:**

```
[
    {
        "state": "Entregado Cobrado",
        "brach": "New Bytes - CABA, CABA",
        "address": "Jujuy 1039, CABA, CABA",
        "date": "2024-08-12 12:00"
    },
    {
        "state": "El envío fue entregado",
        "brach": "Andreani SAN LORENZO (AV SAN MARTIN)",
        "address": "",
        "date": "15-08-2024 15:07"
    }
]

```

Este es el objeto basico, pero seguro se pueden agregar datos como el dia de llegada estimado por el currier y otros, asi que si queres comentame que se te ocurre para agregarle, que sea util.

**Criterios de aceptación:**

- Se debe poder buscar y que acepte número de pedido (NB o LO) o número de tracking en el mismo filtro o parámetro de búsqueda


- La sección debe estar disponible públicamente, sin requerir login.


- El recurso debe manejar casos de error (ej: pedido no encontrado, tracking inválido) con mensajes claros para el usuario.



Actualización:

Al ejecutar este recurso:

API /v4/findShipping?**search=360002203354090**

retornara la siguiente información:

```
{
   "orderInfo": {
      "orderNb": 10355855,
      "orderLo": null,
      "remito": "X000200583858",
      "tracking": "360002203354090",
      "shippingId": 4065,
      "deliveryTimeRange": null
   },
   "trackingInfo": [
      [
         {
            "state": "Armado Finalizado",
            "brach": "C. Distribución - CABA",
            "address": "Jujuy 1039, CABA, CABA",
            "date": "2024-06-24 12:00"
         },
         {
            "state": "Aún no recibimos tu envío. Suscribite al servicio de notificaciones y te enviaremos las novedades por e-mail",
            "brach": "Andreani  ",
            "address": "",
            "date": "24-06-2024 15:36"
         }....
      ]
   ]
}
```
