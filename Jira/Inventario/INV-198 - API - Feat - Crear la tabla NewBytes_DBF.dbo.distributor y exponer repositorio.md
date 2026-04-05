---
jira_key: "INV-198"
aliases: ["INV-198"]
summary: "API - Feat - Crear la tabla [NewBytes_DBF].[dbo].[distributor] y exponer repositorio REST con GET/POST/PATCH/DELETE para administrar distribuidoras."
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-09-02 08:45"
updated: "2025-09-08 10:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-198"
---

# INV-198: API - Feat - Crear la tabla [NewBytes_DBF].[dbo].[distributor] y exponer repositorio REST con GET/POST/PATCH/DELETE para administrar distribuidoras.

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-02 08:45 |
| Actualizado | 2025-09-08 10:47 |
| Etiquetas | ninguna |
| Jira | [INV-198](https://bluinc.atlassian.net/browse/INV-198) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **has action item:** [[INV-197]] API - Refactor - Objeto "item, leer y escribir atributos de distribuidora
- **has action item:** [[INV-200]] APP - Feat - Cambiar atributo "distributor" y poder filtrarlo en el repositorio "items"

## Descripcion

Necesitamos centralizar el catálogo de distribuidoras en base de datos y exponer un CRUD simple para uso interno de backoffice y futuros procesos de integración. La tabla debe contener **solo** las columnas indicadas y quedar inicializada con los registros requeridos.

## Objetivo

- Crear la tabla `[NewBytes_DBF].[dbo].[distributor]` con columnas:

- `distributorId` (PK)


- `distributorDescription`


- `softDelete`


- `updatedAt`




- Publicar endpoints REST: **GET**, **POST**, **PATCH**, **DELETE** sobre `/distributors`.


- Sembrar datos iniciales:
`1 - NB`, `2 - Stylus`, `3 - argseguridad`, `4 - Air`.



## API REST

```
GET {API_URL}/distributors
```

Lista paginada y con búsqueda opcional.

**Query params (opcionales):**

- `q` → busca por `distributorDescription` (substring, case-insensitive si aplica).


- `page` (por defecto 1), `limit` (por defecto 50, máx. 200).


- `sort` (por defecto `distributorId`), `order` (`asc|desc`, por defecto `asc`).



**200 OK**

```
{
  "data": [
    { "distributorId": 1, "distributorDescription": "NB" },
    { "distributorId": 2, "distributorDescription": "Stylus" }
  ],
  "page": 1,
  "limit": 50,
  "total": 4
}

```

### 

```
GET {API_URL}/distributors/{distributorId}
```

**200 OK**

```
{ "distributorId": 3, "distributorDescription": "argseguridad" }

```

**404 Not Found**

```
{ "error": "NotFound", "message": "Distributor not found" }

```

### 

```
POST {API_URL}/distributors
```

Crea una distribuidora.

**Request (JSON)**

```
{
  "distributorId": 5,
  "distributorDescription": "NuevoDistribuidor"
}

```

- `distributorDescription`: string 1–100 chars, único.



**201 Created**

```
{
  "distributorId": 5,
  "distributorDescription": "NuevoDistribuidor"
}

```

**409 Conflict** (duplicado de `distributorId` o `distributorDescription`)

```
{ "error": "Conflict", "message": "Distributor existente" }

```

**422 Unprocessable Entity** (validación)

```
{ "error": "ValidationError", "details": { "distributorDescription": "Required" } }

```

```
PATCH {API_URL}/distributors/{distributorId}
```

Actualiza **parcialmente** (en este caso, típicamente la descripción).

**Request (JSON)**

```
{
  "distributorDescription": "NB"
}
```

**200 OK**

```
{
  "distributorId": 1,
  "distributorDescription": "NB"
}

```

**404 Not Found** / **409 Conflict** / **422 Unprocessable Entity** según corresponda.

### 5) DELETE `/distributors/{distributorId}`

Borra la distribuidora por id (softDelete).

**204 No Content**
**404 Not Found** si no existe.
**409 Conflict** si la entidad está referenciada por otras tablas (si aplicara en el futuro; contemplar control con FK o verificación previa).
