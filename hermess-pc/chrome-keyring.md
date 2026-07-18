# Chrome — deslogueo masivo por keyring roto

Chrome deslogueaba de todos los sitios a la vez (Google, GitHub, X) de forma intermitente, casi a diario, sin cerrar el navegador. Diagnosticado y arreglado el 2026-07-17.

---

## Síntoma

- Sesiones de múltiples sitios (X, GitHub, Google) se cerraban solas, **todas a la vez**.
- Pasaba casi todos los días, sin cerrar el navegador.
- No era un sitio puntual: caían cuentas independientes al mismo minuto.

## Qué se descartó (con evidencia)

- **Hackeo / cuenta comprometida** — cuentas independientes no se cierran todas juntas al mismo minuto.
- **Limpiadores / cron / políticas** de Chrome — no existen (sin BleachBit, sin cron, sin managed policies).
- **Borrado de cookies del disco** — las cookies siguen ahí, persistentes y cifradas `v11` (la de GitHub expira 2027).
- **VPN** (Nord/Surfshark) — sin proxy activo, IP real del ISP (Telecom AR).

## Causa raíz

Keyring de GNOME en estado roto:

- `~/.local/share/keyrings/default.keyring` **corrupto** → `journalctl`: `keyring was in an invalid or unrecognized format`.
- **No existía** el archivo puntero `~/.local/share/keyrings/default` que nombra la colección por defecto.
- La llave `Chrome Safe Storage` vive en `login.keyring` (OK, desde 2025-04-29), pero con la colección default rota + Chrome crasheando (`exit_type: Crashed`), en cada reinicio Chrome **a veces no obtenía la llave a tiempo** → no podía desencriptar ninguna cookie `v11` → **logout masivo**. Es intermitente porque es una condición de carrera.

## Fix aplicado (2026-07-17)

```bash
# 1. Backup
cp -a ~/.local/share/keyrings ~/keyrings-backup-20260717-145137
# 2. Apuntar la colección default al llavero login (se desbloquea con el login via PAM)
printf 'login' > ~/.local/share/keyrings/default
chmod 600 ~/.local/share/keyrings/default
# 3. Eliminar el default.keyring corrupto (ya respaldado)
rm -f ~/.local/share/keyrings/default.keyring ~/.local/share/keyrings/default.keyring~
```

Las cookies **NO se pierden** (la llave `Chrome Safe Storage` no cambió). Toma efecto tras **cerrar sesión y volver a entrar** (o reiniciar), para que `gnome-keyring-daemon` arranque limpio.

Restaurar si algo sale mal:

```bash
rm -rf ~/.local/share/keyrings && cp -a ~/keyrings-backup-20260717-145137 ~/.local/share/keyrings
```

## Cómo verificar si reaparece

```bash
journalctl -b | grep "invalid or unrecognized format"          # debería dar 0
secret-tool search --all application chrome                     # una sola 'Chrome Safe Storage'
# versión de cifrado de cookies: v11 = keyring OK, v10 = fallback sin keyring
sqlite3 ~/.config/google-chrome/Default/Cookies \
  "SELECT substr(encrypted_value,1,3), count(*) FROM cookies GROUP BY 1;"
```

## Pendiente / secundario

- Investigar por qué **Chrome crashea** (`exit_type: Crashed`) — es el disparador que gatilla la carrera. Puede ser GPU o una extensión. Con el keyring arreglado ya no desloguea aunque crashee.
- Extensiones activas que leen cookies y conviene revisar/quitar si no se usan: **Awesome Screen Recorder**, **uTab**.

## Ver también

- [[hermess-pc/earlyoom|earlyoom]] — presión de RAM en este equipo (Chrome es memory-heavy)
- [[hermess-pc/memoria|Memoria de Claude]]
- [[hermess-pc/hermess-pc|Índice hermess-pc]]
