---
jira_key: "EXP-98"
aliases: ["EXP-98"]
summary: "API - Feat - Confirmar despacho de mercaderia"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-12-13 14:13"
updated: "2023-01-27 12:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-98"
---

# EXP-98: API - Feat - Confirmar despacho de mercaderia

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-13 14:13 |
| Actualizado | 2023-01-27 12:01 |
| Etiquetas | ninguna |
| Jira | [EXP-98](https://bluinc.atlassian.net/browse/EXP-98) |

## Relaciones

- **Padre:** [[EXP-15]] Feat - Serializar salida

## Descripcion

Se trata del recurso para despachar una orden una vez finalizada su serializacion 

```
PATCH {API_URL}/v1/orders/{pedido}/dispatch
```

Lo que hace es fijarse que todos los items de la orden devuelvan `true` de esta forma podemos decir que todo el pedido esta `true`
para ser despachado.

Luego de eso solo debemos verificar el `autorizaUser: {token} `que es obligatorio para ejecutar este recurso.

```
{
    autorizaUser: {token}
}

```

 El parámetro para el token es solo para ver que tarjeta autorizo el movimiento.

Para esto podemos usar el hard token que esta en la tabla `nb_web.dbo.usuarios_nb`

Y a partir de ella crearemos un objeto `autorizaUser`

que contendrá

- id del usuario autorizante


- fecha y hora exacta de la autorización


- ip e informacion del browser



Esta informacion deberá quedar asociada a la cabecera del pedido (crearemos nuevas columnas para este fin)

De confirmarse todos los seriales y el token correcto entonces esto cambiaría el estado a pedido según los estados descritos en `[NEW_BYTES].[dbo].[MS_STATUS_REMITO]` y alterando la columna `ID_STATUS` en `[NEW_BYTES].[dbo].[MS_VENTAS_REMITOS]`
