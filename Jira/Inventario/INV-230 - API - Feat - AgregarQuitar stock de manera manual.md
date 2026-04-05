---
jira_key: "INV-230"
aliases: ["INV-230"]
summary: "API - Feat - Agregar/Quitar stock de manera manual"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-07 14:28"
updated: "2025-12-05 04:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-230"
---

# INV-230: API - Feat - Agregar/Quitar stock de manera manual

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-07 14:28 |
| Actualizado | 2025-12-05 04:38 |
| Etiquetas | ninguna |
| Jira | [INV-230](https://bluinc.atlassian.net/browse/INV-230) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios

## Descripcion

Se agregará un recurso que permita modificar manualmente el valor del campo **[NewBytes_DBF].[dbo].[stocks].nstock_d1**.
Este endpoint no debe utilizarse para movimientos de stock operativos (ingresos, egresos, transferencias, etc.), sino exclusivamente para **ajustes manuales directos** sobre el valor existente.

El parámetro `amount` representa el **nuevo valor absoluto** que debe tener la columna `nstock_d1`.
Por ejemplo, si actualmente `nstock_d1 = 5` y se desea incrementar en 2 unidades, se deberá enviar `amount = 7`.

Solo los usuarios con el permiso **[NB_WEB].[dbo].[permisos_agente].alterStock = 1** podrán realizar esta operación.
El parámetro `reason` será obligatorio en todos los casos y servirá para dejar constancia del motivo del ajuste.

Como en todas las operaciones que impactan el stock, el cambio deberá registrarse en la tabla **[NB_WEB].[dbo].[registro_stock]**, con el tipo de registro correspondiente a una regularización.  

```
PATCH {API_URL}/itemsStocks/aleter
```

```
{
  "itemId":323,
  "warehouseStockId": 3,              // ID del registro de stock en depósito (si corresponde a tu modelo)                 // columna destino (enum)
  "amount": 5,                          // unidades a mover
  "reason": "Se agregan porque vinieron 5 de mas"     // opcional: motivo/auditoría
}
```

### **Consideraciones adicionales**

- Validar que el `itemId` y el `warehouseStockId` existan antes de aplicar el cambio.


- Registrar el movimiento en `[NB_WEB].[dbo].[registro_stock]` con `fichero = 'regularizacion'`.


- No debe permitirse ejecutar esta operación sin el permiso correspondiente o sin `reason`.



**Ejemplo de consulta para revisar regularizaciones previas:**

```
SELECT *
FROM [NB_WEB].[dbo].[registro_stock]
WHERE fichero = 'regularizacion';
```
