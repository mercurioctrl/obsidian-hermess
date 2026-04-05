---
jira_key: "PED-929"
aliases: ["PED-929"]
summary: "API - Feat - Agregar tabla complementaria de perfiles y repositorio de perfiles"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-01-10 08:17"
updated: "2025-01-27 17:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-929"
---

# PED-929: API - Feat - Agregar tabla complementaria de perfiles y repositorio de perfiles

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-10 08:17 |
| Actualizado | 2025-01-27 17:33 |
| Etiquetas | ninguna |
| Jira | [PED-929](https://bluinc.atlassian.net/browse/PED-929) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **has action item:** [[PED-930 - APP - Feat - Agregar filtro de perfil en la lista de clientes|PED-930]] APP - Feat - Agregar filtro de perfil en la lista de clientes

## Descripcion

Dado que hasta ahora el dato del perfil se viene manejando sin un repositorio, sino de manera directa en la tabla de clientes (`[NewBytes_DBF].[dbo].[clientes].perfil`) crearemos un repositorio especifico.

Para esto crearemos la tabla `[NewBytes_DBF].[dbo].[clientesProfile]` con las siguientes columnas:

- id (auto)


- profileId (es el que esta en `[NewBytes_DBF].[dbo].[clientes].perfil` y con ella joineamos)


- Description (Una cadena de maximo 150 caracteres que explicara el perfil, al prinicipio solo ponemos “Perfil 1”, “Perfil 2”, etc)


- hide (un operador para ocultar perfiles especificos)



**Repositorio**

```
GET {API_URL}/v1/clientesProfile
```

```
{
id: 23
profileId: 1,
description: "Perfil 1",
hide: 0
}
```
