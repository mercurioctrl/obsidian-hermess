# Contexto — microservicio-envios

## Reglas de negocio

### Cotización
- El precio final se ajusta dentro de un rango (`MIN_QUOTE_LIMIT` / `MAX_QUOTE_LIMIT` en `.env`)
- Existe un precio mínimo de envío configurable (`MIN_PRICE`)
- El bonus de envío se aplica selectivamente: solo a los transportistas especificados (no a todos)
- La lógica de envío gratis (`envioGratis`) se valida con un flag antes de aplicar la cotización gratuita

### Transportistas internos — límites físicos

| Transportista | Variable env | Límite |
|---|---|---|
| Moto | `MAX_WEIGHT_MOTO` | Peso máximo por bulto |
| Moto | `MAX_TOTAL_WEIGHT_MOTO` | Peso total máximo (suma de bultos) |
| Moto | `MAX_PACKAGES_MOTO` | Cantidad máxima de paquetes |
| Moto | `MAX_DIMENSIONS_MOTO` | Dimensión máxima |
| Miniflete | `MAX_WEIGHT_MINIFLETE` / `MIN_WEIGHT_MINIFLETE` | Rango de peso |
| Miniflete | `MAX_DIMENSIONS_MINIFLETE` / `MIN_DIMENSIONS_MINIFLETE` | Rango de dimensiones |

### NbE (envío acordado)
- Se retorna únicamente si corresponde por `companyCode`
- Fue agregado en julio 2025

### Entregar (zona)
- La lógica de zona puede desactivarse con `ENTREGAR_ZONE_ENABLED`
- Las etiquetas ZPL se generan llamando a la API de Entregar una sola vez (optimización 2026-03-12)

### Sugerencia de envío
- Se sugiere el mejor envío según código postal cotizado (feature flag: `SHIPPING_SUGGESTION_ENABLED`)

## Feature flags (`.env`)

| Flag | Efecto |
|---|---|
| `SHIPPING_BONUS_ENABLED=true` | Activa bonificación en cotizaciones |
| `SHIPPING_SUGGESTION_ENABLED=true` | Activa sugerencia del mejor envío por zona |
| `ENTREGAR_ZONE_ENABLED` | Activa lógica de zonas para Entregar |
| `DEBUG=1` | Modo debug |

## Dos bases de datos

El microservicio mantiene dos conexiones simultáneas:
- **MSSQL**: contiene los datos del negocio (items, pedidos, carritos, paquetes) — alimentado por el sistema central de NB
- **MariaDB**: contiene datos propios del microservicio (métodos de envío, usuarios JWT, tokens)

Esta separación implica que los endpoints legacy (cotización por item/pedido/carrito) consultan MSSQL, mientras los endpoints de gestión (login, shipping, bulk) usan MariaDB.

## Ver también

- [[microservicio-envios]] · [[arquitectura]] · [[stack]] · [[changelog]]
