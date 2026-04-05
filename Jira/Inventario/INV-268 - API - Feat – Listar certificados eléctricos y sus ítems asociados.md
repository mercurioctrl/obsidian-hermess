---
jira_key: "INV-268"
aliases: ["INV-268"]
summary: "API - Feat – Listar certificados eléctricos y sus ítems asociados"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-01 08:55"
updated: "2025-12-02 03:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-268"
---

# INV-268: API - Feat – Listar certificados eléctricos y sus ítems asociados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-01 08:55 |
| Actualizado | 2025-12-02 03:27 |
| Etiquetas | ninguna |
| Jira | [INV-268](https://bluinc.atlassian.net/browse/INV-268) |

## Relaciones

- **Padre:** [[INV-260 - Certificados eléctricos por Qr|INV-260]] Certificados eléctricos por Qr
- **has action item:** [[INV-269 - APP - Feat - Nueva pestaña de “Certificados eléctricos” en Inventario|INV-269]] APP - Feat - Nueva pestaña de “Certificados eléctricos” en Inventario

## Descripcion

Se deberán exponer recursos de sólo lectura para:

- **Listar los certificados eléctricos creados.**


- **Listar los ítems asociados a un certificado en particular.**



---

### 1) Recurso: Listar certificados eléctricos

**Endpoint**

```
GET {API_URL}/electricalCertificate
```

Función:
Obtener el listado de certificados eléctricos registrados en la tabla `ElectricalCertificates`.

#### Comportamiento

- Devuelve una lista paginada de certificados.


- Permitir parámetros opcionales:

- `page` (por defecto 1)


- `limit` (por defecto 20)





#### Response ejemplo

```
{
  "data": [
    {
      "id": 7,
      "name": "Certificado Seguridad Baja Tensión",
      "pdf_path": null,
      "created_at": "2025-12-01 10:34:12"
    },
    {
      "id": 8,
      "name": "Certificado General Gabinetes IP54",
      "pdf_path": "http://static.nb.com.ar/img/7290717fe486d2c661ecef2d6fc8056a.pdf",
      "created_at": "2025-12-02 09:11:05"
    }
  ],
  "pagination": {
    "total": 2,
    "page": 1,
    "limit": 20
  }
}

```

#### Criterios de aceptación

- ✅ Devuelve sólo certificados existentes en `ElectricalCertificates`.


- ✅ Soporta `page` y `limit`.


- ✅ No expone datos sensibles ni internos fuera de lo necesario (`id`, `name`, `pdf_path`, timestamps).



---

### 2) Recurso: Listar ítems asociados a un certificado

**Endpoint**

```
GET {API_URL}/electricalCertificate/{id}/items
```

Función:
Obtener todos los ítems vinculados a un certificado eléctrico, usando la tabla de relación `ElectricalCertificateItems`.

#### Comportamiento

- Valida que el certificado `{id}` exista.


- Devuelve un array con los `itemId` asociados.
(Si querés enriquecer más adelante con info del ítem, se puede joinear con la tabla de productos.)



#### Response ejemplo (base)

```
{
  "certificateId": 7,
  "items": [
    {
      "itemId": 104832,
      "linked_at": "2025-12-01 12:10:55"
    },
    {
      "itemId": 120650,
      "linked_at": "2025-12-01 12:11:20"
    }
  ]
}

```

> `linked_at` corresponde a `created_at` de la tabla `ElectricalCertificateItems`.


Si el certificado no existe:

```
{
  "error": "Certificate not found"
}

```

(con `404 Not Found`).

#### Criterios de aceptación

- ✅ El endpoint devuelve `404` si el certificado `{id}` no existe.


- ✅ Si el certificado existe pero no tiene ítems, devuelve `items: []` sin error.


- ✅ La información se obtiene de la tabla `ElectricalCertificateItems` filtrando por `electrical_certificate_id`.


- ✅ El formato de respuesta es consistente con el resto de la API (naming, estructura, códigos HTTP).
