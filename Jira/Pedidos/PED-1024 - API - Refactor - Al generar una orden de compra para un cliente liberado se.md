---
jira_key: "PED-1024"
aliases: ["PED-1024"]
summary: "API - Refactor - Al generar una orden de compra para un cliente \"liberado\" se debe asignar al vendedor que lo esta creando"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-06-25 08:59"
updated: "2025-06-26 03:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1024"
---

# PED-1024: API - Refactor - Al generar una orden de compra para un cliente "liberado" se debe asignar al vendedor que lo esta creando

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-25 08:59 |
| Actualizado | 2025-06-26 03:36 |
| Etiquetas | ninguna |
| Jira | [PED-1024](https://bluinc.atlassian.net/browse/PED-1024) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **has action item:** [[PED-1025 - API - Refactor - Al liquidar un pedido de para un cliente liberado se debe|PED-1025]] API - Refactor - Al liquidar un pedido de para un cliente "liberado" se debe asignar al vendedor que lo esta liquidando

## Descripcion

Dado que existen algunos clientes que tienen la característica de estar liberados (no tienen un vendedor fijo) es necesario que si cumple esa condición todos los registros de una venta se generen para ese vendedor, empezando por la orden de compra.

De esta forma refactorizaremos 

```
POST {API_URL}/v1/orders
```

Para que SI el parámetro `[NewBytes_DBF].[dbo].[clientes].freeSeller=true`(Este parámetro aun no existe y hay que agregarlo)

Entonces guardaremos en `[NewBytes_DBF].[dbo].[pedclit]`

los parámetros `ID_VENDEDOR` y `ccodage_creador`para el vendedor que esta haciendo la operacion en ese momento y no para los del cliente.

---

En caso contrario, es decir que `[NewBytes_DBF].[dbo].[clientes].freeSeller != true` es `false` o `null`

Entonces haremos lo que hacemos siempre, que es usar la información que se encuentra en  `[NewBytes_DBF].[dbo].[clientes].ID_VENDEDOR`y `[NewBytes_DBF].[dbo].[clientes].ccodage`
