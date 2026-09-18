# Importar la planilla en el ERP propio de Laset (comp=11)

> Cómo se corrió la importación completa de `Cotizaciones y Proformas ….xlsx` sobre la
> **base propia de Laset** (`56.125.113.153,4444`), qué falló y por qué. Ejecutado y
> verificado el 2026-09-17.

Ver también: [[Laset]] · [[como-se-importa-laset-comp11]] · [[import-proveedores-sli]] · [[operaciones]] · [[troubleshooting]]

---

## ⚠️ Esto es otra base que la de [[como-se-importa-laset-comp11]]

Aquellas notas describen el **ERP de pedidos de NB**. Acá el mismo código corre contra la
**base propia de Laset** ([[arquitectura|SQL Server 2022, 56.125.113.153,4444]]), que es un
clon del esquema NB del 2026-09-04. Los comandos son los mismos; los datos no. Diferencias
encontradas, todas verificadas:

| | ERP de NB | Base propia de Laset |
|---|---|---|
| Proveedores comp=11 | "pelados" (sin dirección/país/CP/ID fiscal) | **ya tienen** dirección, país y documento; sólo faltaban 56 códigos postales |
| `LST GLOBAL` | existe (`CCODPRO 002607`) | **no existe** en comp=11 |
| `ecc_familia_proveedor` | 94 vínculos | traía 94 **heredados del clon**; recalculados contra los maestros reales quedan **82** |
| Esquema | al día | le faltan columnas que el código ya usa (ver [[troubleshooting]], `doNotUpdateCost`) |

---

## La regla que costó dos pasadas: reimportar exige wipe previo

`"Importar todo"` **no borra nada**: Fase C inserta la planilla **encima** de lo que ya
esté en comp=11. Si la empresa ya tiene una importación anterior, el resultado queda
consistente (remitos completos, stock sin negativos) pero **inflado**: el Delta Check
mostró 666 SKUs con el ERP por encima de la planilla, con casos de 3x.

El wipe es un botón aparte ("Borrar todo comp=11"), y hay que apretarlo **antes**. El
orden correcto es el de [[como-se-importa-laset-comp11]] §Fase B → C → D.

> Detalle que engañó al diagnosticar: de las 1.054 OCs sólo 691 tenían `CSUPROF_TEMP`, así
> que cruzar por proforma **no** detectaba la duplicación — las ~363 viejas nunca pasaron
> por el fix de proforma.

---

## Secuencia que funcionó

```bash
# 0) punto de restauración (15 tablas, ~25k filas)
php artisan laset:snapshot pre_wipe2_20260917

# 1) cargar la planilla en staging (equivalente CLI del botón "Reimportar planilla")
php artisan laset:reimport "/ruta/Cotizaciones y Proformas 2025.10.01 (2).xlsx"

# 2) vaciar comp=11 — deja el staging en MATCHED y resetea stocks
php artisan laset:wipe-transactional

# 3) clasificar
php artisan laset:aggregate-match          # 4.131 MATCHED · 611 IGNORED · 333 STOCK_ONLY

# 4) crear órdenes y maestros (~20 min)
php artisan laset:import-fase-c

# 5) remitos + stock — POR TANDAS (ver abajo)
php artisan laset:import-fase-d --skip-bloqueadas --limit=50    # repetir hasta 0 pendientes

# 6) fixes de cierre
php artisan laset:fix-albprol-faltante
php artisan laset:fix-stock-almacen-comp11
```

**Fase D va por tandas de 50**: en una sola corrida tarda >20 min y la UI/el job la dan por
fallada. Es idempotente (saltea lo que ya tiene remito), así que repetir es gratis.

---

## Fase D aborta entera por una sola orden

`applyStockDelta` tiene un ASSERT: si un grupo (artículo, almacén) no puede crear su fila en
`stocks`, tira **toda** la transacción. Alcanzó **una OC vieja con `warehousesId` NULL y
`cCodAlm='SAF'`** (almacén que no es de comp=11) para bloquear la migración completa:

```
[ABORT Fase D stock] 2 grupos delta sin fila en stocks tras UPDATE+INSERT
```

Eran **7 OCs de prueba preexistentes** (proveedores `nuevo proveedor` y `Proveedor Testing
Laset`, proformas `123`/`3456`, dos sin líneas). Se borraron con guardas. Como sus números
eran bajos (13094-13203), toda tanda las tomaba primero: 8 tandas seguidas no avanzaron una
sola fila.

Corregido en el código: `--skip-bloqueadas` ahora **difiere** las órdenes con almacén fuera
de `FP_Almacen` comp=11, en vez de abortar (igual que ya hacía con los artículos no-comp11).

> El error no llegaba al job: `Artisan::call` guarda el output, pero `lastOutputTail()`
> recortaba a los últimos 1500 chars y el stack de Symfony tapaba la línea del ABORT.
> También corregido (ahora rescata las líneas de error antes del recorte).

---

## Resultado (2026-09-17)

| | |
|---|---|
| OCs / remitos de compra | 661 / 661 |
| Ventas / remitos de venta | 623 / 600 (23 son reservas `cestado=P`, sin remito por diseño) |
| Proveedores / clientes / artículos | 83 / 163 / 1.062 |
| Stock | 1.859 filas, **0 en negativo** |
| Staging | 4.458 `IMPORTED` con linkeo al ERP · 611 `IGNORED` · 6 `STOCK_ONLY_SUPERSEDED` |

**Fidelidad staging → ERP:** compras 219.384 vs 219.378 u (**6 u de diferencia, 0,003%**);
ventas 219.384 vs 195.284 u, diferencia explicada: **333 filas con `year=1900` no tienen ni
proforma ni factura de cliente** (24.555 u) — son ingreso de stock sin venta y así se
importaron.

### El Delta Check medía mal

Daba 220 SKUs con delta que **no eran errores**: filtraba la planilla por
`year_field IN (2025,2026)` mientras contaba **todo** el ERP, sumaba filas `IGNORED` que
nunca se importan, y contaba como venta filas sin proforma ni factura. Corregido: quedan
**24 SKUs**, todos explicables (6 u de compras en 1 SKU + las 23 reservas).

---

## Subir la planilla desde el front

Dos bugs encadenados, los dos corregidos (ver [[troubleshooting]]):

1. **`mimes:xlsx` rechazaba todo .xlsx.** libmagic 8.1.2 no reconoce los xlsx de Excel y
   devuelve `application/octet-stream`; la regla compara contra `guessExtension()`. Se
   reemplazó por `App\Support\XlsxUpload` (extensión + firma ZIP del archivo).
2. **`upload_max_filesize = 2M`.** `docker/php/apache-uploads.ini` ya existía con 100M pero
   **el docker-compose no lo montaba**. Mensaje engañoso: *"El campo file no se pudo subir"*,
   que es la regla `uploaded` de Laravel, no un problema de permisos.

Mientras tanto existe `laset:reimport`, equivalente CLI exacto del botón.

---

## Lo que quedó pendiente

- [ ] **Re-vincular facturas**: el wipe desvincula las CFE de Uruguay (`unlink 123`). El plan
      está calculado: 398 facturas, 399 pares, 168 sin match que no se tocan. Es el botón
      "Re-vincular facturas" de `/syncLaset`.
- [ ] **ECCN**: 23 clasificaciones no entran porque 4 proveedores (`LST GLOBAL`, `ASUS
      COMPUTER INTERNATIONAL`, `PNY`, `ZOTAC`) y 18 categorías no existen en comp=11. Se
      resuelve dando de alta esos maestros, no tocando el import.
- [ ] **Snapshots**: quedaron 6 tags (85 tablas `laset_snap_*`). Conservar el último y
      borrar el resto con `laset:snapshot <tag> --drop`.
- [ ] Desplegar los fixes en el dev de blu (`api.pedidos-laset-dev.blu.net.ar`).
