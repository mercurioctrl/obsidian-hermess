---
jira_key: "NBWEB-40"
aliases: ["NBWEB-40"]
summary: "Crear Carrito de compras"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-21 09:36"
updated: "2022-03-28 12:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-40"
---

# NBWEB-40: Crear Carrito de compras

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-21 09:36 |
| Actualizado | 2022-03-28 12:37 |
| Etiquetas | ninguna |
| Jira | [NBWEB-40](https://bluinc.atlassian.net/browse/NBWEB-40) |

## Relaciones

- **Padre:** [[NBWEB-1]] API - Carrito de compras

## Descripcion

```
POST {{API_URL}}/v1/carrito
```



Proceso:

Se debe crear un registro en la cabecera de carrito en `[NB_WEB].[dbo].[carritos] `Completando las siguientes columnas:

```
[id] -> Codigo autonumerico incremental
[id_usuario] -> Es el id de usuario logueado
[nombre] -> El nombre del carrito es "Nuevo Carrito"
[fechaAbierto] -> Fecha de creacion
[black] -> Se debe indicar true, en caso de que el carrito contenga productos type 1
[tipo] -> Se debe indicar "Pedido"
```


Retorna un objeto con el numero de carrito creado.
