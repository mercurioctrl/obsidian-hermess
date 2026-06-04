# Contexto — BluPartPicker

## Por qué existe

Proyecto propio para consolidar catálogos de distribuidores mayoristas de tecnología argentina en una sola API. Permite comparar precios, stock e imágenes entre distribuidores sin tener que entrar a cada portal por separado.

## Distribuidores integrados

- **Invid Computers** — distribuidor mayorista de IT, catálogo vía Excel autenticado
- **Ceven** — distribuidor mayorista, plataforma NetSuite SCA protegida por Akamai → requiere Playwright
- **Stylus S.A.** — distribuidor mayorista, listas de precios por marca en TSV

## Casos de uso

- Buscar el precio más bajo de un producto entre distribuidores
- Ver historial de variación de precios y stock
- Consultar desde otras apps vía API REST
- Base para futuros desarrollos (comparadores, alertas de precio, etc.)

## Decisiones de diseño

- **SQLite** en vez de Postgres: suficiente para el volumen (~2.500 productos), sin overhead de servidor
- **Un solo archivo DB** (`invid.db`) aunque el nombre sea de Invid — herencia del primer sync
- **source + codigo** como clave compuesta: permite múltiples distribuidores con el mismo código de producto
- **price_stock_history**: registra snapshots solo cuando hay cambios, no en cada sync
- **Playwright solo para Ceven**: los otros distribuidores no tienen bot protection

## Estado actual (jun 2026)

- 3 distribuidores activos · ~2.565 productos · ~2.448 en stock
- API pública en red local 10.10.10.7:4444
- Syncs automáticos cada 4h, desfasados entre sí para no sobrecargar

---

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[arquitectura]] — decisiones técnicas detalladas
- [[changelog]] — historial de lo implementado
- [[memoria]] — próximos pasos posibles
