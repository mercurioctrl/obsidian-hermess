# Monitoreo de WANs (host hermess) + config UniFi

**Fecha:** 2026-06-18 · Última act.: **2026-08-03** · Host `hermess` (`10.10.10.47`), USG-3P. Ver [[Migracion_SQLServer_Dev]] (la DB depende de Telecom) y [[Bily_Skills_Por_Grupo]].

## Topología
- **2 WANs** en el USG: **Telecom (WAN1)** — módem Technicolor en DMZ `192.168.0.1`, IP pública **estática** `190.189.93.116` (ASN 7303) — y **Telecentro (WAN2)** — residencial con IP pública **DINÁMICA** (ASN 27747), actualmente `186.19.68.142` (antes `181.45.192.209`).
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
- **Telecom** = IP **estática** `190.189.93.116` → match exacto.
- **Telecentro** = residencial con IP **dinámica** → **NO se hardcodea**; se define como *"la salida que NO es Telecom"* (sólo hay 2 WANs), vía la función `egress_matches()` en `lib.sh`. Así se **auto-cura** ante cualquier rotación de IP. Exige salida no-vacía (un timeout no debe parecer Telecentro). La variable `TELECENTRO_IP` pasó a ser un sentinela/label (`"telecentro"`), ya no se usa para match.
- **Detección de caída:** si ninguna IP sale por esa WAN (failover) o todas dan timeout → DOWN. Si Telecentro cae, todo el tráfico sale por Telecom → ningún egress ≠ Telecom → down correcto.

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
- Rebalanceo a 50/50 ahora que Telecom volvió (la DB seguiría en Telecom).
- Vigilar Telecentro unos días: post-recuperación mide **~280 Mbps**, bastante por debajo de Telecom (~700). Ver si es normal del plan o degradación.
- Renovar el USG-3P (EOL) por un gateway nuevo (UXG/UDM) traería monitoreo de WAN nativo decente.

## Ver también
- [[Bily_Skills_Por_Grupo]] — Bily corre `status.sh` on-demand desde el grupo Infra Blu.
- [[Migracion_SQLServer_Dev]] — la DB SQL está accesible por Telecom.
