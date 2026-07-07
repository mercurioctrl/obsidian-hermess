# VPN CASA — L2TP/IPSec

VPN nativa de macOS usada para acceder a la red de Blu. Documentada para migrarla a esta Ubuntu ([[hermess-pc/hermess-pc|hermess-pc]]).

> ⚠️ **No es OpenVPN ni WireGuard.** Son protocolos distintos e incompatibles. Para conectarse hace falta un cliente **L2TP/IPSec**.

---

## Datos de la conexión

| Campo | Valor |
|---|---|
| Nombre | VPN CASA |
| Protocolo | **L2TP sobre IPSec** |
| Servidor (gateway) | `db-nb-dev.blu.net.ar` |
| Usuario | `hermess87` |
| Autenticación IPSec | Pre-Shared Key (Shared Secret) |
| Contraseña usuario | cifrada en System Keychain de la Mac |
| Pre-Shared Key (PSK) | cifrado en System Keychain de la Mac |

Origen: VPN nativa de macOS (`scutil --nc list` → `PPP --> L2TP`). Config en `/Library/Preferences/SystemConfiguration/preferences.plist`; secretos en `/Library/Keychains/System.keychain`.

---

## Arquitectura del túnel

```
[Cliente Ubuntu]
   │  L2TP (PPP) encapsulado dentro de...
   │  IPSec (ESP) autenticado con Pre-Shared Key
   ▼
[Gateway VPN: db-nb-dev.blu.net.ar]
   ▼
[Red interna Blu]
```

- **IPSec** establece el canal seguro (Phase1/Phase2) con el PSK compartido.
- **L2TP** crea el túnel PPP por dentro; ahí va usuario + contraseña (MSCHAPv2).

---

## Extraer secretos desde la Mac

```bash
# Contraseña del usuario
sudo security find-generic-password -l "VPN CASA" -w /Library/Keychains/System.keychain

# Listar ítems VPN (el shared secret suele terminar en .SS)
sudo security dump-keychain /Library/Keychains/System.keychain | grep -iE "VPN CASA|\.SS"
```

---

## Migración a Ubuntu (NetworkManager + L2TP)

1. Instalar plugin:
   ```bash
   sudo apt update
   sudo apt install network-manager-l2tp network-manager-l2tp-gnome
   ```
2. Completar placeholders en `vpn-casa.nmconnection` (`~/vpn-casa.nmconnection` en la Mac):
   - `ipsec-psk` → el Shared Secret
   - `password` (sección `[vpn-secrets]`) → la contraseña de `hermess87`
3. Instalar el keyfile:
   ```bash
   sudo cp vpn-casa.nmconnection /etc/NetworkManager/system-connections/
   sudo chown root:root /etc/NetworkManager/system-connections/vpn-casa.nmconnection
   sudo chmod 600 /etc/NetworkManager/system-connections/vpn-casa.nmconnection
   sudo nmcli connection reload
   nmcli connection up "VPN CASA"
   ```
   Permisos 600 + owner root **obligatorios** o NetworkManager ignora el archivo.

### keyfile `.nmconnection`

```ini
[connection]
id=VPN CASA
uuid=db921be1-16c1-4511-9a50-110c02efb26d
type=vpn
autoconnect=false

[vpn]
service-type=org.freedesktop.NetworkManager.l2tp
gateway=db-nb-dev.blu.net.ar
user=hermess87
password-flags=0
ipsec-enabled=yes
ipsec-psk=REEMPLAZAR_SHARED_SECRET
ipsec-ike=aes128-sha1-modp1024,3des-sha1-modp1024
ipsec-esp=aes128-sha1,3des-sha1
mschap-v2=yes
refuse-eap=yes
refuse-pap=yes
refuse-chap=yes
refuse-mschap=yes

[vpn-secrets]
password=REEMPLAZAR_CONTRASEÑA

[ipv4]
method=auto

[ipv6]
method=auto
```

---

## Troubleshooting

- Logs en vivo: `journalctl -u NetworkManager -f`
- Si IPSec no negocia: vaciar `ipsec-ike` / `ipsec-esp` (negociación automática) o pedir los algoritmos exactos al admin de `db-nb-dev.blu.net.ar`.

---

## Ver también

- [[hermess-pc/red|Red — UniFi dual WAN failover]]
- [[hermess-pc/arquitectura|Arquitectura del sistema]]
- [[hermess-pc/changelog|Changelog]]
