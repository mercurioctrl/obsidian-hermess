---
jira_key: "COM-207"
aliases: ["COM-207"]
summary: "API - MVP - Feat Agregar campo de costo sugerido para que aparezca en el listado (selector) de costos de Pedidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-10-01 16:43"
updated: "2025-12-05 03:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-207"
---

# COM-207: API - MVP - Feat Agregar campo de costo sugerido para que aparezca en el listado (selector) de costos de Pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-01 16:43 |
| Actualizado | 2025-12-05 03:33 |
| Etiquetas | ninguna |
| Jira | [COM-207](https://bluinc.atlassian.net/browse/COM-207) |

## Relaciones

- **Padre:** [[COM-77]] Editar orden de compra
- **has action item:** [[COM-208]] DEPRECADA - APP - MVP - Feat Agregar campo de costo sugerido para que aparezca en el listado (selector) de costos de Pedidos

## Descripcion

Refactorizar el recurso


```
GET /v1/providerOrder/{purchaseOrderId}
```


para incluir el campo `suggestedCost` (costo sugerido) por ítem, persistido en una nueva tabla dedicada, y permitir su actualización vía `PATCH`.

---

### Nueva tabla

Crear `[NewBytes_DBF].[dbo].[PedProlSuggested]` con:

- `nnumped` → número de pedido (link con `pedprot` / `orderNumber`)


- `cref` → referencia / SKU


- `ID_Articulo` → id del ítem


- `nPreDivSuggested` → costo sugerido (decimal)



PK lógica: `nnumped + ID_Articulo`.

---

### GET ProviderOrder

En 

```
GET /v1/providerOrder/{purchaseOrderId}
```

- Agregar `suggestedCost` dentro de cada `item`.


- El valor se obtiene desde `PedProlSuggested` por:

- `nnumped = orderNumber`


- `ID_Articulo = item.id` (y `cref` si aplica).




- Si no existe registro → devolver `suggestedCost: null` (sin error).



Ejemplo:

```
{
  "id": 108601,
  "sku": "23148",
  "suggestedCost": 120.00,
  ...
}

```

---

### PATCH ProviderOrder

**Endpoint:**

```
PATCH /v1/providerOrder/{purchaseOrderId}
```

**Payload:**

```
{
  "item": {
    "id": 108601,
    "suggestedCost": 120.00
  }
}

```

**Comportamiento:**

- Si *no existe* registro en `PedProlSuggested` → **INSERT**.


- Si *existe* → **UPDATE** de `nPreDivSuggested`.


- Si el PATCH no incluye `suggestedCost` → no se modifica la tabla.



---

### Criterios de aceptación

- La tabla existe y es consultable por pedido + ítem.


- El GET devuelve `suggestedCost` correctamente o `null` cuando no esté cargado.


- El PATCH crea o actualiza el valor y el GET refleja el cambio.


- No se rompe ningún comportamiento previo del endpoint.
