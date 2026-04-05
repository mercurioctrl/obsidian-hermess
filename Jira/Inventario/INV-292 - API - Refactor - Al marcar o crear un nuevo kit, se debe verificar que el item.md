---
jira_key: "INV-292"
aliases: ["INV-292"]
summary: "API - Refactor - Al marcar o crear un nuevo kit, se debe verificar que el item sea \"nuevo\" (no tenga aun costo promedio), ni tenga ventas (albclil)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-19 08:18"
updated: "2025-12-29 12:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-292"
---

# INV-292: API - Refactor - Al marcar o crear un nuevo kit, se debe verificar que el item sea "nuevo" (no tenga aun costo promedio), ni tenga ventas (albclil)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-19 08:18 |
| Actualizado | 2025-12-29 12:09 |
| Etiquetas | ninguna |
| Jira | [INV-292](https://bluinc.atlassian.net/browse/INV-292) |

## Relaciones

- **Padre:** [[INV-253]] Crear y modificar Kits
- **action item from:** [[INV-254]] API - Feat - Cear un nuevo kit
- **is cloned by:** [[INV-307]] API - Review - Al marcar o crear un nuevo kit, se debe verificar que el item sea "nuevo" (no tenga aun costo promedio), ni tenga ventas (albclil) - QA observaciones

## Descripcion

**API – Refactor – Validación para creación/marcado de kits**

Al crear o marcar un ítem como **kit**, el sistema debe validar previamente que el artículo sea **nuevo**.

Condiciones obligatorias:

- El artículo **no debe tener costo promedio calculado** (`NewBytes_DBF.dbo.articulo.ncosteprom IS NULL`).


- El artículo **no debe registrar ventas** (no debe existir en `NewBytes_DBF.dbo.albclil`).



El recurso a refactorizar es:

```
POST {API_URL}/itemsKits
```

**Respuesta esperada**

- Si cumple las condiciones:



```
{
  "success": true,
  "message": "El artículo fue marcado como kit",
  "itemId": 125120
}
```

- Si no cumple, se debe devolver un error indicando **la causa específica**:

- Tiene ventas asociadas.


- Ya posee costo promedio calculado.





### Caso 1 — No se puede crear el kit porque **ya tiene ventas**

**HTTP 409 Conflict**
(estado del recurso incompatible con la operación solicitada)

```
{
  "success": false,
  "message": "El artículo no puede marcarse como kit porque ya registra ventas.",
  "itemId": 125120
}

```

---

### Caso 2 — No se puede crear el kit porque **ya tiene costo promedio calculado**

**HTTP 409 Conflict**

```
{
  "success": false,
  "message": "El artículo no puede marcarse como kit porque ya tiene costo promedio calculado.",
  "itemId": 125120
}
```
