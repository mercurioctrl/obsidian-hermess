# Arquitectura — botWhatsappBlu

Ver [[botWhatsappBlu]] · [[stack]] · [[contexto]]

## Modulos

| Archivo | LOC | Responsabilidad |
|---|---|---|
| `webhook.js` | 2365 | Express: webhooks de Jira, Chat Viewer, Inbox web, API HTTP, cola de envios |
| `bot.js` | 1537 | Orquestador: recibe mensajes de WhatsApp y despacha |
| `db.js` | 892 | SQLite; migraciones idempotentes en cada arranque |
| `chat.js` | 687 | Motor de conversacion; arma el contexto y rutea al LLM |
| `flujo.js` | 672 | Menu guiado y pasos del flujo MSP |
| `jira.js` | 591 | Jira REST v3: crear tickets (ADF), comentar, adjuntar, buscar |
| `openapi.js` | 405 | Spec de la API HTTP |
| `mcp-whatsapp.js` | 388 | Server MCP `whatsapp-blu` |
| `xpgRewards.js` | 315 | Flujo XPG Rewards, paralelo al MSP |

## Flujo de datos

1. **Cliente -> Bot**: `whatsapp-web.js` recibe el mensaje, `bot.js` lo despacha
2. **Bot -> LLM**: `chat.js` arma historial + system prompt. Texto va a DeepSeek; si hay imagen, a OpenAI
3. **Bot -> Jira**: cuando el LLM emite el JSON de ticket, `jira.js` lo crea via REST v3 en formato ADF
4. **Jira -> Bot -> Cliente**: `webhook.js` recibe los eventos de Jira y reenvia por WhatsApp
5. **Persistencia**: `db.js` guarda contactos y mensajes en `bot.db`

El paso 4 depende de que ngrok exponga el puerto 3100 y de que el webhook siga registrado en Jira
— ahi hay una trampa documentada en [[contexto]].

## Base de datos

`bot.db` (SQLite, WAL). Tablas: `contactos`, `mensajes`, `cola_envios`, `push`, `xpg`.
Las migraciones corren solas y son idempotentes, asi que no hay paso manual al desplegar.

**`cola_envios`** es el punto unico de salida: todo lo que sale por WhatsApp se encola y un worker
despacha cada 10 segundos con hasta 5 reintentos. El MCP y la API HTTP escriben ahi, no al cliente
de WhatsApp directamente. Encolado no es entregado.

## Decisiones de diseno

**Cola persistente en vez de envio directo.** Sobrevive a reinicios de PM2 y a que Chrome se cuelgue,
que en esta VM pasa. Ademas centraliza el formateo de enlaces y los reintentos.

**LLM hibrido por costo.** DeepSeek cubre el texto, que es el grueso; OpenAI solo entra cuando hay
imagen y hace falta vision. El ruteo vive en `chat.js`.

**Se evita el wrapper de `Chat` de whatsapp-web.js.** `getChat()`, `getChats()` y `fetchMessages()`
revientan con `Error: r` para chatIds `@lid`. Donde hace falta se lee `window.Store` crudo por
`pupPage.evaluate` — asi estan resueltos `/api/grupos` y `/api/grupo/:chatId/messages`.

**Clave inversa `customfield_10080` (reportUser).** Es el puente estable entre el ticket de Jira y el
usuario de WhatsApp: sobrevive a que el cliente cambie de numero o de chatId.

## Superficies HTTP (puerto 3100)

- `POST /jira-webhook/:secret` — eventos de Jira
- **Chat Viewer** `/chat/user/:chatId` — la conversacion completa, linkeada desde cada ticket
- **Inbox web** `/inbox` — lista de conversaciones, toggle bot on/off por chat, envio de archivos
- **Deep link** `/inbox/c/:chatId` — la misma SPA, abierta en esa conversacion (ver abajo)
- **API publica** — `POST /inbox/send` y afines, autenticadas por `INBOX_API_TOKEN`

Las paginas HTML pasan por `requiereAuth` (redirige al login) y los endpoints JSON por
`requiereAuthApi` (401). Ambos aceptan cookie de sesion **o** `INBOX_API_TOKEN`.

## El Inbox es una SPA servida desde un template literal

`generarHTMLInbox()` devuelve HTML + CSS + JS en un solo template literal de `webhook.js`; no hay
build, ni framework, ni archivos estaticos. Consecuencia practica al editarlo: el JS **del cliente**
esta dentro de un string, asi que las barras invertidas y los `${` van escapados, y
`node --check webhook.js` no lo valida (para el parser es texto). Ver [[contexto]].

**Deep links (2026-09-08).** `/inbox/c/:chatId` sirve exactamente el mismo HTML que `/inbox`: el
routing real es del lado del cliente, que lee el chatId de `location.pathname` y abre esa conversacion
al cargar. `abrirChat()` empuja `history.pushState` y un handler de `popstate` cubre back/forward. La
URL deja el `@` sin escapar para que sea legible y pegable.

Para que un link compartido sobreviva al login, `requiereAuth` redirige a `/inbox/login?next=<ruta>`
y el POST del login vuelve a ese destino. `rutaInternaSegura()` acepta solo rutas que empiecen con
`/` y no con `//`; cualquier otra cosa cae a `/inbox`. **El link no es un secreto por conversacion**:
la barrera sigue siendo la sesion del Inbox, no la URL.

## MCP `whatsapp-blu`

`mcp-whatsapp.js` expone el envio de WhatsApp como tools para Claude. Es un **wrapper sobre la API
HTTP**, no habla con Puppeteer: todo entra a la misma `cola_envios`. Las tools de envio tienen un
parametro `confirmado` que arranca en `false` y solo devuelve la previsualizacion — los envios van a
clientes reales y son irreversibles.
