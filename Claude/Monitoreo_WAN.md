# Monitoreo de WANs (host hermess) + config UniFi

**Fecha:** 2026-06-18 · Host `hermess` (`10.10.10.47`), USG-3P. Ver [[Migracion_SQLServer_Dev]] (la DB depende de Telecom) y [[Bily_Skills_Por_Grupo]].

## Topología
- **2 WANs** en el USG: **Telecom (WAN1)** — módem Technicolor en DMZ `192.168.0.1`, IP pública `190.189.93.116` — y **Telecentro (WAN2)** — IP pública `181.45.192.209`.
- **Balanceo:** weighted **90% Telecentro / 10% Telecom** (configurado por API cuando Telecom estaba degradado). El USG balancea **por destino** (hash src+dst): cada destino sale siempre por la misma WAN.
- La regla de port-forward de la DB (`SQL-dev-41433`) quedó en **Telecom (WAN1)**.

## Incidente Telecom (2026-06-18)
Telecom se degradó a **<1 Mbps** (lento pero "up", por eso el failover nativo del USG —que pinguea el módem— no lo detectó). Catriel reportó al ISP y se **recuperó a ~630-690 Mbps** el mismo día. Esto motivó armar el monitoreo custom.

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
