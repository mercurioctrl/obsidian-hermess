# Planilla Acciones Bully

Planilla de Google Sheets para opciones financieras. Usa Apps Script para consultar precios desde la API `https://api.bully.lio.red/options`.

---

## Documentacion

- [[Planilla Acciones Bully/Documentacion Apps Script - Opciones API|Documentacion Apps Script - Opciones API]] — Referencia completa del script: config, columnas, flujo, API, historial de cambios

---

## Prompts

Prompts listos para pegar en Claude Code cuando se necesite modificar la API:

- [[Planilla Acciones Bully/prompt-optimizar-api|Prompt - Optimizar API]] — Cache de sesion/crumb, eliminar logs innecesarios, connection pooling
- [[Planilla Acciones Bully/prompt-agregar-stock-data-api|Prompt - Agregar stock data API]] — Agregar stockPrice, changePct, low52, high52, beta al endpoint

---

## Codigo

Versiones del script `Code.gs` en la carpeta `codigo/`:

| Version | Archivo | Estado | Descripcion |
|---------|---------|--------|-------------|
| Original | `Code_gs_original.js` | Reemplazada | Version inicial sin optimizaciones |
| v4 | `Code_gs_v4_optimizado.js` | Reemplazada | Cache, pre-lectura batch, semaforo visual |
| v5 | `Code_gs_v5_sin_googlefinance.js` | **Deployada** | Elimina GOOGLEFINANCE, datos de stock via API |

---

## Links

- API: `https://api.bully.lio.red/options`
- Apps Script editor: `https://script.google.com/u/0/home/projects/1GQ32BC3XcLudtVARbvMyT1lgJ0WOpCynYUlff8zd2KXhZaB3K7ygRlVO/edit`
