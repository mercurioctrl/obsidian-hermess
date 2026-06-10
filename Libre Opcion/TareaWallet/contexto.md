# Contexto — TareaWallet

## 2026-06-07

### Integración de pasarelas de pago — MODO, GetNet, Payway

**Objetivo:** Integrar MODO (billetera digital QR), GetNet y Payway como medios de pago en el checkout.

**Problema principal resuelto — MODO QR no aparecía:**

El flujo de `confirmar.vue` llama en `asyncData` a `store.dispatch("checkout/obtenerPedido", { query, step: 3 })`.
Ese action hace fetch a la API v3, que devuelve `medioPagoId = 0` (no conoce MODO, cuyo id es 5079 y es frontend-only).
Luego llama `commit("ACTUALIZAR_PEDIDO", response)` que reemplaza todo `state.pedido` via `Vue.set`, borrando el `medioPagoId` seleccionado.

**Fix en `checkout.js`:**
```js
const medioPagoIdPrevio = state.pedido?.paquetes?.[0]?.pago?.medioPagoId ?? 0;
commit("ACTUALIZAR_PEDIDO", response);
if (medioPagoIdPrevio !== 0 && state.pedido.paquetes[0]?.pago?.medioPagoId === 0) {
  const paquetesRestaurados = state.pedido.paquetes.map((p, i) =>
    i === 0 ? { ...p, pago: { ...p.pago, medioPagoId: medioPagoIdPrevio } } : p
  );
  commit("ACTUALIZAR_PAQUETES", paquetesRestaurados);
}
```

**Problema secundario resuelto — 404 en rutas nuevas de pago:**

Las rutas `payment/modo/create-intention`, `payment/getnet/tokenize` y `payment/payway/tokenize` fueron añadidas al `routes/api.php` pero PHP-FPM tenía OPcache activo con una versión vieja del archivo en memoria. Retornaban 404 a pesar de que via tinker el router sí las encontraba. Fix: reiniciar el contenedor (`docker restart sitio-api-rest-4.1-laravel`).

> ⚠️ Después de añadir rutas nuevas al API, siempre reiniciar el contenedor para limpiar OPcache de PHP-FPM.

**Arquitectura MODO SDK v2:**
- Auth: `POST {MODO_URL_API}/v2/stores/companies/token` con `username/password`
- Payment: `POST {MODO_URL_API}/v2/payment-requests/` con Bearer token
- Frontend SDK: `https://ecommerce-modal.preprod.modo.com.ar/bundle.js`
- Init: `window.ModoSDK.modoInitPayment({ version: '2', qrString, checkoutId, deeplink, ... })`
- Env preprod: `MODO_URL_API=https://merchants.preprod.playdigital.com.ar`

**ID de medio de pago MODO:** 5079 (frontend-only, no existe en la API v3 ni en la DB de medios de pago)

**Medios de pago pendientes de test en navegador:**
- Payway — backend confirmado OK, frontend listo
- GetNet — servidor `190.189.93.116` necesita ser whitelisteado en Santander sandbox

---

## 2026-05-12

### Análisis sistema de recategorización (LIO-630)

Se revisó la feature de Franco en rama `LIO-630-api-review-recategorizar-productos-sin-categoria-concurrencia-del-job-y-filtro-solo-con-stock`.

**Hallazgos clave:**

- El `CategoriaMatcher` está **completamente hardcodeado** en PHP: keywords, exclusiones e IDs de categoría destino son reglas escritas a mano por Franco basadas en conocimiento del catálogo.
- Las tablas `categoriasPrediccionMatchFree/Required/Exclude` existen en DB con 545/8/581 filas respectivamente pero **no están conectadas** al matcher. `precargarMapas()` está vacío.
- El campo `via` puede ser `nombre`, `alias` o `switch`, pero el matcher actual **solo devuelve `switch`** — los otros dos nunca se incrementan.
- El orden de las reglas en `resolverPorTitulo` es intencional: mousepad antes que mouse, discos antes que notebook, cable al final por ser genérico.

**Control de concurrencia (último commit):**
- Doble bloqueo: Service verifica corrida activa antes de crear el Job, y el Job hace UPDATE atómico para marcar `running`.
- `solo_con_stock=true` es obligatorio — hardcodeado en el Service, retorna 422 si no se cumple.

**Diseño propuesto para migrar a DB-driven:**
- Parsear `%A%B%` → lista de tokens ordenados
- Índice invertido: `primer_token → [(categoria, tokens[])]`
- Aplicar Free → filtrar con Exclude → validar Required → resolver por especificidad (más tokens gana)
- Ver [[arquitectura-recategorizacion]] para detalle completo

---

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
- [[arquitectura-recategorizacion]]
- [[changelog]]
