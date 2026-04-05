---
jira_key: "PEGA-189"
aliases: ["PEGA-189"]
summary: "API - Refactor - Agregar parámetros de envío a items"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-20 14:49"
updated: "2025-06-30 10:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-189"
---

# PEGA-189: API - Refactor - Agregar parámetros de envío a items

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-20 14:49 |
| Actualizado | 2025-06-30 10:46 |
| Etiquetas | ninguna |
| Jira | [PEGA-189](https://bluinc.atlassian.net/browse/PEGA-189) |

## Relaciones

- **Padre:** [[PEGA-177]] Envios Gratis

## Descripcion

Agregar los campos `shipping` y `freeShipping` a la tabla `items` y asegurarse de que estén disponibles en los endpoints públicos `GET /v1/items` y `GET /v1/itemDetail/{id}`.

#### 1. **Base de datos**

Agregar dos columnas a la tabla `[PEGA].[dbo].[items]`:

- `shipping` (`BIT`, permite `NULL`, default `0`)


- `freeShipping` (`BIT`, permite `NULL`, default `0`)



#### 2. **Agregar recursos en **

```
GET /v1/items
```

```
GET /v1/itemDetail/{id}
```

### Criterios de aceptación

- La tabla `[items]` contiene correctamente las nuevas columnas `shipping` y `freeShipping` como valores booleanos (`true` / `false` en la capa API).


- Ambos campos se incluyen en los resultados de `GET /v1/items`.


- Ambos campos se incluyen en la respuesta de `GET /v1/itemDetail/{id}`.


- Si los valores son nulos en la base de datos, se devuelven como `false` por defecto en la respuesta JSON.


- No se afecta la performance ni el contenido de otros campos existentes.
