---
jira_key: "LIO-540"
aliases: ["LIO-540"]
summary: "API - Feat - Migrar inventario -> Marcas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-02-18 09:36"
updated: "2026-02-24 17:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-540"
---

# LIO-540: API - Feat - Migrar inventario -> Marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-18 09:36 |
| Actualizado | 2026-02-24 17:18 |
| Etiquetas | ninguna |
| Jira | [LIO-540](https://bluinc.atlassian.net/browse/LIO-540) |

## Relaciones

- **Padre:** [[LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **has action item:** [[LIO-545]] APP - Refactor - Incorporar filtros ya migrados de categoría y marca

## Descripcion

Como consumidor de la API, necesito que los endpoints de marcas del recurso Inventories sean migrados a la nueva API, para que el frontend pueda seguir consultando marcas y sus filtros sin interrupciones durante y después de la migración.

## Contexto técnico

> **Implementación actual**

Resource: `app/resources/Inventories.php` (líneas 295–365) Service: `app/services/InventoryService.php` (líneas 540–634)


La API v3 actúa como proxy puro: no ejecuta queries directas a la base de datos. Recibe la petición del cliente, inyecta autenticación interna y reenvía la llamada al servicio de inventario downstream.

**Autenticación**

- El cliente envía un JWT Bearer Token válido.


- La API extrae el `vendedor_id` del token para construir la URL al downstream.


- Internamente agrega el header: `TOKEN_AUTH: {TOKEN_SERVICE_INVENTORY}`



## Endpoints a migrar

```
GET /inventories/brands
```

**Llamada al servicio downstream**

```
GET {URL_SERVICE_INVENTORY}brands
Headers:
  TOKEN_AUTH: {TOKEN_SERVICE_INVENTORY}
```

**Respuestas posibles**

| HTTP Code | Descripción |
| --- | --- |
| 200 OK | Array de marcas — respuesta directa del servicio downstream |
| 401 Unauthorized | Token JWT no presente o inválido |
| 4xx / 5xx | Error del servicio downstream, se propaga con el mismo status code |

**Tabla que utilizaremos:**

Query 1 — GET /brands                                                                                                            

```
  SELECT                                                                                                                           
      [M].id,                                                                                                                      
      [M].nombre AS name                                                                                                           
  FROM [LO].[dbo].[marcas] M                                
  WHERE [M].activa = 1
  AND   [M].eliminada = 0
  ORDER BY [M].nombre ASC
```

  Es la más simple de las dos. Solo toca una tabla:` [LO].[dbo].[marcas]`.

  ¿Qué hace?
  Trae el id y el nombre de todas las marcas que cumplan dos condiciones:

- activa = 1 → la marca está habilitada


- eliminada = 0 → no fue dada de baja (borrado lógico)



  El resultado viene ordenado alfabéticamente por nombre.

  ¿Por qué no filtra por vendedor?
  Porque este endpoint (GET /brands) es un listado general — no está atado a ningún catálogo de vendedor en particular. Es el que
  se usa para poblar un selector de marcas al crear un producto, por ejemplo.

  Resultado típico:


```
  [
    { "id": 1, "name": "LG" },
    { "id": 2, "name": "Samsung" },
    { "id": 3, "name": "Sony" }
  ]
```

###
