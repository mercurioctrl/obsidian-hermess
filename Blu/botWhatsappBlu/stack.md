# Stack — botWhatsappBlu

Ver [[botWhatsappBlu]] · [[arquitectura]]

## Runtime

- **Node.js 22** sobre Ubuntu 24.04 (`engines.node >=20`)
- **PM2** con 2 procesos: `ngrok` (id 0) y `whatsapp-bot` (id 1). Sin Docker, sin `--watch`
- VM chica: **2.2 GB RAM, sin GUI**. Los limites de heap del bot y de Chrome estan tuneados a proposito

## Dependencias

| Paquete | Para que |
|---|---|
| `whatsapp-web.js` | Cliente de WhatsApp; Chromium bundled, sesion en `.wwebjs_auth/` |
| `openai` | SDK usado para los dos proveedores de LLM (DeepSeek expone API compatible) |
| `better-sqlite3` | `bot.db` en modo WAL, migraciones idempotentes en cada arranque |
| `express` (v5) | Puerto 3100: webhooks de Jira, Chat Viewer, Inbox web y API |
| `@modelcontextprotocol/sdk` + `zod` | Server MCP `whatsapp-blu` |
| `web-push` | Notificaciones push del Inbox |
| `mime-types`, `qrcode-terminal`, `dotenv` | Utilidades |

**No** se usa el SDK de Anthropic — decision explicita del usuario.

## Servicios externos

- **DeepSeek** (`deepseek-chat`) — todo el texto, por costo
- **OpenAI** (`gpt-4o-mini`) — solo imagenes, por vision
- **Jira Cloud** — `bluinc.atlassian.net`, proyecto SNB. Cuenta de servicio, ver [[contexto]]
- **ngrok** — URL publica para los webhooks Jira -> bot. Dominio reservado

## Variables de entorno

En `.env` (ignorado por git); el detalle completo esta en el `README.md` del repo.
Las de Jira son `JIRA_BASE_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN`, `JIRA_PROJECT_KEY`.
`INBOX_API_TOKEN` autentica la API HTTP y lo reusa el MCP.
