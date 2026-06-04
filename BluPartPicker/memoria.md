# Memoria Claude — BluPartPicker

Decisiones y contexto no obvio para retomar trabajo futuro rápido.

## Credenciales de distribuidores

| Distribuidor | Usuario | Clave | Notas |
|---|---|---|---|
| Invid | `30709246638` | `kilo3458` | Campo `usuari` (no `email`) |
| Ceven | `mrebreg@nb.com.ar` | `Nb20262026` | Solo funciona con Playwright |
| Stylus | `stylus@stylus.com.ar` | `Arbol78` | Campo `Email` con mayúscula |

## Gotchas críticos

**Invid:**
- El Excel tiene headers repetidos en el medio → skipear `codigo.lower() == "codigo"`
- Hay códigos duplicados → usar dict (última ocurrencia gana)
- El campo del formulario de login se llama `usuari`, no `usuario` ni `email`

**Ceven:**
- NUNCA mover las llamadas fuera del contexto de Playwright. Akamai valida TLS fingerprint + cookie juntos
- Las categorías no vienen en la respuesta del item → calls separados por `commercecategoryurl`
- ~108/464 productos sin categoría es esperado (no están en ninguna página de categoría)

**Stylus:**
- `lista_precios_xls.php` devuelve TSV disfrazado de XLS → `r.content.decode("latin-1")` + split por `\t`
- `parse_usd()`: reemplazar punto→nada, coma→punto (formato argentino)
- El filtro `?Codigo=XXX` en la URL del catálogo NO filtra — devuelve todo

## Convenciones de código

- Todos los sync scripts siguen el mismo patrón: `login → fetch_data → normalize → upsert_products → sync_log`
- `upsert_products()` siempre registra historial en INSERT; en UPDATE solo si cambia precio/stock
- `isinstock` es siempre 0 o 1 (nunca NULL)
- `stock` puede ser NULL (Invid no tiene stock numérico)
- `precio_final` siempre con IVA incluido

## Portabilidad — cómo correr en un host nuevo

`bash start.sh` es suficiente desde cualquier clone. Maneja solo:
- **pip no instalado** (Ubuntu nuevo) → lo bootstrappea vía apt / ensurepip
- **Playwright sin build oficial** (Ubuntu 26.04+) → usa `PLAYWRIGHT_HOST_PLATFORM_OVERRIDE=ubuntu24.04-x64` (la arch en el string es obligatoria) + instala libs `t64` vía apt
- **systemd unit** → se genera con `User=$(id -un)` y el path real del clone, no hay nada hardcodeado

**Bug conocido resuelto:** `sync_invid.py` en versiones anteriores al commit `42a0eb7` no tenía `categoria` en el `CREATE TABLE`. Si la DB fue creada con esa versión vieja, hacer `ALTER TABLE itemsRepository ADD COLUMN categoria TEXT` manualmente.

## Agregar un nuevo distribuidor

1. Crear `sync_NOMBRE.py` siguiendo patrón de `sync_stylus.py`
2. `SOURCE = "nombre"` — sin espacios, minúsculas
3. La DB ya tiene todos los campos — no hace falta ALTER TABLE
4. Cron desfasado al menos 1h de los existentes (actualmente usan 00, 01, 02)
5. Verificar en `GET /sources`

## Estado de la DB (jun 2026)

- Archivo: `/var/www/blupartpicker/invid.db` (~1.9 MB)
- Nombre heredado de la primera sincronización con Invid
- 2.565 productos · 939 entradas en historial · 3 fuentes

## Próximos pasos posibles

- Agregar más distribuidores (Distecna, Totvision, etc.)
- Frontend para comparar precios entre fuentes
- Alertas cuando un precio cae X%
- Cross-match por nro_parte entre distribuidores para ver el mismo producto en varios

---

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[resellers]] — casos puntuales detallados por distribuidor
- [[arquitectura]] — schema y convenciones de la DB
- [[changelog]] — historial de cambios
