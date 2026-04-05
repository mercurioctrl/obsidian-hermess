---
jira_key: "LIO-511"
aliases: ["LIO-511"]
summary: "APP - Feat - Migrar endpoint “Responder pregunta de producto” desde Legacy"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-12 08:30"
updated: "2026-02-12 22:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-511"
---

# LIO-511: APP - Feat - Migrar endpoint “Responder pregunta de producto” desde Legacy

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-12 08:30 |
| Actualizado | 2026-02-12 22:59 |
| Etiquetas | ninguna |
| Jira | [LIO-511](https://bluinc.atlassian.net/browse/LIO-511) |

## Relaciones

- **Padre:** [[LIO-498]] Listado de preguntas
- **action item from:** [[LIO-533]] API - Feat - Listar preguntas del vendedor

## Descripcion

Colaborar para Migrar a API v4 el endpoint que permite a un **vendedor responder una pregunta** realizada sobre uno de sus productos, **manteniendo exactamente el mismo comportamiento funcional, validaciones, errores y notificaciones** que en Legacy.

El cambio debe permitir que, **modificando solo el dominio/baseURL**, el front continúe funcionando sin cambios.

## Endpoint a migrar (contrato congelado) [link](https://bluinc.atlassian.net/browse/LIO-533) 

```
POST {API_V4}/productos/preguntas/{preguntaId}/respuesta
```

### Parámetros

- `preguntaId` (path): ID de la pregunta


- Body JSON:



```
{
  "respuesta": "texto de la respuesta"
}
```

### Autenticación y seguridad

- Requiere JWT Bearer


- Solo accesible por usuarios con perfil **vendedor**



---

## Flujo y validaciones (orden obligatorio)

### 1- Validación de datos

- Debe existir el campo `respuesta` en el body


- No puede estar vacío


- Error: **mismo status y mensaje que Legacy**



---

### 2- Validación de permisos

- Solo usuarios con perfil `vendedor`


- Si no cumple:

- HTTP **403**


- Mensaje idéntico a Legacy





### 3-  Verificar existencia de la pregunta

- Buscar pregunta por `preguntaId`


- Si no existe:

- HTTP **400**


- Mensaje: `"La pregunta no existe."`





---

### 4- Verificar que sea SU pregunta

- La pregunta debe pertenecer al `vendedor_id` del usuario autenticado


- Si intenta responder una pregunta de otro vendedor:

- HTTP **403**


- Mensaje: `"No podés responder la pregunta de otro vendedor."`





---

### 5-  Verificar que no esté ya respondida

- Una pregunta **solo puede responderse una vez**


- Si ya existe respuesta:

- HTTP **403**


- Mensaje: `"No podés responder más de una vez a una misma pregunta."`





---

## Persistencia (modelo / repositorio)

### Inserción protegida (obligatoria)

La inserción debe mantener **doble protección**:

- Validación previa en código


- Protección a nivel SQL



```
IF NOT EXISTS (
    SELECT 1
    FROM LO.dbo.productosRespuestas
    WHERE pregunta_id = @preguntaId
)
BEGIN
    INSERT INTO LO.dbo.productosRespuestas (
        pregunta_id,
        usuario_id,
        texto
    )
    VALUES (
        @preguntaId,
        @usuarioId,
        @texto
    )
END

```

⚠️ **No eliminar el IF NOT EXISTS**, aunque parezca redundante.

---

### Verificación post-insert

- Volver a obtener la pregunta completa


- Si no existe la respuesta:

- Retornar error funcional:

- success = false


- mensaje igual a Legacy







---

## Notificaciones (side-effects obligatorios)

Al guardar la respuesta, se deben disparar **las 3 notificaciones**, sin cambios:

- Notificación Web


- Notificación Push


- Email



---

## Reglas de negocio (no negociables)

-  Solo vendedores pueden responder


- Solo pueden responder preguntas de **sus** productos


- Una pregunta = una respuesta


-  Protección doble contra respuestas duplicadas


-  El usuario que preguntó recibe 3 notificaciones automáticas



---

## Criterios de aceptación (DoD)

-  El endpoint existe en v4 con la misma URL y método


-  Cambiando solo el dominio, el front funciona igual


-  No es posible responder dos veces la misma pregunta


- Las 3 notificaciones se disparan correctamente


-  La respuesta contiene la pregunta completa con la respuesta incluida
