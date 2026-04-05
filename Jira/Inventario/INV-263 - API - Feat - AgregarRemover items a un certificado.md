---
jira_key: "INV-263"
aliases: ["INV-263"]
summary: "API - Feat - Agregar/Remover items a un certificado"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-01 08:02"
updated: "2025-12-02 08:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-263"
---

# INV-263: API - Feat - Agregar/Remover items a un certificado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-01 08:02 |
| Actualizado | 2025-12-02 08:17 |
| Etiquetas | ninguna |
| Jira | [INV-263](https://bluinc.atlassian.net/browse/INV-263) |

## Relaciones

- **Padre:** [[INV-260]] Certificados eléctricos por Qr
- **has action item:** [[INV-264]] APP - Feat - Agregar/Remover items a un certificado

## Descripcion

Se deberá permitir **asociar y desasociar ítems de producto** a un certificado eléctrico, para saber qué productos quedan respaldados por cada certificado.

### 1) Nueva tabla de relación en SQL Server

Crear una tabla de vínculo entre certificados e ítems:

**Tabla:** `ElectricalCertificateItems` (nombre de ejemplo, ajustable a tu convención)

Campos mínimos:

- `id` → INT IDENTITY, **PK**


- `electrical_certificate_id` → INT, **FK** a `ElectricalCertificates.id`


- `itemId` → INT, **NOT NULL** (ID del producto/ítem en el sistema)


- `created_at` → DATETIME **NOT NULL**



Reglas:

- No permitir duplicados de par (`electrical_certificate_id`, `itemId`).



---

### 2) Endpoint – Agregar ítems a un certificado

**POST** `{API_URL}/electricalCertificate/{id}/items`

Asocia uno o varios ítems al certificado indicado.

#### Request

```
{
  "items": [104832, 120650, 119212]
}

```

- `items` → array de `itemId` (obligatorio, al menos 1).



Comportamiento:

- Ignorar silenciosamente los ítems ya asociados (idempotente), o devolverlos como `skipped` según preferencia.


- Insertar las nuevas relaciones en `ElectricalCertificateItems`.



#### Response ejemplo

```
{
  "certificateId": 7,
  "addedItems": [104832, 120650],
  "skippedItems": [119212]
}

```

---

### 3) Endpoint – Remover ítems de un certificado

**DELETE** `{API_URL}/electricalCertificate/{id}/items`

Desasocia uno o varios ítems del certificado.

#### Request

```
{
  "items": [104832, 119212]
}

```

#### Response ejemplo

```
{
  "certificateId": 7,
  "removedItems": [104832],
  "notFoundItems": [119212]
}

```

---

### 4) Criterios de aceptación

- ✅ Existe la tabla de relación `ElectricalCertificateItems` en SQL Server con FK al certificado.


- ✅ `POST /electricalCertificate/{id}/items`:

- Valida que el certificado exista.


- Valida que se reciba al menos un `itemId`.


- Crea las relaciones nuevas sin duplicar las existentes.




- ✅ `DELETE /electricalCertificate/{id}/items`:

- Elimina únicamente las relaciones existentes entre el certificado y los ítems enviados.




- ✅ Ambas operaciones devuelven un JSON indicando qué ítems se agregaron / removieron y cuáles fueron ignorados o no encontrados.
