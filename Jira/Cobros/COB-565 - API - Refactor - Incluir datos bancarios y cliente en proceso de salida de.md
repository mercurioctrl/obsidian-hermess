---
jira_key: "COB-565"
aliases: ["COB-565"]
summary: "API - Refactor - Incluir datos bancarios y cliente en proceso de salida de fondos que se hace con cashOut para procesar una solicitud de salida"
status: "Finalizada"
type: "Tarea"
priority: "Low"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-06-03 08:07"
updated: "2025-07-14 10:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-565"
---

# COB-565: API - Refactor - Incluir datos bancarios y cliente en proceso de salida de fondos que se hace con cashOut para procesar una solicitud de salida

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Low |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-03 08:07 |
| Actualizado | 2025-07-14 10:33 |
| Etiquetas | ninguna |
| Jira | [COB-565](https://bluinc.atlassian.net/browse/COB-565) |

## Relaciones

- **Padre:** [[COB-19]] Cola de salidas
- **has action item:** [[COB-564]] APP - Refactor - Agregar nuevos campos dentro del formulario de solicitud de salida de retiro (y precarga para generar la salida)

## Descripcion

Revisa la historia completa y avisame si consideras que requiere algún cambio

El recurso actual 

```
PATCH /v1/cashOut
```

 permite procesar la salida de fondos (transferencia bancaria o retiro) sobre una o varias solicitudes previamente creadas, como esta:

```
[
  {
    "date": "18-03-2025 15:48",
    "id": 75,
    "userId": "LO",
    "agentName": "SAF SAF",
    "agentId": 0,
    "amount": 3,
    "paymentMethodId": 1,
    "outputConceptId": 43,
    "reference": "",
    "currencyQuote": 927,
    "pending": true,
    "type": "cashOut",
    "agentIdCreator": 0,
    "agentNameCreator": "",
    "userBoxCreator": "",
    "checkbox": {
      "disabled": false,
      "value": false
    }
  }
]

```

Se necesita **refactorizar** este endpoint para permitir y procesar correctamente los siguientes **nuevos campos**:

```
{
  "userIdLo": 32,
  "clientId": 3434,
  "clientsBankAccountId": 432,
  "bankCBU": "2850590940090418135201",
  "bankAlias": "juanperez.mp",
  "outputConceptId": 43 //"retiros billetera libre opcion"
}

```

**Criterios de aceptación:**

- El recurso debe aceptar y procesar los campos: `userIdLo`, `clientId`, `clientsBankAccountId`, `bankCBU`, `bankAlias` y `output_concept_id`.


- Validar que `clientId` sea un cliente válido dentro del contexto de NB.


- Confirmar que la cuenta bancaria (`clientsBankAccountId`) corresponda al `clientId` vinculado.


- Persistir o auditar los datos bancarios (`CBU`, `Alias`) si corresponden a una transferencia (`type: bankTransfers`).


- Validar que `outputConceptId` se corresponda con su forma legible (`output_concept_id`) y guardarla si es necesario.


- Garantizar que el cambio no rompa compatibilidad con solicitudes anteriores que no enviaban estos campos.
