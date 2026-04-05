---
jira_key: "COM-233"
aliases: ["COM-233"]
summary: "API - MVP - Agregar filtro de empresa a la pestaña de impuestos/gasto (tariffTax)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-10-16 18:27"
updated: "2025-11-20 15:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-233"
---

# COM-233: API - MVP - Agregar filtro de empresa a la pestaña de impuestos/gasto (tariffTax)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-16 18:27 |
| Actualizado | 2025-11-20 15:09 |
| Etiquetas | ninguna |
| Jira | [COM-233](https://bluinc.atlassian.net/browse/COM-233) |

## Relaciones

- **Padre:** [[COM-98]] Repositorio de impuestos por posicionar arancelaria
- **has action item:** [[COM-232]] APP - MVP - Agregar filtro de empresa a la pestaña de impuestos/gasto (tariffTax)
- **relates to:** [[COM-250]] APP - MVP - Refactor - Crear y editar impuesto/gasto -> agregar selector de empresa
- **relates to:** [[COM-254]] API - MVP - Refactor - Listar repositorio de impuestos/gastos -> Agregar companyCode y companyDescription

## Descripcion

Actualizado:

Se debe implementar el filtrado en el recurso:

cpde

```
GET {{API_URL}}/v1/tariffTax?distribute=true&companyCode=11
```

Para esto se requiere el siguente campo.

```sql
alter table NewBytes_DBF.[dbo].[FP_IMPUESTOS]
add companyCode int     default 0
```





Debido a que se agrego este nuevo campo tambien se ajustaron los recurso para editar y crear. 

permitiendo ajustar el campo companyCode.

Crear:

```
POST {{API_URL}}/v1/tariffTax
```



Actualizar:

```
PATCH {{API_URL}}/v1/tariffTax
```
