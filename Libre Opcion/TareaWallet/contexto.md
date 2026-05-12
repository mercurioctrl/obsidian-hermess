# Contexto — TareaWallet

## 2026-05-11

### Análisis del flujo de ingreso a la wallet

Se investigó cómo se crean ingresos en la wallet del sistema.

**Hallazgo principal:** No existe un endpoint dedicado de ingreso. El único tipo de ingreso
era `TR_CODIGO = 475` (comisión de referido), creado automáticamente vía `POST /syncUp/referralConversions`.

**Flujo completo:**
```
POST /syncUp/referralConversions
  → SyncUpReferralConversions (Controller)
  → ReferralConversionService::processConversions()
  → ReferralRepository::processEachConversion()  ← calcula fee %
  → WalletCreditService::creditReferralCommission()
  → WalletRepository::createReferralCreditMovement()  ← INSERT SQL
```

**Tabla:** `NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS`
**Join de usuario a cliente:** `LO.dbo.usuarios.id = NewBytes_DBF.dbo.clientes.clientLo → ID_CLIENTE`
**Cotización:** `NEW_BYTES.dbo.MS_COTIZACIONES WHERE NOMBRE = 'PESOSLO'`

**HMAC:** Cada movimiento requiere un hash HMAC-SHA256 generado con `HMAC_KEY` del .env.
Los campos firmados (en este orden exacto) son:
`ID_CCMOVIMIENTO, ID_CLIENTE, TR_CODIGO, CC_FECHAMOVIMIENTO, CC_HORAMOVIMIENTO, CC_OBSERVACIONES, CC_IMPORTEUSD, CC_ANULADO, COTIZACION`

---

### Airdrop OpcionFest — $15.000 ARS

**Objetivo:** Acreditar $15.000 ARS a todos los usuarios con email en `LO.dbo.usuarios`.
**Evento:** OpcionFest

**Decisiones tomadas:**

1. **Nuevo TR_CODIGO 476** creado en `NEW_BYTES.dbo.GL_TRANSACCIONES`:
   - `TR_NOMBRE` = 'Airdrop OpcionFest'
   - `TR_INDICADOR_SIGNO_F10` = '+' (ingreso)
   - Clonado de TR_CODIGO 475 (mismo SIS_CODIGO, PROD_CODIGO, etc.)

2. **`CC_IMPORTEUSD`** = 15000 / cotizacion (se guarda en USD, se muestra en ARS)

3. **HMAC** se genera en Python post-insert, requiere la HMAC_KEY del .env del servidor.

**Queries de ejecución (en orden):**

```sql
-- 1. Cotización
SELECT COTIZACION FROM NEW_BYTES.dbo.MS_COTIZACIONES WHERE NOMBRE = 'PESOSLO';

-- 2. Usuarios con ID_CLIENTE
SELECT c.ID_CLIENTE
FROM LO.dbo.usuarios u
INNER JOIN NewBytes_DBF.dbo.clientes c ON c.clientLo = u.id
WHERE u.email IS NOT NULL;

-- 3. Próximo ID (antes de cada insert)
SELECT MAX(ID_CCMOVIMIENTO) + 1 AS next_id
FROM NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS;

-- 4. Insert
INSERT INTO NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS
    (ID_CCMOVIMIENTO, ID_CLIENTE, TR_CODIGO,
     CC_FECHAMOVIMIENTO, CC_HORAMOVIMIENTO,
     CC_OBSERVACIONES, CC_IMPORTEUSD, CC_ANULADO,
     COTIZACION, pending, fechaMovimiento, showWallet)
VALUES (:next_id, :id_cliente, 476, :fecha, :hora,
        'airdrop_opcionfest', :importe_usd, 'NO', :cotizacion, 0, GETDATE(), 1);

-- 5. Leer para HMAC
SELECT ID_CCMOVIMIENTO, ID_CLIENTE, TR_CODIGO,
       CC_FECHAMOVIMIENTO, CC_HORAMOVIMIENTO,
       CC_OBSERVACIONES, CC_IMPORTEUSD, CC_ANULADO, COTIZACION
FROM NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS
WHERE ID_CCMOVIMIENTO = :next_id;

-- 6. Update HMAC
UPDATE NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS
SET HMAC = :hmac
WHERE ID_CCMOVIMIENTO = :next_id;
```

**HMAC en Python:**
```python
import hmac, hashlib, json
payload = json.dumps(data, separators=(',', ':'))  # orden de keys es crítico
token = hmac.new(HMAC_KEY.encode(), payload.encode(), hashlib.sha256).hexdigest()
```

> ⚠️ Probar con un solo usuario por email antes de correr masivamente.

---

## Ver también

- [[TareaWallet]]
