# Backend - API Routes y Controllers

## Estructura de autenticacion

```
POST /api/auth/login         <- publico
GET  /api/presupuestos/*/pdf <- token via query string
Todo lo demas -> middleware auth:sanctum (Bearer token)
Rutas de admin -> middleware adicional EnsureIsAdmin
```

## Auth
```
POST   /api/auth/login       -> AuthController@login
POST   /api/auth/logout      -> AuthController@logout
GET    /api/auth/me          -> AuthController@me
```

## Busqueda global
```
GET    /api/busqueda          -> BusquedaController (invokable)
         param: q (string, minimo 2 caracteres)
         Busca en: clientes, presupuestos, proyectos, gastos
```

Ver [[Frontend#Busqueda global]] para la UI.

## Clientes
```
GET    /api/clientes                  -> index (filtros: search, activo)
POST   /api/clientes                  -> store
GET    /api/clientes/{id}             -> show [con wrapper data:]
PUT    /api/clientes/{id}             -> update [con wrapper data:]
DELETE /api/clientes/{id}             -> destroy (soft: activo=false)
GET    /api/clientes/{id}/cuenta      -> cuenta (movimientos)
GET    /api/clientes/{id}/presupuestos
GET    /api/clientes-export/csv
```

## Presupuestos
```
GET    /api/presupuestos              -> index
         filtros: estado, cliente_id, search, etiqueta_id, mes, anio
         (mes y anio filtran sobre presupuestos.fecha)
POST   /api/presupuestos              -> store [con wrapper data:]
GET    /api/presupuestos/{id}         -> show [con wrapper data:]
PUT    /api/presupuestos/{id}         -> update [con wrapper data:]
DELETE /api/presupuestos/{id}         -> destroy (solo BORRADOR)
POST   /api/presupuestos/{id}/transicion -> cambio de estado
GET    /api/presupuestos/{id}/pdf
POST   /api/presupuestos/{id}/etiquetas      -> syncEtiquetas
POST   /api/presupuestos/{id}/crear-proyecto
POST   /api/presupuestos/{id}/enviar-invoice -> enviarInvoice
         body: email (required|email)
         efecto: guarda email en cliente si cambió, envía Mailable con PDF adjunto
         BCC automático a payments@blustudioinc.com (MAIL_PAYMENTS_BCC)
```

Ver [[Reglas de Negocio#Presupuestos - Flujo de estados]] para transiciones y efectos automaticos.

**Transicion a COBRADO** requiere `banco_caja_id` + `email` + `password` en el body. Ver [[Reglas de Negocio#Operaciones que requieren credenciales admin]].

**Envío de invoice:** El Mailable `PresupuestoInvoiceMail` genera el PDF in-memory con `Pdf::loadView(...)->output()` (no toca filesystem) y lo adjunta. El BCC se setea en el `Envelope()` del Mailable, no en el controller. Ver [[Stack e Infraestructura#Mail SMTP]] y [[memoria#Mail SMTP y envío de invoices]].

> Nota sobre el param `anio`: se usa ASCII (no `año`) en query params para evitar issues de encoding URL/PHP. Ver [[memoria#Query params sin caracteres no-ASCII]].

## Proyectos
```
GET    /api/proyectos                        -> index (sin wrapper)
         filtros: etiqueta_id, cliente_id, mes, anio
         (mes y anio filtran sobre proyectos.fecha_inicio)
GET    /api/proyectos/{id}                   -> show (sin wrapper, incluye empleados, jira_boards)
PUT    /api/proyectos/{id}                   -> update
POST   /api/proyectos/{id}/empleados         -> asignarEmpleado
DELETE /api/proyectos/{id}/empleados/{emp}   -> desasignarEmpleado
GET    /api/proyectos/{id}/adjuntos
POST   /api/proyectos/{id}/adjuntos/enlace
POST   /api/proyectos/{id}/adjuntos/archivo  -> multipart, max 10MB
DELETE /api/proyectos/{id}/adjuntos/{adj}
POST   /api/proyectos/{id}/jira-boards       -> vincularJiraBoard
DELETE /api/proyectos/{id}/jira-boards/{board}
```

Ver [[Frontend#Modulo Jira]] para la integracion de tableros.

## Cuenta Corriente
```
GET    /api/cuenta-corriente/{cliente_id}  -> movimientos (sin wrapper)
POST   /api/cuenta-corriente               -> crear movimiento manual
GET    /api/cuenta-corriente-deudores
GET    /api/cuenta-corriente-resumen
```

Ver [[Reglas de Negocio#Cuenta Corriente vs Gastos]] para la distincion.

## Bancos y Cajas
```
GET    /api/bancos-cajas           -> index (sin wrapper)
POST   /api/bancos-cajas           -> store
PUT    /api/bancos-cajas/{id}      -> update
DELETE /api/bancos-cajas/{id}      -> destroy (falla si tiene gastos)
POST   /api/bancos-cajas/{id}/ajuste -> ajuste manual de saldo
```

## Gastos
```
GET    /api/gastos                 -> index paginado [con wrapper data: + meta]
GET    /api/gastos/{id}            -> show [con wrapper data:, incluye campo editable]
POST   /api/gastos                 -> store (descuenta saldo BancoCaja)
PUT    /api/gastos/{id}            -> update (ajusta diferencia)
DELETE /api/gastos/{id}            -> destroy (devuelve saldo)
GET    /api/gastos/categorias      -> lista de categorias (ANTES del apiResource!)
POST   /api/gastos/categorias      -> crear categoria
GET    /api/gastos/cotizacion      -> cotizacion dolar oficial BCRA
GET    /api/gastos-resumen
```

> Las rutas `/gastos/categorias` y `/gastos/cotizacion` deben registrarse ANTES del `apiResource`. Ver [[Errores Comunes#Rutas especificas despues de apiResource colisionan con id]].

> `monto` es calculado por el controller, nunca se envia desde el [[Frontend]]. Ver [[Reglas de Negocio#IVA en Gastos]].

> Proteccion por estado: PUT y DELETE fallan con 422 si presupuesto COBRADO/FACTURADO. Ver [[Reglas de Negocio#Gastos - Proteccion por estado de presupuesto]].

## Dashboard
```
GET    /api/dashboard              -> KPIs
GET    /api/dashboard/ingresos-gastos -> datos mensuales para grafico
```

## Staff y Empleados
Ver [[Modulo Personal]] para documentacion completa.
```
GET    /api/staff                  -> usuarios del sistema (sin wrapper)
GET|POST|PUT|DELETE /api/empleados/{id}
POST   /api/empleados/{id}/proyectos
DELETE /api/empleados/{id}/proyectos/{proy}
GET|POST /api/empleados/{id}/pagos
DELETE /api/empleados/{id}/pagos/{pago}
```

## Jira (integracion externa)
```
POST   /api/jira/test
GET    /api/jira/projects
GET    /api/jira/projects/{key}/statuses
GET    /api/jira/projects/{key}/issues      -> cursor-based
GET    /api/jira/projects/{key}/search-issues
GET    /api/jira/hitos
POST   /api/jira/issues/{issueKey}/crear-hito
```

Auth Jira: Basic Auth con `email:api_token` de Atlassian. Configurado en tabla `configuracion`.

## Evidencias / Activaciones
```
GET    /api/evidencias                      -> index
         filtros: proyecto_id, etiqueta_id, cliente_id, mes, anio
         (mes y anio filtran sobre pruebas_ejecucion.periodo_desde)
         (cliente_id filtra via proyecto.presupuesto.cliente_id)
POST   /api/evidencias                      -> store
GET|PUT|DELETE /api/evidencias/{evidencia}  -> CRUD
POST   /api/evidencias/{evidencia}/generar-descripcion -> IA con DeepSeek
POST   /api/evidencias-copiar              -> copiar entre proyectos
GET    /api/evidencias/{evidencia}/pdf      -> PDF sobre membretada
```

> Parametro de ruta es `{evidencia}` (no `{prueba}`).

## MercadoPago, Stripe, Mercury
Ver [[Medios de Pago]] para documentacion completa de las tres integraciones.

## Etiquetas
```
GET    /api/etiquetas              -> listado (sin wrapper)
POST   /api/etiquetas              -> crear (body: nombre, color)
PUT    /api/etiquetas/{id}
DELETE /api/etiquetas/{id}         -> cascade borra pivots
```

## Config y Usuarios
```
GET    /api/config      -> configuracion empresa
PUT    /api/config      -> solo admin
GET|POST|PUT|DELETE /api/usuarios  -> solo admin [con wrapper data:]
PUT    /api/usuarios/{id}/password -> solo admin
```

## wrapper `data:` en respuestas

| Con wrapper `data:` | Sin wrapper (JSON directo) |
|--------------------|--------------------------|
| /clientes/{id} | /proyectos |
| /presupuestos/{id} | /bancos-cajas |
| /gastos (paginado) | /dashboard |
| /usuarios | /gastos/categorias |
| | /cuenta-corriente-* |
| | /staff, /empleados |
| | /etiquetas |
| | /mercadopago/*, /stripe/*, /mercury/* |

**Patron frontend siempre seguro:** `const res = await api.get(...); modelo.value = res?.data ?? res`

Ver [[Errores Comunes#Olvidar el wrapper data en endpoints que usan API Resource]].

---

## Ver tambien

- [[Backend - Modelos]] - Modelos que usan estos endpoints
- [[Frontend]] - Paginas que consumen esta API
- [[Modulo Permisos]] - Enmascaramiento de campos sensibles
- [[Medios de Pago]] - Endpoints de MP, Stripe, Mercury
- [[Errores Comunes]] - Bugs frecuentes de API
- [[memoria]] - Convenciones de filtros y query params
