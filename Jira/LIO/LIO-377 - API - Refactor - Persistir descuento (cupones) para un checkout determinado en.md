---
jira_key: "LIO-377"
aliases: ["LIO-377"]
summary: "API - Refactor - Persistir descuento (cupones) para un checkout determinado en la base de datos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-07-06 19:33"
updated: "2025-07-16 10:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-377"
---

# LIO-377: API - Refactor - Persistir descuento (cupones) para un checkout determinado en la base de datos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-06 19:33 |
| Actualizado | 2025-07-16 10:38 |
| Etiquetas | ninguna |
| Jira | [LIO-377](https://bluinc.atlassian.net/browse/LIO-377) |

## Relaciones

- **Padre:** [[LIO-373]] Seguridad del checkout y protección de transacciones

## Descripcion

Se requistra en la tabla  `LO.dbo.checkout_snapshot_data` tanto el `payload` como el `response` del recurso.

en los campos cupon_payload, cupon_response.

-- CUPON descuento

```
POST /descuentos/cupones/validar
```


`payload`:


```json
{
    "pedidoId": 734996,
    "codigo": "CLIENTEFELIZ25"
}
```

`resoponse`:

```json
{
    "678421": {
        "descuentoCupon": 4720.5,
        "descuentoFinal": 4720.5
    }
}
```



En la tabla se marca en primera instancia tanto updated_at como created_at, posteriormente solo es actualizado el campo updated_at.
