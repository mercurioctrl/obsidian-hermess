---
jira_key: "INV-243"
aliases: ["INV-243"]
summary: "API - Feat - Hacer regularización global para arreglar un defecto de stock (globalRegularization)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-12 17:01"
updated: "2025-12-05 04:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-243"
---

# INV-243: API - Feat - Hacer regularización global para arreglar un defecto de stock (globalRegularization)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-12 17:01 |
| Actualizado | 2025-12-05 04:55 |
| Etiquetas | ninguna |
| Jira | [INV-243](https://bluinc.atlassian.net/browse/INV-243) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios
- **has action item:** [[INV-245]] APP - Feat - Hacer regularización global para arreglar un defecto de stock (globalRegularization)

## Descripcion

Se incorporará un nuevo recurso que permitirá modificar el valor del campo `[NewBytes_DBF].[dbo].[stocks].regularizacion_global` para un ítem y depósito específicos.
Esta operación se utilizará para ajustar manualmente diferencias históricas de stock que hayan sido previamente detectadas y asimiladas.

### **Restricciones y permisos**

Solo podrán ejecutar esta operación los usuarios que posean el permiso:
`[NB_WEB].[dbo].[permisos_agente].stocksGlobalAlter`.
Cualquier solicitud sin este permiso deberá ser rechazada.

### **Nuevo endpoint**

```
PATCH {API_URL}/itemsStocks/globalAlter
```

### **Payload**

```
{
  "amount": 5,
  "warehouseStockId": 2,
  "itemId": 121215
}

```

- **amount**: nuevo valor que se asignará a `regularizacion_global`.


- **warehouseStockId**: depósito al que corresponde el registro de stock.


- **itemId**: identificador del ítem.



### **Respuesta**

```
{
  "success": true,
  "message": "Se realizó la regularización global",
  "itemId": 121215,
  "warehouseStockId": 2,
  "amount": 5
}

```

---

## **Criterios de Aceptación (4–5 ítems)**

- Solo usuarios con el permiso **stocksGlobalAlter** pueden ejecutar el endpoint; los demás reciben error de autorización.


- El endpoint debe actualizar correctamente el campo `regularizacion_global` en la tabla `[stocks]` para el ítem y depósito indicados.


- En caso de parámetros inválidos o inexistentes (item, depósito, etc.), debe devolverse un error claro y validado por backend.
