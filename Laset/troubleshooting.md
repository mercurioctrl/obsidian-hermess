# Troubleshooting

Ver también: [[Laset]] · [[operaciones]] · [[arquitectura]]
Versión completa en el repo: `/var/www/laset/docs/troubleshooting.md`.

## Back
- **500 `Adaptive Server is unavailable (172.31.10.208)`** → DB del backup es de otra red (VPC AWS),
  sin ruta. Usar `db-nb-massql-dev.blu.net.ar,4444` (user `cmercurio`) en los `.env`.
- **500 Laravel `valid cache path` / `vendor/autoload.php not found`** → falta `vendor/` y/o `storage/`
  (ambos gitignoreados). Ver [[operaciones]].
- **composer: "affected by security advisories"** → `--no-security-blocking`.
- **composer: `ext-gd`/`ext-zip` (cobros)** → `--ignore-platform-reqs`.
- **`Unable to read environment file`** → `.env` en 600, `chmod 644`.
- **`all predefined address pools have been fully subnetted`** → usar `laset-net` compartida; no red por app; no `prune`.
- **`container name already in use` / puerto ocupado** → falta sufijo `-laset` / puerto 81xx-39xx.
- **`docker compose up --build` falla en `pecl install sqlsrv`** → no buildear; usar imagen `*-laset` (`image:`).

## Front
- **`npm install` falla en `canvas`/node-pre-gyp** (comprobante-pdf) → `--ignore-scripts`.
- **build falla `ERR_OSSL_EVP_UNSUPPORTED`** → `NODE_OPTIONS=--openssl-legacy-provider`.
- **`pm2 start: Script not found nuxt.js`** → install no dejó `nuxt`, reinstalar con `--ignore-scripts`.
- **`ERESOLVE`** → `--legacy-peer-deps`.
- **Host sin RAM al levantar fronts** → bajar `instances` a `2` (no `'max'`).
