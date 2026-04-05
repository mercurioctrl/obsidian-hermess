# Frontend - Nuxt 3

## Configuracion (nuxt.config.ts)

```ts
ssr: false                  // SPA PURA. Auth usa localStorage, no cookies.
components: [{ path: '~/components', pathPrefix: false }]
// Componentes de components/ui/ se usan SIN prefijo
// OK: <FormField> <Modal> <DataTable>
// MAL: <UiFormField> <UiModal>

runtimeConfig.public.apiBase = NUXT_PUBLIC_API_BASE || 'http://localhost/api'
```

Ver [[Errores Comunes#Componentes UI con prefijo de directorio]].

## Estructura de paginas

```
pages/
+- login.vue                    <- layout: auth
+- index.vue                    <- Dashboard
+- clientes/                    <- CRUD + cuenta corriente
+- presupuestos/                <- Listado + detalle + PDF + etiquetas
+- proyectos/                   <- Detalle + gastos + Jira + activaciones
+- evidencias/                  <- Activaciones con hitos + IA
+- gastos/                      <- CRUD + cotizacion + IVA
+- mercury/                     <- Integracion Mercury Bank
+- mercadopago/                 <- Integracion MercadoPago
+- bancos-cajas/                <- Cards BANCO/CAJA + integraciones
+- cuenta-corriente/            <- Deudores
+- staff/                       <- Empleados (ver [[Modulo Personal]])
+- usuarios/                    <- Solo admin (ver [[Modulo Permisos]])
+- configuracion/               <- Solo admin
```

## Layouts

| Layout | Uso |
|--------|-----|
| `default` | Todas las paginas autenticadas. Sidebar + topbar + busqueda global |
| `auth` | Solo `/login`. Sin sidebar |

## Middleware

**Un solo middleware:** `middleware/auth.global.ts` (se aplica a TODAS las rutas).

> **NUNCA** usar `definePageMeta({ middleware: 'auth' })`. Ver [[Errores Comunes#definePageMeta middleware auth rompe la navegacion]].

El middleware verifica permisos `VER_SECCION_*` para rutas no-admin. Ver [[Modulo Permisos#Frontend]].

## Busqueda global

Input en el topbar derecho. Busca via `GET /api/busqueda?q=texto`.
- Debounce 300ms, minimo 2 caracteres
- Dropdown con resultados agrupados por tipo
- Navegacion con flechas + Enter
- Atajo de teclado `/` para enfocar

## Stores (Pinia)

### `stores/auth.ts`
```ts
state:
  token: ref<string | null>    // leido de localStorage
  usuario: ref<Usuario | null>
computed:
  isAdmin: usuario?.rol === 'ADMIN'
  verMontos: ADMIN || permisos.includes('VER_MONTOS_SALDOS')
methods:
  fetchMe()    // GET /auth/me -> data?.data ?? data (desenvolver wrapper!)
  logout()
  tienePermiso(key: string)
```

> `fetchMe()` debe usar `data?.data ?? data`. Ver [[Errores Comunes#auth me devuelve wrapper data y fetchMe lo ignora]].

### `stores/config.ts`
```ts
state: config: ref<Configuracion | null>
methods: fetchConfig()  // GET /config, con cache interna
```

## Composables

### `composables/useApi.ts`
```ts
api.get<T>(endpoint)
api.post<T>(endpoint, body)
api.put<T>(endpoint, body)
api.delete<T>(endpoint)
// Auto: Bearer token, 401 -> redirect /login, 204 -> retorna {}
```

> Para DELETE con body: `api.delete(url, { data: {...} })`, NO `{ body: {...} }`.
> En catch: usar `e.message`, NO `e?.data?.message`.

### `composables/useNotification.ts`
```ts
const { success, error, info } = useNotification()
```

## Componentes UI

Usados SIN prefijo gracias a `pathPrefix: false`. Ver [[Componentes UI]] para specs detalladas.

| Componente | Uso |
|-----------|-----|
| `<FormField>` | Input con label, error, hint |
| `<DataTable>` | Tabla con columnas configurables |
| `<Modal>` | Dialog modal. **Siempre con `v-model`**, nunca `v-if` + `@close` |
| `<StatusBadge>` | Badge de estado coloreado |
| `<StatsCard>` | Card de KPI |
| `<Toast>` | Notificaciones toast |

## Iconos

```vue
<!-- SIEMPRE con prefijo lucide: -->
<Icon name="lucide:search" class="w-4 h-4" />
<!-- NUNCA sin prefijo (se renderiza como texto) -->
```

Ver [[Errores Comunes#Iconos sin prefijo lucide se renderizan como texto]].

## Sistema de diseno

Ver [[Design Tokens]] para la especificacion completa.

```
Fondo: #F5F5F0 | Sidebar: #F7F7F2 | Cards: white
Bordes: #E8E8E3 | Accent verde: #2D8C5A | Texto: #1A1A1A
Tipografia: Inter (UI) + JetBrains Mono (numeros)
```

## Navegacion (sidebar)

```
Principal:
  / (Dashboard)        lucide:layout-dashboard
  /presupuestos        lucide:clipboard-list
  /proyectos           lucide:bar-chart-2
  /evidencias          lucide:folder (Activaciones)
  /clientes            lucide:building-2
  /cuenta-corriente    lucide:arrow-left-right
Operaciones:
  /gastos              lucide:credit-card
  /bancos-cajas        lucide:landmark
  /mercury             lucide:wallet
  /mercadopago         lucide:smartphone
Administracion (solo admin):
  /staff (Personal)    lucide:users
  /usuarios            lucide:shield
  /configuracion       lucide:settings
```

## Modulo Activaciones

El sidebar lo llama "Activaciones" pero la ruta es `/evidencias`.

- `/evidencias/{id}`: tabla de hitos con edicion inline, QB auto-calculado, columna Jira, busqueda Jira, descripcion IA con DeepSeek
- En `proyectos/[id].vue`: card "ACTIVACIONES" en sidebar

## Modulo Jira (en proyectos/[id].vue)

- Multi-board: tabs por board vinculado
- Tablero de issues con 3 botones de categoria (Por hacer / En curso / Finalizado)
- Buscador inline con debounce 400ms
- Vinculacion Jira <-> Activaciones: badge verde "Act. #N" o boton "Crear hito"

## Modulo MercadoPago

Ver [[Medios de Pago#MercadoPago]] para detalle backend. Branding celeste `#009ee3`.

## Modulo Stripe

Ver [[Medios de Pago#Stripe]] para detalle backend. Branding purpura `#635BFF`.

## Modulo Mercury

Ver [[Medios de Pago#Mercury]] para detalle backend. Branding azul `#0A85E0`.

---

## Ver tambien

- [[Backend - API]] - Endpoints que consume
- [[Design Tokens]] - Paleta de colores y tipografia
- [[Componentes UI]] - Specs de componentes reutilizables
- [[Layout System]] - Estructura sidebar + contenido
- [[Modulo Permisos]] - Control de acceso en frontend
- [[Errores Comunes]] - Bugs frecuentes de frontend
