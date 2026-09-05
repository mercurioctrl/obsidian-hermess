# Bóveda accesible desde el exterior — Cloudflare Tunnel + Access

Acceso remoto **seguro** a esta bóveda Obsidian para que instancias de Claude (u otras herramientas) en otros servidores puedan leer/escribir las notas en vivo, sin abrir puertos en el [[Red|USG]] ni exponer la IP de casa.

## Arquitectura

```
Claude remoto ──HTTPS──> Cloudflare (Access valida service token)
                              │  túnel saliente (QUIC)
                              ▼
        hermess-desktop 10.10.10.7 : cloudflared (systemd)
                              │  https://127.0.0.1:27124 (noTLSVerify)
                              ▼
        Obsidian "Local REST API" (plugin) ── esta bóveda
```

- **Endpoint público:** `https://cmer-boveda.blustudioinc.com`
- **DNS:** CNAME (proxied) → túnel `boveda-cmer` (`c5cda1e4-…`). No hay A-record a la IP.
- **Servicio:** `cloudflared.service` (systemd) en `10.10.10.7`. Config en `/etc/cloudflared/config.yml`.
- **Origen local:** plugin **Local REST API** de Obsidian, HTTPS en `27124` (Obsidian tiene que estar **abierto** en el server para que responda).

## Dos capas de autenticación

| Capa | Qué valida | Headers |
|---|---|---|
| **Cloudflare Access** (service token) | El borde, antes del túnel | `CF-Access-Client-Id`, `CF-Access-Client-Secret` |
| **Obsidian REST API** (Bearer) | El acceso al plugin | `Authorization: Bearer <apiKey>` |

Sin los headers de Access → `403` en el borde. Con Access pero sin Bearer → `401`. Necesita **las dos** para entrar.

## Dónde están las credenciales (NO en git)

> ⚠️ Los secretos **no** viven en la bóveda (esto se sincroniza a GitHub). Están en el server, fuera de git:
> `~/.config/boveda-remota/creds.env` (chmod 600).

Contiene: `BOVEDA_URL`, `CF_ACCESS_CLIENT_ID`, `CF_ACCESS_CLIENT_SECRET`, `OBSIDIAN_API_KEY`.
El `apiKey` del plugin también está en Obsidian → Settings → Local REST API.

## Cómo conectar un Claude remoto

1. Copiar `creds.env` al server remoto (chmod 600) y cargarlo: `set -a; source creds.env; set +a`.
2. Probar:

```bash
# listar la raíz de la bóveda
curl -s "$BOVEDA_URL/vault/" \
  -H "CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID" \
  -H "CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET" \
  -H "Authorization: Bearer $OBSIDIAN_API_KEY"

# leer una nota
curl -s "$BOVEDA_URL/vault/Home.md" -H "CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID" \
  -H "CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET" -H "Authorization: Bearer $OBSIDIAN_API_KEY"
```

3. **Vía MCP:** si se usa un MCP de Obsidian que no soporte headers custom de Access, correr en el server remoto un puente `cloudflared access` con el service token (variables `TUNNEL_SERVICE_TOKEN_ID`/`TUNNEL_SERVICE_TOKEN_SECRET`) y apuntar el MCP al puerto local; así el MCP solo manda el Bearer y cloudflared inyecta el Access.

## Operación

```bash
sudo systemctl status cloudflared        # estado del túnel
sudo journalctl -u cloudflared -f        # logs en vivo
cloudflared tunnel info boveda-cmer      # conexiones al edge
```

- **Rotar Bearer:** Obsidian → Local REST API → regenerar API Key → actualizar `creds.env`.
- **Revocar acceso remoto:** borrar el service token `boveda-claude-remoto` en Zero Trust → Access → Service Auth (corta a todos los remotos de un saque).
- **App Access:** "Boveda Obsidian CMER" en Zero Trust → Access → Applications.

## Pendientes / notas

- El plugin escucha en `0.0.0.0:27124`, así que en la **LAN** también es alcanzable directo (sin pasar por Access), protegido solo por el Bearer. Si se quiere forzar todo por Access, cambiar `bindingHost` a `127.0.0.1` en el plugin.
- Quedó un vhost viejo de Apache `boveda.conf` (ServerName igual) que ya no recibe tráfico porque el DNS ahora es CNAME al túnel; se puede borrar.

Ver también: [[Red]], [[08-home-assistant]]
