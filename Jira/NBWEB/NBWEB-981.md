---
jira_key: "NBWEB-981"
summary: "API - Refactor - Repositorio de marcas sensible a parámetros de ocultamiento"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-15 09:08"
updated: "2025-07-28 10:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-981"
---

# NBWEB-981: API - Refactor - Repositorio de marcas sensible a parámetros de ocultamiento

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-15 09:08 |
| Actualizado | 2025-07-28 10:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-981](https://bluinc.atlassian.net/browse/NBWEB-981) |

## Descripción

Tal como se hiciera en su momento para poder permitir compartir elementos (productos, o categorías) entre familias con la variable de entorno `MAIN_COMPANY_HIDE=" AND ocultarNbe = 0 "` o en `MAIN_COMPANY_HIDE_CATEGORIES = " AND ocultarNbeC = 0 "`

donde se utiliza una cadena de texto para concatenar en las query y de esa forma poder mantener ocultas de manera arbitraria productos o categorías, haremos los mismo para las marcas.

Este caso de uso se da porque en el caso de NBE hay algunos productos que se comparte con NB, de forma tal que solo filtrar entre empresas no es suficiente, pero al introducir junto a los parámetros de empresa la posibilidad de ocultar cada entidad de manera particular, la flexibilidad es total.

Es por esto que refactorizaremos el recurso 


```
GET {API_URL}/v1/brands
```

Actualmente disponemos de las variables de entorno

- `MAIN_COMPANY_HIDE=" AND ocultarNbe = 0"`


- `MAIN_COMPANY_HIDE_CATEGORIES=" AND ocultarNbeC = 0"`



que se concatenan en las consultas SQL para productos y categorías, permitiendo ocultarlos selectivamente. Debemos aplicar la misma lógica a las marcas.

- **Base de datos**

- Añadir columna `ocultarNbeC BIT NOT NULL DEFAULT 0` a la tabla `[NewBytes_DBF].[dbo].[FP_Marcas]`.




- **Configuración**

- Definir la nueva variable de entorno EN `.env`:

`MAIN_COMPANY_HIDE_BRANDS=" AND ocultarNbeC = 0" `




- **Backend**

- Refactorizar el repositorio que implementa `/v1/brands` para incluir `MAIN_COMPANY_HIDE_BRANDS` en todas las cláusulas `WHERE` de las consultas SQL.


- Asegurar que, si la variable de entorno no está definida, el comportamiento por defecto no cambia (se muestran todas las marcas)..





---

**Criterios de aceptación**

- Al ejecutar `GET /v1/brands` con `MAIN_COMPANY_HIDE_BRANDS=" AND ocultarNbeC = 0"`, la lista sólo incluye marcas con `ocultarNbeC = 0`.


- Si `MAIN_COMPANY_HIDE_BRANDS` no está definida, no juega ningún rol.


- La base de datos contiene la nueva columna `ocultarNbeC` con valor por defecto `0` tango en gamma como en prod.
