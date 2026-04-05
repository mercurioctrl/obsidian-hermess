---
jira_key: "COB-438"
aliases: ["COB-438"]
summary: "APP - Refactor - Agregar etiqueta indicativa y filtro para clientes activos/inactivos/todos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-06-05 07:58"
updated: "2023-06-07 16:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-438"
---

# COB-438: APP - Refactor - Agregar etiqueta indicativa y filtro para clientes activos/inactivos/todos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-05 07:58 |
| Actualizado | 2023-06-07 16:48 |
| Etiquetas | ninguna |
| Jira | [COB-438](https://bluinc.atlassian.net/browse/COB-438) |

## Relaciones

- **Padre:** [[COB-54]] APP - Feat - Listar clientes
- **blocks:** [[SNB-812]] CLIENTES REPETIDOS - VER EN SISTEMA 
- **is blocked by:** [[COB-437]] API - Refactor - Agregar parametro y filtro para clientes activos/inactivos/todos

## Descripcion

Basándonos en el requerimiento [link](https://lioteam.atlassian.net/browse/SNB-812) agregaremos el filtro con las opciones

- Activos


- Inactivos


- Todos




Al iniciar la pestaña debe estar desactive=false para mostrar solo los activos

Usaremos el refactor de [link](https://lioteam.atlassian.net/browse/COB-437) 

```
GET {API_RUL}/v1/clients
```

Y ahora el objeto debería traer el atributo `desactive` con el cual mostraremos una “etiqueta” tipo  

```json
{
    "clientId": "026887",
    "clientName": "PIGNANI MATIAS NICOLAS",
    "clientBusinessName": "PIGNANI MATIAS NICOLAS",
    "clientTaxNumber": "20-33947793-1",
    "clientPerception": 0.0,
    "limitCheckBalanceAmount": 2004252.04,
    "usedCheckBalanceAmount": 2004252.04,
    "limitBalanceAmount": 2000.0,
    "usedBalanceAmount": 122.06,
    "desactive": {true/false} < SE AGREGA UN NUEVO PARAMETRO
    }
```
