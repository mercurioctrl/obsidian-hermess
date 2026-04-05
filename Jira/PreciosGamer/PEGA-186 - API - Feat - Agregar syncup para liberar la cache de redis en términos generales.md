---
jira_key: "PEGA-186"
aliases: ["PEGA-186"]
summary: "API - Feat - Agregar syncup para liberar la cache de redis en términos generales "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-13 13:16"
updated: "2025-06-05 01:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-186"
---

# PEGA-186: API - Feat - Agregar syncup para liberar la cache de redis en términos generales 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-13 13:16 |
| Actualizado | 2025-06-05 01:20 |
| Etiquetas | ninguna |
| Jira | [PEGA-186](https://bluinc.atlassian.net/browse/PEGA-186) |

## Relaciones

- **Padre:** [[PEGA-185]] REDIS

## Descripcion

Crearemos un recuirso para liberar la cache de redis

```
DELETE {{API_URL}}/v1/sync/items/cache
```

### 🎯 Criterios de aceptación:

- Se define el endpoint `DELETE /v1/sync/items/cache`.


- El token debe validarse contra el valor definido en `.env`, por ejemplo:
`SYNC_CACHE_TOKEN=valor_seguro`


- Si el token no coincide o no está presente, se debe devolver un error `403 Forbidden`.



### ✅ Ejemplo de respuesta exitosa (`200 OK`):

```
{
  "status": "success",
  "message": "Se libero la cache de redis"
}
```



---

### ❌ Ejemplo de error por token inválido o ausente (`403 Forbidden`):

```
{
  "status": "error",
  "message": "Sin token de autorizacion"
}
```
