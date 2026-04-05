---
jira_key: "PED-13"
aliases: ["PED-13"]
summary: "API - Feat - Repositorio agentes (vendedores)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-07-31 07:26"
updated: "2023-08-01 11:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-13"
---

# PED-13: API - Feat - Repositorio agentes (vendedores)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-31 07:26 |
| Actualizado | 2023-08-01 11:54 |
| Etiquetas | ninguna |
| Jira | [PED-13](https://bluinc.atlassian.net/browse/PED-13) |

## Relaciones

- **Padre:** [[PED-7 - Repositorios y base del proyecto|PED-7]] Repositorios y base del proyecto

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
