---
jira_key: "PED-578"
aliases: ["PED-578"]
summary: "API - Feat - Eliminar direccion -> Evitar que se eliminen direcciones vinculadas a pedidos pendietes de ser despachadas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-03-01 15:28"
updated: "2024-03-05 16:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-578"
---

# PED-578: API - Feat - Eliminar direccion -> Evitar que se eliminen direcciones vinculadas a pedidos pendietes de ser despachadas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-01 15:28 |
| Actualizado | 2024-03-05 16:23 |
| Etiquetas | ninguna |
| Jira | [PED-578](https://bluinc.atlassian.net/browse/PED-578) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **is blocked by:** [[PED-52 - API - Feat - Eliminar direccion|PED-52]] API - Feat - Eliminar direccion

## Descripcion

Modificaremos el recurso

```
GET {{API_URL}}/v1/shippingAddress/{clientId}/{idDirCli}
```

Para evitar que se puedan eliminar direcciones en caso de que cualquier pedido que contenga ese id de dirección se encuentre en los siguientes estados (`1,2,4,3,9,11,10`). 

De esta forma se intenta evitar que existan cambios de dirección, en medio de una transacción en curso. 

Adicionalmente y para que sea mas fácil encontrar el causante de que no se pueda realizar la accion, debemos informar que pedido y en que estado encontramos que produce el inconveniente en un mensaje de `succes:fail`
