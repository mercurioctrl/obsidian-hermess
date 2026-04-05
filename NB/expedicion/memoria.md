# Memoria — Expedición

Registro de decisiones, problemas y soluciones encontradas durante el trabajo en el proyecto.

---

## 2026-04-05 — Setup inicial en Apple Silicon

### Problema: Dockerfile no buildea (Ubuntu 18.04 EOL)

**Síntoma:** `docker-compose up --build` falla con `Unable to locate package msodbcsql17`

**Causa raíz:** Ubuntu 18.04 es EOL. Microsoft dejó de publicar paquetes ODBC para esa versión. Además, `msodbcsql17` no tiene binarios ARM64 (Apple Silicon).

**Solución aplicada:**
1. Actualizar base image de Ubuntu 18.04 → **22.04**
2. Actualizar PHP 8.0 → **8.3** (8.0 fue removido del PPA de ondrej)
3. Cambiar `msodbcsql17` → **`msodbcsql18`** (tiene binarios ARM64)
4. Instalar `sqlsrv` y `pdo_sqlsrv` via PECL (la versión actual requiere PHP >= 8.3)
5. Los `.so` pre-compilados del repo (`docker/sqlsrv.so`, `docker/pdo_sqlsrv.so`) ya no se usan — eran para PHP 8.0 (API 20200930)

**Archivos modificados:**
- `docker/Dockerfile` — reescrito completo
- `docker-compose.yml` — path del php.ini actualizado a 8.3

---

### Problema: ODBC Driver 18 falla con error 0x2746

**Síntoma:** `SQLSTATE[08001]: [Microsoft][ODBC Driver 18 for SQL Server]TCP Provider: Error code 0x2746`

**Causa raíz:** ODBC Driver 18 fuerza TLS por defecto. Ubuntu 22.04 usa OpenSSL 3.x que tiene requisitos más estrictos de TLS. El SQL Server remoto (legacy) no soporta los niveles de TLS que OpenSSL 3.x exige.

**Solución aplicada (dos partes):**

1. **DSN con flags de encriptación** en `app/src/App/Database.php`:
   ```
   sqlsrv:Server=HOST,PORT;Database=DB;TrustServerCertificate=yes;Encrypt=no
   ```

2. **Reconfigurar OpenSSL** en el Dockerfile para bajar el security level:
   ```
   [ssl_sect]
   system_default = system_default_sect
   [system_default_sect]
   MinProtocol = TLSv1
   CipherString = DEFAULT@SECLEVEL=0
   ```

**Importante:** Solo cambiar el DSN NO es suficiente. El ODBC Driver 18 usa OpenSSL a nivel sistema, y OpenSSL 3.x rechaza la conexión antes de que los flags del DSN apliquen. Se necesitan ambas cosas.

**Archivos modificados:**
- `app/src/App/Database.php` — DSN actualizado
- `docker/Dockerfile` — OpenSSL config agregada

---

### Problema: Frontend no compila (Node.js 25 + Webpack 4)

**Síntoma:** `Error: error:0308010C:digital envelope routines::unsupported`

**Causa raíz:** Node.js 25 usa OpenSSL 3.x internamente. Webpack 4 (usado por Nuxt 2) usa funciones hash de OpenSSL legacy (MD4) que fueron deshabilitadas en OpenSSL 3.x.

**Solución:** Agregar variable de entorno al arrancar:
```bash
NODE_OPTIONS=--openssl-legacy-provider npm run dev
```

**No se modificó ningún archivo.** Es un workaround de runtime.

---

### Problema: Falta build-version.json

**Síntoma:** `Cannot find module '../build-version.json'` al iniciar Nuxt

**Causa raíz:** El server-middleware `version.js` importa `build-version.json` que se genera con el script `prebuild` y no está en git.

**Solución:**
```bash
node scripts/update-build-version.js
```

---

### Conexión Front ↔ Back

**Problema:** `API_HOST` vacío en el `.env` del frontend.

**Solución:** Setear `API_HOST=http://localhost:8084/v1` en `expedicion-web-app-v1/app/.env`

---

## Decisiones de arquitectura

### Por qué PHP 8.3 y no 8.0/8.1

- PHP 8.0: removido del PPA de ondrej (EOL desde Nov 2023)
- PHP 8.1: las extensiones PECL sqlsrv actuales requieren PHP >= 8.3
- PHP 8.3: compatible con Slim 4, extensiones PECL se instalan sin problemas
- El código del proyecto es compatible sin cambios (solo warnings menores de `use` statements en Database.php)

### Por qué ODBC 18 y no 17

- `msodbcsql17` no tiene binarios ARM64 (Apple Silicon)
- `msodbcsql18` sí los tiene
- La diferencia principal es que 18 fuerza encriptación por defecto (resuelto con OpenSSL config)

---

## Gotchas conocidos

1. **DB credentials en `$_SERVER`**, no en `$_ENV` — las variables `DB_USER` y `DB_PASS` se leen de `$_SERVER` en `Database.php`
2. **Multi-database JOINs** — queries frecuentes hacen LEFT JOIN entre `NB_WEB`, `NEW_BYTES` y `NewBytes_DBF` (requiere SQL Server cross-database)
3. **JWT secret hardcodeado** en `TokenManager.php` y `TokenManagerAdmin.php`
4. **Sin tests** — ni PHPUnit ni Jest/Vitest configurados
5. **Firebase SW config hardcodeada** — `static/firebase-messaging-sw.js` tiene config de Firebase inline (no usa env vars), inmutable después del build
6. **Pagination 300** — `BIGGER_INITIAL_ITEMS_PER_PAGE=300` para envíos/retiro parece excesivo para el frontend

---

## Ver también

- [[NB/expedicion/arquitectura|Arquitectura]] — Decisiones de diseño actuales
- [[NB/expedicion/stack|Stack]] — Versiones que explican estas decisiones
- [[NB/expedicion/documentacion|Documentación]] — Setup con los workarounds aplicados
- [[NB/expedicion/changelog|Changelog]] — Cuándo se hicieron estos cambios
- [[NB/expedicion/contexto|Contexto]] — Estado general del proyecto
