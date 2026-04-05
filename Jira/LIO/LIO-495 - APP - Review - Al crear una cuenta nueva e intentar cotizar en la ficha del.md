---
jira_key: "LIO-495"
aliases: ["LIO-495"]
summary: "APP - Review - Al crear una cuenta nueva e intentar cotizar en la ficha del producto, si el usuario no posee codigo postal, debe usar el default"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-23 10:14"
updated: "2026-01-05 10:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-495"
---

# LIO-495: APP - Review - Al crear una cuenta nueva e intentar cotizar en la ficha del producto, si el usuario no posee codigo postal, debe usar el default

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-23 10:14 |
| Actualizado | 2026-01-05 10:28 |
| Etiquetas | ninguna |
| Jira | [LIO-495](https://bluinc.atlassian.net/browse/LIO-495) |

## Relaciones

- **Padre:** [[LIO-162 - Mejoras generales para envios|LIO-162]] Mejoras generales para envios

## Descripcion

Existe un caso típico, cuando recién creas una cuenta que muestra un error al cotizar, ya que el usuario aun no lo cargo.

[adjunto]
Sucede al ejecutar el recurso de la siguiente manera

```
curl 'https://omega-api.libreopcion.com.ar/envios/producto/cotizacion' \
  --data-raw '{"productoId":573936,"codigoPostalVendedor":"1229","codigoPostalCliente":""}'
```

osea con `"codigoPostalCliente":""`

Previendo esto, nosotros asignamos por default, para cuando no tengo el código postal, dentro del objeto `user` un `codigoPostalDefault` que es el que deberíamos usar en este caso

```
{
    "user": {
        "id": 316275,
 ....
        "codigoPostalDefault": 1407, <----
        "activeWallet": false
    }
}
```
