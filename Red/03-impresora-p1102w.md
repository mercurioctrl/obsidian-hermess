# 03 — Impresora HP LaserJet Professional P1102w

Impresora láser WiFi. Es un modelo **host-based** (2011): solo entiende **ZjStream**, no PostScript ni PCL estándar, y es **solo 2.4 GHz (b/g)**. Requiere driver propietario para funcionar en Linux.

## Configuración final (funcionando)

| Componente | Valor |
|---|---|
| Cola CUPS | `HP_LaserJet_Professional_P_1102w` (en hermess-desktop) |
| Driver | `hpcups 3.23.12` + **plugin propietario HPLIP** instalado |
| PPD | `hplip:0/ppd/hplip/HP/hp-laserjet_professional_p1102w.ppd` |
| Backend | `hp:/net/HP_LaserJet_Professional_P_1102w?ip=10.10.10.189` |
| IP | **10.10.10.189** (reserva DHCP fija) |
| MAC | `70:18:8b:a1:d6:3b` |
| SSID | **`nexus-printers`** (2.4 GHz, WPA2-AES) — ver [[Red#Redes (SSIDs / VLANs)]] |
| Web admin (EWS) | http://10.10.10.189 → Networking → Wireless |

Verificación del plugin: `cat /var/lib/hp/hplip.state` → `installed = 1`, `lj.so` en `/usr/share/hplip/prnt/plugins/`.

---

## Sesión de diagnóstico (2026-07-12)

**Síntoma:** se enviaban impresiones pero no salían.

**Diagnóstico — una causa real y varias pistas falsas:**

1. **Cola pausada, transporte IPP roto** (`stop printer`, `cups-ipp-conformance-failure`). → Cambié el backend de `ipp://…:631` a `socket://…:9100`. *Síntoma, no causa.*
2. **WiFi caía bajo carga** (LED azul titilando, `broken pipe`). La señal en UniFi era en realidad **perfecta** (−36 dBm, satisfaction 100, ping 60s sin pérdida). El SSID principal `nexus-lot` tenía **BSS Transition (802.11v)** activo, que voltea a clientes viejos. → Creé SSID IoT dedicado **`nexus-printers`** (clonado de `nexus-lot` con 11v / 11r / PMF / band-steering **OFF**) + reserva DHCP fija. *Contribuía, no era el fondo.*
3. **CAUSA RAÍZ — driver equivocado:** la cola estaba configurada como **IPP Everywhere / URF** (formato AirPrint). La P1102w **no soporta IPP Everywhere ni URF**, así que recibía datos que no entendía y cortaba la conexión (`broken pipe` por socket, `stop printer` por IPP). → Instalé el **plugin propietario HPLIP 3.23.12** (desde OpenPrinting) y reconfiguré la cola con el driver **hpcups**. ✅

**Resultado:** página de prueba salió limpia, sin errores ni broken pipe.

> Nota: el SSID dedicado `nexus-printers` es el mismo patrón propuesto para la [[02-camaras#Cámara Ezviz (exterior)|Ezviz]] (`nexus-cam`): un SSID por dispositivo problemático en vez de pinear a un AP.

---

## Si deja de imprimir — checklist

1. `lpstat -p HP_LaserJet_Professional_P_1102w` → ¿pausada? → `cupsenable …`
2. Driver correcto: `grep NickName /etc/cups/ppd/HP_LaserJet_Professional_P_1102w.ppd` debe decir **hpcups**, NO "IPP Everywhere".
3. Plugin presente: `cat /var/lib/hp/hplip.state` → `installed = 1`.
4. Red: el **LED azul debe quedar fijo** (titilando = wifi inestable); `ping 10.10.10.189`.

## Ver también

- [[Red]] — índice de la red hogareña
- [[02-camaras]] — mismo patrón de SSID dedicado para la Ezviz
