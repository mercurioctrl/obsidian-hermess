# Arquitectura — bluFixture

## Estructura del proyecto

```
bluFixture/
├── backend/                        # Laravel 11
│   ├── app/Http/Controllers/       # 9 controladores
│   ├── app/Models/                 # 7 modelos
│   ├── database/migrations/        # 12 migraciones (0001–0012)
│   ├── database/seeders/           # DatabaseSeeder + EstadiosSeeder + AsignarEstadiosSeeder
│   ├── config/auth.php             # ⚠️ Guard sanctum SIN provider (multi-model)
│   └── routes/api.php
├── frontend/                       # Nuxt 3 SPA
│   ├── pages/                      # 16 páginas (file-based routing)
│   ├── components/                 # 11 componentes
│   ├── layouts/                    # auth / admin / empresa / portal
│   ├── composables/                # useApi · useNotification · usePrivacyMode
│   └── stores/auth.ts              # Pinia — token en localStorage
├── nginx/default.conf
├── docker-compose.yml
└── start.sh                        # Init completo desde cero
```

---

## Autenticación multi-model (decisión crítica)

`config/auth.php` NO tiene `'provider'` en el guard `sanctum`. Esto permite que tanto `User` (admin) como `Participante` usen el mismo guard sin conflicto.

**Si se agrega `provider`, los tokens de Participante devuelven 401.**

```
POST /api/auth/login
  → busca primero en tabla users
  → si no, busca en tabla participantes
  → devuelve { token, user: { id, nombre, email, rol, empresa_id, empresa? } }
```

El token se guarda en `localStorage['bf_token']` y viaja como `Authorization: Bearer {token}`.

---

## Modelos

| Modelo | Tabla | Notas |
|--------|-------|-------|
| `User` | `users` | HasApiTokens. Roles: super_admin, empresa_admin |
| `Participante` | `participantes` | HasApiTokens. Auth multi-model |
| `Empresa` | `empresas` | slug único, logo, color, puntos, premios, token registro |
| `Partido` | `partidos` | 72 partidos Copa 2026. FK → estadios |
| `Estadio` | `estadios` | 16 venues oficiales. emoji, dato_curioso |
| `Pronostico` | `pronosticos` | unique(participante_id, partido_id) |
| `Comentario` | `comentarios` | Scoped por empresa_id |

---

## Migraciones (en orden)

```
0001 → empresas
0002 → users  
0003 → personal_access_tokens (Sanctum, polymorphic)
0004 → participantes
0005 → partidos
0006 → pronosticos
0007 → comentarios
0008 → slug + logo_url en empresas
0009 → logo_fondo en empresas
0010 → estadios
0011 → estadio_id en partidos
0012 → registro_token + registro_abierto en empresas
```

---

## Frontend: SPA pura

- `ssr: false` en nuxt.config.ts → SPA, no hay server-side rendering
- Sin `useCookie`, sin lógica server-side
- Token en `localStorage`
- `pages/middleware/auth.ts` protege `/admin`, `/empresa`, `/portal`
- `layout: false` en login, [slug] y registro/[token]

### Rutas y layouts

```
Públicas (layout: false):
  /login             → login.vue
  /{slug}            → [slug].vue (login branded por empresa)
  /registro/{token}  → registro/[token].vue (auto-registro)

Privadas:
  /admin/**          → layout: admin
  /empresa/**        → layout: empresa
  /portal/**         → layout: portal
```

---

## Patrón de respuesta API

Algunos endpoints usan Laravel Resource (envuelven en `{data:{}}`), otros devuelven directo. Normalizar siempre:

```typescript
const data = res?.data ?? res
```

---

## Seeders idempotentes

Todos los seeders usan `doesntExist()` antes de insertar. Seguro correr en cualquier momento:

```bash
docker exec blufixture-backend php artisan db:seed --force
```

- `DatabaseSeeder`: 1 super_admin + 72 partidos (Grupos A–L)
- `EstadiosSeeder`: 16 venues FIFA 2026 con emoji/dato_curioso
- `AsignarEstadiosSeeder`: 57/72 partidos asignados. Miami, Denver, Orlando = no confirmados oficialmente

---

## Multi-tenancy

Cada empresa es completamente aislada:
- Participantes pertenecen a una empresa
- Pronósticos y comentarios se filtran por empresa
- Login branded por slug (`/{slug}`)
- Puntos configurables por empresa (`pts_exacto`, `pts_resultado`)
- Premios propios
- Token de registro propio (abrir/cerrar/regenerar)

## Ver también

- [[stack]] · [[api]] · [[contexto]] · [[changelog]]
