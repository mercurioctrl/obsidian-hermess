# Arquitectura — enviosMailDrop

## Estructura del proyecto

```
enviosMailDrop/
├── enviar_airdrop.py         # Envío masivo (manual)
├── cron_airdrop_wallet.py    # Acreditación wallet (cron cada 2 min)
├── send_wallet_airdrop.py    # Obsoleto — flujo anterior
├── acreditar_wallet_airdrop.py # Obsoleto — flujo anterior
├── template_wallet_airdrop.html
├── template.html
└── CLAUDE.md
```

## Flujo principal

```
INSERT email → LO.dbo.airdrop_recipients
        ↓
enviar_airdrop.py
  Lee: email_sent_at IS NULL AND mail_intentos < 3
  Envía SMTP → marca email_sent_at = GETDATE()
  BCC: notificalibreopcion@gmail.com
        ↓
cron_airdrop_wallet.py (cada 2 min)
  Lee: email_sent_at IS NOT NULL AND airdrop_done_at IS NULL
  Busca correo en LO.dbo.usuarios
  Si existe:
    → UPDATE usuarios SET activeWallet = 1
    → INSERT MC_CCORRIENTES_MOVIMIENTOS (TR_CODIGO=476, airdrop_opcionfest)
    → UPDATE HMAC
    → UPDATE airdrop_recipients SET airdrop_done_at = GETDATE()
  Si no existe: reintenta en próxima ejecución
```

## Tablas

### LO.dbo.airdrop_recipients (tabla principal)

| Columna | Tipo | Descripción |
|---|---|---|
| `id` | INT IDENTITY | PK |
| `email` | VARCHAR(255) UNIQUE | Destinatario |
| `user_id` | INT NULL | ID usuario LO cuando matchea |
| `email_sent_at` | DATETIME NULL | NULL = pendiente de envío |
| `airdrop_done_at` | DATETIME NULL | NULL = pendiente de acreditación |
| `amount_usd` | DECIMAL NULL | Monto acreditado |
| `mail_intentos` | TINYINT | Contador intentos envío (máx 3) |
| `mail_error` | VARCHAR(500) NULL | Último error de envío |
| `created_at` | DATETIME | Alta del registro |

### NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS

- `TR_CODIGO = 476` — tipo de transacción airdrop
- `CC_OBSERVACIONES = airdrop_opcionfest` — identifica los movimientos de esta campaña
- `showWallet = 1` — visible en la wallet del usuario
- `HMAC` — firma SHA256 del movimiento con key `superconductor`

## Email / SMTP

- **Host:** `box.lio.red:465` SSL
- **From:** `no-responder@libreopcion.com`
- **BCC:** `notificalibreopcion@gmail.com` (copia en cada envío)
- **DKIM:** selector `mail`, firmado por OpenDKIM
- **Fix crítico:** `From` debe formatearse con `formataddr((str(Header(nombre,"utf-8")), email))`
  para que OpenDKIM pueda parsear el header y firmar el mail

## HMAC del movimiento

```python
payload = json.dumps(mov_dict, default=str, separators=(",",":"), sort_keys=True)
hmac.new("superconductor".encode(), payload.encode(), hashlib.sha256).hexdigest()
```

Campos incluidos: `ID_CCMOVIMIENTO`, `ID_CLIENTE`, `TR_CODIGO`, `CC_FECHAMOVIMIENTO`,
`CC_HORAMOVIMIENTO`, `CC_OBSERVACIONES`, `CC_IMPORTEUSD`, `CC_ANULADO`, `COTIZACION`

## Ver también

- [[enviosMailDrop]] — índice
- [[stack]] — dependencias
- [[contexto]] — reglas de negocio y decisiones
