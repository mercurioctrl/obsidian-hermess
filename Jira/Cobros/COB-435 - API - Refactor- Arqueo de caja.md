---
jira_key: "COB-435"
aliases: ["COB-435"]
summary: "API - Refactor- Arqueo de caja"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2023-05-22 13:08"
updated: "2023-06-12 07:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-435"
---

# COB-435: API - Refactor- Arqueo de caja

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2023-05-22 13:08 |
| Actualizado | 2023-06-12 07:09 |
| Etiquetas | ninguna |
| Jira | [COB-435](https://bluinc.atlassian.net/browse/COB-435) |

## Relaciones

- **is blocked by:** [[COB-436 - APP - Refactor - Arqueo de caja|COB-436]] APP - Refactor - Arqueo de caja

## Descripcion

Se recibe en el form un parametro

`cashRegisterOk`:false o true, cuando es true es manual y cuando es false no debe cambiar el valor en el objeto user

```json
{
cashRegisterOk:false, // true || false
amounts:[
    {
        "scAmount": 484294.459,
        "paymesntId": 1
    },
    {
        "scAmount": 13162142,
        "paymentId": 2
    },
    {
        "scAmount": 0,
        "paymentId": 15
    }
 ]
}
```
