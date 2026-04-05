---
jira_key: "COB-100"
aliases: ["COB-100"]
summary: "API - Feat - Opciones concepto salidas varias"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-09-15 09:13"
updated: "2022-10-13 09:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-100"
---

# COB-100: API - Feat - Opciones concepto salidas varias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-15 09:13 |
| Actualizado | 2022-10-13 09:01 |
| Etiquetas | ninguna |
| Jira | [COB-100](https://bluinc.atlassian.net/browse/COB-100) |

## Relaciones

- **Padre:** [[COB-21]] Base del proyecto y formularios

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
