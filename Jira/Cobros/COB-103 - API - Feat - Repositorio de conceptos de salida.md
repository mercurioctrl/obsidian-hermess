---
jira_key: "COB-103"
aliases: ["COB-103"]
summary: "API - Feat - Repositorio de conceptos de salida"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-09-15 09:27"
updated: "2022-10-25 09:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-103"
---

# COB-103: API - Feat - Repositorio de conceptos de salida

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-15 09:27 |
| Actualizado | 2022-10-25 09:04 |
| Etiquetas | ninguna |
| Jira | [COB-103](https://bluinc.atlassian.net/browse/COB-103) |

## Relaciones

- **Padre:** [[COB-101]] Feat - Realizar salida de caja
- **relates to:** [[SNB-350]] TIPOS DE SALIDA - CAJA 

## Descripcion

Basados en la tabla `SELECT * from dbo.BA_BP_DESTINOS_SALIDAS;`

```
GET {URL_API}/v1/outputConcepts
```

```json
[
  {
    "ID": 1,
    "description": "Liquidacion Cupones Visa"
  },
  {
    "ID": 34,
    "description": "Pase entre Caja y Cuenta - Salida"
  },
  {
    "ID": 2,
    "description": "IVA BANCOS"
  },
  {
    "ID": 3,
    "description": "Pagos de Facturas"
  },
  {
    "ID": 35,
    "description": "Pago a Proveedores"
  }
  ...
  ]
```
