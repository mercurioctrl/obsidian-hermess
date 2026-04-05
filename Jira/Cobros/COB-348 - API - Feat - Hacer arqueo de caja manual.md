---
jira_key: "COB-348"
aliases: ["COB-348"]
summary: "API - Feat - Hacer arqueo de caja manual"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-10 08:29"
updated: "2023-03-13 11:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-348"
---

# COB-348: API - Feat - Hacer arqueo de caja manual

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-10 08:29 |
| Actualizado | 2023-03-13 11:02 |
| Etiquetas | ninguna |
| Jira | [COB-348](https://bluinc.atlassian.net/browse/COB-348) |

## Relaciones

- **Padre:** [[COB-347 - Poder ver saldo inicial y final de caja en cada día|COB-347]] Poder ver saldo inicial y final de caja en cada día
- **blocks:** [[COB-350 - APP - Feat - Modal para hacer arqueo de caja manual|COB-350]] APP - Feat - Modal para hacer arqueo de caja manual

## Descripcion

Agregaremos un recurso para contabilizar el saldo actual de la caja PERO FISICO. Es decir lo que cuenta el cajero.

Para esto ofreceremos un modal [link](https://lioteam.atlassian.net/browse/COB-350)  donde el cajero puede ingresar 3 valores, uno para PESOS, otro para DOLARES y otro para CHEQUES.

Una vez que tengamos estos valores los guardaremos en `[NEW_BYTES].[dbo].[MC_SALDOS_INICIO]`.

A esta tabla, le haremos un “refactor” para agregar la columna “`SI_IMPORTE_MANUAL`" columnas extra donde registrar el conteo manual.

De esta forma podremos registrar los saldos de sistema en `SI_IMPORTE` y el conteo manual que acaba de ingresar el usuario en `SI_IMPORTE_MANUAL`

```
POST {API_URL}/v1/boxBalance/{caja}/cashRegister
```

```
{
    "scAmount": 484294.459,
    "paymentId": 1
},
{
    "scAmount": 13162142,
    "paymentId": 2
},
{
    "scAmount": 0,
    "paymentId": 3
}
```

Solo puede hacerse una vez por fecha para cada caja y deben estar los 3 saldos.

En caso de que estos importes difieran debo retornar el objeto discrepancy indicando las diferencias como en el ejemplo siguiente.

```
{
succes:true,
commnet: "Se registraron los saldos, pero existen diferencias con los saldos contabilizados y registrados en sistemas"
discrepancy: [
    {
    "discrepancyAmount": 4234,
    "paymentId": 2
    },
    {
    "discrepancyAmount": 434,
    "paymentId": 3
    }
  ]
}
```

En caso de que todo este bien, devolvemos

```
{
succes:true,
commnet: "Se registraron los saldos"
}
```
