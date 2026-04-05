---
jira_key: "NBWEB-518"
aliases: ["NBWEB-518"]
summary: "que el cliente visualice los seriales de su compra"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-02-02 15:07"
updated: "2023-02-14 17:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-518"
---

# NBWEB-518: que el cliente visualice los seriales de su compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-02-02 15:07 |
| Actualizado | 2023-02-14 17:06 |
| Etiquetas | ninguna |
| Jira | [NBWEB-518](https://bluinc.atlassian.net/browse/NBWEB-518) |

## Relaciones

- **causes:** [[SNB-316 - que el cliente visualice los seriales de su compra|SNB-316]] que el cliente visualice los seriales de su compra
- **is blocked by:** [[NBWEB-175 - APP - Mi cuenta - Pedidos|NBWEB-175]] APP - Mi cuenta - Pedidos

## Descripcion

Por un requerimiento de postventa tenemos que agregar los seriales que están vinculados a un producto, para eso crearemos un recurso llamado

```
GET {API_URL}/v1/orders/{pedido}/serials/{itemId}
```

Que debe traer algo como lo siguiente

```
   [
        {
            "serial": "104798198220002",
        },
        {
            "serial": "104798198220003",
        },
        {
            "serial": "104798198220004",
        },
        {
            "serial": "104798198220005",
        }
    ]
```

Podes mirar como esta realizado aca algo muy parecido, y preguntarle a  [link](https://lioteam.atlassian.net/browse/EXP-101) 



nos comentan varios clientes que necesitan poder visualizar en la parte de comprobantes los seriales de la compra que realizaron, entiendo que es posible por que es información que poseemos
