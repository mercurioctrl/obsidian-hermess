# Changelog — Expedición

Registro de cambios del proyecto, consolidado desde los repositorios de API y Frontend.

---

## 2026-04-05

### Setup local (sesión con Claude)
- refactor: Dockerfile actualizado de Ubuntu 18.04 a 22.04, PHP 8.0 a 8.3, ODBC 17 a 18 (ARM64)
- fix: Configuración OpenSSL para compatibilidad con SQL Server legacy (error 0x2746)
- fix: DSN actualizado con `TrustServerCertificate=yes;Encrypt=no` para ODBC Driver 18
- config: Frontend conectado al backend local (`API_HOST=http://localhost:8084/v1`)
- config: Generado `build-version.json` para server middleware
- docs: Creada base de conocimiento en Obsidian (`NB/expedicion/`)
- docs: Configurada bóveda de Obsidian en CLAUDE.md

Archivos principales: `docker/Dockerfile`, `docker-compose.yml`, `app/src/App/Database.php`, `expedicion-web-app-v1/app/.env`

---

## 2026-04-04

### API
- feat(EXP-538): Datos adicionales de expedición en respuestas API
- feat(LAW-59): Unlock hand y dispatch — permisos para bypass de autorización en armado y despacho

### Frontend
- feat(EXP-537): Nuevo permiso `expMakeVoucher` para generación de facturas
- refactor(LAW-60): Evitar autorización en finalizar armado si el usuario tiene permiso `expUnlockHand`
- refactor(LAW-58): Evitar autorización en despacho si el usuario tiene permiso `expUnlockDispatch`

---

## 2026-04-01

### API
- feat: Campo `expMakeVoucher` (`exp_facturacion`) agregado al JWT y respuesta de `/auth/user`
- fix: Corrección en providers repository

### Frontend
- refactor: Permiso de facturación depende de campo específico de usuario (`expMakeVoucher`)

---

## 2026-03-31

### API
- fix: Token y auth corrections (múltiples fixes)
- feat: Implementación de unlock hand y dispatch en backend

### Frontend
- refactor(LAW-60): Permiso `expUnlockHand` bypass en armado
- refactor(LAW-58): Permiso `expUnlockDispatch` bypass en despacho

---

## 2026-03-30

### API
- feat(EXP-534): Datos de expedición extendidos
- feat(EXP-531): Pending counts filtrados por company code

### Frontend
- refactor(EXP-532): Company code en burbujas de pendings, alineado con cantidades de pestañas
- refactor(EXP-535): Pestañas visibles según permiso de visualización del usuario
- refactor(EXP-530): Enviar `eTicket` en vez de `factura` si la orden es de Laset
- feat: Icono de Laset en Logo si el cliente es de esa empresa

---

## 2026-03-27

### API
- feat: Permisos de expedición agregados al JWT y endpoint `/auth/user`
- feat(EXP-531): Pending with filter company code

### Frontend
- refactor(EXP-535): Mostrar/ocultar pestañas según permisos del usuario

---

## 2026-03-19

### API
- fix: Cotización de nota de crédito en expedición

---

## 2026-03-06

### Frontend
- refactor(EXP-530): e-Ticket para órdenes de Laset en vez de factura

---

## 2026-02-09–10

### Frontend
- feat(EXP-528): Información extendida del envío y confección del paquete
- refactor(EXP-526): Agregar `stockWarehouseId` al ingreso de seriales
- style: Formateo ESLint aplicado
