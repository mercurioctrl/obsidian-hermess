# Memoria — botWhatsappBlu

Consolidacion de la memoria de Claude del proyecto
(`~/.claude/projects/-home-hermessbot-botWhatsappBlu/memory/`), 24 notas al 2026-08-31.
Esta nota es un espejo legible: la fuente de verdad son esos archivos.

Ver [[botWhatsappBlu]] · [[contexto]] · [[arquitectura]]

## Feedback — como trabajar en este proyecto

| Tema | Regla |
|---|---|
| Commits | Nunca `Co-Authored-By` de Claude. Todo a nombre de Catriel Mercurio. Regla **dura** |
| Commits tematicos | Con backlog de varios temas, partir en commits separados. `git add -p` esta bloqueado (interactivo): extraer hunks y aplicar con `git apply --cached` |
| PM2 | Reiniciar `whatsapp-bot` proactivamente tras editar codigo de runtime, sin esperar que lo pidan |
| `ecosystem.config.js` | `pm2 restart` **no** toma los cambios: `pm2 delete` + `pm2 start` + `pm2 save` |
| Tickets | Mencionarlos siempre como `SNB-XXXX - Titulo completo` |

## Proyecto — como funciona

- **Arquitectura general**: stack, que hace cada archivo, PM2/ngrok, specifics de Ubuntu 24.04
- **Flujo MSP**: conversacion, datos del cliente (auto vs manual), comandos `/humano` `/bot` `/menu`
  `/nuevo` `/tickets`, debounce y recordatorios de inactividad
- **Handoff y Slack**: reenvio de mensajes del cliente mientras espera, con recordatorios; truco de
  msgId-tracking para distinguir mensajes del bot de los de un humano
- **Esquema SQLite**: tablas, indices, WAL y el patron de migraciones idempotentes
- **Inbox y Chat Viewer**: endpoints del Express en 3100, panel de edicion de contacto, `/send-media`
- **XPG Rewards**: flujo paralelo al MSP, 3 tablas, scripts de invitacion, lookup self-healing
- **LLM hibrido**: DeepSeek para texto por costo, OpenAI solo para vision; ruteo en `chat.js`
- **Jira SNB**: issue types, custom fields, labels, categorias, webhooks, link al Chat Viewer
- **Cuenta de servicio Jira**: ver [[contexto]] — es el cambio del 2026-08-29
- **Clave inversa**: `customfield_10080` (reportUser) = `contactos.usuario`; puente estable que
  sobrevive a cambios de chatId
- **chatIds `@c.us` vs `@lid`**: migracion silenciosa de WhatsApp, `getNumberId` y self-healing
- **VM**: RAM/swap, headless, limites de heap; condiciona cuanto margen hay para procesos extra
- **Datos sensibles**: que hay en los archivos no versionados y que tiene que regenerar quien clone

## Fallas conocidas

- **Sesion zombie**: WhatsApp desvinculado deja Chrome colgado con timeouts y PM2 sigue diciendo
  `online` — engana al diagnostico
- **`getChat()` roto para `@lid`**: `Error general: r`; rompio todo el wrapper de `Chat`
- **Media rota**: WhatsApp renombro `msg.id._serialized`, `downloadMedia()` tiraba `r: r` y todo
  quedaba como `[Media adjunta]`
- **Summary de Jira**: un `\n` en el summary da 400; `crearTicket` lo sanea siempre

## Pendiente

- Ticket de Andrea (New Bytes) que fallo el 2026-07-07 y nunca se creo. Borrar la nota al resolver
