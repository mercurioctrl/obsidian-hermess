# Changelog — botWhatsappBlu

Ver [[botWhatsappBlu]] · [[contexto]]

## 2026-08-31

- `docs`: documentada la cuenta de servicio de Jira, los permisos de SNB y el 403 del webhook

Se agrego al `README.md` la seccion *Cuenta de servicio y permisos* (por que el token define el
reporter, que SNB es un JSM, y la tabla de que chequeo de permisos sirve y cual da falsos positivos),
mas el 403 del webhook explicado como esperado. `CLAUDE.md` suma la regla de commits tematicos.

Archivos: `README.md`, `CLAUDE.md`

## 2026-08-29

- `feat`: cuenta de servicio de Jira en lugar del token personal
- `feat`: MCP `whatsapp-blu` para enviar WhatsApp desde Claude
- `fix`: no reenviar al cliente los comentarios que el bot copia desde WhatsApp
- `feat`: cortacircuitos anti-loop y pin opcional de version de WhatsApp Web

**Cuenta de servicio:** los tickets salian a nombre de una persona porque Jira autentica con Basic
`email:token` y el reporter es siempre el dueno del token. Se paso a `soporte@blustudioinc.com`
("Soporte Blu"), que hubo que agregar al rol *Service Desk Team* de SNB. La deteccion de comentarios
propios paso del literal `'Blubot'` a `NOMBRES_BOT`.

**Anti-loop:** los numeros de servicio y marketing contestan automaticamente, y el bot les respondia:
el 2026-08-07 un chat acumulo 174 mensajes en 2h30. Se vigilan los mensajes salientes y la senal no es
el volumen sino la **repeticion** del mismo texto.

**Comentarios eco:** los comentarios que el propio bot copia desde WhatsApp volvian al cliente como si
fueran respuesta de un agente. El filtro por autor no alcanzaba porque Jira Cloud no manda
`emailAddress` en los webhooks.

Archivos: `jira.js`, `webhook.js`, `bot.js`, `mcp-whatsapp.js`, `.mcp.json`, `package.json`

## 2026-08-27

- `fix`: descargar media entrante sin depender de `id._serialized`

WhatsApp Web renombro `_serialized` y `downloadMedia()` tiraba `r: r`; todo entraba como
`[Media adjunta]`.

## 2026-07-21

- `fix`: evitar `msg.getChat()` (roto para `@lid`) y catch robusto en el handler

## 2026-07-08

- `feat`: LLM hibrido DeepSeek (texto) + OpenAI (vision); summary de Jira de una sola linea
- `docs`: documentado el hibrido en README y `.env.example`

Jira rechaza con 400 cualquier `summary` que tenga `\n`, asi que `crearTicket` lo sanea siempre.

## 2026-07-01

- `feat`: menu guiado con "Volver a empezar", saludos y titulos de tickets
- `feat`: reenvio a Slack y recordatorios mientras un cliente espera atencion

## 2026-06-30

- `feat`: notificaciones push (Web Push) para el Inbox
