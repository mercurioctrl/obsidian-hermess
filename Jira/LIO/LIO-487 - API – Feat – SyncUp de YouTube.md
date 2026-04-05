---
jira_key: "LIO-487"
aliases: ["LIO-487"]
summary: "API – Feat – SyncUp de YouTube"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2025-12-05 08:57"
updated: "2025-12-16 10:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-487"
---

# LIO-487: API – Feat – SyncUp de YouTube

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-05 08:57 |
| Actualizado | 2025-12-16 10:13 |
| Etiquetas | ninguna |
| Jira | [LIO-487](https://bluinc.atlassian.net/browse/LIO-487) |

## Relaciones

- **Padre:** [[LIO-481]] Recomendaciones de loki
- **has action item:** [[LIO-489]] API - Refactor - El recurso de SyncUp estará detrás de un token fijado en las variables de entorno

## Descripcion

Implementar un **proceso de sincronización (syncup)** que permita traer desde YouTube los **Shorts nuevos** y guardarlos en la tabla:

> `[LO].[dbo].[yt_videos]`


La sincronización **debe agregar únicamente los videos que aún no existan** en la tabla, evitando duplicados.

---

### Endpoint

**Nuevo recurso:**

```
POST {API_URL}/v4/yt/shorts/syncUp?label={label}
```

Ejemplo:

```
POST /v4/yt/shorts/syncUp?label=recomendaciones-de-loki
```

---

### Seguridad

- El endpoint debe estar protegido con **token interno del API** (el mismo esquema ya usado en recursos admin / internos).


- Sin token válido → `401 Unauthorized`.



---

### Configuración YouTube

- El consumo de la API de YouTube debe utilizar una **API Key configurada por **`.env` (ejemplo: `YOUTUBE_API_KEY`).


- No se hardcodean credenciales.



---

### Comportamiento del Sync

- Validar que llegue el parámetro `label`.


- Consultar YouTube y obtener los **Shorts del canal configurado**.


- Detectar cuáles de esos videos **no existen aún en la tabla** `[yt_videos]` (comparando por `url`).


- Insertar solo los nuevos registros con:

- `label` → el recibido por parámetro.


- `url` → URL pública del video.


- `thumbnail` → URL del thumbnail.


- `deleted = 0`


- `show = 1`


- `homeShow = 0`


- `createdAt` → fecha actual.





---

### Respuesta esperada

El endpoint debe devolver un resumen del resultado del sync:

```
{
  "label": "recomendaciones-de-loki",
  "fetchedFromYoutube": 25,
  "inserted": 7
}

```

---

### Criterios de aceptación

- El sync **inserta únicamente videos nuevos**.


- No se generan duplicados.


- Sin token válido → `401`.


- Sin `label` → `400`.


- El endpoint de lectura existente:



```
GET {API_URL}/v4/yt/shorts?label=recomendaciones-de-loki

```

continúa funcionando sin cambios y refleja los registros sincronizados.
