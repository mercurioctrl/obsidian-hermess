# Monitoreo de WANs (host hermess) + config UniFi

**Fecha:** 2026-06-18 · Host `hermess` (`10.10.10.47`), USG-3P. Ver [[Migracion_SQLServer_Dev]] (la DB depende de Telecom) y [[Bily_Skills_Por_Grupo]].

## Topología
- **2 WANs** en el USG: **Telecom (WAN1)** — módem Technicolor en DMZ `192.168.0.1`, IP pública `190.189.93.116` — y **Telecentro (WAN2)** — IP pública `181.45.192.209` (⚠️ cambió a `186.19.68.142` el 2026-08-02, es dinámica).
- **Balanceo:** weighted **90% Telecentro / 10% Telecom** (configurado por API cuando Telecom estaba degradado). El USG balancea **por destino** (hash src+dst): cada destino sale siempre por la misma WAN.
- La regla de port-forward de la DB (`SQL-dev-41433`) quedó en **Telecom (WAN1)**.

## Incidente Telecom (2026-06-18)
Telecom se degradó a **<1 Mbps** (lento pero "up", por eso el failover nativo del USG —que pinguea el módem— no lo detectó). Catriel reportó al ISP y se **recuperó a ~630-690 Mbps** el mismo día. Esto motivó armar el monitoreo custom.

## Incidente Telecentro caída (2026-07/08)
**Telecentro (WAN2) estuvo caída** varios días: en el controlador, `wan2` (eth2/lan2) tenía **IP `0.0.0.0`** con `up=True` (enlace físico OK pero sin dirección del ISP → sin internet por esa vía). El log de eventos (`EVT_GW_WANTransition` eth2) mostró que venía caída desde antes del 2026-07-27 (inicio del log), con dos intentos fallidos de ~45 seg (2026-07-29 20:47 y 2026-08-02 11:22) y **recuperó de verdad el 2026-08-02 17:28** (obtuvo IP `186.19.68.142`). Diagnóstico hecho desde la LAN: con el balanceo por destino, hitear muchas IPs Cloudflare (`curl --resolve` + `/cdn-cgi/trace`) y contar egress: 0/25 salían por Telecentro → confirmaba WAN2 abajo; tras recuperar, ya aparecía egress por `186.19.68.142`.
- ⚠️ **Seed desactualizado:** los scripts `wan-mon` tienen `181.45.192.209` como seed de Telecentro; al cambiar a `186.19.68.142` conviene verificar que `find_ip_for_wan()` se re-adaptó (si no, actualizar el seed).
- **Cómo ver estado por-WAN en el controlador (API):** login `POST /api/login` (user `hermess`), luego `GET /api/s/default/stat/device` → objeto del `UGW3` → claves `wan1`/`wan2` (campos `ip`, `up`, `enable`). `ip=0.0.0.0` = esa WAN sin dirección. Health resumido: `GET /api/s/default/stat/health` (subsystem `wan`/`www`) solo muestra la WAN primaria.

## Monitores (carpeta `~/wan-mon/`)
Avisan por WhatsApp (Bily) al grupo **Infra Blu** (target en `lib.sh`, variable `WHATSAPP`).

| Script | Cron | Qué hace |
|---|---|---|
| `uptime.sh` | `* * * * *` (1 min) | Caídas de ambas WANs. Avisa solo al **cambiar de estado** (up↔down), debounce de 2 ciclos. |
| `speed.sh` | `0 * * * *` (1 h) | Velocidad de ambas WANs, reporte horario. |
| `status.sh` | on-demand | Estado fresco de ambas WANs (lo corre Bily a pedido). |
| `lib.sh` | — | Funciones compartidas. |

**Mecanismo:** como el USG balancea por destino, los scripts pinean (`curl --resolve`) **IPs Cloudflare que salen por la WAN deseada**, verificando con `cf-meta-ip`/`/cdn-cgi/trace` (Telecom=`190.189.93.116`, Telecentro=`181.45.192.209`, ASN Telecom=7303). Si una seed cambia de WAN, `find_ip_for_wan()` re-busca. Velocidad = descarga de `speed.cloudflare.com/__down?bytes=50000000` (50MB; 200MB falla por rate-limit). Caída = ninguna IP sale por esa WAN (failover) o timeouts.

## Lo nativo de UniFi (por qué no alcanza)
- Detección de caída nativa = **ping a la gateway** (en Telecom, el módem en DMZ) → solo confirma que el módem vive, NO el internet. No ve degradación.
- Se activó **`report_wan_event=true`** en ambas WANs (loguea eventos up/down en el controlador → Insights/Events).
- El health-check con target propio (1.1.1.1) NO es configurable sin `config.gateway.json`; no hay SMTP/alertas nativas armadas. Por eso el monitor custom cubre el hueco.

## Pendientes
- Rebalanceo a 50/50 ahora que Telecom volvió (la DB seguiría en Telecom).
- Renovar el USG-3P (EOL) por un gateway nuevo (UXG/UDM) traería monitoreo de WAN nativo decente.

## Ver también
- [[Bily_Skills_Por_Grupo]] — Bily corre `status.sh` on-demand desde el grupo Infra Blu.
- [[Migracion_SQLServer_Dev]] — la DB SQL está accesible por Telecom.
