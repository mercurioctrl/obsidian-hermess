---
jira_key: "COB-393"
aliases: ["COB-393"]
summary: "API - Feat - Repositorio de agentes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-04-04 13:06"
updated: "2023-07-31 07:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-393"
---

# COB-393: API - Feat - Repositorio de agentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-04 13:06 |
| Actualizado | 2023-07-31 07:29 |
| Etiquetas | ninguna |
| Jira | [COB-393](https://bluinc.atlassian.net/browse/COB-393) |

## Relaciones

- **Padre:** [[COB-21]] Base del proyecto y formularios

## Descripcion

```
GET {API_URL}/v1/agents
```

Basándonos en la consulta SQL que extrae el código de agente, nombre y ID del agente desde la tabla de 'agentes', se implementará un nuevo repositorio que filtrará los agentes por nombre o apellido, o los mostrará todos si no se aplica ningún filtro. La API devolverá una lista de objetos con los agentes que coincidan con el término de búsqueda, donde cada objeto contiene el código del agente, su descripción (nombre y apellido) y su ID

```
SELECT  
    [ccodage]
    ,[capeage]
    ,[cnbrage]
    ,[ID_VENDEDOR]
FROM [NewBytes_DBF].[dbo].[agentes]
```

agregaremos le siguiente repositorio que filtra por nombre, apellido de los agentes, o bien los muestra todos si no tiene filtro

```
GET {API_URL}/v1/agents?search=marcelo
```

Devuelve un objeto como el siguiente

```
[
  {
    "ccodage": "01",
    "description": "Andrada Diego",
    "id": 1
  },
  {
    "ccodage": "26",
    "description": "Quirch Marcelo",
    "id": 26
  },
  {
    "ccodage": "03 ",
    "description": "Garcia Alejandro",
    "id": 3
  }
  ...
  ]
```
