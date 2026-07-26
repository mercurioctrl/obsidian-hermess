# 04 — DVR Dahua HCVR

Grabador de video principal del hogar. **No confundir** con el NVR Hikvision (kit wifi, otra IP) — este es un equipo aparte.

## Datos

- **Modelo:** Dahua **DHI-HCVR4116HS-S3** (OEM "浩云"/HaoYun, build 2016)
- **IP:** `10.10.10.101`
- **Tipo:** híbrido — **CH1–4 analógicas (BNC)** + **CH5–18 IP** (hasta 14 IP, soporta AnalogToDigital)
- **Usuario:** `herrmess87` (con doble r) · pass en gestor de contraseñas
- **Serial:** 2E04EB2PAMPHGU2

## Acceso / operación por API (Dahua RPC2)

La web UI (`http://10.10.10.101`) necesita **plugin ActiveX** (IE/Windows). Pero se opera por consola con la **API RPC2** (JSON sobre HTTP) — sin plugin. Cliente de referencia en `/tmp/dahua*.py` (host hermess-desktop).

**Login:** POST `/RPC2_Login` `global.login` (devuelve `realm`/`random`) → `hash = MD5(user:realm:pass).upper()`, `final = MD5(user:random:hash).upper()` → segundo `global.login` con `authorityType/passwordType: "Default"`. Después, RPC en `/RPC2` con cookie `DhWebClientSessionID=<session>`.

> ⚠️ Limita re-logins seguidos (error *"login challenge"*). Usar **una sola sesión** por corrida.

**RPC útiles:**
- `LogicDeviceManager.getCameraAll` / `getCameraState {"uniqueChannels":[-1]}` — cámaras y estado por canal (base-0)
- `configManager.getConfig` / `setConfig` `{"name":"ChannelTitle"}` (nombres) / `{"name":"RemoteDevice"}` (cámaras IP)
- Snapshot: `GET /cgi-bin/snapshot.cgi?channel=N` (auth digest)
- **Mover cámara IP de canal:** editar la tabla `RemoteDevice` (slots `uuid:System_CONFIG_NETCAMERA_INFO_N`, N = canal base-0), mandar la tabla completa por `setConfig`.

## Mapeo de canales (tras reordenar, 2026-07-26)

| Canal | Tipo | Cámara | Nombre DVR |
|---|---|---|---|
| CH1–4 | Analógica | 4 analógicas | FRENTE DER / FRENE IZQ ⚠️(typo) / NEGOCIO / CAM 4 |
| CH5 | IP | Dahua `10.10.10.216` | JARDIN |
| CH6 | IP | Portero VTO `10.10.10.102` | PORTERO |
| CH7 | IP | Hik `10.10.10.192` (PASILLO-C) | PUERTA |
| CH8 | IP | Hik ColorVu `10.10.10.65` | Camera 01 |
| **CH9** | IP | **PTZ `10.10.10.64`** ([[02-camaras#Cámara PUERTA PTZ — DS-2CV1F23G2-LIDWF\|PUERTA PTZ]]) | CAM 9 |
| CH10–18 | — | vacíos | — |

## Sesión de reordenamiento (2026-07-26)

**Problema:** al abrir la app (DMSS) o el DVR aparecían canales negros en el medio. Las 8 cámaras (CH1–8) estaban consecutivas, pero la **PTZ había quedado suelta en CH11** con CH9–10 vacíos.

**Solución:** como la PTZ es IP y los CH5–18 son IP-capaces, se **movió la PTZ de CH11 → CH9** por software (editando `RemoteDevice`, sin tocar cables ni reiniciar). Resultado: **CH1–9 consecutivas**. Verificado con snapshot real de CH9.

- Backup de `RemoteDevice` previo: `/tmp/nvr_remotedevice_backup.json`.
- Grabaciones viejas de la PTZ quedan bajo CH11; las nuevas van a CH9.
- Pendiente opcional: renombrar CH9 "CAM 9" → "PUERTA PTZ".

## Ver también

- [[02-camaras]] — Inventario de cámaras IP
- [[Red]] — Infraestructura de red hogareña
