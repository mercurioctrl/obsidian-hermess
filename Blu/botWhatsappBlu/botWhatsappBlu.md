# botWhatsappBlu — Blubot

Bot de WhatsApp para soporte MSP de BLU. Recibe consultas de clientes por WhatsApp, las
resuelve con un LLM y, cuando hace falta, abre y sigue tickets en Jira (proyecto SNB).
Incluye un Inbox web para que los agentes tomen la conversacion a mano.

Repo: `git@github.com:BluIncStudio/supportBotJiraWhatsapp.git` · rama `main`
Corre en la VM `hermessbot` bajo PM2 (`ngrok` + `whatsapp-bot`), sin Docker.

## Notas

- [[arquitectura]] — modulos, flujo de datos, integracion con Jira y el Inbox
- [[stack]] — dependencias, servicios externos, variables de entorno
- [[changelog]] — que se trabajo y cuando
- [[contexto]] — reglas de negocio, decisiones y trampas conocidas
- [[memoria]] — memoria de Claude del proyecto, consolidada

## De un vistazo

| | |
|---|---|
| Canal | WhatsApp (whatsapp-web.js + Puppeteer) |
| LLM | Hibrido: DeepSeek para texto, OpenAI para vision |
| Tickets | Jira Cloud REST v3 (ADF), proyecto SNB |
| Storage | SQLite (`bot.db`, WAL) |
| HTTP | Express 5 en puerto 3100 + ngrok |
| Tamano | ~9.300 lineas de JS |

Ultima sincronizacion: 2026-08-31
