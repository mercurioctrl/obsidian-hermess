# API - Fix - Script de regularización stock doble-descuento

**Proyecto:** [[pedidos|Pedidos]]
**Estado:** Listo (dry-run validado — pendiente correr `--apply` con sign-off)
**Fecha:** 2026-06-11
**Relacionado:** [[API - Fix - Corregir doble-descuento de stock por race en MakeSale|Fix del bug de doble-descuento]]

Script que **repone el stock perdido** por el bug de doble-descuento (race en `MakeSaleService`): **138 artículos / 683 unidades**. Complementa el fix de código (que evita nuevos casos) corrigiendo los datos ya dañados.

Ubicación del archivo runnable: `inventario/ms-metadata/scripts/regularizar_doble_descuento.py`

---

## Decisión: reponer a `nstock` (no `regularizacion_global`)

Las 683 unidades son **pérdidas fantasma**: el stock físico **está** en el depósito, pero el sistema lo descontó dos veces por el bug. Por eso la corrección correcta es **devolverlas al stock real** (`stocks.nstock += pérdida`), no maquillar el delta con `regularizacion_global` (que dejaría `nstock` en 0, es decir, el sistema seguiría sin "ver" mercadería que existe).

> ⚠️ Antes de `--apply` conviene un **conteo físico spot** de los items top (117542, 119699, 115239…) para confirmar que la mercadería está. Si en algún caso NO está (se vendió/movió por fuera), ese item se regulariza distinto.

---

## Cómo calcula la pérdida

Misma firma validada en el análisis (item 119699 = 70):

- Detecta remitos con **≥2 movimientos `MakeSaleService` para el mismo `(cref, remito, sAnterior)`** (la huella del race).
- Pérdida por `(cref, remito)` = `unidades netas removidas del stock − unidades documentadas en albclil`.
- Asigna cada remito a su depósito (de las filas `MakeSale`) y agrupa por `(artículo, depósito)`.

Dry-run confirma: **138 filas, total exacto 683 unidades** (todas con depósito asignado, sin NULLs).

---

## Seguridad del script

- **Dry-run por defecto:** sin `--apply` no toca nada, solo imprime el plan.
- **Idempotente:** omite items que ya tengan el movimiento marcador (`fichero = 'Regularizacion doble-descuento | fix race MakeSale'`). Correrlo dos veces no duplica.
- **Transaccional:** todo dentro de una transacción; ante cualquier error → rollback total.
- **Auditable:** cada ajuste deja una fila en `registro_stock` (`remito='REGULARIZACION'`, con `sAnterior`/`sPosterior` reales).
- Filas sin depósito (NULL) se reportan y **no** se aplican (revisión manual).

## Uso

```bash
cd inventario/ms-metadata
# Dry-run (no modifica nada):
OPENSSL_CONF=/ruta/openssl_legacy.cnf .venv/bin/python scripts/regularizar_doble_descuento.py
# Aplicar de verdad (tras sign-off):
OPENSSL_CONF=/ruta/openssl_legacy.cnf .venv/bin/python scripts/regularizar_doble_descuento.py --apply
```

> `OPENSSL_CONF` con `MinProtocol=TLSv1` + `CipherString=DEFAULT@SECLEVEL=0` solo hace falta en macOS con Driver 18/OpenSSL 3 contra el SQL Server viejo. En el server puede no necesitarse.

---

## Script completo

```python
#!/usr/bin/env python3
"""
Regularización de stock perdido por el bug de doble-descuento (race en MakeSaleService).

Repone a [NewBytes_DBF].[dbo].[stocks].nstock las unidades que el bug descontó dos veces
y nunca repuso (pérdidas fantasma: el stock físico está, el sistema cree que no).

- Por DEFECTO corre en DRY-RUN: no modifica nada, solo imprime el plan.
- Para aplicar de verdad:   python regularizar_doble_descuento.py --apply
- Es IDEMPOTENTE: omite items que ya tengan un movimiento de regularización con
  el `fichero` marcador (no vuelve a sumar si se corre dos veces).

Detección (misma firma validada en el análisis del item 119699 = 70):
  >=2 movimientos 'MakeSaleService' para el mismo (cref, remito, sAnterior) -> doble descuento.
  Pérdida = (unidades netas removidas del stock) - (unidades documentadas en albclil),
  calculada por (artículo, depósito).

Conexión: usa el .env de ms-metadata (DB_SERVER/DB_USER/DB_PASS/...).
Driver 17 + Encrypt=no. En macOS con SQL Server viejo puede requerir OpenSSL permisivo:
  OPENSSL_CONF=/ruta/openssl_legacy.cnf  (MinProtocol=TLSv1, CipherString=DEFAULT@SECLEVEL=0)
"""
import os
import sys
from dotenv import load_dotenv
import pyodbc

MARCADOR_FICHERO = 'Regularizacion doble-descuento | fix race MakeSale'

# Reconciliación: pérdida por (artículo, depósito).
# Cruza el kardex (registro_stock) contra los documentos (albclil), por depósito.
SQL_PERDIDAS = """
WITH dup AS (
    SELECT cref, remito
    FROM NB_WEB.dbo.registro_stock
    WHERE fichero LIKE '%MakeSaleService%'
      AND remito IS NOT NULL AND LTRIM(RTRIM(remito)) <> '' AND cantidad < 0
    GROUP BY cref, remito, sAnterior, cantidad
    HAVING COUNT(*) >= 2
),
affected AS (SELECT DISTINCT cref, remito FROM dup),
mov AS (   -- neto removido por (cref, remito) -- SIN deposito (metodo validado = 683)
    SELECT rs.cref, rs.remito,
           REPLACE(REPLACE(rs.remito, 'R-', 'X'), '-', '') AS remkey,
           SUM(rs.cantidad) AS net
    FROM NB_WEB.dbo.registro_stock rs
    JOIN affected a ON a.cref = rs.cref AND a.remito = rs.remito
    WHERE (rs.fichero LIKE '%MakeSaleService%' OR rs.fichero LIKE '%RemoveSaleService%')
    GROUP BY rs.cref, rs.remito
),
wh AS (   -- deposito donde ocurrio el descuento (de las filas MakeSale del remito)
    SELECT cref, remito, MIN(ID_ALMACEN) AS ID_ALMACEN
    FROM NB_WEB.dbo.registro_stock
    WHERE fichero LIKE '%MakeSaleService%' AND ID_ALMACEN IS NOT NULL
    GROUP BY cref, remito
),
art AS (SELECT cRef, MIN(ID_ARTICULO) AS id FROM NewBytes_DBF.dbo.articulo GROUP BY cRef),
sold AS (  -- documentado en albclil por (cref, remito) -- SIN deposito
    SELECT a.cRef AS cref, l.ID_NROREMCLI_ENC AS remkey, SUM(l.ncanent) AS units
    FROM NewBytes_DBF.dbo.albclil l
    JOIN art a ON a.id = l.Id_Articulo
    GROUP BY a.cRef, l.ID_NROREMCLI_ENC
)
SELECT art.id AS id_articulo, mk.cref, wh.ID_ALMACEN,
       CAST(SUM(-mk.net - ISNULL(s.units, 0)) AS INT) AS perdida
FROM mov mk
JOIN art ON art.cRef = mk.cref
LEFT JOIN wh ON wh.cref = mk.cref AND wh.remito = mk.remito
LEFT JOIN sold s ON s.cref = mk.cref AND s.remkey = mk.remkey
GROUP BY art.id, mk.cref, wh.ID_ALMACEN
HAVING SUM(-mk.net - ISNULL(s.units, 0)) > 0
ORDER BY perdida DESC
"""


def connect():
    load_dotenv()
    for drv in ("ODBC Driver 17 for SQL Server", "ODBC Driver 18 for SQL Server"):
        try:
            cs = (f"DRIVER={{{drv}}};SERVER={os.getenv('DB_SERVER')};DATABASE={os.getenv('DB_NAME')};"
                  f"UID={os.getenv('DB_USER')};PWD={os.getenv('DB_PASS')};"
                  "Encrypt=no;TrustServerCertificate=yes;Connection Timeout=30;")
            return pyodbc.connect(cs, timeout=30)
        except Exception as e:
            print(f"[conn fail {drv}] {str(e)[:80]}", file=sys.stderr)
    raise SystemExit("No se pudo conectar a la DB")


def ya_regularizado(cur, id_articulo, id_almacen):
    cur.execute(
        "SELECT COUNT(*) FROM NB_WEB.dbo.registro_stock "
        "WHERE codigo = ? AND ID_ALMACEN = ? AND fichero = ?",
        [id_articulo, id_almacen, MARCADOR_FICHERO])
    return cur.fetchone()[0] > 0


def main():
    apply = "--apply" in sys.argv
    conn = connect()
    cur = conn.cursor()

    cur.execute(SQL_PERDIDAS)
    filas = cur.fetchall()
    total = sum(r.perdida for r in filas)
    sin_dep = [r for r in filas if r.ID_ALMACEN is None]
    aplicables = [r for r in filas if r.ID_ALMACEN is not None]
    print(f"{'id_articulo':>12} {'cref':>22} {'deposito':>9} {'perdida':>8}")
    for r in filas:
        dep = r.ID_ALMACEN if r.ID_ALMACEN is not None else 'NULL'
        print(f"{r.id_articulo:>12} {str(r.cref):>22} {str(dep):>9} {r.perdida:>8}")
    print("-" * 56)
    print(f"Filas (artículo×depósito): {len(filas)} | TOTAL pérdida: {total} unidades")
    if sin_dep:
        print(f"AVISO: {len(sin_dep)} fila(s) sin depósito (NULL) por "
              f"{sum(r.perdida for r in sin_dep)} u. -> requieren revisión manual, NO se aplican.")

    if not apply:
        print("\nDRY-RUN: no se modificó nada. Para aplicar, correr con --apply")
        return

    print("\n*** MODO APPLY: se modificará el stock en producción ***")
    aplicadas = omitidas = unidades = 0
    try:
        conn.autocommit = False
        for r in aplicables:
            if ya_regularizado(cur, r.id_articulo, r.ID_ALMACEN):
                omitidas += 1
                continue
            # 1) reponer stock físico
            cur.execute(
                "UPDATE NewBytes_DBF.dbo.stocks SET nstock = nstock + ? "
                "WHERE ID_ARTICULO = ? AND ID_ALMACEN = ?",
                [r.perdida, r.id_articulo, r.ID_ALMACEN])
            # 2) registrar el movimiento de auditoría (sAnterior/sPosterior reales)
            cur.execute("""
                INSERT INTO NB_WEB.dbo.registro_stock
                    (fecha, codigo, cref, cantidad, remito, agente, exito, fichero,
                     sAnterior, sPosterior, query, ID_ALMACEN)
                VALUES (GETDATE(), ?, ?, ?, 'REGULARIZACION', 0, 1, ?,
                    (SELECT (nstock + nstock_lo + nstock_en_cola) FROM NewBytes_DBF.dbo.stocks
                     WHERE ID_ARTICULO = ? AND ID_ALMACEN = ?) - ?,
                    (SELECT (nstock + nstock_lo + nstock_en_cola) FROM NewBytes_DBF.dbo.stocks
                     WHERE ID_ARTICULO = ? AND ID_ALMACEN = ?),
                    'regularizar_doble_descuento.py', ?)
            """, [r.id_articulo, r.cref, r.perdida, MARCADOR_FICHERO,
                  r.id_articulo, r.ID_ALMACEN, r.perdida,
                  r.id_articulo, r.ID_ALMACEN, r.ID_ALMACEN])
            aplicadas += 1
            unidades += r.perdida
        conn.commit()
        print(f"OK. Aplicadas: {aplicadas} | Omitidas (ya regularizadas): {omitidas} "
              f"| Unidades repuestas: {unidades}")
    except Exception as e:
        conn.rollback()
        print(f"ERROR, rollback. Nada se modificó. Detalle: {e}", file=sys.stderr)
        raise
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()
```

## Ver también

- [[API - Fix - Corregir doble-descuento de stock por race en MakeSale|Fix del bug (causa raíz + solución)]]
- [[modulo-makesale|MakeSale]] · [[modulo-removesale|RemoveSale]]
- [[relacion-tablas-articulo-stocks|Artículo y stocks]]
