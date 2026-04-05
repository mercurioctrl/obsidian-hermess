---
jira_key: "NBWEB-44"
aliases: ["NBWEB-44"]
summary: "API - Procesar carrito de compras (enviar pedido)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-21 09:37"
updated: "2022-04-29 11:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-44"
---

# NBWEB-44: API - Procesar carrito de compras (enviar pedido)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-21 09:37 |
| Actualizado | 2022-04-29 11:07 |
| Etiquetas | ninguna |
| Jira | [NBWEB-44](https://bluinc.atlassian.net/browse/NBWEB-44) |

## Relaciones

- **Padre:** [[NBWEB-1]] API - Carrito de compras
- **relates to:** [[NBWEB-139]] Agregar comentario al procesar el carrito

## Descripcion

```
{{API_URL}}/v1/carrito/procesar
```

Se trata del proceso mediante el cual, un carrito se transforma en una orden de compra.

Para esto se debe crear una cabecera en la tabla `[NewBytes_DBF].[dbo].[pedclit]` Donde ademas de ID de la tabla, existen dos campos que son claves para definir la numeración: cnumped y cnumsuc.

#### ¿como funcionan las columnas cnumsuc y cnumped?

`cnumsuc, es la sucursal. '0002' es la sucursal normal y '0010' es la sucursal para aquellos productos que estan marcados como tpye =1 o 'super oferta'.`

`cnumped debe incrementar segun su sucursal (cnumsuc) ya que ambos conforman un numero de orden en su conjunto`

Todo esto quiere decir que debo agrupar los productos por su “type”.

En caso de tener todos productos type = 0, creo un solo pedido con cabecera cnumsuc = '0002'

En caso de tener todos productos type = 1, creo un solo pedido con cabecera cnumsuc = '0010'

En caso de tener productos type = 1 y type = 0 en el mismo carrito, debo crear dos pedidos, osea dos cabeceras una con cnumsuc = ‘0002' y otra cnumsuc = '0010’

---

#### Creando la cabecera

Se debe crear la cabecera en `NewBytes_DBF.dbo.pedclit` incrementando en una unidad el campo `cnumped` según `cnumsuc`, y completando con ceros a la izquierda hasta alcanzar 8 caracteres. No tiene auto incremento, debe ser incrementado.

Ejemplo:

```
Si tenemos el par cnumsuc - cnumped 

0002 - 00023535 y 0010 - 00004953

El próximo pedido para cada caso sera 

0002 - 00023536 y 0010 - 00004954
```

Las columnas que que deben participar son 

```
cnumped -> Es el numero de pedido (string 8 caracteres, completa con cero)
cnumsuc -> Es el numero de sucursal segun type (string 4 caracteres, completa con cero)
ccodcli -> Es el numero de cliente (string 6 caracteres, completa con cero),
dfecped -> Fecha/Hora creacion (datetime,getdate()),
ccodalm -> Siempre es 'SAF',
cestado -> Inicializa en 'P' para indicar que esta pendiente,
cobserv -> Inicializa en 'PEDIDO DE INTERNET',
ccodage -> ccodage de la tabla clientes ([NewBytes_DBF].[dbo].[clientes], la clave es entre [NewBytes_DBF].[dbo].[clientes].ccodcli y [NB_WEB].[dbo].[usuarios_nb].codigoFP) ,
ID_VENDEDOR -> ID_VENDEDOR de la tabla clientes ([NewBytes_DBF].[dbo].[clientes], la clave es entre [NewBytes_DBF].[dbo].[clientes].ccodcli y [NB_WEB].[dbo].[usuarios_nb].codigoFP) ,
ID_ALMACEN -> Inicializa en 2,
ID_CLIENTE  -> ID_CLIENTE de la tabla clientes ([NewBytes_DBF].[dbo].[clientes], la clave es entre [NewBytes_DBF].[dbo].[clientes].ccodcli y [NB_WEB].[dbo].[usuarios_nb].codigoFP) ,
ID_Sucursal ->Inicializa en 2,
```

#### Creando el detalle

Se debe crear el detalle en la tabla `NewBytes_DBF.dbo.pedclil` con las siguientes columnas



```
cnumsuc (es clave con pedclit), 
cnumped (es clave con pedclit), , 
ncanped -> Es la cantidad de unidades seleccionada del producto, 
npreunit -> es el precio para ese cliente, calculado con el metodo de precios, 
cref -> el cref del producto en la talbra [NewBytes_DBF].[dbo].[articulos]
id_articulo -> el id del producto en la talbra [NewBytes_DBF].[dbo].[articulos]
ndto -> si el precio para el cliente ya fue calculaado va en cero, 
niva ->es el iva del producto
```



- Cualquier duda de todo esto, podemos velor por slack o meet
