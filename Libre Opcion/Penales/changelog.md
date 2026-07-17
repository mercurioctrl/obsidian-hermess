# Changelog — Penales

## 2026-07-17

- **fix(API): consumir el token solo tras guardar con éxito.** El token se consumía en la validación, antes del chequeo de nombre repetido; un rechazo por nombre en uso (409) lo quemaba y el reintento con otro nombre daba "Token ya utilizado" (obligaba a rejugar). Se separó `validarYConsumir()` en `validar()` + `consumir()`; el controller consume recién tras `registrarResultado()` OK.
  - Rama `fix-penales-token-consume` (base `origin/fix-penales`), commit `482735f1`. PRs **#706 → Gamma**, **#707 → Development**.
  - Verificado sin escribir en DB: 2 envíos con mismo token y firma inválida → el 2do sigue rechazando por firma (token no se quema).

Archivos: `app/app/Service/Penales/PenalesTokenService.php`, `app/app/Http/Controllers/Penales/PenalesScoreStoreController.php`

## 2026-07-15

- **feat(API): dedup por email y nombre en el ranking.** Email = identidad (una mejor marca por email); nombre repetido de otro email → 409 "Ese nombre ya está en uso"; mismo email → upsert quedándose con la mejor marca.
  - Rama `fix-penales`, commit `336d65a9`, mergeada a **Gamma** (PR #704).
- **Experimentos de fondo descartados.** `fondov2.png` y `bannerv3.png` como fondo desktop: no ajustan al layout del juego (arco de otra proporción/posición). Revertidos. Ver [[contexto]].

## 2026-07-11

- **feat(front): barra de potencia progresiva + cronómetro + sprite.** La barra se acelera por penal (1100→580 ms; step 130, piso 480). Cronómetro en pantalla que se congela al terminar y coincide con el tiempo enviado al ranking. Sprite del arquero actualizado.
  - Commit `14c220916` en `test-penales-mundial`.
- **Setup de la feature (fixes de arranque):**
  - Creada la tabla `[LO].[dbo].[penales_ranking]` en SQL Server (no existía → "score no se pudo guardar").
  - Agregados al `.env` del front: `HOME_PENALES_GAME=1` (el banner no cargaba) y `PENALES_FIRMA_KEY=peñales-2025-x7k9` (sin la clave, el front no firmaba → error al guardar).
