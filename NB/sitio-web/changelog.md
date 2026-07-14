# Changelog

Ver índice: [[sitio-web]]

## 2026-07-14

- **infra:** Actualizados ambos repos a sus ramas de desarrollo. API `Development` avanzó 34 commits (→ `ccc2053`); frontend `development` (→ `f4889d8`). Cambios locales de infra (`predis` en composer, `ecosystem.config.js` PM2) preservados con stash/pop.
- **fix (hotfix PR #658):** Corregido bug donde **todos los productos devolvían acelerador 10**. `ProductoRepository::getAcelerator()` matcheaba solo por `cDetalle LIKE txtMatch` e ignoraba `marcaId`/`familiaId`. Los aceleradores por marca (RAZER/GENIUS/GX GAMING x10) tienen `txtMatch NULL` y en SQL Server `CONCAT('%',NULL,'%') = '%%'` → matcheaban todo. Ahora el JOIN evalúa los 3 criterios como AND, tratando cada NULL como comodín. Ver detalle en [[contexto]].
  - Rama `hotfix-acelerador-filtro-marca-familia` → merge a `Development` (commit `dc801d7`).
  - Archivo: `app/src/Repository/ProductoRepository.php`
