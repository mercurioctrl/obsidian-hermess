# Migración SQL Server

## Target

- **Engine:** SQL Server 2012+.
- **Database:** `NewBytes_DBF` (configurable vía `DB_TABLE` en `.env`).
- **Tabla:** `dbo.AfipComprobantesRecibidos`.

Para detalle de columnas y códigos AFIP: ver [[tabla-referencia]].

## Creación inicial

```sql
CREATE TABLE dbo.AfipComprobantesRecibidos (
    id                          BIGINT IDENTITY(1,1) NOT NULL,
    cuit_titular                VARCHAR(11)     NOT NULL,
    fecha_emision               DATE            NOT NULL,
    tipo_comprobante            SMALLINT        NOT NULL,
    punto_venta                 INT             NOT NULL,
    numero_desde                BIGINT          NOT NULL,
    numero_hasta                BIGINT          NOT NULL,
    cae                         VARCHAR(14)     NULL,
    tipo_doc_emisor             SMALLINT        NOT NULL,
    nro_doc_emisor              VARCHAR(20)     NOT NULL,
    denominacion_emisor         NVARCHAR(200)   NULL,
    tipo_doc_receptor           SMALLINT        NULL,
    nro_doc_receptor            VARCHAR(20)     NULL,
    tipo_cambio                 DECIMAL(18, 6)  NULL,
    moneda                      VARCHAR(5)      NULL,
    imp_neto_gravado_iva_0      DECIMAL(18, 2)  NULL,
    iva_2_5                     DECIMAL(18, 2)  NULL,
    imp_neto_gravado_iva_2_5    DECIMAL(18, 2)  NULL,
    iva_5                       DECIMAL(18, 2)  NULL,
    imp_neto_gravado_iva_5      DECIMAL(18, 2)  NULL,
    iva_10_5                    DECIMAL(18, 2)  NULL,
    imp_neto_gravado_iva_10_5   DECIMAL(18, 2)  NULL,
    iva_21                      DECIMAL(18, 2)  NULL,
    imp_neto_gravado_iva_21     DECIMAL(18, 2)  NULL,
    iva_27                      DECIMAL(18, 2)  NULL,
    imp_neto_gravado_iva_27     DECIMAL(18, 2)  NULL,
    imp_neto_gravado_total      DECIMAL(18, 2)  NULL,
    imp_neto_no_gravado         DECIMAL(18, 2)  NULL,
    imp_op_exentas              DECIMAL(18, 2)  NULL,
    otros_tributos              DECIMAL(18, 2)  NULL,
    total_iva                   DECIMAL(18, 2)  NULL,
    imp_total                   DECIMAL(18, 2)  NOT NULL,
    origen_archivo              NVARCHAR(400)   NULL,
    cargado_en                  DATETIME2(0)    NOT NULL CONSTRAINT DF_AfipRec_cargado_en DEFAULT (SYSDATETIME()),
    CONSTRAINT PK_AfipComprobantesRecibidos PRIMARY KEY CLUSTERED (id)
);
GO

-- Clave natural para idempotencia. Ver [[arquitectura]].
CREATE UNIQUE NONCLUSTERED INDEX UX_AfipRec_natural
    ON dbo.AfipComprobantesRecibidos (
        cuit_titular, tipo_comprobante, punto_venta, numero_desde, nro_doc_emisor
    );
GO

CREATE NONCLUSTERED INDEX IX_AfipRec_fecha
    ON dbo.AfipComprobantesRecibidos (cuit_titular, fecha_emision);
GO

CREATE NONCLUSTERED INDEX IX_AfipRec_emisor
    ON dbo.AfipComprobantesRecibidos (nro_doc_emisor, fecha_emision);
GO

CREATE NONCLUSTERED INDEX IX_AfipRec_cae
    ON dbo.AfipComprobantesRecibidos (cae);
GO
```

### Gotchas importantes

- **`cae` es NULLable a propósito.** Los comprobantes `tipo_comprobante = 81` (Tique Factura A) y otros tickets de controladores fiscales usan **CAI/COE** en lugar de CAE, y llegan con esa columna vacía. Si se vuelve a `NOT NULL`, la carga de cualquier mes que tenga tickets falla con "Cannot insert NULL into column 'cae'".
- **No poner comentarios `--`** al final de una línea de definición de columna. Algunos clientes SQL parsean mal la concatenación y leen la palabra siguiente como nombre de columna sin tipo.

## Migración sobre una tabla ya creada (ALTER)

Si la tabla ya está creada con `cae NOT NULL` (versión inicial del repo, anterior al 2026-04-22):

```sql
ALTER TABLE dbo.AfipComprobantesRecibidos ALTER COLUMN cae VARCHAR(14) NULL;
```

## Verificación post-creación

```sql
SELECT COUNT(*) FROM dbo.AfipComprobantesRecibidos;
SELECT name, is_unique, type_desc
FROM sys.indexes
WHERE object_id = OBJECT_ID('dbo.AfipComprobantesRecibidos');
-- Debe listar 5: PK + UX_AfipRec_natural + 3 IX_*
```

## Evolución — reglas para agregar columnas

1. `ALTER TABLE ... ADD nueva_columna TIPO NULL;` en SQL.
2. Agregarla al `CSV_TO_COL` y al set `INT_COLS` / `DEC_COLS` en `afip/db.py`.
3. Agregarla a `TARGET_COLS`.
4. Agregarla al `CREATE TABLE #staging` dentro de `load_csv`.

## Cambiar clave natural

Si se decide que la clave debe incluir otro campo:

```sql
DROP INDEX UX_AfipRec_natural ON dbo.AfipComprobantesRecibidos;
CREATE UNIQUE NONCLUSTERED INDEX UX_AfipRec_natural
    ON dbo.AfipComprobantesRecibidos (
        cuit_titular, tipo_comprobante, punto_venta, numero_desde, nro_doc_emisor, cae
    );
```

Actualizar también la cláusula `ON` del `MERGE` en `afip/db.py`. Ojo: si se incluye `cae` y está `NULL`, SQL Server trata dos NULLs como NO iguales → el comprobante sin CAE se insertaría múltiples veces. No incluirla en la clave.

## Rollback

```sql
IF OBJECT_ID('dbo.AfipComprobantesRecibidos', 'U') IS NOT NULL
    DROP TABLE dbo.AfipComprobantesRecibidos;
```

## Tamaños esperados

| Volumen (por CUIT)         | Filas/mes | Anual × 7 CUITs |
|----------------------------|-----------|-----------------|
| PyME con pocas facturas    | 50-200    | ~20 MB          |
| Distribuidora (caso [[NB]])| 500-1500  | ~150 MB         |
| Operador intenso           | 5000+     | ~800 MB         |

Si crece demasiado → particionar por año usando `fecha_emision`.

## Ver también

- [[sincroAfip]]
- [[tabla-referencia]]
- [[arquitectura]]
