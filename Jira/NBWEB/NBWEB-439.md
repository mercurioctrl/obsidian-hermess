---
jira_key: "NBWEB-439"
summary: "API - CMS - Editar medios de envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-04 16:13"
updated: "2022-11-09 11:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-439"
---

# NBWEB-439: API - CMS - Editar medios de envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-04 16:13 |
| Actualizado | 2022-11-09 11:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-439](https://bluinc.atlassian.net/browse/NBWEB-439) |

## Descripción

```
PATCH {{API_URL}}/v1/cms/shippingMethods
```

Request

```
[
  {
  'shippingMethodId': 3,
  'description': 'Moto',
  'active': 1
  } 
]
```

Segun el parametro que se envie, se modifica. Puede ser uno o varios, pero siempre debe estar el id.

Los campos editables son

-  name


- description


- active


- extraDayMin


- extraDayMax


- kmPrice


- minFee


- maxDistance


- insuredLimit
