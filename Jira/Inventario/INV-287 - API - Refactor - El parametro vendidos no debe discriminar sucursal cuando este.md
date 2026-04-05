---
jira_key: "INV-287"
aliases: ["INV-287"]
summary: "API - Refactor - El parametro vendidos no debe discriminar sucursal cuando este no esta definido en el recurso"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-17 10:15"
updated: "2025-12-22 20:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-287"
---

# INV-287: API - Refactor - El parametro vendidos no debe discriminar sucursal cuando este no esta definido en el recurso

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-17 10:15 |
| Actualizado | 2025-12-22 20:53 |
| Etiquetas | ninguna |
| Jira | [INV-287](https://bluinc.atlassian.net/browse/INV-287) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios

## Descripcion

### **Recurso afectado**

```
GET {API_URL}/itemsStocks?stock=1&companyCode=4&categoryId={categoryId}&brandId={brandId}&search={title|sku|id}
```

---

```
SELECT 
    SUM(albclil.ncanent) AS RESERVAS
FROM NewBytes_DBF.dbo.albclil
LEFT OUTER JOIN NewBytes_DBF.dbo.albclit 
    ON albclil.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC
WHERE albclil.ID_Articulo = @itemId
  AND albclil.ID_ALMACEN = @warehouseId <--- solo si viene definido warehouseId, sino no se incluye en el query
  AND albclit.ntipoalb > 1

```
