---
jira_key: "NBWEB-582"
aliases: ["NBWEB-582"]
summary: "API - CMS - Feat - Pausar ventas y definir un mensaje para mostrar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-09-15 08:40"
updated: "2024-04-16 12:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-582"
---

# NBWEB-582: API - CMS - Feat - Pausar ventas y definir un mensaje para mostrar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-15 08:40 |
| Actualizado | 2024-04-16 12:20 |
| Etiquetas | ninguna |
| Jira | [NBWEB-582](https://bluinc.atlassian.net/browse/NBWEB-582) |

## Relaciones

- **Padre:** [[NBWEB-581]] CMS - Carrito web
- **is blocked by:** [[NBWEB-580]] API - Feat - Carrito -> Cerrar ventas y mostrar un mensaje según se indico en el cms
- **blocks:** [[NBWEB-580]] API - Feat - Carrito -> Cerrar ventas y mostrar un mensaje según se indico en el cms

## Descripcion

Crearemos una sección nueva en el cms (con lo que eso implica en permisos y demas) llamada 

```
POST {CMS_URL}/cart
```

Donde definiremos un formulario que tenga un “conmutador” o “checbox” para pausar o reanudar la venta.

Adicionalmente se nos permite definir un mensaje para mostrar de máximo 250 caracteres, para cuando alguien intenta procesar un carrito y las ventas estan cerradas.

Agregaremos dos columnas a la tabla

`[NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS]`

- closeCart (si esta en true, cierra el carrito)


- closeCartMsg (Es donde guardaremos el string que querremos que muestre en el mesaje)
