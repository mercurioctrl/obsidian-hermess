---
jira_key: "PED-1335"
aliases: ["PED-1335"]
summary: "API - Feat - Billing Kit Report"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-03-18 08:05"
updated: "2026-03-30 10:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1335"
---

# PED-1335: API - Feat - Billing Kit Report

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-18 08:05 |
| Actualizado | 2026-03-30 10:34 |
| Etiquetas | ninguna |
| Jira | [PED-1335](https://bluinc.atlassian.net/browse/PED-1335) |

## Relaciones

- **Padre:** [[PED-213]] Reportes de ventas
- **has action item:** [[PED-1336]] APP - Feat - Descargar Billing Kit Report
- **action item from:** [[SNB-3781]] NB: Reportes KIT

## Descripcion

Se debe genera un reporte de facturación que identifique qué productos salieron como parte de un kit, para que las marcas que asignan fondos por bundle puedan validar que la designación se respetó correctamente.

---

## Contexto del negocio

Un **kit** es un agrupamiento visual de dos o más componentes que se presentan como un bundle en la orden y en la factura, pero que a lo largo de todo el proceso interno se manejan como unidades separadas. El sistema actualmente no tiene un campo explícito de "kit" en los datos de facturación — la única señal disponible es que **múltiples líneas de producto distintas comparten el mismo número de FACTURA**.

El reporte debe:

- Detectar automáticamente cuándo un producto salió como parte de un kit (misma factura, múltiples SKUs distintos)


- **Devolver únicamente las líneas que forman parte de un kit** — los productos vendidos individualmente (factura de una sola línea) no se incluyen en el resultado


- Mostrar cada componente del kit de forma individual (sin duplicar unidades)


- Indicar en cada línea con qué otros SKUs fue agrupado y el nombre completo del kit



---

## Endpoint nuevo

```
GET /v1/reports/billingKitReport?clientId={}&categoryId={}&branch={}&date={}&search={}&brandId={}&format={}
```

Este es un endpoint **nuevo** (no extiende uno existente). Devuelve el listado de líneas de facturación enriquecido con información de detección de kits, en formato JSON o XLSX según el parámetro `format`.

### Query params

| Parámetro | Tipo | Requerido | Descripción |
| --- | --- | --- | --- |
| `clientId` | string | No | Filtra por ID de cliente (columna CLIENTE_ID) |
| `categoryId` | string | No | Filtra por categoría (columna CATEGORIA) |
| `branch` | string | No | Filtra por sucursal (columna SUCURSAL) |
| `date` | string | No | Filtra por fecha de factura (FECHA_FACTURA) |
| `search` | string | No | Búsqueda libre sobre TITULO o SKU |
| `brandId` | string | No | Filtra por marca (columna MARCA) |
| `format` | string | No | `json` (default) devuelve array JSON. `xlsx` devuelve archivo descargable |

---

## 

## Response esperada

### format=json (default)

```
[
  {
    "FECHA_FACTURA": "12-02-2026 15:44",
    "TITULO": "MOTHER ASUS (AM4) PRIME A520M-K CSM",
    "CANTIDAD": 2,
    "PRECIO": "50,53",
    "FACTURA": "A000400170796",
    "TOTAL_FACTURA": 100,
    "SKU": "PRIME A520M-K/CSM",
    "is_kit": true,
    "kit_invoice": "A000400170796",
    "kit_siblings": ["VA24EHF-J", "VG249QL3A-J"],
    "kit_name": "MOTHER ASUS (AM4) PRIME A520M-K CSM + MONITOR 24 ASUS VA24EHF FHD IPS 100Hz 1ms + MONITOR 24 ASUS VG249QL3A GAMING FHD IPS 180Hz 1ms Pie profesional Altura Ajustable"
  },
  {
    "FECHA_FACTURA": "12-02-2026 15:44",
    "TITULO": "MONITOR 24 ASUS VA24EHF FHD IPS 100Hz 1ms",
    "CANTIDAD": 1,
    "PRECIO": "76,77",
    "FACTURA": "A000400170796",
    "TOTAL_FACTURA": 76,
    "SKU": "VA24EHF-J",
    "is_kit": true,
    "kit_invoice": "A000400170796",
    "kit_siblings": ["PRIME A520M-K/CSM", "VG249QL3A-J"],
    "kit_name": "MOTHER ASUS (AM4) PRIME A520M-K CSM + MONITOR 24 ASUS VA24EHF FHD IPS 100Hz 1ms + MONITOR 24 ASUS VG249QL3A GAMING FHD IPS 180Hz 1ms Pie profesional Altura Ajustable"
  }
]
```

### format=xlsx

Descarga un archivo `.xlsx` con nombre `billing-kit-report-DD-MM-YYYY.xlsx`. Contiene las mismas columnas del JSON más `is_kit`, `kit_invoice`, `kit_name` y `kit_siblings` (esta última como string separado por comas). Headers en la fila 1, datos desde la fila 2.

---

## Criterios de aceptación

- Productos vendidos individualmente (factura de una sola línea) **no aparecen** en el resultado


- Facturas con múltiples líneas del mismo SKU tampoco aparecen (compra múltiple, no kit)


- Solo se devuelven líneas pertenecientes a facturas con 2 o más SKUs distintos


- `kit_name` contiene los TITULOS de todos los productos del kit separados por `+`, y es idéntico para todas las líneas de la misma factura


- Las unidades (`CANTIDAD`) no se alteran ni se duplican en ningún caso


- Una factura con múltiples líneas del **mismo SKU** no se marca como kit (es compra múltiple)


- Todos los filtros (`clientId`, `categoryId`, `branch`, `date`, `search`, `brandId`) funcionan en forma combinada


- El campo `search` busca por TITULO y por SKU (case-insensitive)


- El endpoint responde sin error cuando no se envía ningún filtro (devuelve todos los registros del período disponible o requiere al menos `date`)


- No hay filas duplicadas en el resultado


- `format=json` devuelve `Content-Type: application/json`


- `format=xlsx` devuelve un archivo descargable con `Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`


- El XLSX contiene exactamente las mismas filas y campos que el JSON equivalente


- `kit_siblings` en el XLSX es un string legible (ej: `"VA24EHF-J, VG249QL3A-J"`), no un array serializado


- Un `format` con valor inválido devuelve error 422
