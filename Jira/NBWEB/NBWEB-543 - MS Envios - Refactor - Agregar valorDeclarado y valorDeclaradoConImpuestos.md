---
jira_key: "NBWEB-543"
aliases: ["NBWEB-543"]
summary: "MS Envios - Refactor - Agregar \"valorDeclarado\" y \"valorDeclaradoConImpuestos"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-05-10 08:54"
updated: "2023-05-15 14:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-543"
---

# NBWEB-543: MS Envios - Refactor - Agregar "valorDeclarado" y "valorDeclaradoConImpuestos

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-10 08:54 |
| Actualizado | 2023-05-15 14:15 |
| Etiquetas | ninguna |
| Jira | [NBWEB-543](https://bluinc.atlassian.net/browse/NBWEB-543) |

## Relaciones

- **Padre:** [[NBWEB-507 - Refactor cotizacion de envios en el sitio|NBWEB-507]] Refactor cotizacion de envios en el sitio

## Descripcion

Agregaremos al recurso [link](https://lioteam.atlassian.net/browse/NBWEB-528) los dos nuevos parametros que llamaremos

- declaredValue


- valueDeclaredWithTax



De esta forma 

```
{{API_URL}}/addTrackingOrder/nbDistributor
```

```
{
    "branch": "0002",
    "order": "10289017",
    "packageGroup": 1,
    "declaredValue": 100,
    "declaredValuethWhithTax": 121
}
```

De no encontrarse los parametros en el payload, entonces tomara un valor por defecto que se encuentra en el fichero .env



**15/05/2023 : Tarea Modificada **debido a los criterios de implementacion de Andreani.

```
{
    "branch": "0002",
    "order": "10289017",
    "packageGroup": 1,
    "assignValue": true
}
```



De ser enviado el atributo `"assignValue"` en `true` se aplica un importe definido de forma interna a cada bulto. siempre y cuando el `packageGroup` coincida con el cotizado interno. en cantidades de bultos.

de no enviarse, o enviarse en `false` se aplica la logica de tomar el importe total de la orden y dividirla por la cantidad de bultos generadas al despachar.





```
GET /order/nb/{branch}-{order}/cp/7600?assignValue=true
```

```
GET /cart/nb/{cartId}/cp/7600?assignValue=true
```



Tanto para el recurso ***cotizar por carrito*** como ***cotizar por Orden***,  se le es posible pasar **assignValue** de ser** true **aplica de forma interna un importe para cada bulto calculado por el precio de cada items, de no enviarse o ser **false, **aplica el valor definido en el .**ENV.  **`DEFAULT_VALUE_PACKAGE=4000` que hace referencia a $4000 pesos, esto es aplicado a cada bulto.
