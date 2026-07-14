# Contexto (reglas de negocio y aprendizajes)

Ver índice: [[sitio-web]]

## Aceleradores (`NB_WEB.dbo.acelerators`)

Multiplican puntos/ranking según el producto. Una fila matchea un artículo cuando **todos** sus criterios poblados coinciden (AND), tratando cada campo NULL como comodín:

- `txtMatch` — si está seteado, `cDetalle LIKE '%txtMatch%'`; si NULL, comodín de texto.
- `marcaId` — si está seteado, debe igualar `articulo.ID_MARCA`.
- `familiaId` — si está seteado, debe igualar `articulo.ID_FAMILIA`.

Solo es **catch-all global** cuando los tres están en NULL.

- `acelerators.marcaId` mapea 1:1 con `articulo.ID_MARCA` (ej: 85=RAZER, 47=GENIUS, 79=GX GAMING).
- La query toma `TOP 1 ... ORDER BY acelerator DESC` (gana el valor más alto activo).
- **Trampa SQL Server:** `CONCAT('%', NULL, '%')` = `'%%'` (CONCAT convierte NULL en string vacío) → un `txtMatch` NULL sin filtro de marca matchea todo el catálogo. Bug corregido el 2026-07-14, ver [[changelog]].

## Stocks / almacenes

`NewBytes_DBF.dbo.stocks` tiene **una fila por almacén** (`ID_ALMACEN`). Sin filtrar devuelve varias filas y tomar `[0]` puede dar el stock 0 de otro almacén.

- Env `WAREHOUSE_IDS` (ej. `2` o `2,4,6`) define los almacenes válidos.
- Regla: reemplazar JOIN directo a `stocks` por subquery con `SUM + GROUP BY + WHERE ID_ALMACEN IN (WAREHOUSE_IDS)`.
- Archivos con el patrón corregido: `ProductoRepository`, `FichaProductoController`, `ProductCatalogueController`, `ProductecaRepository`, `BrandController`.

## Preferencias / convenciones

- **No** agregar autoría de Claude en commits (sin `Co-Authored-By` ni menciones).
- Cambios locales de infra (`composer.json`/`.lock` con predis, `ecosystem.config.js`) se mantienen **sin commitear** en el working tree; excluirlos de los commits de feature/fix.
- Consultas a la BD de prod requieren autorización explícita del usuario.

## Ver también

- [[arquitectura]] · [[changelog]] · [[infraestructura]]
