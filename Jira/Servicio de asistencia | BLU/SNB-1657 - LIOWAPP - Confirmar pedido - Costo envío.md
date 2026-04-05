---
jira_key: "SNB-1657"
aliases: ["SNB-1657"]
summary: "LIOWAPP - Confirmar pedido - Costo envío"
status: "Finalizada"
type: "Nueva función"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-03-19 17:04"
updated: "2024-03-21 16:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-1657"
---

# SNB-1657: LIOWAPP - Confirmar pedido - Costo envío

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Nueva función |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-19 17:04 |
| Actualizado | 2024-03-21 16:29 |
| Etiquetas | ninguna |
| Jira | [SNB-1657](https://bluinc.atlassian.net/browse/SNB-1657) |

## Relaciones

*Sin relaciones*

## Descripcion

Cuando se realiza una compra desde el sitio de LO con envío gratis, el costo adicional se registra como cero. Este campo es importante para calcular el costo real del envío para la empresa.
`NewBytes_DBF.dbo.pedclil.ncostoextra`

[adjunto]
```
{{API_URL}}/pedidos/checkout/confirmar
```
