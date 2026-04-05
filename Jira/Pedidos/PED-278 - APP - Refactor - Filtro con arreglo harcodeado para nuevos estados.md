---
jira_key: "PED-278"
aliases: ["PED-278"]
summary: "APP - Refactor - Filtro con arreglo \"harcodeado\" para nuevos estados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-11-23 08:43"
updated: "2024-05-09 14:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-278"
---

# PED-278: APP - Refactor - Filtro con arreglo "harcodeado" para nuevos estados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-23 08:43 |
| Actualizado | 2024-05-09 14:51 |
| Etiquetas | ninguna |
| Jira | [PED-278](https://bluinc.atlassian.net/browse/PED-278) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **relates to:** [[PED-710]] APP - Refactor - Mejora para conservar linealidad en el filtro de estados cambiar reservas por remitidos

## Descripcion

Agregaremos dos nuevos estados al siguiente filtro, sumando debajo los que vienen en el repositorio.


[adjunto]
- Pendiente


- Reservado



Cuando elegimos cualquiera de estos dos estados, en vez de enviar el paramento `orderStatus`  enviaremos `status`

tomando los valores `P` o `s` según corresponda.

```
{{API_URL}}/v1/orders?itemsPerPage=15&currentPage=1&orderStatus=5&status=S
```
