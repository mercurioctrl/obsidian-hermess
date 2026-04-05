---
jira_key: "POS-78"
aliases: ["POS-78"]
summary: "APP - Feat - Contadores para burbujas de cantidad pendientes"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-08-23 14:53"
updated: "2022-10-12 08:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-78"
---

# POS-78: APP - Feat - Contadores para burbujas de cantidad pendientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-23 14:53 |
| Actualizado | 2022-10-12 08:50 |
| Etiquetas | ninguna |
| Jira | [POS-78](https://bluinc.atlassian.net/browse/POS-78) |

## Relaciones

- **Padre:** [[POS-12 - Bases del proyecto y formularios|POS-12]] Bases del proyecto y formularios
- **is blocked by:** [[POS-55 - API - Feat - Contadores para burbujas de cantidad pendientes|POS-55]] API - Feat - Contadores para burbujas de cantidad pendientes

## Descripcion

Se trata de un recurso necesario para cargar las cantidades de elementos pendientes para cada pestaña.

En principio actualizaremos la cantidad cada 5 min, o con cada cambio de pestaña.

Las pestañas son:

- Pre-Ingresos (Los que aun no fueron pasados a ingreso)


- Ingresos (Los que aun no tienen asignado un técnico, o tienen técnico pero no diagnostico)


- Pases de mercadería (Pases de mercadería que aun están pendientes)


- Créditos (Créditos pendientes no realizados)



 

```
GET {API_URL}/v1/pendings
```

```
{
  "preAfterSales":3,
  "afterSales":5,
  "passes":4,
  "aftersalesCredits":3
}
```
