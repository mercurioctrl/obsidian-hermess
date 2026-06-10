# API Reference — bluFixture

Base: `http://localhost:8830/api`  
Auth: `Authorization: Bearer {token}` (token en localStorage como `bf_token`)

---

## Endpoints públicos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/auth/login` | Login (busca en users, luego en participantes) |
| GET | `/publica/empresa/{slug}` | Info empresa para login branded |
| GET | `/publica/registro/{token}` | Info empresa para auto-registro |
| POST | `/publica/registro/{token}` | Crear participante + retorna token (auto-login) |

---

## Endpoints protegidos

### Auth
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/auth/me` | Usuario autenticado con empresa embebida |
| POST | `/auth/logout` | Revocar token |

### Empresas
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/empresas` | Listar empresas |
| POST | `/empresas` | Crear empresa |
| GET | `/empresas/{id}` | Ver empresa (incluye registro_token, registro_abierto) |
| PUT | `/empresas/{id}` | Actualizar empresa |
| DELETE | `/empresas/{id}` | Eliminar empresa |
| POST | `/empresas/{id}/logo` | Upload logo (multipart) |
| POST | `/empresas/{id}/registro/abrir` | Genera token + abre inscripción |
| POST | `/empresas/{id}/registro/cerrar` | Cierra inscripción |
| POST | `/empresas/{id}/registro/regenerar` | Nuevo token (invalida anterior) |

### Participantes
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/participantes?empresa_id={id}` | Listar participantes de empresa |
| POST | `/participantes` | Crear participante |
| PUT | `/participantes/{id}` | Actualizar |
| DELETE | `/participantes/{id}` | Eliminar |
| GET | `/participantes/exportar` | Descarga XLSX |
| POST | `/participantes/importar` | Importar XLSX/CSV (multipart: archivo + empresa_id) |

### Partidos y Estadios
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/partidos` | Listar partidos (eager loads `venue`) |
| PUT | `/partidos/{id}` | Actualizar resultado/estadio |
| GET | `/estadios` | Lista venues agrupados por país |

### Pronósticos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/mis-pronosticos` | Pronósticos del participante autenticado |
| POST | `/pronosticos` | Guardar pronóstico `{partido_id, goles_local, goles_visitante}` |
| GET | `/partidos/{id}/pronosticos` | Pronósticos de todos (solo post-partido finalizado) |

### Social
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/partidos/{id}/comentarios` | Comentarios del partido (filtrado por empresa) |
| POST | `/partidos/{id}/comentarios` | Nuevo comentario |
| DELETE | `/comentarios/{id}` | Borrar comentario |
| GET | `/contrincantes/{participante_id}` | Perfil + pronósticos de contrincante |

### Ranking
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/ranking/mi-empresa` | Ranking de la empresa del usuario autenticado |
| GET | `/ranking/empresa/{id}` | Ranking de empresa específica |

---

## Patrones de respuesta

```typescript
// Endpoints con Resource → { data: { ... } }
// Endpoints sin Resource → objeto directo

// Siempre normalizar:
const data = res?.data ?? res
```

---

## Login response

```json
{
  "token": "1|abc...",
  "user": {
    "id": 1,
    "nombre": "Admin",
    "email": "admin@blufixture.com",
    "rol": "super_admin",
    "empresa_id": null,
    "empresa": null
  }
}
```

Para participante, `rol = "participante"` y `empresa` incluye:
```json
{
  "id": 1,
  "nombre": "Empresa Demo",
  "slug": "demo",
  "logo_url": "...",
  "logo_fondo": "color",
  "color_primario": "#2D8C5A",
  "pts_exacto": 3,
  "pts_resultado": 1
}
```

## Ver también

- [[arquitectura]] · [[contexto]]
