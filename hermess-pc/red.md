# Red — UniFi dual WAN failover

Configuración de red con USG-3P, UniFi controller en Docker y failover Telecom/Telecentro.

---

## Hardware de red

| Dispositivo | Detalle |
|------------|---------|
| Router | UniFi USG-3P |
| Controller | Docker: `lscr.io/linuxserver/unifi-controller:latest` |
| ISP Principal | Telecom |
| ISP Secundario | Telecentro |

---

## Interfaces USG-3P

| Puerto | Interfaz | ISP | IP | Modo |
|--------|---------|-----|-----|------|
| Port 1 | eth0 | Telecom | 192.168.0.125 | Primary |
| Port 2 | eth1 | LAN | — | LAN |
| Port 3 | eth2 | Telecentro | 10.131.202.19/24 | Failover Only |

- Gateway Telecentro: 10.131.202.1
- Modem Telecentro en **modo router** con DHCP activo (no bridge)
- Load Balancing: **Failover Only** — Telecentro solo activa si Telecom cae

---

## Controller Docker

```bash
# Logs
docker logs unifi-controller -f

# Bind mount
/var/www/hermess/unifi/config  →  /config  (dentro del contenedor)
```

---

## Archivos clave

| Archivo | Rol |
|---------|-----|
| `/var/www/hermess/unifi/config/data/sites/default/config.gateway.json` | Override config USG (leído por el controller) |
| `/config/config.boot` en USG (10.10.10.1) | Config persistente del USG (EdgeOS/Vyatta) |

### config.gateway.json actual

```json
{
    "interfaces": {
        "ethernet": {
            "eth2": {
                "address": ["dhcp"],
                "description": "WAN2 Telecentro",
                "dhcp-options": {
                    "default-route-distance": "210",
                    "name-server": "no-update"
                },
                "firewall": {
                    "in":    { "name": "WAN_IN" },
                    "local": { "name": "WAN_LOCAL" },
                    "out":   { "name": "WAN_OUT" }
                }
            }
        }
    }
}
```

> El archivo debe ser propiedad de uid 1000 (`abc` dentro del contenedor).

---

## Problemas encontrados

### eth2 deshabilitado
- `config.boot` tenía `disable` en eth2 — interface no levantaba
- Fix: SSH al USG, `sed` para remover `disable` y agregar DHCP

### NAT conflict (rules 6004-6006)
- Primer config.gateway.json generó reglas NAT parciales con `network-group`
- El controller luego quiso crear rule 6004 con `address-group`
- Error EdgeOS: "Can't combine network and address group for source"
- Fix: eliminar reglas stale 6004-6006 de `config.boot`

### load-balancing tree inválido
- USG-3P firmware 4.4.57 NO soporta `load-balancing wan-load-balance`
- El controller usa internamente `load-balance group wan_failover`
- No incluir este bloque en config.gateway.json

---

## Comandos útiles

```bash
# SSH al USG
ssh hermess@10.10.10.1

# Ver estado WAN
show wan-load-balance

# Ver interfaces
show interfaces ethernet detail

# Ver ruta default activa
ip route show default

# Forzar provision desde controller (requiere auth cookie válida)
curl -sk -b /tmp/unifi-cookie.txt -X POST \
  https://localhost:8443/api/s/default/cmd/devmgr \
  -H "Content-Type: application/json" \
  -d '{"cmd":"force-provision","mac":"MAC_DEL_USG"}'
```

---

## Ver también

- [[hermess-pc/arquitectura|Arquitectura del sistema]]
- [[hermess-pc/changelog|Changelog]]

- [[hermess-pc/vpn-casa|VPN CASA — L2TP/IPSec]]
