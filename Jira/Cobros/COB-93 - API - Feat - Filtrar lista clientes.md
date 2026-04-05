---
jira_key: "COB-93"
aliases: ["COB-93"]
summary: "API - Feat - Filtrar lista clientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-09-06 09:49"
updated: "2022-10-20 17:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-93"
---

# COB-93: API - Feat - Filtrar lista clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-06 09:49 |
| Actualizado | 2022-10-20 17:08 |
| Etiquetas | ninguna |
| Jira | [COB-93](https://bluinc.atlassian.net/browse/COB-93) |

## Relaciones

- **Padre:** [[COB-5 - API - Feat - Obtener cuenta corriente de un cliente|COB-5]] API - Feat - Obtener cuenta corriente de un cliente
- **is blocked by:** [[COB-94 - API - Feat - Listar condiciones fiscales|COB-94]] API - Feat - Listar condiciones fiscales

## Descripcion

```
{API_URL}/v1/clients/{terminos de busqueda}?currentPage=1&itemsPerPage=15
```

Se deben poder filtrar por los siguientes parametros

- Nombre del cliente


- Condicion Fiscal (monotributo, responsable inscripto, etc) (para esto vamos a necesitar un repo para listarlos [link](https://lioteam.atlassian.net/browse/COB-94) )



Se debe poder odernar por

- Orden alfabetico


- Los parámetros de saldo (limite de credito, disponible, deuda cheque, limite de cheque)
