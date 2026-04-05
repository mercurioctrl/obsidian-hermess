---
jira_key: "NBWEB-971"
aliases: ["NBWEB-971"]
summary: "API - Refactor - Agregaremos a la edición que hacen los clientes en integraciones para categorias y prodcutos para hacer flush de cache de redis para ese cliente"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-27 17:22"
updated: "2025-06-12 09:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-971"
---

# NBWEB-971: API - Refactor - Agregaremos a la edición que hacen los clientes en integraciones para categorias y prodcutos para hacer flush de cache de redis para ese cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-27 17:22 |
| Actualizado | 2025-06-12 09:49 |
| Etiquetas | ninguna |
| Jira | [NBWEB-971](https://bluinc.atlassian.net/browse/NBWEB-971) |

## Relaciones

- **Padre:** [[NBWEB-957]] Redis
- **has action item:** [[SNB-2998]] Conector NB - Se muestran artículos de categorías ocultas por el cliente

## Descripcion

Segun lo conversador ll llamar a los siguiente recursos desde una cuenta de usuario liberaremos la cache de redis para ese mismo usuario (cliente) con la clave creada en [link](https://bluinc.atlassian.net/browse/NBWEB-970) 

```
POST /v1/miCuenta/misCategorias
```

```
PATCH /v1/miCuenta/misCategorias
```

```
POST /v1/miCuenta/misProductos
```

```
PATCH /v1/miCuenta/misProductos
```
