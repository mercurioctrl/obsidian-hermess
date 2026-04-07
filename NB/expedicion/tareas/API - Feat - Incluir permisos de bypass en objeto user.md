# API - Feat - Incluir permisos de bypass en objeto user

**Proyecto:** [[NB/expedicion/expedicion|Expedición]]
**Estado:** Pendiente
**Fecha:** 2026-04-06

---

## Descripción

Los 3 permisos nuevos para saltear validaciones de serials (barcode, medidas, PPU) deben venir incluidos en el objeto `user` que se obtiene del token/auth, tal como ya ocurre con otros permisos del sistema.

De esta forma, el controller (`ProvidersOrderSerial`) no necesita hacer una consulta extra a `permisos_agente` en cada request, sino que lee los permisos directamente del usuario autenticado.

### Contexto

Esto es un requisito previo / complementario a la tarea [[NB/expedicion/tareas/API - Feat - Permisos por agente para saltear validaciones de serials|Permisos por agente para saltear validaciones de serials]]. Los permisos se crean en esa tarea; esta tarea se encarga de que lleguen al objeto user.

### Comportamiento esperado

- Al autenticarse, el sistema consulta `permisos_agente` y carga los permisos del usuario
- Los 3 permisos de bypass se incluyen en el objeto `user` (igual que los demás permisos)
- Cualquier controller/service puede consultar `$user->permisos` (o como esté modelado) sin query adicional

## Criterios de aceptación

- [ ] Los 3 permisos de bypass (barcode, medidas, PPU) se cargan en el objeto user al autenticarse
- [ ] Se sigue el mismo patrón que ya usan los demás permisos del sistema
- [ ] El controller `ProvidersOrderSerial` puede leer los permisos desde el request/user sin consulta extra
- [ ] No se rompe la carga de permisos existentes
- [ ] Si el usuario no tiene estos permisos asignados, simplemente no aparecen (sin error)

## Notas técnicas

### Investigar

- Cómo se arma actualmente el objeto `user` al autenticarse (endpoint `/auth/login` o `/auth/user`)
- Dónde se consulta `permisos_agente` y cómo se inyectan los permisos en el token/sesión
- Formato actual del objeto de permisos (array, objeto, flags booleanos, etc.)

### Archivos probablemente involucrados

- Endpoint de auth / login (ver `App/Routes/`)
- Middleware de autenticación
- Servicio o repositorio que consulta `permisos_agente`
- `ProvidersOrderSerial.php` — consumidor final de estos permisos

## Ver también

- [[NB/expedicion/tareas/API - Feat - Permisos por agente para saltear validaciones de serials|Tarea: Permisos por agente para saltear validaciones]]
- [[NB/expedicion/arquitectura|Arquitectura]]
- [[NB/expedicion/documentacion|Documentación]]
