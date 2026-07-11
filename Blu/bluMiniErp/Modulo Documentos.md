# Módulo Documentos (descarga original + formato BLU)

Sección para alojar y descargar **documentos útiles de la empresa**. Cada documento se ofrece en dos variantes: el **PDF original** (tal cual emitido) y una versión con **formato BLU** (mismo contenido re-maquetado con la membretada de la empresa). Documentación técnica en repo: `arquitectura/12-modulo-documentos.md`.

**Agregado:** 2026-07-11 (rama `feat/documentos-empresa`, **PR #5** — sin mergear)

## Concepto

- Cada documento tiene dos descargas: **Original** y **Formato BLU** (render en tiempo real con Spatie Browsershot + Chromium, mismo pipeline que el PDF de presupuesto).
- La versión con formato BLU lleva un **disclaimer** aclarando que el PDF original emitido por el organismo es el único con validez formal.

## Diseño: registry, sin base de datos

- **No usa tablas ni migraciones.** Los documentos se declaran en un registry curado: `mini-saas/backend/config/documentos.php` (clave = slug → `titulo`, `descripcion`, `categoria`, `archivo_original`, `nombre_original`, `vista_formateada`, `nombre_formateado`).
- La página es **dinámica** → agregar un documento nuevo **no requiere tocar frontend, rutas ni permisos**. Solo: subir el PDF a `storage/app/documentos/`, (opcional) crear el blade, y registrar la entrada.

## Backend

- `DocumentoController`: `index` (`GET /api/documentos`, JSON directo, dentro de `auth:sanctum`) + `original` + `formateado`. Ver [[Backend - API]].
- Las dos rutas de **descarga van fuera de `auth:sanctum`** (junto a los PDF de presupuesto), autenticadas con `?token=` (query) + permiso `VER_SECCION_DOCUMENTOS`. Mismo patrón que `PresupuestoController::pdf` — ver [[Modulo Permisos]].
- `PdfService::renderVistaPdf(vista, datos)`: método genérico agregado que renderiza cualquier blade a bytes PDF con la config de Browsershot; `renderPresupuestoPdf` se refactorizó para reusarlo.
- ⚠️ El partial `pdf._logo.blade.php` usa `$config->empresa_nombre` → hay que pasarle `['config' => Configuracion::first()]` al renderizar. Ver [[Errores Comunes]].
- Blades en `resources/views/pdf/documentos/`; originales en `storage/app/documentos/` (se hornean en la imagen vía `COPY . .`, no gitignoreado).

## Frontend

- `pages/documentos/index.vue`: tabla con columnas **Documento / Categoría / Original / Formato BLU**. Descarga con `window.open(url?token=)`. Ver [[Frontend]].
- NavItem "Documentos" (`lucide:file-text`) en el sidebar (Principal) + mapping de ruta en `middleware/auth.global.ts` + permiso `VER_SECCION_DOCUMENTOS` en la pantalla de Usuarios.

## Documentos iniciales (2026-07-11)

| slug | Categoría | Formato BLU |
|------|-----------|-------------|
| `alta-iibb` | Fiscal | Constancia de alta IIBB (AGIP) — 1 pág. |
| `arca-constancia` | Fiscal | Constancia de inscripción (ARCA) — 1 pág. |
| `mercury-bank-letter` | Bancario | Carta de verificación bancaria (inglés) — 1 pág. |
| `mercury-wire-details` | Bancario | Datos wire doméstico + internacional — 2 págs. (`page-break-before`) |
| `constitucion` | Societario | Escritura de constitución SRL — transcripción, 3 págs. |

## Ver también

- [[Backend - API]] — rutas del módulo
- [[Modulo Permisos]] — `VER_SECCION_DOCUMENTOS`
- [[Frontend]] — página y sidebar
- [[Errores Comunes]] — `$config` en el partial del logo
- [[changelog]] · [[memoria]]
