# Changelog — inventario

## 2026-05-05

### Backend (ms-metadata)
- **hotfix**: Arreglo stock en kits (PR #263)

## 2026-04-16

### Backend (ms-metadata)
- fix: corrección en módulo de brands

## 2026-04-15

### Backend (ms-metadata)
- fix: arreglo stock syncup (sincronización de stock)

## 2026-04-29

### Frontend (inventario-web-app)
- **SNB-3913**: Cambio en la visualización de banderas en PED, INV y COM (PR #370)

## 2026-04-15

### Frontend (inventario-web-app)
- **INV-346**: Fix paginado incorrecto en pestaña de kits (PR #368)
- **INV-345**: Altura máxima en contenedor de tabla de stock para evitar scroll doble del body (PR #366)

## 2026-03-18

### Backend (ms-metadata)
- fix: corrección listado de productos
- fix: arreglo paginación en products

### Frontend (inventario-web-app)
- Refactor paginado en kits: alineado a derecha, sin scroll doble
- Refactor utilidades de control de precio: texto en shadow para campos editados, quitada línea vertical que dificultaba la vista

## 2026-03-02

### Frontend (inventario-web-app)
- **INV-343**: Al crear una categoría, se puede enviar `companyCode` (PR #362)
- **INV-342**: Al crear una marca, se puede enviar `companyCode` (PR #360)

## 2026-02-18 – 2026-02-20

### Backend (ms-metadata) — INV-BundleCostUtility
- feat: agregar costos al bundle (PR #255, #257, #259, #261)
- feat: precio por utilidad para productos individuales (INV-338)
- feat: objeto `prices` dentro del inventario de productos (INV-335, PR #252, #253)
- fix: cálculo de ganancia estipulada y precio en bundles
- fix: `ncosteprom` (costo promedio) en bundles

## Ver también

- [[inventario]] · [[arquitectura]] · [[contexto]]
