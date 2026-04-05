---
jira_key: "POS-134"
aliases: ["POS-134"]
summary: "MS - Feat - Repositorio de tipos de comprobante que podemos emitir"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-09-16 12:53"
updated: "2022-10-27 17:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-134"
---

# POS-134: MS - Feat - Repositorio de tipos de comprobante que podemos emitir

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-16 12:53 |
| Actualizado | 2022-10-27 17:38 |
| Etiquetas | ninguna |
| Jira | [POS-134](https://bluinc.atlassian.net/browse/POS-134) |

## Relaciones

- **Padre:** [[POS-123 - MS - Servicio de emision de comprobantes|POS-123]] MS - Servicio de emision de comprobantes
- **blocks:** [[POS-132 - MS - Feat - Emitir comprobante|POS-132]] MS - Feat - Emitir comprobante

## Descripcion

Basados en la tabla `[NewBytes_DBF].[dbo].[FP_TiposDocumentosCobro] `

Crearemos un recurso para obtener facilmente que tipos de documentos podemos emitir. 

```
GET {API_URL}/v2/voucherTypes
```

retorna

```json
[
  {
    "id": 3,
    "description": "NOTA DE DEBITO",
    "order": 3,
    "signo": 1,
    "cod_A": "02",
    "cod_B": "07",
    "cod_C": "12",
    "cod_E": "20"
  },
  {
    "id": 1,
    "description": "FACTURA",
    "order": 1,
    "signo": 1,
    "cod_A": "01",
    "cod_B": "06",
    "cod_C": "11",
    "cod_E": "19"
  },
  {
    "id": 2,
    "description": "NOTA DE CREDITO",
    "order": 4,
    "signo": -1,
    "cod_A": "03",
    "cod_B": "08",
    "cod_C": "13",
    "cod_E": "21"
  },
  ...
  ]
```
