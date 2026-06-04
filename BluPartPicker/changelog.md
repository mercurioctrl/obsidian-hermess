# Changelog — BluPartPicker

## 2026-06-03 (continuación)

### Repositorio Git
- Subido a `git@github.com:BluIncStudio/bluPartPicker.git` (privado), rama `main`
- `.gitignore`: excluye `invid.db`, `*.log`, `__pycache__`, `settings.local.json`

### Bóveda Obsidian configurada
- Carpeta `BluPartPicker/` en la bóveda con 7 notas: índice, arquitectura, resellers, stack, contexto, changelog, memoria
- `CLAUDE.md` del proyecto en `.claude/CLAUDE.md` con sección Obsidian
- `Home.md` actualizado con la nueva sección

---

## 2026-06-03

### Nuevo distribuidor: Stylus
- `sync_stylus.py` — 906 productos, 42 marcas, TSV por marca + scraping catálogo
- Cron configurado: `0 2,6,10,14,18,22 * * *`
- Login: `POST /login.php` con `action=send, url=home.php`
- Precios en TSV latin-1 con formato `"U$S 1.282,87"` (no es Excel real)
- Stock numérico desde scraping del catálogo web (~103 páginas)

### Columna `categoria` agregada a todos los distribuidores
- `ALTER TABLE itemsRepository ADD COLUMN categoria TEXT`
- **Invid:** RUBRO derivado del slug de categoría (ej: "notebooks--prod--152" → "Notebooks")
- **Ceven:** `commercecategoryurl` calls separados por cada una de las 26 categorías → `categoria_map`
- **Stylus:** columna RUBRO del TSV
- API `/items` actualizada para incluir `categoria` en la respuesta

### Documentación
- `docs/architecture.md` y `docs/resellers.md` creados en el repo
- `README.md` con guía de uso y endpoints
- `start.sh` para setup desde cero con un comando
- Bóveda Obsidian configurada en `BluPartPicker/`
- Memoria Claude guardada en `~/.claude/projects/-var-www-blupartpicker/memory/`

## 2026-06-02 (sesión anterior)

### Invid Computers
- Login autenticado via session cookies (campo `usuari`, no `email`)
- Excel desde `genera_excel.php` — openpyxl, fila 10, dedup con dict
- `isinstock` derivado de `observaciones`
- Scraping de 22 categorías para `imagen_url`, `url_ficha`, `categoria`

### Ceven
- Playwright requerido (Akamai bloquea requests/curl)
- NetSuite SCA API `/api/personalized/items` con paginación 100
- 26 categorías mapeadas via `commercecategoryurl`
- Fix: 2 itemids duplicados resueltos con dict dedup

### API FastAPI
- Puerto 4444
- Endpoints: sources, items, item detalle, historia, sync/log, fabricantes
- systemd service `blupartpicker-api.service`
- CORS abierto para GET

### DB
- `itemsRepository`: catálogo unificado con UNIQUE(source, codigo)
- `price_stock_history`: historial de precios/stock
- `sync_log`: log de ejecuciones

---

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[arquitectura]] — estado actual del sistema
- [[contexto]] — motivación y decisiones de diseño
