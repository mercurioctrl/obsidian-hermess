# Changelog

Registro de trabajo reciente en [[Comprobantes]]. Consolida commits de los dos repos.

## 2026-04-22

- chore: generado `CLAUDE.md` en raíz de `/Users/hermess/www/comprobantes/` con guía de ambos sub-repos para Claude Code.
- chore: vinculada bóveda Obsidian (`NB/Comprobantes/`) y sincronizadas notas de [[arquitectura]], [[stack]], [[contexto]].

## 2026-04-15 — API

- `86c6654` — fix: arreglo emisor condición fiscal en voucher.

## 2026-03-16 — API (receipt kits)

- `8e73ae7` / `e4522f5` — Soporte de **kits** en receipts (agrupar productos como kit en la respuesta del voucher). Afecta `ReceiptKitDto` y el flujo en `ReceiptController` → `ReceiptService` → `ReceiptRepository`.

## 2026-03-02 a 2026-03-06 — Facturu UY push a prod

API (`microservicio-comprobantes-v2`):
- `4c3d6a2` — feat: **Facturu NC** (notas de crédito Uruguay).
- `ef1104e` — fix: tipo comprobante.
- `055c93a` — feat: "atar todo para prod" (último wiring antes de release de Facturu).
- `dad3487` — fix: arreglo dirección en DTO.
- `a449c98` / `815cf16` — feat: arreglos sobre DTO de Facturu, cambios en package list.
- `71ba069` / `8c084c3` — fix: header y CAE.

Web app (`servicio-compobante-pdf-web-app`):
- `bd13163` + `5024918` (**LOCAPP-85**) — feat: conectar **packing list** a la API usando recursos de facturación; ajustes en `shipto`.
- `00ea86c` (**LOCAPP-107**) — review: adenda se muestra correctamente.

## 2026-01 a 2026-02 — Kits en comprobantes fiscales

Web app:
- `66fab95` (**LOCAPP-106**) — refactor: remito fiscal muestra kits igual que facturas.
- `12bc634` (**LOCAPP-103**) — refactor: comprobantes fiscales muestran kits.

## 2025-12 a 2026-01 — Certificados eléctricos (QR)

Web app:
- `ce34b88` (**LOCAPP-98**) — certificado hardcodeado (mismo patrón que casos previos).
- `7d43890` / `cd77fd3` (**LOCAPP-96**) — QR descargable y hardcodeo de IDs `102069`, `103319`, `2936`.
- `8bd7b25` — ajustes para certificados.

## Ver también

- [[Comprobantes]]
- [[arquitectura]] (mapeo Nuxt ↔ API)
- [[contexto]] (gotchas)
