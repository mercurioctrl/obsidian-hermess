# Memoria del Proyecto

Consolidacion de la memoria persistente de Claude para este proyecto. Organizada por tipo.

Ultima sincronizacion: 2026-04-04

---

## Feedback (patrones tecnicos)

Lecciones aprendidas y correcciones del usuario. Estas guian el comportamiento de desarrollo.

### Docker
- **Local vs servidor:** En local, docker corre desde `mini-saas/`. En servidor Ubuntu necesita `sudo`. `git pull` puede fallar por backups con permisos root
- **Frontend rebuild:** Siempre usar `--no-cache` y reiniciar nginx despues para resolver nueva IP del container. Ver [[Stack e Infraestructura#Comandos de deploy]]

### PHP / Laravel
- **env() vs config():** Nunca usar `env()` directo en controllers. PHP-FPM no hereda env vars del container. Registrar en `config/services.php` y leer con `config()`. Ver [[Errores Comunes#env no lee variables de entorno del container en PHP-FPM]]
- **Gasto.categoria:** Es string plano, NO relacion Eloquent. Nunca usar `with('categoria')`
- **RolUsuario:** Es enum casteado. Comparar con `RolUsuario::ADMIN`, no con string ni `->value`. Ver [[Backend - Modelos#Usuario]]
- **Rutas apiResource:** Las rutas especificas (`/gastos/categorias`) deben registrarse ANTES del `apiResource`. Ver [[Errores Comunes#Rutas especificas despues de apiResource colisionan con id]]

### Frontend / Vue
- **Modal:** Siempre usar `v-model`, nunca `v-if` + `@close`. Ver [[Frontend#Componentes UI]]
- **useApi.delete con body:** Usar `{ data: {...} }`, no `{ body: {...} }`
- **useApi errores:** Los catch reciben Error estandar. Usar `e.message`, no `e?.data?.message`

---

## Proyecto (features y decisiones)

### Infraestructura
- **Docker entrypoint:** `docker-entrypoint.sh` recrea `storage/framework` dirs en cada arranque. Resuelve "valid cache path" error. Ver [[Stack e Infraestructura#Entrypoint del backend]]
- **Storage uploads:** Volumen `uploads_storage` + symlink en Dockerfile. PDFs en `pdf_storage`. Ver [[Stack e Infraestructura#Volumenes Docker]]
- **Backup/Restore:** Scripts bash `backup.sh` y `restore.sh` para backup completo (DB, PDFs, uploads, .env)

### Presupuestos
- **Edicion:** Editables en cualquier estado excepto COBRADO/FACTURADO. Moneda editable. Movimientos CC se actualizan al guardar. Ver [[Reglas de Negocio#Presupuestos - Flujo de estados]]
- **Suscripciones:** Renovacion automatica mensual. Campos: `es_suscripcion`, `suscripcion_inicio`, `suscripcion_meses`, `suscripcion_frecuencia`. Scheduler `monthlyOn(1,'03:00')`
- **Etiquetas:** Etiquetas de colores asignables desde presupuesto y proyecto. Pivot migraciones 0044-0045. Filtrable en ambos listados. Ver [[Reglas de Negocio#Etiquetas de Presupuestos]]

### Gastos
- **Cotizacion e IVA:** Cada gasto registra tasa_cambio (BCRA) e IVA (0/10.5/21/27%). Monto final = subtotal + IVA. Migracion 0047. Ver [[Reglas de Negocio#IVA en Gastos]]
- **Edicion:** Editables desde listado y proyecto. Proteccion por estado presupuesto COBRADO/FACTURADO. Campo `editable` en GastoResource. Ver [[Reglas de Negocio#Gastos - Proteccion por estado de presupuesto]]
- **Campo realizado:** Indica si el pago al acreedor fue cancelado. Toggle PATCH, desmarcar requiere admin. Migracion 0048. Ver [[Reglas de Negocio#Gastos - Campo realizado]]

### Proyectos
- **Adjuntos:** Enlaces y archivos adjuntos por proyecto. Upload a `storage/public`. Max 10MB. Ver [[Backend - API#Proyectos]]
- **Jira multi-board:** Multiples tableros Jira por proyecto. Tabla `proyecto_jira_boards`. Las columnas `jira_project_key/name` ya NO existen en proyectos
- **Orden por actividad:** Presupuestos y proyectos ordenados por `updated_at` DESC. Touch automatico al modificar hijos

### Activaciones
- **Copiar:** Copiar activaciones entre proyectos del mismo cliente. Periodo opcional. Estructura copiada, datos de ejecucion vacios
- **Eliminacion:** Requiere credenciales admin. Modal email+password. Backend valida rol ADMIN
- **PDFs:** TCPDF+FPDI sobre membretada Blu (portrait A4). Presupuestos siguen con DomPDF. Plantilla en `storage/app/templates/membretada.pdf`
- **DeepSeek IA:** Descripciones automaticas con DeepSeek API. Config en `services.php`. Campos `descripcion_ia` y `descripcion_ia_cant_hitos`

### Integraciones
- **MercadoPago:** Access token + banco vinculado. Movimientos via `/v1/payments/search`. Sync saldo manual. Conversion USD->ARS. Limitaciones API (balance 403, movements requiere permisos especiales). Ver [[Medios de Pago#MercadoPago]]
- **Stripe:** Secret key + banco vinculado. Montos en centavos. Checkout Sessions. Conversion moneda. Ver [[Medios de Pago#Stripe]]
- **Conversion monedas:** Dolar oficial BCRA venta (dolarapi.com). USD->ARS multiplica, ARS->USD divide

### Otros
- **Busqueda global:** Buscador en topbar. GET `/api/busqueda?q=`. Busca en clientes, presupuestos, proyectos, gastos. Max 5 por tipo. Ver [[Frontend#Busqueda global]]
- **Bancos y Cajas:** Transferencias, retiros, historial movimientos. Tabla `movimientos_banco_caja`. Proteccion admin para eliminar/ajustar saldo. Ver [[Reglas de Negocio#Bancos y Cajas - Saldo automatico]]
- **Dashboard multimoneda:** 6 KPI cards con tooltips info. Cobros MP/Stripe multimoneda
- **Freelance:** Tipo contrato FREELANCE agregado a empleados (migracion 0028). Ver [[Modulo Personal#Tipo de contrato]]

---

## Ver tambien

- [[Changelog]] - Registro de commits recientes
- [[Reglas de Negocio]] - Reglas de dominio
- [[Errores Comunes]] - Bugs conocidos
- [[Backend - API]] - Endpoints del sistema
