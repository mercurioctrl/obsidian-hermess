---
jira_key: "LIO-533"
aliases: ["LIO-533"]
summary: "API - Feat - Listar preguntas del vendedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-02-06 13:25"
updated: "2026-02-10 21:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-533"
---

# LIO-533: API - Feat - Listar preguntas del vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-06 13:25 |
| Actualizado | 2026-02-10 21:59 |
| Etiquetas | ninguna |
| Jira | [LIO-533](https://bluinc.atlassian.net/browse/LIO-533) |

## Relaciones

- **Padre:** [[LIO-532 - Migración PreguntasRespuestas API (Vendedores)|LIO-532]] Migración Preguntas/Respuestas API (Vendedores)
- **has action item:** [[LIO-511 - APP - Feat - Migrar endpoint “Responder pregunta de producto” desde Legacy|LIO-511]] APP - Feat - Migrar endpoint “Responder pregunta de producto” desde Legacy

## Descripcion

Como vendedor autenticado quiero ver todas las preguntas recibidas en mis productos para poder responderlas y gestionarlas

---

## Autorización JWT

```
El vendedor_id se obtiene del token.
Nunca se recibe por request.
```

Flujo:

```
1. Middleware valida JWT
2. Se obtiene vendedor_id del token
3. Se filtran preguntas por ese vendedor_id
```

---

## Endpoint

| Campo | Valor |
| --- | --- |
| Método | GET |
| Endpoint | `/api/v4/questions/seller` |
| Auth | Bearer JWT |
| Permiso | Perfil vendedor |

---

## Query params

| Param | Tipo | Default | Descripción |
| --- | --- | --- | --- |
| p | int | 1 | Página |
| estado | string | todas | pendientes | respondidas | todas |
| per_page | int | 10 | Items por página |

---

## Response 200

```
{
  "data": [
    {
      "id": 12345,
      "texto": "¿Cuánto dura la batería?",
      "fecha": "2024-01-15 14:30:00",
      "usuario": {
        "id": 9876,
        "nombre": "Juan Pérez",
        "avatar": 5,
        "bloqueado": false
      },
      "producto": {
        "id": 54321,
        "nombre": "Notebook Dell Inspiron",
        "img": "imagen_producto.jpg"
      },
      "vendedor": {
        "id": 111,
        "usuarioId": 9876,
        "nombre": "Tecnoshop Argentina"
      },
      "respuesta": {
        "id": 6789,
        "texto": "La batería dura aproximadamente 8 horas de uso continuo.",
        "fecha": "2024-01-15 16:45:00",
        "usuario_id": 9876,
        "respuesta_util": null
      }
    }
  ],
  "metadata": {
    "page": 1,
    "perPage": 10,
    "total": 45
  }
}

```

---

## Ejemplo request

```
curl -X GET "https://api.ejemplo.com/api/v4/questions/seller?p=1&estado=pendientes" \
  -H "Authorization: Bearer TOKEN"
```

---

## SQL principal

```
SELECT
    PP.id, PP.texto, PP.fecha, PP.usuario_id,
    U.nombre AS usuario_nombre, U.avatar AS usuario_avatar,
    CASE WHEN PPUB.id IS NOT NULL THEN 1 ELSE 0 END AS usuario_bloqueado,
    PP.producto_id, P.titulo AS producto_nombre, I.nombre_imagen AS producto_img,
    PP.vendedor_id, V.usuarioID as vendedor_usuario_id, V.nombre AS vendedor_nombre,
    PR.id AS respuesta_id, PR.texto AS respuesta_texto, PR.fecha AS respuesta_fecha,
    PR.usuario_id AS respuesta_usuario, PR.respuesta_util AS respuesta_util
FROM LO.dbo.productosPreguntas PP
LEFT JOIN LO.dbo.productosRespuestas PR ON PR.pregunta_id = PP.id
LEFT JOIN LO.dbo.vendedores V ON V.id = PP.vendedor_id
LEFT JOIN LO.dbo.usuarios U ON U.id = PP.usuario_id
LEFT JOIN CS.dbo.productos P ON P.id = PP.producto_id
LEFT JOIN CS.dbo.imagenes I ON I.producto_id = P.id AND I.orden = 1
LEFT JOIN LO.dbo.productosPreguntasUsuariosBloqueados PPUB 
  ON PPUB.producto_id = PP.producto_id AND PPUB.usuario_id = PP.usuario_id
WHERE PP.ocultar = 0 AND PP.vendedor_id = :vendedor_id
ORDER BY PP.id DESC
OFFSET (:page - 1) * :per_page ROWS FETCH NEXT :per_page ROWS ONLY
```
