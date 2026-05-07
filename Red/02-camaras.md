# 02 — Cámaras IP

## Inventario

| Nombre | IP | MAC | Modelo | Conexión | AP / Puerto |
|---|---|---|---|---|---|
| Ezviz (exterior) | 10.10.10.43 | 98:f1:12:3f:f0:a6 | Ezviz (Hikvision) | WiFi | AP Galeria |
| PASILLO-C | 10.10.10.192 | 18:68:cb:d0:df:21 | DS-2CD1001-I | Cable | Switch (no administrado) |

---

## Cámara PASILLO-C — DS-2CD1001-I

**Modelo:** Hikvision DS-2CD1001-I (1MP, 2017)  
**Firmware:** V5.4.5 build 170208  
**Credenciales:** admin / (ver gestor de contraseñas)  
**IP:** 10.10.10.192 (estática, máscara /23)

### Problema: imagen se interrumpe cada tanto

**Causa principal — cable degradado:**
- Link negociado a **10Mbps half-duplex** en vez de 100Mbps full-duplex
- Half-duplex genera colisiones cuando hay tráfico simultáneo → cortes de imagen
- Auto-negociación habilitada pero falla por cable dañado, mal crimpado o solo 2 pares activos

**Causa secundaria — RAM al límite:**
- RAM usage: ~93-96% (solo ~2-3 MB disponibles)
- Modelo muy básico con poca RAM de base
- Con 16+ días de uptime acumula memory leaks

### Cambios aplicados

- UPnP deshabilitado (liberaba memoria innecesariamente)
- Multicast deshabilitado en ambos streams (main 101 y sub 102)
- Reboot manual realizado → RAM bajó de 96% a 93%
- **Cron diario 3:40am** configurado en hermess-desktop para reboot automático:
  ```
  40 3 * * * curl -sk --digest -u 'admin:...' -X PUT 'http://10.10.10.192/ISAPI/System/reboot'
  ```

### Configuración de streams

| Stream | Resolución | Codec | Bitrate | FPS |
|---|---|---|---|---|
| Main (101) | 1280×720 | H.264 Main | VBR 512 kbps | 25 |
| Sub (102) | 352×288 | H.264 Main | VBR 256 kbps | 25 |

### ⚠️ Tarea pendiente — reemplazar cable

El cable de red del pasillo necesita ser reemplazado o re-crimpado. Mientras no se cambie, los cortes de imagen van a persistir independientemente de cualquier otra optimización.

**Checklist para resolver:**
- [ ] Revisar el recorrido del cable en el pasillo
- [ ] Probar con un cable de reemplazo temporario para confirmar que es el cable
- [ ] Si es un patch cord: reemplazar directamente
- [ ] Si es cable de pared: re-crimpear o tirar cable nuevo
- [ ] Confirmar que el link queda en 100Mbps full-duplex luego del cambio

---

## Cámara Ezviz (exterior)

**Conexión:** WiFi — debe conectarse siempre a **AP Galeria**  
**Señal actual:** -43 dBm en AP Galeria (antes estaba en AP Oficina con -58 dBm)  
**Retries acumulados:** 387.515 (histórico antes del kick)

### ⚠️ Tarea pendiente — pinear a AP Galeria

UniFi no soporta pinear un cliente a un AP específico de forma nativa. Si la cámara vuelve a migrar a AP Oficina, opciones:

- **Opción recomendada:** crear SSID `nexus-cam` asignado solo a AP Galeria y reconectar la cámara a esa red
- **Alternativa:** kick manual desde el controlador para forzar reconexión (temporal)
