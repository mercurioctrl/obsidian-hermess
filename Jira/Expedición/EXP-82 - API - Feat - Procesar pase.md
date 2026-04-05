---
jira_key: "EXP-82"
aliases: ["EXP-82"]
summary: "API - Feat - Procesar pase "
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-17 13:30"
updated: "2022-12-14 10:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-82"
---

# EXP-82: API - Feat - Procesar pase 

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-17 13:30 |
| Actualizado | 2022-12-14 10:47 |
| Etiquetas | ninguna |
| Jira | [EXP-82](https://bluinc.atlassian.net/browse/EXP-82) |

## Relaciones

- **Padre:** [[EXP-18 - Feat - Listar pases|EXP-18]] Feat - Listar pases
- **is blocked by:** [[POS-97 - API - Feat - Procesar pase de mercadería (Deposito)|POS-97]] API - Feat - Procesar pase de mercadería (Deposito)
- **blocks:** [[EXP-83 - APP - Feat - Modal procesar pase de mercaderia|EXP-83]] APP - Feat - Modal procesar pase de mercaderia

## Descripcion

En este caso llevaremos adelante un recurso muy similar al que ya realizamos en [link](https://lioteam.atlassian.net/browse/POS-97)

```
ATCH {{API_URL}}/v1/passes
```

```
{
       "statusId":1,
        "passId":11,
        autorizaUser: {token},
        "items": [
        {
            "productId": 100,
            "productDescription": "Placa de video",
            "serial": "sn8907433987"
        },
        {
            "productId": 100,
            "productDescription": "Placa de video",
            "serial": "sn8907433988"
        }
        ]
}
```

El paso es el mismo, pero en lugar de nuestro formulario del correo (que vive en la aplicaciond e postventa), ahora estara integrado en un modal en la app de expedición

[adjunto]
Agregaremos a partir de ahora, un parámetro extra, que es el token que valida quien realizo en definitiva la operación, mas allá de quien es el usuario logueado. Ademas, el autorizante, debe tener un permiso especifico para autorizar ese tipo de accion en la tabla de permisos.

El parámetro para el token es solo para ver que tarjeta autorizo el movimiento.

Para esto podemos usar el hard token que esta en la tabla `nb_web.dbo.usuarios_nb`

Y a partir de ella crearemos un objeto `autorizaUser`

que contendrá

- id del ususario autorizante


- fecha y hora exacta de la autorización


- ip e informacion del browser



Esta informacion deberá quedar asociada a la cabecera del pase (crearemos nuevas columnas para este fin)
