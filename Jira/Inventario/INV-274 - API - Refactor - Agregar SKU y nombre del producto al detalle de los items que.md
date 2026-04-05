---
jira_key: "INV-274"
aliases: ["INV-274"]
summary: "API - Refactor - Agregar SKU y nombre del producto al detalle de los items que tiene vinculado el certificado"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-05 08:27"
updated: "2025-12-06 07:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-274"
---

# INV-274: API - Refactor - Agregar SKU y nombre del producto al detalle de los items que tiene vinculado el certificado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-05 08:27 |
| Actualizado | 2025-12-06 07:25 |
| Etiquetas | ninguna |
| Jira | [INV-274](https://bluinc.atlassian.net/browse/INV-274) |

## Relaciones

- **Padre:** [[INV-260]] Certificados eléctricos por Qr
- **has action item:** [[INV-267]] APP -Refactor - Agregar SKU y nombre del producto cuando veo el modal para adminstrar sus productos vinculados

## Descripcion

Agregaremos estos detalles que pidieron extra para mejorar la usabilidad de la herramienta 

```
GET {API_URL}/electricalCertificate/{id}/items
```

```
{
  "certificateId": 7,
  "items": [
    {
      "itemId": 104832,
      "sku": "sku-del-producto", <-- se agrega
      "description": "Nombre del producto", <-- se agrega
      "linked_at": "2025-12-01 12:10:55"
    },
    {
      "itemId": 120650,
      "sku": "sku-del-producto", <-- se agrega
      "description": "Nombre del producto", <-- se agrega
      "linked_at": "2025-12-01 12:11:20"
    }
  ]
}

```
