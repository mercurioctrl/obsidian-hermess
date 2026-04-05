---
jira_key: "LIO-543"
aliases: ["LIO-543"]
summary: "API - Feat - Migrar inventario -> Categorias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-02-19 11:46"
updated: "2026-02-24 17:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-543"
---

# LIO-543: API - Feat - Migrar inventario -> Categorias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-19 11:46 |
| Actualizado | 2026-02-24 17:38 |
| Etiquetas | ninguna |
| Jira | [LIO-543](https://bluinc.atlassian.net/browse/LIO-543) |

## Relaciones

- **Padre:** [[LIO-537 - Migración de repositorios previa deprecación de la api legacy|LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **has action item:** [[LIO-545 - APP - Refactor - Incorporar filtros ya migrados de categoría y marca|LIO-545]] APP - Refactor - Incorporar filtros ya migrados de categoría y marca

## Descripcion

Actualmente el endpoint **GET **`/inventories/categories` del **API REST v3** actúa como **proxy** hacia el microservicio `microservicio-inventory-v1`, el cual consulta **SQL Server**.
El objetivo es **migrar** este recurso a la **nueva API v4**, consultando la base de datos **directamente** y eliminando la dependencia del microservicio intermediario.

---

#### Recurso

| Ítem | Valor |
| --- | --- |
| Verbo | `GET` |
| Path | `/inventories/categories` |
| Autenticación | **Bearer JWT requerido** |

---

#### Filtros / Query params

Actualmente el endpoint **no acepta ni reenvía parámetros**.
En la migración se mantiene el mismo comportamiento: **sin filtros**, debe devolver **todas las categorías activas**.

---

#### Query a ejecutar (SQL Server)

```
SELECT
    C.id,
    C.nombre AS name
FROM LO.dbo.categorias C
WHERE C.activa = 1
  AND C.eliminada = 0
ORDER BY C.nombre ASC;

```

**Notas**

- Base de datos: **SQL Server**


- Tabla: **LO.dbo.categorias**


- **Sin JOINs** ni subconsultas



---

#### Payload de request

No aplica (GET sin body).

---

#### Respuesta exitosa — 200 OK

```
[
  { "id": 1, "name": "Laptops" },
  { "id": 2, "name": "Mouses" },
  { "id": 3, "name": "Teclados" }
]
```

| Campo | Tipo | Descripción |
| --- | --- | --- |
| id | integer | ID de la categoría |
| name | string | Nombre de la categoría |

---

#### Respuestas de error

| Código | Caso |
| --- | --- |
| 401 | Token ausente o inválido |
| 500 | Error interno al consultar la base de datos |

---

#### Criterios de aceptación

- El endpoint responde en **GET **`/inventories/categories`


- Requiere **autenticación JWT** válida


- Devuelve solo categorías con `activa = 1` y `eliminada = 0`


- Respuesta **ordenada alfabéticamente** por nombre


- **No depende** del microservicio `microservicio-inventory-v1` ni de llamadas HTTP internas
