# enviosMailDrop

Script Python para envío masivo de emails HTML y acreditación automática de wallet para campañas de Libre Opción.

**Última sincronización:** 2026-05-11

## Stack

- Python 3.12 — scripts CLI
- SMTP SSL — `box.lio.red:465` vía `smtplib`
- SQL Server (DB `LO`) — tabla `airdrop_recipients` como fuente de verdad
- SQL Server (DB `NEW_BYTES`) — movimientos de cuenta corriente (wallet)

## Scripts

| Archivo | Descripción |
|---|---|
| `enviar_airdrop.py` | Envía mails a pendientes en `airdrop_recipients`. Correr manualmente. |
| `cron_airdrop_wallet.py` | Acredita wallets. Corre en cron cada 2 min. |
| `send_wallet_airdrop.py` | Script original (tabla `mail_campana_envios`). Obsoleto. |
| `acreditar_wallet_airdrop.py` | Script original de acreditación. Obsoleto. |
| `template_wallet_airdrop.html` | Plantilla HTML campaña Opción Fest |
| `template.html` | Plantilla original notificación ventas |

## Uso

```bash
# 1. Insertar emails (anti-duplicado automático)
python3 enviar_airdrop.py  # detecta pendientes en airdrop_recipients

# 2. El cron acredita wallets automáticamente cada 2 min
# Ver: /tmp/airdrop_wallet.log
```

## Notas

- [[arquitectura]] — flujo, tablas y decisiones técnicas
- [[stack]] — dependencias y configuración
- [[contexto]] — reglas de negocio, flujo operativo, problemas resueltos
- [[changelog]] — historial de cambios

## Ver también

- [[Libre Opcion/Libre Opcion|Libre Opción]] — proyecto padre
