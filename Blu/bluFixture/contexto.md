# Contexto y patrones — bluFixture

## Reglas de negocio

### Pronósticos
- Un participante puede pronosticar hasta que el partido **inicia** (no hasta que finaliza)
- Los pronósticos de otros participantes son **invisibles hasta que el partido finaliza**
- Puntos se calculan automáticamente al marcar `finalizado = true`
  - `pts_exacto` (default 3): marcador exacto (goles local Y visitante correctos)
  - `pts_resultado` (default 1): solo resultado correcto (ganador o empate)

### Empresas
- Cada empresa es un tenant aislado (participantes, pronósticos, comentarios)
- El slug es único y define la URL de login branded `/{slug}`
- El `logo_fondo` puede ser `'color'` (usa `color_primario` de fondo) o `'transparente'` (fondo blanco)

### Registro por link
- Admin genera token de 48 chars → URL pública `/registro/{token}`
- Admin puede cerrar la inscripción (el link deja de funcionar)
- Admin puede regenerar el token (invalida el anterior)
- Al registrarse, el participante queda auto-logueado (backend devuelve Sanctum token)

---

## Patrones de código

### Fetch con auth (useApi)

```typescript
const api = useApi()
// GET
const res = await api.get('/endpoint')
// POST JSON
const res = await api.post('/endpoint', body)
// PUT JSON
const res = await api.put('/endpoint', body)
// DELETE
await api.delete('/endpoint')
// Upload multipart (NO usar post, usa postForm)
const res = await api.postForm('/endpoint', formData)
```

### Normalizar respuesta API

```typescript
// SIEMPRE usar este patrón (algunos endpoints tienen Resource wrapper, otros no)
const data = res?.data ?? res
```

### Notificaciones

```typescript
const notify = useNotification()
notify.success('Texto')
notify.error('Error message')
```

### Auth store

```typescript
const authStore = useAuthStore()
// Verificar rol
if (authStore.isSuperAdmin) { ... }
if (authStore.isEmpresaAdmin) { ... }
if (authStore.isParticipante) { ... }
// Empresa del usuario (participante)
const empresa = authStore.usuario?.empresa
```

---

## Componentes reutilizables

### EmpresaLogo
```vue
<EmpresaLogo
  :logo-url="empresa.logo_url"
  :logo-fondo="empresa.logo_fondo"    <!-- 'color' | 'transparente' -->
  :color-primario="empresa.color_primario"
  :nombre="empresa.nombre"
  size="sm"    <!-- sm | md | lg -->
/>
```

### PoweredByBlu
```vue
<PoweredByBlu />
<!-- Muestra link a blustudioinc.com con logo /blu_logo.png -->
<!-- Presente en todos los layouts y páginas de login/registro -->
```

### Modal
```vue
<Modal v-model="showModal" title="Título">
  <!-- Contenido -->
  <template #footer>
    <button @click="showModal = false">Cancelar</button>
    <button @click="guardar">Guardar</button>
  </template>
</Modal>
```

---

## Gotchas conocidos

### Sanctum multi-model
`config/auth.php` NO puede tener `'provider'` en el guard `sanctum`. Si se agrega, los tokens de `Participante` fallan con 401. Fue un bug encontrado en desarrollo — la solución fue remover esa clave.

### postForm vs post
Para uploads siempre usar `api.postForm()`. La razón: si se setea `Content-Type: application/json`, el browser no puede enviar multipart/form-data con el boundary correcto.

### Nuxt SPA strict
- No usar `useCookie()` (no hay server-side)
- No usar `useServerSideRendering` ni ninguna API de servidor
- Los middleware de ruta deben ser client-only

### Estadios no confirmados
Miami (Hard Rock Stadium), Denver (Empower Field) y Orlando (Camping World Stadium) NO son venues oficiales del Mundial 2026. No tienen `estadio_id` asignado (15 de 72 partidos).

### Import Excel
PhpSpreadsheet requiere `ext-gd`. En Docker se instala con `--ignore-platform-req=ext-gd`. El export devuelve un blob XLSX que se descarga directamente desde el frontend con `URL.createObjectURL`.

---

## Decisiones de diseño tomadas

- **SPA en lugar de SSR**: Para simplificar el deploy y evitar problemas con Sanctum stateful en SSR
- **Multi-model Sanctum sin provider**: Permite un solo endpoint de login que detecta el tipo de usuario automáticamente
- **Seeders idempotentes**: Para poder correr `db:seed --force` en producción sin perder datos
- **Token en localStorage** (no cookie): Por ser SPA y facilitar el debug. Riesgo XSS aceptado en contexto interno.
- **57/72 estadios asignados**: Los 15 sin asignar tienen venues no confirmados oficialmente por FIFA

---

## Próximos posibles features

- Fase eliminatoria (octavos, cuartos, semi, final)
- Notificaciones cuando un partido inicia o finaliza
- Comparar pronósticos propios vs grupo
- Panel mobile dedicado (layout responsive completo)

## Ver también

- [[arquitectura]] · [[api]] · [[stack]]
