#!/usr/bin/env python3
"""
Diagnóstico rápido de la red UniFi hogareña (nexus).
Login por API, imprime APs (radios, canal, TX, Min RSSI) y clientes wifi
ordenados por señal (para cazar sticky clients con señal baja).

Uso:  UNIFI_PASS='...' python3 unifi_diag.py
      (o edita CLAVE abajo)

Doc: ver Red/06-sticky-client-roaming.md (runbook + reglas de oro).
NO hace cambios, solo lectura.
"""
import os, ssl, json, urllib.request, http.cookiejar

CTRL = "https://10.10.10.7:8443"
USER = "hermess"
CLAVE = os.environ.get("UNIFI_PASS", "")  # exportar UNIFI_PASS o pegar aquí

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(
    urllib.request.HTTPSHandler(context=ctx),
    urllib.request.HTTPCookieProcessor(cj))


def call(path, data=None, method=None):
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(CTRL + path, data=body, method=method,
                                 headers={"Content-Type": "application/json"})
    return json.load(opener.open(req, timeout=20))["data"]


call("/api/login", {"username": USER, "password": CLAVE})
dev = call("/api/s/default/stat/device")
sta = call("/api/s/default/stat/sta")

aps = {}
print("===== APs =====")
for a in dev:
    if a.get("type") != "uap":
        continue
    aps[a.get("mac")] = a.get("name")
    print(f"\n{a.get('name')}  ip={a.get('ip')}  uplink={a.get('uplink',{}).get('type')}  clientes={a.get('num_sta')}")
    stats = {r.get("radio"): r for r in a.get("radio_table_stats", [])}
    for rc in a.get("radio_table", []):
        band = "2.4GHz" if rc.get("radio") == "ng" else "5GHz "
        st = stats.get(rc.get("radio"), {})
        mr = f"-{abs(rc.get('min_rssi'))}" if rc.get("min_rssi_enabled") else "OFF"
        print(f"  {band}: ch={st.get('channel')} TX={st.get('tx_power')}dBm util={st.get('cu_total','?')}% sta={st.get('num_sta')} MinRSSI={mr}")

print("\n===== Clientes wifi (peor señal primero) =====")
w = [s for s in sta if not s.get("is_wired", True)]
w.sort(key=lambda s: s.get("signal", 0))
for s in w:
    name = (s.get("name") or s.get("hostname") or s.get("mac"))[:26]
    ap = str(aps.get(s.get("ap_mac"), s.get("ap_mac")))[:14]
    tag = "  <-- STICKY?" if s.get("signal", 0) <= -75 else ""
    print(f"  {name:26} AP={ap:14} {s.get('signal')}dBm {s.get('radio_proto')} ch={s.get('channel')}{tag}")
print(f"\nTotal wifi: {len(w)}  |  <= -75 dBm (candidatos sticky): {sum(1 for s in w if s.get('signal',0)<=-75)}")
