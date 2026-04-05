---
jira_key: "NBWEB-661"
summary: "API - Feat - Agregar comprobante de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-20 13:52"
updated: "2024-03-25 02:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-661"
---

# NBWEB-661: API - Feat - Agregar comprobante de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-20 13:52 |
| Actualizado | 2024-03-25 02:20 |
| Etiquetas | ninguna |
| Jira | [NBWEB-661](https://bluinc.atlassian.net/browse/NBWEB-661) |

## Descripción

Crearemos un recurso para guardar imágenes (comprobantes) para NB 

```
PATCH {API_URL}/v1/order/paymentVoucher
```

```
[NBWEB].[dbo].[pedidosCabeceraComprobantePago]
```

```
[{
"branch":"0002",
"order":"10332469",
"fileImg":"4a509ce80414ee34f0336b06723319c8.png",
"cbu":"8888888888888888888888",
"nroOperacion":"42343242",
"nameOwner":"nombre del tituloar",
}
]
```
