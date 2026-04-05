---
jira_key: "PED-1109"
aliases: ["PED-1109"]
summary: "API - Refactor - Al generar remito ajustar id de pago de ser necesario en los casos LO"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-09-23 17:07"
updated: "2025-09-25 11:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1109"
---

# PED-1109: API - Refactor - Al generar remito ajustar id de pago de ser necesario en los casos LO

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-09-23 17:07 |
| Actualizado | 2025-09-25 11:24 |
| Etiquetas | ninguna |
| Jira | [PED-1109](https://bluinc.atlassian.net/browse/PED-1109) |

## Relaciones

- **Padre:** [[PED-91]] APP - Feat - Generar pedido
- **action item from:** [[SNB-3295]] Error en el Medio de Pago

## Descripcion

Se detectó un caso en el que algunos pedidos de **LO** presentan el campo `ID_FORMADEPAGO` en la tabla `NewBytes_DBF.dbo.pedclit` con valor **NULL**.
Esto genera un problema en el proceso de liquidación, ya que los vendedores no pueden identificar cuál fue la forma de pago original seleccionada por el cliente.

Como no fue posible replicar el caso en gamma, se decidió implementar un ajuste al momento de **generar el remito**, dado que esta instancia ocurre antes de la liquidación.
El refactor consiste en que, si el campo **ID_FORMADEPAGO** está vacío o es null, el sistema tome el valor original desde la tabla **Lo.dbo.pedidoCabeceraPaquete** y lo asigne a `pedclit`, garantizando así la trazabilidad de la información.

Además, se contempla la referencia correspondiente en la tabla **NEW_BYTES.dbo.MS_FORMASPAGO_REMITOS_VENDEDORES**. para obtener el valor id de pago utilizado para `pedclit`.

```
Route::post('makeSale', [MakeSaleController::class, 'execute']);
```





Forma de probar esto:

Al crear un pedido desde LO. se le debe ejecutar el siguiente update

```
-- update NewBytes_DBF.dbo.pedclit
-- set  ID_FORMADEPAGO = null
-- where idLo = {id de cabecera LO}

```



Luego al generar el pedido con el endpoint POST `makeSale`.

el campo `ID_FORMADEPAGO` de `pedclit` deberia tener el valor original seleccionado por el cliente. que se puede saber de la siguiente manera:

```
SELECT (SELECT ID_FORMA FROM NEW_BYTES.dbo.MS_FORMASPAGO_REMITOS_VENDEDORES where medioPagoIdLo = medioPagoElegidoID)
FROM [LO].[dbo].[pedidosCabeceraPaquete]
where pedidoCabeceraID = {id de cabecera LO}
```
