# Contexto — Penales

## Reglas de negocio (ranking / ganadores)

- **Orden:** más goles → menos tiempo → más atajadas → id menor. El tiempo es el **primer desempate**, no el criterio principal.
- **Email = identidad:** una sola "mejor marca" por email (upsert). Si jugás de nuevo con peor puntaje, la API responde `success:true` pero conserva y devuelve tu marca anterior (mejor).
- **Nombre único por email:** usar un nombre ya registrado por otro email → 409 "Ese nombre ya está en uso".
- **Métricas:** goles (máx 5), atajadas (máx 5), tiempo (segundos desde el 1er penal hasta el game over).

## Anti-cheat

- **Token de sesión one-time-use** (`penales/start`): `nonce:timestamp:HMAC(app.key)`, TTL 30 min, **edad mínima 5 s** (enviar antes → 403 "Token demasiado reciente").
- **Firma HMAC del payload** (`{token}:{goles}:{atajadas}:{tiempo}`) con clave compartida front/back.
- **Clave HMAC hardcodeada** en `PenalesTokenService::PAYLOAD_SECRET = 'peñales-2025-x7k9'` → **debe coincidir** con `PENALES_FIRMA_KEY` del `.env` del front.

## Decisiones / cosas que no funcionaron

- **Fondos `fondov2.png` y `bannerv3.png` descartados como fondo desktop.** El arco de esas imágenes tiene otra proporción/posición que `banner.png`, y el juego dibuja arquero/pelota/arco en coordenadas fijas calibradas a mano. Adaptarlo requería distorsionar la imagen o cambiar las constantes del juego (`KEEPER_Y`, `KICK_TARGETS`, `KEEPER_JUMP_X`).
  - **Recomendación:** que el diseñador arme el fondo respetando el layout de `banner.png` (arco a la misma altura/tamaño) y entra sin tocar la lógica.

## Pendientes

- **DB de desarrollo:** apuntar la API v4 a `10.10.10.47:1433` está pendiente de **credenciales** (usuario/pass/base). El servidor responde pero da "Login failed for user 'web'". El `.env` quedó apuntando a **producción** (`190.210.23.97:4444`); el host de dev quedó comentado.
- **UX (opcional):** cuando alguien reenvía con su mismo email y peor puntaje, el front (`leaderboard.js`) muestra `data` sin aclarar que "se mantiene tu mejor marca".

## Ver también

- [[arquitectura]] — cómo se implementa esto.
- [[changelog]] — cuándo se hizo cada cosa.
