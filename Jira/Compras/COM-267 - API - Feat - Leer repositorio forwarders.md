---
jira_key: "COM-267"
aliases: ["COM-267"]
summary: "API - Feat - Leer repositorio forwarders"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-08 09:33"
updated: "2026-01-21 10:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-267"
---

# COM-267: API - Feat - Leer repositorio forwarders

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-08 09:33 |
| Actualizado | 2026-01-21 10:51 |
| Etiquetas | ninguna |
| Jira | [COM-267](https://bluinc.atlassian.net/browse/COM-267) |

## Relaciones

- **Padre:** [[COM-265 - Forwarders|COM-265]] Forwarders
- **has action item:** [[COM-268 - APP - Feat - Agregar pestaña de alta y edicion de forwarders|COM-268]] APP - Feat - Agregar pestaña de alta y edicion de forwarders

## Descripcion

### 

```
GET /v1/forwarders?currentPage=1&itemsPerPage=15&companyCode={companyCode}&search={nombre/prefijo/id}
```

Devuelve el listado de forwarders disponibles para la empresa del usuario autenticado.

## Respuesta esperada

```
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "DHL Global Forwarding",
      "code": "DHLGF",
      "address": "Av. Example 123",
      "phone": "+54 11 4444-4444",
      "email": "ops@dhl.com",
      "companyCode": 4
    },
    {
      "id": 2,
      "name": "Kuehne + Nagel",
      "code": "KN",
      "address": "Av. Otra 456",
      "phone": "+54 11 5555-5555",
      "email": "arg@kuehne-nagel.com",
      "companyCode": 4
    }
  ]
}

```

---

## Errores

- **401**:  inválido / ausente


- **200 + data vacía**: no hay forwarders cargados (no es error)



---

## Criterios de aceptación

- Existe `GET /v1/forwarders`


- Permite filtros simples por `code` y `name`


- Devuelve array vacío si no hay resultados


- Respeta el mismo formato de respuesta que el resto de la API
