---
jira_key: "PED-402"
aliases: ["PED-402"]
summary: "APP - Feat - Ver seriales tomados para un pedido determinado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-12-27 13:05"
updated: "2023-12-28 17:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-402"
---

# PED-402: APP - Feat - Ver seriales tomados para un pedido determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-27 13:05 |
| Actualizado | 2023-12-28 17:57 |
| Etiquetas | ninguna |
| Jira | [PED-402](https://bluinc.atlassian.net/browse/PED-402) |

## Relaciones

- **Padre:** [[PED-400]] Ver serializacion
- **is blocked by:** [[PED-401]] API - Feat - Ver seriales tomados para un pedido determinado

## Descripcion

Agregaremos  un “Accionable” llamado “Ver serializacion” en el menu “boton derecho” al hacer clic sobre **una orden que esta liquidada**



Utilizando el recurso 

```
GET {API_URL}/v1/orders/{PEDIDO}/serials
```

levantaremos un modal de este tipo

[adjunto]
para poder mostrar los seriales para cada item que fueron tomando un producto
