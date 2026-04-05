---
jira_key: "COB-65"
aliases: ["COB-65"]
summary: "API - Feat - Realizar un pasa a otra caja "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-26 10:25"
updated: "2022-10-20 17:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-65"
---

# COB-65: API - Feat - Realizar un pasa a otra caja 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-26 10:25 |
| Actualizado | 2022-10-20 17:11 |
| Etiquetas | ninguna |
| Jira | [COB-65](https://bluinc.atlassian.net/browse/COB-65) |

## Relaciones

- **Padre:** [[COB-12]] Feat - Procesar pases de caja
- **blocks:** [[COB-67]] APP - Feat - Modal para realizar un pase a otra caja

## Descripcion

Este recurso se trata sobre como crear un pase desde la caja de origen, hasta la caja destino. Luego este debe ser aceptado por la caja de destino para (en ese momento impactamos el monto) finalizar la operación. También existe la posibilidad de que sea rechazado.

Para esto:

Se debe generar una operación en `[MC_LOG_OPERACIONES]`

Mediante el recurso 

```
POST {{API_URL}}/v1/passesTrade
```

se envía la siguiente request

```
[
  {
    description: 'Pases egresos', // puede no estar porque  esta transactionTypeId
    ammount: 2343.34,
    currency: 'Pesos',
    comment: 'Un comentario cualquiera',
    origin: 'Caja1',
    destiny: 'Dario',
    status: 'Abierto',
    satusId: 1,
    paymentMethodId: 1,
    transactionTypeId: 20
  }
  ]
```

Con esta informacion mas la informacion disponible en el back se debe confeccionar una fila en `[MC_LOG_OPERACIONES]`
