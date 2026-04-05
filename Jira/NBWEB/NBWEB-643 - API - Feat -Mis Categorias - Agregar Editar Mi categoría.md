---
jira_key: "NBWEB-643"
aliases: ["NBWEB-643"]
summary: "API - Feat -Mis Categorias -> Agregar / Editar \"Mi categoría\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-13 21:46"
updated: "2025-10-31 09:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-643"
---

# NBWEB-643: API - Feat -Mis Categorias -> Agregar / Editar "Mi categoría"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-13 21:46 |
| Actualizado | 2025-10-31 09:54 |
| Etiquetas | ninguna |
| Jira | [NBWEB-643](https://bluinc.atlassian.net/browse/NBWEB-643) |

## Relaciones

- **Padre:** [[NBWEB-641 - Listas de precio|NBWEB-641]] Listas de precio
- **relates to:** [[SNB-3504 - NBWEB - API - Mis Categorías - Error al modificar porcentaje de utilidad|SNB-3504]] NBWEB - API - Mis Categorías -> Error al modificar porcentaje de utilidad

## Descripcion

Usando la tabla creada en [link](https://lioteam.atlassian.net/browse/NBWEB-642) 

Crearemos el recurso

```
POST {API_URL}/v1/miCuenta/misCategorias
```

Que se encargara de crear relaciones entre las categorías originales que tiene la api y las que crea el usuario (cliente).

Para esto enviaremos la siguiente carga util

```
{
categoryId:35
utility: 2.5
descriptio: "Nombre del reseller para la categoria"
}  
```



Solo puede crearse uno por categoria, si esa categoria ya esta vinculada en nuestra nueva tabla, para ese cliente, entonces avisamos que ya fue creada.

Tambien crearemos el recurso analogo para editar categorias del cliente

```
PATCH {API_URL}/v1/miCuenta/misCategorias
```
