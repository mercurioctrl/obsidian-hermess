---
jira_key: "NBWEB-266"
summary: "API - Feat - Contacto - Vendedores"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-21 17:34"
updated: "2022-06-26 21:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-266"
---

# NBWEB-266: API - Feat - Contacto - Vendedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-21 17:34 |
| Actualizado | 2022-06-26 21:10 |
| Etiquetas | ninguna |
| Jira | [NBWEB-266](https://bluinc.atlassian.net/browse/NBWEB-266) |

## Descripción

```
GET {{API_URL}}/v1/contact/agents
```

Dada la tabla

```sql
SELECT
[firma_puesto] 
,[firma_whatsapp]  
,[firma_telefono]  
,[firma_nombre]  
, agentes.cemail 
FROM [NewBytes_DBF].[dbo].[agentes]
where     (rtrim(ltrim(firma_nombre)) IS NOT NULL OR rtrim(ltrim(firma_puesto)) IS NOT NULL)
```

Retornar

```json
[
  {
    "roleAgent": "Ejecutivo de cuentas",
    "whatsappAgent": "(+54911) 7082-0099",
    "phoneAgent": "(5411) 4011-8813",
    "nameAgent": "Patricio Contardi",
    "emailAgent": "pcontardi@nb.com.ar                               "
  },
  {
    "roleAgent": "Ejecutivo de cuentas",
    "whatsappAgent": null,
    "phoneAgent": "(5411) 4011-8815",
    "nameAgent": "Cristian Baldissera",
    "emailAgent": "cbaldissera@nb.com.ar                             "
  },
  {
    "roleAgent": "Product Manager",
    "whatsappAgent": "(+54911) 4011-8814",
    "phoneAgent": "(5411) 4011-8814",
    "nameAgent": "Galo Blanco",
    "emailAgent": "galo@nb.com.ar                                   "
  },
  {
    "roleAgent": "Ejecutiva De Cuentas",
    "whatsappAgent": "(+54911) 7081-0011",
    "phoneAgent": "(5411) 4011-8809",
    "nameAgent": "Andrea Altamiranda",
    "emailAgent": "aaltamiranda@nb.com.ar                       "
  },
  ...
  ]
```
