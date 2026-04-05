---
jira_key: "NBWEB-303"
summary: "API - Feat - Mi vendedor"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-28 09:13"
updated: "2022-07-11 15:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-303"
---

# NBWEB-303: API - Feat - Mi vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-28 09:13 |
| Actualizado | 2022-07-11 15:13 |
| Etiquetas | ninguna |
| Jira | [NBWEB-303](https://bluinc.atlassian.net/browse/NBWEB-303) |

## Descripción

Se trata de la informacion respecto al vendedor, para saber que vendedor corresponde a cada cliente: En la tabla `newbytes_dbf.dbo.clientes` podemos encontrar la columna `ccodage`

```
GET {{API_URL}}/v1/miCuenta/miVendedor
```



```
[
  {
    "roleAgent": "Ejecutivo de cuentas",
    "whatsappAgent": "(+54911) 7082-0099",
    "phoneAgent": "(5411) 4011-8813",
    "nameAgent": "Patricio Contardi",
    "emailAgent": "pcontardi@nb.com.ar                               "
  }
]
```
