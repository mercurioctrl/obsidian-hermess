---
jira_key: "POS-49"
summary: "API - Feat - Agregar filtros en lista de postventa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-02 07:38"
updated: "2022-10-04 09:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-49"
---

# POS-49: API - Feat - Agregar filtros en lista de postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-02 07:38 |
| Actualizado | 2022-10-04 09:55 |
| Etiquetas | ninguna |
| Jira | [POS-49](https://bluinc.atlassian.net/browse/POS-49) |

## Descripción

```
GET {API_URL}/v1/aftersales/{terminos de busqueda}?between=01-01-202_101-01-2022&status=processed&failType=2&outboundStatus=2&testSatuts=2&testProductStatus=2
```

Los terminos de busqueda pueden incluir

- Id de pre ingreso


- Id de ingreso


- id del cliente


- nombre del cliente


- nombre del producto


- numero de serie


- nombre de usuario


- fechas


- estado (si ya fue ingresado o no)


- failType


- outboundStatus


- testSatuts


- testProductStatus
