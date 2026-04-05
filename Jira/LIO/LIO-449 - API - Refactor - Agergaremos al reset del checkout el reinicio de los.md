---
jira_key: "LIO-449"
aliases: ["LIO-449"]
summary: "API - Refactor - Agergaremos al \"reset\" del checkout el reinicio de los parametros de la wallet (usedHere))"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-12 14:40"
updated: "2025-09-23 10:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-449"
---

# LIO-449: API - Refactor - Agergaremos al "reset" del checkout el reinicio de los parametros de la wallet (usedHere))

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-12 14:40 |
| Actualizado | 2025-09-23 10:43 |
| Etiquetas | ninguna |
| Jira | [LIO-449](https://bluinc.atlassian.net/browse/LIO-449) |

## Relaciones

- **Padre:** [[LIO-231]] Billetera

## Descripcion

Teniendo en cuenta lo realizado en [link](https://bluinc.atlassian.net/browse/LIO-381) 

Refactorizaremos el recurso 

```
PATCH {API_URL}/pedidos/checkout/{idPedido}/reset
```

Para reinicializar tambien los parámetros de uso de dinero en wallet

- `[pedidosDetalle].walletUsedHere`


- `[pedidosCabeceraVendedor].walletUsedHere`


- `[pedidosCabeceraVendedor].walletAvailable`
