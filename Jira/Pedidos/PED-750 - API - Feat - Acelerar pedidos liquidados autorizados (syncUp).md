---
jira_key: "PED-750"
aliases: ["PED-750"]
summary: "API - Feat - Acelerar pedidos liquidados autorizados (syncUp)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-24 10:17"
updated: "2025-06-26 13:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-750"
---

# PED-750: API - Feat - Acelerar pedidos liquidados autorizados (syncUp)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-24 10:17 |
| Actualizado | 2025-06-26 13:00 |
| Etiquetas | ninguna |
| Jira | [PED-750](https://bluinc.atlassian.net/browse/PED-750) |

## Relaciones

- **Padre:** [[PED-748]] Incentivo 25 años
- **blocks:** [[NBWEB-755]] APP - Feat - Ranking 
- **is blocked by:** [[PED-755]] API - Acelerar pedidos liquidados autorizados (syncUp) - Error de Proxy
- **has action item:** [[PED-1026]] API - Refactor - Se agregan pequeñas diferencias en las reglas de aceleracion para acciones travel

## Descripcion

```
PATCH {{API_URL}}/v1/syncUp/acelerateOrders
```

Crearemos un recurso para acelerar los items comprados en `[NewBytes_DBF].[dbo].[pedclil]`

Para esto usaremos la columna que creamos en [link](https://lioteam.atlassian.net/browse/PED-749)  para este fin y en ella guardaremos el puntaje obtenido de la tabla `NB_WEB.dbo.acelerators.acelerator`

Solo si matchea  con los términos de  `NB_WEB.dbo.acelerators.txtMatch` o cualquiera si hay un acelerador activado con `*`

Solo lo haremos para los pedidos que ya fueron liquidados

Guardaremos el indice de aceleracion en 

`[NewBytes_DBF].[dbo].[pedclil].acelerator`
