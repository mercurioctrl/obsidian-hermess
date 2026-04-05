---
jira_key: "LIO-532"
aliases: ["LIO-532"]
summary: "Migración Preguntas/Respuestas API (Vendedores)"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-02-06 13:22"
updated: "2026-02-24 14:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-532"
---

# LIO-532: Migración Preguntas/Respuestas API (Vendedores)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-06 13:22 |
| Actualizado | 2026-02-24 14:25 |
| Etiquetas | ninguna |
| Jira | [LIO-532](https://bluinc.atlassian.net/browse/LIO-532) |

## Relaciones

- **Padre:** [[LIO-531]] Migraciones Legacy a V4
- **Subtarea:** [[LIO-533]] API - Feat - Listar preguntas del vendedor
- **Subtarea:** [[LIO-534]] API - Feat - Responder preguntas

## Descripcion

# Resumen del proyecto

Migración de endpoints de preguntas y respuestas desde API Legacy (v3) hacia API Nueva (v4 Laravel).

Alcance del documento:

```
SOLO funcionalidades de vendedores (gestión y respuesta de preguntas).
Las funcionalidades de compradores quedan fuera (por ahora).
```

---

# Reglas globales de autenticación JWT

## Regla obligatoria para TODOS los endpoints

```
El vendedor_id o usuario_id SIEMPRE se obtiene del JWT.
El cliente NUNCA envía su ID en body, params o URL.
```

---

## Middleware utilizado

```
Route::middleware('token.auth')->group(function () {
    // Todas las rutas de preguntas/respuestas
});
```

---

## Cómo acceder al usuario autenticado

```
$user = $request->attributes->get('auth_user');

$vendedorId = $user->vendedor_id; // vendedor
$usuarioId  = $user->id;          // cualquier usuario
```

---

## Ejemplo de payload JWT

```
{
  "id": 9876,
  "nombre": "Juan Pérez",
  "email": "juan@ejemplo.com",
  "vendedor_id": 111
}
```

---

# Resumen de endpoints

| Método | Endpoint |
| --- | --- |
| GET | `/api/v4/questions/seller` |
| POST | `/api/v4/questions/{id}/answer` |

---

# Estructura de tablas

## productosPreguntas

```
id
producto_id
vendedor_id
usuario_id
texto
fecha
ocultar

```

## productosRespuestas

```
id
pregunta_id
usuario_id
texto
fecha
respuesta_util

```

## productosPreguntasUsuariosBloqueados

```
id
producto_id
usuario_id
fecha
```
