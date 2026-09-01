# Checklist: agregar un permiso nuevo en permisos_agente

Para agregar un **permiso nuevo** (flag booleano por agente) en el backend hay que tocarlo en **4 lugares**, no 2. Omitir cualquiera hace que el flag no llegue al front.

1. **Columna** en `NB_WEB.dbo.permisos_agente` (`ALTER TABLE ... ADD {flag} BIT NOT NULL DEFAULT 0`), en el `.sql` del feature.
2. **`Repositories/Auth/AuthRepository.php`** — `ISNULL(permisos_agente.{flag}, 0) as {flag}` en **las DOS** queries: `login()` (~L21) y `getByToken()` (~L70).
3. **`Dto/Auth/UserDto.php`** — ⚠️ **el gotcha**: `UserDto` es una **lista blanca** de propiedades. `GET /auth/user` (lo que puebla `$auth.user` vía `@nuxtjs/auth-next`) pasa por este DTO. Si el flag no está declarado + asignado en el constructor, **no llega al front** aunque el SQL lo devuelva. Agregar `public bool ${flag};` y `$this->{flag} = (bool)($data->{flag} ?? false);`.
4. **Middleware** (si la ruta se gatea): `Http/Middleware/{X}Middleware.php` (patrón `RebillMiddleware`), 401 si `empty($user->{flag})`, aplicado al grupo de rutas.

**Por qué:** El token embebe el user de `login()` (row crudo, ahí sí llega), pero `$auth.user` se puebla desde `/auth/user` (`autoFetchUser`), que devuelve `UserDto`. En 2026-09 la pestaña de [[feature-modulo-presupuestos|Presupuestos]] no aparecía justamente por faltar el paso 3.

**Aplicar:** después de tocar los 4 lugares, `/auth/user` lee la base en vivo (getByToken), así que **un refresh** del front alcanza (no hace falta re-login). Habilitar a un usuario: `UPDATE NB_WEB.dbo.permisos_agente SET {flag}=1 WHERE agente_fp={idVendedor}`.

Mismo patrón que el flag `includeNull` (ese estaba solo en AuthRepository, sin UserDto, porque no lo consumía el front).

## Ver también

- [[feature-modulo-presupuestos]] — primer uso de este checklist (permiso `presupuestos`)
