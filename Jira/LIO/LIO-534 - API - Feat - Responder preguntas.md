---
jira_key: "LIO-534"
aliases: ["LIO-534"]
summary: "API - Feat - Responder preguntas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-02-06 13:27"
updated: "2026-02-24 14:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-534"
---

# LIO-534: API - Feat - Responder preguntas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-06 13:27 |
| Actualizado | 2026-02-24 14:21 |
| Etiquetas | ninguna |
| Jira | [LIO-534](https://bluinc.atlassian.net/browse/LIO-534) |

## Relaciones

- **Padre:** [[LIO-532]] Migración Preguntas/Respuestas API (Vendedores)
- **has action item:** [[LIO-510]] APP - Feat - Migrar endpoint “Listado de preguntas para vendedor (corregir paginado)” actualemente en Legacy

## Descripcion

Como vendedor autenticado quiero responder una pregunta en mis productos para informar al comprador

---

## Autorización JWT

Flujo:

```
1. JWT → obtener vendedor_id
2. Buscar pregunta por question_id
3. Validar que pregunta.vendedor_id == vendedor_id
4. Si no coincide → 403
```

---

## Endpoint

| Campo | Valor |
| --- | --- |
| Método | POST |
| Endpoint | `/api/v4/questions/{question_id}/answer` |
| Auth | JWT |
| Permiso | Dueño de la pregunta |

---

## Request body

```
{
  "respuesta": "Texto de la respuesta del vendedor"
}
```

---

## SQL insertar respuesta

```
INSERT INTO LO.dbo.productosRespuestas
(pregunta_id, usuario_id, texto, fecha, respuesta_util)
VALUES (:pregunta_id, :usuario_id, :texto, GETDATE(), NULL);
SELECT SCOPE_IDENTITY() as respuesta_id;
```

---

## SQL verificar respuesta existente

```
SELECT COUNT(*) as count
FROM LO.dbo.productosRespuestas
WHERE pregunta_id = :question_id
```
