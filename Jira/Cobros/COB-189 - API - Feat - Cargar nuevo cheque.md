---
jira_key: "COB-189"
aliases: ["COB-189"]
summary: "API - Feat - Cargar nuevo cheque"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-10-20 16:03"
updated: "2022-12-15 14:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-189"
---

# COB-189: API - Feat - Cargar nuevo cheque

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-20 16:03 |
| Actualizado | 2022-12-15 14:18 |
| Etiquetas | ninguna |
| Jira | [COB-189](https://bluinc.atlassian.net/browse/COB-189) |

## Relaciones

- **Padre:** [[COB-188]] Feat - Cargar nuevo cheque
- **blocks:** [[COB-190]] APP - Feat - Cargar nuevo cheque
- **relates to:** [[COB-259]] API - Refactor - Cargar nuevo cheque

## Descripcion

Según las tablas obtenidas en [link](https://lioteam.atlassian.net/browse/COB-179) se debe poder crear un registro de un nuevo cheque, en base a los datos obtenidos de un modal de entrada con un formulario [link](https://lioteam.atlassian.net/browse/COB-186)

```
POST {API_URL}/v1/checks
```

```
{
checkNumber: 67104822,
clientId: 34324,
branch: 150,
bankId: 3,
bankAccountNumber: 3,
ammount: 826495.99,
receptionDate: 27/09/2022,
emitDate: 27/09/2022,
dateCharged: 27/09/2022,
clearingTime: 48hs,
status: //aca el ejemplop dice recibido, por ahi se esta gurdando como un string, pero de tener un id, es mejor ir por ahi
own: true,
AccountHolder: 34324,
branch: 0002,
cnnumab: //numero de pedido o remito fp
}
```



En el próximo paso, agregaremos la conexión entre el paso de cobro y el alta de cheque, que no siempre se dan en simultaneo, pero casi siempre es asi, ver: [link](https://lioteam.atlassian.net/browse/COB-126)

Importante: Esto impacta en el saldo de cheques, consultar con Ema de que forma impactar sobre el saldo de cheque.
