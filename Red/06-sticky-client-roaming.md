# 06 — Sticky client 5GHz + incidente DFS

> **Estado: RESUELTO (2026-08-09).** Ver [[#Resolución definitiva (2026-08-09)]]. El incidente de julio quedó abajo como registro de qué NO hacer.

## Problema inicial

La notebook **"Mac" de Ale** quedaba **pegada al AP Galeria** (de otra planta) en vez de asociarse al AP más cercano. Aparecía con **dos MAC aleatorias** (macOS randomiza MAC e IP):

| Cliente | IP | AP | Banda | Señal | Estado |
|---|---|---|---|---|---|
| `9e:d2:49:38:40:68` | 10.10.10.98 | AP Galeria | 5GHz (ch 161) | **-85 dBm** | 9 roams, pésima |
| `b6:8c:85:6d:31:6a` | 10.10.10.91 | AP Galeria | 5GHz (ch 161) | **-81 dBm** | mala |

## Causa raíz del sticky client

El **Minimum RSSI** (mecanismo que desasocia al cliente con señal débil para forzarlo a reconectar al AP más cercano) estaba activado **solo en 2.4GHz** y **desactivado en 5GHz** en los 3 APs. Como 5GHz atenúa más entre plantas, el cliente se quedaba pegado a un AP lejano a -85 dBm y nada lo obligaba a soltarse.

## ⚠️ Qué salió mal (y por qué NO se debe hacer así)

**Intento fallido:** se activó Min RSSI -75 dBm en 5GHz en los 3 APs. Consecuencias:

1. **`nexus` es solo-5GHz.** Con Min RSSI en 5GHz, un cliente que no cumple el umbral es rechazado, y como `nexus` no tiene 2.4GHz, **se queda sin red** (no hay banda donde caer). → Ale no podía conectar iPhone ni Mac.
2. **El cambio de `radio_table` disparó reprovisionamiento de los APs**, y el VAP de `nexus` en 5GHz **no levantó en Vestidor ni Oficina** (quedó emitiendo solo en Galeria). → El SSID `nexus` "desapareció" para todos; solo se veía `nexus-lot` (2.4GHz).

**Lección:** nunca activar Min RSSI en una banda cuando el SSID es exclusivo de esa banda. Y todo cambio de `radio_table` reprovisiona el AP (corta clientes ~1 min).

## Resolución aplicada

1. **Revertido el Min RSSI de 5GHz** → OFF en los 3 APs (estado original).
2. **Force-provision de Oficina y Vestidor** → reconstruyó el VAP de `nexus` en 5GHz (volvió a emitirse en los 3 APs).
3. **Causa del "no aparece al lado de Oficina": canal DFS.** Oficina tenía autoselección de canal y había caído en **ch104 (DFS)**. En canales DFS el AP hace un chequeo de radar (o se calla si detecta uno) y **no emite beacon** aunque el controlador diga "RUN".
   - **Fijado el 5GHz de Oficina a canal 149 (no-DFS)** y desactivada la optimización automática de canal (`channel_optimization_enabled=false`), para que no vuelva a saltar a un DFS.

## Estado final (verificado)

| AP | 2.4GHz | 5GHz canal | tipo | `nexus` 5G |
|---|---|---|---|---|
| Vestidor | ch6 RUN | **40** | no-DFS | ✅ |
| Galeria | ch11 RUN | **161** | no-DFS | ✅ |
| Oficina | ch1 RUN | **149** (fijado) | no-DFS | ✅ (5 clientes) |

- Min RSSI: **2.4GHz ON (-75), 5GHz OFF** en los 3 (estado original restaurado).
- Canales 5GHz 40 / 149 / 161: no se pisan entre sí.

## Resolución definitiva (2026-08-09)

Se aplicó el plan correcto que había quedado pendiente, **en este orden** (cada paso reprovisiona ~1-2 min; verificar VAPs antes de seguir al siguiente):

1. **Min RSSI -78 dBm en AMBAS bandas** (ng + na) en los 3 APs.
   - 2.4GHz: bajado de -75 → **-78** (las luces WiZ fijas vivían en el borde a -74/-75 y el -75 las podía patear en loop).
   - 5GHz: estaba **OFF** → activado a **-78** (esto es lo que faltaba para soltar al sticky client).
   - Por qué -78 y no -75: patea a los pegados reales (-80/-85) sin molestar a equipos legítimos a ~-75.
2. **Canales 5GHz fijados no-DFS**: Vestidor **40**, Oficina **149**, Galeria **161**. Vestidor venía en **DFS 108** (autoselección lo había vuelto a mover a DFS desde julio). No-DFS evita dropouts por radar y acorta reprovisiones.
3. **`nexus` pasado a doble banda** (`wlan_band` `5g` → `both`). **Este es el paso que hace seguro el Min RSSI de 5GHz**: el cliente pateado del 5GHz lejano ahora cae al **2.4GHz del AP cercano** en vez de quedar sin red (que fue lo que rompió en julio). Band steering (ON) lo vuelve a subir a 5GHz cuando la señal da.

**Verificado (2026-08-09):** `nexus` UP en 2.4GHz **y** 5GHz en los 3 APs. Esta vez el VAP **no** se cayó (a diferencia de julio con -75).

| AP | 2.4GHz | 5GHz canal | Min RSSI (ambas) | nexus 2.4 | nexus 5G |
|---|---|---|---|---|---|
| Vestidor | ch6 | **40** no-DFS | -78 | ✅ UP | ✅ UP |
| Galeria | ch11 | **161** no-DFS | -78 | ✅ UP | ✅ UP |
| Oficina | ch1 | **149** no-DFS | -78 | ✅ UP | ✅ UP |

## Runbook — operar la red UniFi por API

Controlador: `https://10.10.10.7:8443` (self-signed → `curl -sk`). Site: `default`.

```bash
# 1) Login (guarda cookie de sesión)
curl -sk -c /tmp/unifi_cookie.txt -X POST https://10.10.10.7:8443/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"hermess","password":"<clave>"}'

# 2) Leer APs / radios / clientes (todo bajo /api/s/default/)
curl -sk -b /tmp/unifi_cookie.txt https://10.10.10.7:8443/api/s/default/stat/device   # APs: radio_table, radio_table_stats, vap_table, uplink
curl -sk -b /tmp/unifi_cookie.txt https://10.10.10.7:8443/api/s/default/stat/sta       # clientes: rssi, signal(dBm), ap_mac, radio_proto, channel
curl -sk -b /tmp/unifi_cookie.txt https://10.10.10.7:8443/api/s/default/list/wlanconf  # SSIDs: wlan_band, bss_transition(11v), fast_roaming(11r), band steering

# 3) Cambiar Min RSSI o canal de un AP → PUT del radio_table completo
#    (leer device, modificar radio_table[].min_rssi/min_rssi_enabled/channel, re-PUT)
curl -sk -b /tmp/unifi_cookie.txt -X PUT https://10.10.10.7:8443/api/s/default/rest/device/{_id} \
  -H "Content-Type: application/json" -d '{"radio_table":[...]}'

# 4) Cambiar banda de un SSID → PUT wlanconf
curl -sk -b /tmp/unifi_cookie.txt -X PUT https://10.10.10.7:8443/api/s/default/rest/wlanconf/{_id} \
  -H "Content-Type: application/json" -d '{"wlan_band":"both"}'
```

**Interpretación de valores:** `signal` es el dBm real (-85 = pésimo, -50 = excelente); `rssi` en `stat/sta` es señal sobre ruido (~signal+96). Radio `ng`=2.4GHz, `na`=5GHz. Canales DFS 5GHz = 52–144; no-DFS = 36/40/44/48 y 149/153/157/161/165.

**Reglas de oro (aprendidas a los golpes):**
- ⚠️ **Nunca** activar Min RSSI en una banda si el SSID es exclusivo de esa banda → el cliente pateado se queda sin red. Pasar el SSID a doble banda primero.
- Todo PUT a `radio_table` **o** `wlanconf` **reprovisiona** el AP (corta ~1-2 min). Aplicar de a un cambio y **verificar `vap_table`** que los SSID vuelvan antes de seguir.
- Canales DFS pueden no emitir beacon (chequeo de radar) → fijar no-DFS y `channel_optimization` off para que la autoselección no los vuelva a mover.
- macOS/iOS usan MAC/IP aleatoria → buscar por **nombre**, no por MAC.

## Ajustes finos pendientes (opcionales, no urgentes)

- Bajar **TX de 5GHz de Galeria** (~22 dBm, la más alta) para que no "grite" a otras plantas y las celdas sean más chicas (mejor roaming).
- **Vestidor 5GHz** tenía TX bajo (14 dBm) — evaluar subir para mejor cobertura de esa zona.
- Si en algún punto muerto real hay cortes con -78, aflojar ese AP puntual a **-80**.

## Notas

- **macOS/iOS usan MAC aleatoria** → el mismo equipo aparece con varias MAC/IP. Buscarlo por **nombre "Mac"** o por IP, no por MAC fija.
- Todo cambio de `radio_table` vía API (`PUT /rest/device/{_id}`) reprovisiona el AP. Verificar siempre después que los VAPs volvieron a levantar.

## Ver también

- [[01-cambios-2025-05]] — activación original de Min RSSI (solo 2.4GHz, mayo 2025)
- [[Red]] — índice de la red
