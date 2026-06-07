# Libre Opcion

Diagnóstico, mejoras de SEO/performance, features y landings para libreopcion.com.ar.
Última sincronización: 2026-06-07.

---

## Proyecto

- [[arquitectura|Arquitectura]] — Checkout integrado (MP/GetNet/Payway/MODO), iframeResizer, banners
- [[stack|Stack]] — Tecnologías, versiones, servicios externos
- [[changelog|Changelog]] — Registro de trabajo por fecha
- [[memoria|Memoria]] — Consolidación de feedback, reglas y contexto del proyecto

## Pasarelas de pago (en desarrollo)

Checkout con formulario embebido para múltiples proveedores. Ver [[arquitectura#Pasarelas de pago — Checkout integrado|Arquitectura § Pasarelas]].

| ID | Proveedor | Estado |
|---|---|---|
| 5076 | MercadoPago | ✅ Producción |
| 5077 | GetNet by Santander | ⚠️ Bloqueado (IP whitelist pendiente Santander) |
| 5078 | Payway | 🔧 Implementado, pendiente test navegador |
| 5079 | MODO | ✅ QR operativo en sandbox (2026-06-07) |

**Pendiente:** Contactar Santander para habilitar IP `190.189.93.116` en sandbox GetNet.

## Herramientas internas

### enviosMailDrop
Script Python para envío masivo de emails HTML. Integración con SQL Server para control de campañas.
- [[enviosMailDrop/enviosMailDrop|enviosMailDrop]] — Índice
- [[enviosMailDrop/arquitectura|Arquitectura]] · [[enviosMailDrop/stack|Stack]] · [[enviosMailDrop/contexto|Contexto]] · [[enviosMailDrop/changelog|Changelog]]

## Wallet & Categorización — API v4

### TareaWallet
Análisis e implementación del módulo de billetera y features relacionadas. Integración pasarelas de pago checkout. Airdrop OpcionFest $15.000 ARS. Sistema de recategorización de productos.
- [[TareaWallet/TareaWallet|TareaWallet]] — Índice
- [[TareaWallet/contexto|Contexto]] — MODO QR fix, OPcache gotcha, flujo wallet, TR_CODIGO 476, queries, HMAC
- [[TareaWallet/changelog|Changelog]] — Historial por fecha
- [[TareaWallet/arquitectura-recategorizacion|Arquitectura recategorización]]
