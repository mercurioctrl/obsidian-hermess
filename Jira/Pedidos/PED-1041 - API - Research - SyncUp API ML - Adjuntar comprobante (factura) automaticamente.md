---
jira_key: "PED-1041"
aliases: ["PED-1041"]
summary: "API - Research - SyncUp API ML - Adjuntar comprobante (factura) automaticamente si esta generada (con un syncUp)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-07 19:58"
updated: "2025-07-18 15:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1041"
---

# PED-1041: API - Research - SyncUp API ML - Adjuntar comprobante (factura) automaticamente si esta generada (con un syncUp)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-07 19:58 |
| Actualizado | 2025-07-18 15:53 |
| Etiquetas | ninguna |
| Jira | [PED-1041](https://bluinc.atlassian.net/browse/PED-1041) |

## Relaciones

- **Padre:** [[PED-915]] MercadoLibre
- **is blocked by:** [[PED-1042]] API - Comprobantes - Agregar metodo para descargar el comprobante automaticamente

## Descripcion

Buscaremos la forma de en principio, ver como adjuntar un comprobante o factura para una venta determinada realizada

Teóricamente es algo como esto

```
curl -X POST "https://api.mercadolibre.com/packs/$PACK_ID/fiscal_documents" \
     -H "Authorization: Bearer <ACCESS_TOKEN>" \
     -H "Content-Type: multipart/form-data" \
     -F "fiscal_document=@/ruta/a/Factura.pdf"
```

Nuestro desafió es que como nosotros en realidad las generamos diatónicamente, seguro tengamos que guardarla temporalmente, enviarla y luego borrarla, una vez que ya la marcamos como que le pudimos adjuntar la factura en nuestro `[NewBytes_DBF].[dbo].[pedcliML]`
