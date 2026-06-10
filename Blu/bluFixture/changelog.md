# Changelog — bluFixture

## 2026-06-08

### Features completados en esta sesión

**Información de estadios por partido**
- Nueva tabla `estadios` (0010) con 16 venues oficiales FIFA 2026: nombre, ciudad, emoji, capacidad, año inauguración, dato curioso
- FK `estadio_id` en `partidos` (0011)
- `EstadiosSeeder` + `AsignarEstadiosSeeder` (idempotentes) — 57/72 partidos asignados
- Portal participante: card de estadio visible en cada partido (`portal/partidos.vue`)
- Panel empresa: fixture con dropdown de estadio agrupado por país (`empresa/fixture.vue`)

**Registro por link (auto-inscripción)**
- Migración 0012: `registro_token` (varchar 64, unique) + `registro_abierto` (bool) en empresas
- `RegistroPublicoController`: endpoints `GET /publica/registro/{token}` (info) y `POST` (registrar)
- `EmpresaController`: métodos `abrirRegistro`, `cerrarRegistro`, `regenerarToken`
- Frontend: `pages/registro/[token].vue` — formulario con branding de empresa, auto-login al registrarse
- Panel empresa: sección "Registro por link" en participantes (toggle abrir/cerrar, URL copiable, regenerar)

**Deploy en servidor nuevo**
- `start.sh` reescrito: genera APP_KEY + DB passwords automáticamente, poll de health check, verifica datos post-seed
- `docker-entrypoint.sh`: migra + seedea en cada arranque (idempotente)

**Branding**
- Componente `PoweredByBlu.vue` — link a blustudioinc.com con logo `/blu_logo.png`
- Presente en todos los layouts (sidebar, abajo) y páginas sin layout (login, slug, registro)

**Documentación**
- `README.md` completo con arquitectura, API reference, comandos Docker y patrones
- Notas Obsidian sincronizadas: arquitectura, stack, api, contexto, changelog

### Fixes anteriores (sesiones previas)

- Sanctum 401 para Participante: removido `'provider'` del guard sanctum en `config/auth.php`
- `[slug].vue` build error: faltaba `</div>` en contenedor de logos
- `AsignarEstadiosSeeder` syntax error: comillas curvas en interpolación PHP
- `start.sh` macOS/Linux: compatibilidad `sed` con check `sed --version`
- `APP_KEY` en start.sh: agregar prefijo `base64:` al valor generado con openssl

---

## Sesiones anteriores

### Import/export XLSX de participantes
- PhpSpreadsheet instalado con `--ignore-platform-req=ext-gd`
- `ParticipanteController`: `exportar()` + `importar()` — genera passwords automáticos si faltan
- Frontend: botones exportar/importar + modal de resultado + modal de password generado

### Crop de logo con canvas
- Editor pan/zoom en upload de logo: mousedown/move, scroll hacia cursor, pinch-zoom touch
- `clampCrop()` evita bordes blancos, `exportCrop()` produce 400×400px
- Componente `EmpresaLogo` para mostrar logo con fondo color o transparente

### Login branded por empresa
- Ruta dinámica `/{slug}` → `pages/[slug].vue` con branding de la empresa
- `GET /publica/empresa/{slug}` sin autenticación

### Sistema de puntos y premios
- Puntos configurables por empresa (pts_exacto, pts_resultado)
- Premios 🥇🥈🥉 en sidebar del portal
- Leyenda de puntos en sidebar

### Social (comentarios + contrincantes)
- Comentarios por partido filtrados por empresa
- `portal/contrincantes/` — lista + perfil individual con pronósticos

