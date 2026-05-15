# Changelog — microservicio-envios

## 2026-04-20

- **fix:** Validar flag `envioGratis` antes de aplicar cotización gratuita — evitaba que se aplicara gratis sin que corresponda

## 2026-03-17

- **fix:** Optimización de consultas N+1 en generación de etiquetas ZPL de Andreani — se agrupan queries para evitar llamadas repetidas por cada bulto

## 2026-03-12

- **perf:** Llamada a Entregar API una sola vez en generación de etiquetas ZPL — antes se llamaba por cada etiqueta

## 2026-01-28

- **fix:** Validaciones robustas en cotizadores con fallback automático cuando un currier no responde o lanza error

## 2025-10-15

- **refactor:** Cotizador por items activa caso `freeQuote` correctamente

## 2025-10-13

- **fix:** Corrección de estructura de objeto en cotización por pedido

## 2025-10-09 — 2025-10-10

- **fix:** Lógica `freeQuote` en cotizador por pedido: solo se activa cuando corresponde
- **fix:** En recurso por pedido, se asigna gratis al transportista de menor precio

## 2025-08-28

- **refactor:** `AlterShippingBonus` aplica descuentos únicamente a los transportistas especificados (no a todos)

## 2025-08-27

- **refactor:** Implementado `MAX_TOTAL_WEIGHT_MOTO` (sumatoria de bultos) y `MAX_PACKAGES_MOTO` (cantidad máx de paquetes para Moto)

## 2025-08-25 — 2025-08-26

- **refactor:** Implementado `QuotesFieldDetector` para contemplar múltiples estructuras de respuesta de curriers
- **feat:** Sugerencia de envío por zona según código postal (`SHIPPING_SUGGESTION_ENABLED`)
- **refactor:** Se resta costo de envío gratis a las demás opciones al activar bonus

## 2025-07-28

- **feat:** Agregado medio de envío **NbE** (envío acordado) — se retorna según `companyCode`
- **refactor:** Ajuste de decimales en costo/precio/total de Moto y Camioneta
