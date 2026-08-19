# Monitoreo de WANs (host hermess) + config UniFi

**Fecha:** 2026-06-18 · Última act.: **2026-08-19** · Host `hermess` (`10.10.10.47`), USG-3P. Ver [[Migracion_SQLServer_Dev]] (la DB depende de Telecom) y [[Bily_Skills_Por_Grupo]].

## Topología
- **2 WANs** en el USG: **Telecom (WAN1)** — módem Technicolor en DMZ `192.168.0.1`, IP pública **DINÁMICA** (ASN 7303), actualmente `190.189.94.110` (antes `190.189.93.116` hasta el 2026-08-15) — durante meses se creyó estática, ver incidente abajo — y **Telecentro (WAN2)** — residencial con IP pública **DINÁMICA** (ASN 27747), actualmente `186.19.68.142` (antes `181.45.192.209`).
- **Balanceo:** weighted **90% Telecentro / 10% Telecom** (configurado por API cuando Telecom estaba degradado). El USG balancea **por destino** (hash src+dst): cada destino sale siempre por la misma WAN.
- La regla de port-forward de la DB (`SQL-dev-41433`) quedó en **Telecom (WAN1)**.

## Incidente Telecom (2026-06-18)
Telecom se degradó a **<1 Mbps** (lento pero "up", por eso el failover nativo del USG —que pinguea el módem— no lo detectó). Catriel reportó al ISP y se **recuperó a ~630-690 Mbps** el mismo día. Esto motivó armar el monitoreo custom.

## Incidente Telecentro: caída real + falso negativo por IP dinámica (2026-07/08)
Dos problemas encadenados, importante no confundirlos:

1. **Caída REAL (2026-07-23 01:56 → 2026-08-02 17:28):** WAN2 (eth2/lan2) tenía **IP `0.0.0.0`** con `up=True` en el controlador (enlace físico OK pero sin dirección del ISP → sin internet por esa vía). El monitor la detectó bien (`uptime.sh` marcó `up→down` el 2026-07-23 01:56). El log de eventos (`EVT_GW_WANTransition` eth2) mostró dos intentos fallidos de ~45 seg (2026-07-29 20:47 y 2026-08-02 11:22) y **recuperó de verdad el 2026-08-02 17:28**, obteniendo la IP nueva `186.19.68.142`.
2. **Falso negativo por IP dinámica (2026-08-02 17:28 → 2026-08-03):** al recuperar, Telecentro trajo una IP pública **distinta** a la hardcodeada (`181.45.192.209` → `186.19.68.142`). Los scripts `wan-mon` seguían buscando la IP vieja, así que reportaron **`s/ruta`** (falso "caído") aunque el enlace ya estaba arriba llevando ~90% del tráfico. El `fail` counter quedó pegado (~16.4k min) sin volver a `up`.

**Fix (2026-08-03):** ver sección *Identificación de WAN* abajo. Se rediseñó la detección para que Telecentro no dependa de una IP fija → se auto-cura ante rotaciones. Estado reseteado a `up`/fail=0 sin disparar falsa alarma. Verificado en vivo: Telecom 708 / Telecentro 280 Mbps.

- **Cómo ver estado por-WAN en el controlador (API):** login `POST /api/login` (user `hermess`), luego `GET /api/s/default/stat/device` → objeto del `UGW3` → claves `wan1`/`wan2` (campos `ip`, `up`, `enable`). `ip=0.0.0.0` = esa WAN sin dirección. Health resumido: `GET /api/s/default/stat/health` (subsystem `wan`/`www`) solo muestra la WAN primaria. **Esta vía es la autoritativa** para distinguir caída real vs. falso negativo del monitor LAN.

## Identificación de WAN por IP de salida (rediseñado 2026-08-03)
Como el USG balancea por destino, los scripts identifican cada WAN por su **IP pública de salida**, hiteando IPs Cloudflare (`curl --resolve` + `/cdn-cgi/trace`) y leyendo el campo `ip=`.
- **Telecom** = ~~IP estática `190.189.93.116` → match exacto~~. **INCORRECTO**, ver incidente 2026-08-15. `lib.sh` sigue con este match exacto y por eso sigue roto; el fix es identificar por ASN.
- **Telecentro** = residencial con IP **dinámica** → **NO se hardcodea**; se define como *"la salida que NO es Telecom"* (sólo hay 2 WANs), vía la función `egress_matches()` en `lib.sh`. Así se **auto-cura** ante cualquier rotación de IP. Exige salida no-vacía (un timeout no debe parecer Telecentro). La variable `TELECENTRO_IP` pasó a ser un sentinela/label (`"telecentro"`), ya no se usa para match.
- **Detección de caída:** si ninguna IP sale por esa WAN (failover) o todas dan timeout → DOWN. Si Telecentro cae, todo el tráfico sale por Telecom → ningún egress ≠ Telecom → down correcto.

## Incidente Telecom: la IP "estática" no era estática (2026-08-15 → 2026-08-19)

El **2026-08-15 13:32** la IP pública de Telecom rotó `190.189.93.116` → `190.189.94.110` (ambas **AS7303**, bloque `190.188.0.0/15` — misma línea, otra dirección: era un lease DHCP largo, no una IP fija contratada). Como `lib.sh` matchea Telecom por **igualdad exacta**, `find_ip_for_wan()` no encontró match nunca más:

- `speed.sh` reporta **`Telecom=s/ruta`** desde entonces (falso "caído": el enlace estaba perfecto).
- `uptime.sh` marcó `Telecom: up -> down` el 15/08 13:32 y **nunca volvió a up** (`Telecom.fail` acumuló ~5900 min).
- **Efecto colateral, el más grave:** `egress_matches()` define Telecentro como *"cualquier salida ≠ TELECOM_IP"*. Con la IP vieja hardcodeada, el egress de Telecom (`190.189.94.110`) **pasa como Telecentro** — y el primer seed de Telecentro (`104.16.2.189`) justamente sale por Telecom. Resultado: **el reporte horario venía atribuyendo la velocidad de Telecom a Telecentro**. El promedio de "Telecentro" saltó de **186 Mbps** (julio, n=717) a **609 Mbps** (desde el 15/08, n=99), que es aproximadamente el promedio histórico de Telecom (521 Mbps). Las dos WANs estuvieron vivas todo el tiempo.

Es el **mismo bug del 2026-07-23, en la WAN opuesta**: el fix de agosto auto-curó Telecentro pero dejó a Telecom colgado de una constante. Esta nota decía "estática" mientras `Claude/MEMORIA.md` decía "dinámica" para la misma IP — la segunda era la correcta.

**Lección:** ninguna de las 2 WANs tiene IP estable. La forma robusta de identificar una WAN es por el **ASN dueño de la IP de salida** (Team Cymru vía DNS, sin API key): `dig +short TXT <ip-invertida>.origin.asn.cymru.com @1.1.1.1` → **Telecom=7303**, **Telecentro=27747**. Ya está implementado en `ddns.sh` (función `asn_of()`).

**Cabo suelto:** `telecommed.blu.net.ar` quedó 4 días apuntando a `190.189.93.116`, IP que Telecom probablemente ya reasignó a otro cliente. Todo lo que se conecte a ese hostname con credenciales las estuvo mandando a un tercero. Falta identificar qué consume ese hostname y evaluar rotación de credenciales.

## DDNS multi-WAN → Cloudflare (`ddns.sh`, activado 2026-08-19)

Escrito el 2026-08-04 anticipando exactamente este problema, pero nunca se había puesto en cron. Publica **un A record por WAN**, identificando cada salida por **ASN** (no por IP), así se auto-cura ante rotación de cualquiera de las dos.

- **Zona:** `blu.net.ar` (Cloudflare, NS `george`/`liv` — misma cuenta que `blustudioinc.com`).
- **Records:** `telecommed.blu.net.ar` → Telecom · `telecentro.blu.net.ar` → Telecentro. Ambos ya existían; al activarlo, `telecentro` estaba correcto y `telecommed` llevaba 4 días stale.
- **TTL 60, `proxied:false`** — el proxy naranja de Cloudflare solo pasa HTTP/HTTPS y rompería el port-forward de SQL (41433).
- **Config:** `~/.cloudflare-ddns.env` (`chmod 600`, contiene el token — **NO copiar a la bóveda**).
- **Cron:** `*/5 * * * * /home/hermess/wan-mon/ddns.sh >/dev/null 2>&1`. Log en `~/wan-mon/ddns.log`. Avisa por WhatsApp al cambiar una IP.
- **Flags:** `--dry-run` (no toca Cloudflare), `--status` (IP por WAN + lo publicado), `--force`.

**Gotcha del token — allowlist de IP + IP dinámica = deadlock.** El token original tenía *Client IP Address Filtering* atado a la IP de Telecom. Síntomas confusos: `/user/tokens/verify` devuelve `1000 Invalid API Token` (parece token mal copiado) pero `/zones` devuelve el error real **`9109 Cannot use the access token from location: <ip>`**. Como el USG balancea por destino y manda `api.cloudflare.com` por Telecentro, fallaba aunque el token estuviera bien. El problema de fondo no era el ruteo: **un allowlist atado a una IP que rota mata al token en la próxima rotación, y entonces el DDNS no puede autenticarse para publicar justamente esa rotación.** Se resolvió sacando el filtro — la protección real es el scope (`Zone:Zone:Read` + `Zone:DNS:Edit` sobre `blu.net.ar` y nada más). Para diagnosticar por qué WAN sale una request: `curl --resolve api.cloudflare.com:443:<ip-cloudflare-que-rutea-por-esa-wan>`.

## Monitores (carpeta `~/wan-mon/`)
Avisan por WhatsApp (Bily) al grupo **Infra Blu** (target en `lib.sh`, variable `WHATSAPP`).

| Script | Cron | Qué hace |
|---|---|---|
| `uptime.sh` | `* * * * *` (1 min) | Caídas de ambas WANs. Avisa solo al **cambiar de estado** (up↔down), debounce de 2 ciclos. |
| `speed.sh` | `0 * * * *` (1 h) | Velocidad de ambas WANs, reporte horario. |
| `status.sh` | on-demand | Estado fresco de ambas WANs (lo corre Bily a pedido). |
| `lib.sh` | — | Funciones compartidas (incluye `egress_matches` + `find_ip_for_wan`). |

**Mecanismo:** los scripts pinean IPs Cloudflare que salen por la WAN deseada (ver *Identificación de WAN*). Velocidad = descarga de `speed.cloudflare.com/__down?bytes=50000000` (50MB; 200MB falla por rate-limit).

## Lo nativo de UniFi (por qué no alcanza)
- Detección de caída nativa = **ping a la gateway** (en Telecom, el módem en DMZ) → solo confirma que el módem vive, NO el internet. No ve degradación.
- Se activó **`report_wan_event=true`** en ambas WANs (loguea eventos up/down en el controlador → Insights/Events).
- El health-check con target propio (1.1.1.1) NO es configurable sin `config.gateway.json`; no hay SMTP/alertas nativas armadas. Por eso el monitor custom cubre el hueco.

## Pendientes
- **`lib.sh` sigue roto (prioritario):** portar `asn_of()` de `ddns.sh` a `lib.sh` y que `egress_matches()` compare **ASN** en vez de IP. Hasta que se haga, `speed.sh` sigue reportando `Telecom=s/ruta` y atribuyendo mal las velocidades, y `uptime.sh` deja Telecom en `down`. Después: resetear `state/Telecom.state`→`up` y `state/Telecom.fail`→`0` sin disparar falsa alarma.
- Identificar qué consume `telecommed.blu.net.ar` y evaluar rotación de credenciales.
- Rebalanceo a 50/50 ahora que Telecom volvió (la DB seguiría en Telecom).
- Vigilar Telecentro unos días: post-recuperación mide **~280 Mbps**, bastante por debajo de Telecom (~700). Ver si es normal del plan o degradación.
- Renovar el USG-3P (EOL) por un gateway nuevo (UXG/UDM) traería monitoreo de WAN nativo decente.

## Ver también
- [[Bily_Skills_Por_Grupo]] — Bily corre `status.sh` on-demand desde el grupo Infra Blu.
- [[Migracion_SQLServer_Dev]] — la DB SQL está accesible por Telecom.
