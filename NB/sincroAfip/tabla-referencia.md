# Referencia tabla `AfipComprobantesRecibidos`

Diccionario de columnas + códigos AFIP + queries tipo para reporting.

Para DDL de creación: ver [[migracion]].

## Columnas

| Columna                      | Tipo SQL        | Null | Origen CSV                   | Notas                                               |
|------------------------------|-----------------|------|------------------------------|-----------------------------------------------------|
| `id`                         | BIGINT IDENTITY | NO   | -                            | PK surrogate.                                       |
| `cuit_titular`               | VARCHAR(11)     | NO   | path del CSV                 | CUIT "nuestro" (receptor representado), sin guiones.|
| `fecha_emision`              | DATE            | NO   | Fecha de Emisión             |                                                     |
| `tipo_comprobante`           | SMALLINT        | NO   | Tipo de Comprobante          | Código AFIP — ver tabla abajo.                      |
| `punto_venta`                | INT             | NO   | Punto de Venta               |                                                     |
| `numero_desde`               | BIGINT          | NO   | Número Desde                 |                                                     |
| `numero_hasta`               | BIGINT          | NO   | Número Hasta                 | Suele ser = numero_desde.                           |
| `cae`                        | VARCHAR(14)     | **SÍ** | Cód. Autorización         | 14 dígitos. **NULL** en Tique Factura (tipo 81) y otros controladores fiscales que usan CAI/COE. |
| `tipo_doc_emisor`            | SMALLINT        | NO   | Tipo Doc. Emisor             | Código AFIP — ver tabla abajo.                      |
| `nro_doc_emisor`             | VARCHAR(20)     | NO   | Nro. Doc. Emisor             | CUIT del proveedor, sin guiones.                    |
| `denominacion_emisor`        | NVARCHAR(200)   | SÍ   | Denominación Emisor          | Razón social.                                       |
| `tipo_doc_receptor`          | SMALLINT        | SÍ   | Tipo Doc. Receptor           | Normalmente 80 (CUIT).                              |
| `nro_doc_receptor`           | VARCHAR(20)     | SÍ   | Nro. Doc. Receptor           | Debería coincidir con `cuit_titular`.               |
| `tipo_cambio`                | DECIMAL(18, 6)  | SÍ   | Tipo Cambio                  | Coma → punto. Pesos = 1.000000.                     |
| `moneda`                     | VARCHAR(5)      | SÍ   | Moneda                       | `$`, `USD`, `EUR`...                                |
| `imp_neto_gravado_iva_0`     | DECIMAL(18, 2)  | SÍ   | Imp. Neto Gravado IVA 0%     |                                                     |
| `iva_2_5`, `..._5`, `..._10_5`, `..._21`, `..._27`  | DECIMAL(18, 2) | SÍ | IVA discriminado por alícuota                          |
| `imp_neto_gravado_iva_*`     | DECIMAL(18, 2)  | SÍ   | Base gravada por cada alícuota                          |
| `imp_neto_gravado_total`     | DECIMAL(18, 2)  | SÍ   | Imp. Neto Gravado Total      | Suma de bases gravadas.                             |
| `imp_neto_no_gravado`        | DECIMAL(18, 2)  | SÍ   | Imp. Neto No Gravado         |                                                     |
| `imp_op_exentas`             | DECIMAL(18, 2)  | SÍ   | Imp. Op. Exentas             |                                                     |
| `otros_tributos`             | DECIMAL(18, 2)  | SÍ   | Otros Tributos               | Percepciones, impuestos internos, etc.              |
| `total_iva`                  | DECIMAL(18, 2)  | SÍ   | Total IVA                    |                                                     |
| `imp_total`                  | DECIMAL(18, 2)  | NO   | Imp. Total                   | Total facturado.                                    |
| `origen_archivo`             | NVARCHAR(400)   | SÍ   | -                            | CSV de origen (auditoría).                          |
| `cargado_en`                 | DATETIME2(0)    | NO   | -                            | Timestamp de ingesta.                               |

## Códigos AFIP más usados

### Tipo de comprobante

| Código | Descripción                         |
|--------|-------------------------------------|
| 1      | Factura A                           |
| 2      | Nota de Débito A                    |
| 3      | Nota de Crédito A                   |
| 4      | Recibo A                            |
| 6      | Factura B                           |
| 7      | Nota de Débito B                    |
| 8      | Nota de Crédito B                   |
| 9      | Recibo B                            |
| 11     | Factura C                           |
| 12     | Nota de Débito C                    |
| 13     | Nota de Crédito C                   |
| 15     | Recibo C                            |
| 19     | Factura E (exportación)             |
| 51     | Factura M                           |
| **81** | **Tique Factura A (controlador fiscal) — viene con CAE NULL (usa CAI/COE)** |
| **82** | **Tique Factura B (controlador fiscal) — viene con CAE NULL**               |
| 201    | FCE MiPyMEs A                       |
| 206    | FCE MiPyMEs B                       |
| 211    | FCE MiPyMEs C                       |

### Tipo de documento

| Código | Descripción   |
|--------|---------------|
| 80     | CUIT          |
| 86     | CUIL          |
| 87     | CDI           |
| 96     | DNI           |
| 94     | Pasaporte     |
| 99     | Sin identificar |

## Queries típicas

### Total facturado por proveedor en un mes

```sql
SELECT
    nro_doc_emisor,
    denominacion_emisor,
    COUNT(*)       AS cant_comprobantes,
    SUM(imp_total) AS total
FROM dbo.AfipComprobantesRecibidos
WHERE cuit_titular  = '30709246638'
  AND fecha_emision >= '2026-04-01'
  AND fecha_emision <  '2026-05-01'
GROUP BY nro_doc_emisor, denominacion_emisor
ORDER BY total DESC;
```

### IVA crédito del mes (solo A — genera crédito fiscal)

```sql
SELECT
    SUM(iva_2_5)  AS iva_2_5,
    SUM(iva_5)    AS iva_5,
    SUM(iva_10_5) AS iva_10_5,
    SUM(iva_21)   AS iva_21,
    SUM(iva_27)   AS iva_27,
    SUM(total_iva) AS total
FROM dbo.AfipComprobantesRecibidos
WHERE cuit_titular  = '30709246638'
  AND fecha_emision >= '2026-04-01'
  AND fecha_emision <  '2026-05-01'
  AND tipo_comprobante IN (1, 2, 3);
```

### Comprobantes nuevos hoy (monitoreo)

```sql
SELECT cuit_titular, COUNT(*) AS nuevos
FROM dbo.AfipComprobantesRecibidos
WHERE cargado_en >= CAST(GETDATE() AS DATE)
GROUP BY cuit_titular;
```

### Tickets de controladores fiscales (sin CAE)

```sql
SELECT COUNT(*), SUM(imp_total)
FROM dbo.AfipComprobantesRecibidos
WHERE cuit_titular = '30709246638'
  AND cae IS NULL;
```

### Detectar huecos (días sin comprobantes en últimos 3 meses)

```sql
;WITH fechas AS (
    SELECT DISTINCT fecha_emision
    FROM dbo.AfipComprobantesRecibidos
    WHERE cuit_titular = '30709246638'
      AND fecha_emision >= DATEADD(MONTH, -3, CAST(GETDATE() AS DATE))
)
SELECT
    fecha_emision,
    LAG(fecha_emision) OVER (ORDER BY fecha_emision) AS fecha_anterior,
    DATEDIFF(DAY,
             LAG(fecha_emision) OVER (ORDER BY fecha_emision),
             fecha_emision) AS dias_entre
FROM fechas
ORDER BY fecha_emision DESC;
```

## Ver también

- [[sincroAfip]]
- [[migracion]]
- [[arquitectura]]
