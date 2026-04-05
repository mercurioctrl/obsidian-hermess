---
jira_key: "PED-699"
aliases: ["PED-699"]
summary: "APP - Feat - Si tengo el parametro orderOwner en el objeto user mostrare esos pedidos/filtros del vendedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-04-25 15:54"
updated: "2024-04-29 09:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-699"
---

# PED-699: APP - Feat - Si tengo el parametro orderOwner en el objeto user mostrare esos pedidos/filtros del vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-25 15:54 |
| Actualizado | 2024-04-29 09:26 |
| Etiquetas | ninguna |
| Jira | [PED-699](https://bluinc.atlassian.net/browse/PED-699) |

## Relaciones

- **Padre:** [[PED-10]] Login y credenciales 
- **is blocked by:** [[PED-698]] API - Refactor - Agregar orderOwner como parametro opcional al objeto users
- **blocks:** [[SNB-1826]] NUMERO DE VENTA

## Descripcion

Como existen algunos vendedores que “ven” los datos de otro vendedor que los agrupa (ej: el caso de juan y camila que ven libre opcion), agregaremos a los selectores el agente o vendedor que viene en 

[link](https://lioteam.atlassian.net/browse/PED-698)  en el parametro `orderOwner` cuando este exsite, sino usaremos el de siempre.
