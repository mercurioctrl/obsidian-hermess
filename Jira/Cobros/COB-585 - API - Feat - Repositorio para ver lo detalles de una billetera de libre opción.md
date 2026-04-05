---
jira_key: "COB-585"
aliases: ["COB-585"]
summary: "API - Feat - Repositorio para ver lo detalles de una billetera de libre opción determinada (transactions)"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-10-03 08:35"
updated: "2025-10-09 15:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-585"
---

# COB-585: API - Feat - Repositorio para ver lo detalles de una billetera de libre opción determinada (transactions)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-03 08:35 |
| Actualizado | 2025-10-09 15:09 |
| Etiquetas | ninguna |
| Jira | [COB-585](https://bluinc.atlassian.net/browse/COB-585) |

## Relaciones

- **Padre:** [[COB-581 - Repositorio y Gestión de Billeteras Libre Opción|COB-581]] Repositorio y Gestión de Billeteras Libre Opción
- **has action item:** [[COB-586 - APP - Feat - Ver transacciones de billetera por usuario LO|COB-586]] APP - Feat - Ver transacciones de billetera por usuario LO

## Descripcion

De la misma forma que lo hacemos en Libre Opcion, agregaremos el recurso “transactions” para poder visualizar el detalle de una billetera

```
GET {API_URL}/v4/wallets/transactions/{loUserId}
```

```
{
    "transactions": [
        {
            "transactionId": 908851,
            "amount": 2590,
            "currency": "ARS",
            "conceptId": 0,
            "concept": "Pago Comisiones",
            "date": "2025-07-18 14:48:09",
            "transactionType": "income",
            "pending": false
        }
    ],
    "pagination": {
        "total": 1,
        "offset": 0,
        "limit": 10,
        "order": "desc"
    }
}
```

### Path Params

- `loUserId` (int, requerido): identificador del usuario de Libre Opción.



### Query Params opcionales

- `offset` (int, default: 0)


- `limit` (int, default: 10, máx. 100)


- `order` (string, default: `"desc"`, valores permitidos: `"asc"`, `"desc"`)



## Criterios de Aceptación 

- El recurso debe devolver la lista de transacciones asociadas al `loUserId`.


- Cada transacción debe incluir:

- `transactionId`


- `amount`


- `currency`


- `conceptId`


- `concept`


- `date`


- `transactionType` (`income` o `expense`)


- `pending` (true/false)




- La respuesta debe incluir bloque `pagination` con `total`, `offset`, `limit`, `order`.


- El orden por defecto de las transacciones es `desc` (más recientes primero).


- Si `loUserId` no existe → devolver `404 Not Found`.


- Si el usuario no tiene transacciones → devolver `"transactions": []` con paginación en `total=0`.


- Sin token válido → `401 Unauthorized`.
