# Contexto — botWhatsappBlu

Ver [[botWhatsappBlu]] · [[arquitectura]] · [[changelog]]

## Jira: cuenta de servicio y permisos

Jira autentica con Basic `email:token`, asi que **el reporter de todo ticket que crea el bot es el
dueno del token**. Con un token personal, todos los tickets salen a nombre de esa persona: fue
exactamente el problema resuelto el 2026-08-29. Hoy se usa `soporte@blustudioinc.com` ("Soporte Blu").

**SNB no es un proyecto Jira comun sino un Jira Service Management** (`service_desk`, company-managed,
id 10024). El acceso va por roles: para crear, comentar y adjuntar hay que estar en el rol
**Service Desk Team** (id 10005), o sea ser agente, lo que **consume una licencia JSM paga**.

Al verificar permisos hay dos falsos positivos que ya costaron un diagnostico erroneo:

| Chequeo | Sirve | Por que |
|---|---|---|
| `createmeta?projectKeys=SNB` | **si** | Si `projects` viene vacio, la cuenta no puede crear tickets |
| `mypermissions?projectKey=SNB` | no | Devuelve todo OK aunque la cuenta no vea el proyecto |
| JQL `project = SNB` | no | Responde 200 con `issues: []` en vez de error |

Jira tampoco devuelve `emailAddress` de otros usuarios: solo el de la cuenta duena del token. Por eso
el filtro de comentarios propios necesita el fallback por `displayName`
(`NOMBRES_BOT = ['Soporte Blu', 'Blubot']` en `jira.js` y `webhook.js`). **Si se cambia la cuenta de
servicio, hay que sumar su displayName a ese array en los dos archivos.**

## El 403 del webhook es esperado

En cada arranque aparece:

```
[WEBHOOK] Error al crear webhook: 403 - No tienes permiso para crear el WebHook 'whatsapp-bot-webhook'
```

Se usa `/rest/webhooks/1.0/webhook`, que exige **ADMINISTER global de Jira**; la cuenta de servicio
solo tiene rol de proyecto. **No rompe nada**: el webhook ya esta registrado, `enabled: true` y sin
expiracion.

**Riesgo latente, asumido a proposito:** si cambia la URL publica de ngrok, el bot no podra actualizar
el webhook y **el reenvio de comentarios al cliente se corta en silencio** — solo loguea el 403 y
sigue andando. Habria que re-registrarlo a mano una vez con una cuenta que tenga ADMINISTER. Se
evaluaron parchear el codigo y darle ADMINISTER al bot; el usuario eligio dejarlo asi y documentarlo.

## Operacion

- **Reiniciar PM2 tras tocar codigo de runtime** (`bot.js`, `webhook.js`, `chat.js`, `jira.js`,
  `db.js`, `flujo.js`, `xpgRewards.js`): `pm2 restart whatsapp-bot`. No hay `--watch`
- **Cambios en `ecosystem.config.js` no los toma `pm2 restart`**: hay que hacer
  `pm2 delete whatsapp-bot && pm2 start ecosystem.config.js && pm2 save`
- **VM de 2.2 GB sin GUI**: evaluar el margen antes de sumar procesos
- **Datos sensibles fuera del repo**: `bot.db`, `media/`, `publicStorage/*.csv` (passwords en
  plaintext), `.env`, `core` y `*.bak` estan en `.gitignore`

## Trampas conocidas

- **Sesion zombie de WhatsApp**: PM2 dice `online` pero Chrome quedo congelado y todo da timeout
- **`getChat()` roto para `@lid`**: rompio todo el wrapper de `Chat`; se lee `window.Store` crudo
- **Media rota por `_serialized`**: resuelto el 2026-08-27
- **`summary` de Jira de una sola linea**: un `\n` da 400
- **Los envios del MCP van a clientes reales y son irreversibles**: siempre previsualizar con
  `confirmado=false` antes de mandar

## Convenciones

Idioma espanol en todo (codigo, comentarios, commits, mensajes al cliente). Commits a nombre de
Catriel Mercurio, **nunca** `Co-Authored-By`. Commits tematicos aunque haya que partir un archivo por
hunks. Al mencionar un ticket, escribirlo siempre como `SNB-XXXX - Titulo completo`.

## Pendientes

- **Prueba de punta a punta del cambio de cuenta**: falta ver un ticket real creado desde WhatsApp con
  reporter Soporte Blu. Lo verificado es que la cuenta tiene permisos y ve los mismos campos
- **Ticket de Andrea (New Bytes)**: fallo el 2026-07-07 y nunca se creo
- Backups `.env.bak`, `jira.js.bak` y `webhook.js.bak` quedaron en la VM, ignorados por git
