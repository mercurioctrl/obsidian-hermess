---
jira_key: "COB-562"
aliases: ["COB-562"]
summary: "API - Refactor - Agregar informacion a las salidas pendientes necesaria para retiros de wallet  (POST)"
status: "Finalizada"
type: "Tarea"
priority: "Low"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-06-02 14:29"
updated: "2025-07-14 10:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-562"
---

# COB-562: API - Refactor - Agregar informacion a las salidas pendientes necesaria para retiros de wallet  (POST)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Low |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-02 14:29 |
| Actualizado | 2025-07-14 10:37 |
| Etiquetas | ninguna |
| Jira | [COB-562](https://bluinc.atlassian.net/browse/COB-562) |

## Relaciones

- **Padre:** [[COB-19 - Cola de salidas|COB-19]] Cola de salidas
- **has action item:** [[COB-564 - APP - Refactor - Agregar nuevos campos dentro del formulario de solicitud de|COB-564]] APP - Refactor - Agregar nuevos campos dentro del formulario de solicitud de salida de retiro (y precarga para generar la salida)

## Descripcion

Revisa la historia completa y avisame si consideras que requiere algún cambio

Actualmente el recurso 

```
POST /v1/pendingCashOut
```

permite registrar una solicitud de retiro con los siguientes campos:

```
{
  "amount": "1",
  "paymentMethodId": 2,
  "outputConceptId": 30,
  "reference": "Algo de prueba",
  "currencyQuote": 927,
  "type": "bankTransfers",
  "agentId": "49"
}
```

Sin embargo, se necesita **refactorizar este endpoint** para incluir los siguientes **campos adicionales**:

```
{
  "userIdLo": 32,
  "clientId": 3434 <-- Este es el cliente para NB
  "clientsBankAccountId": 432,
  "bankCBU": "2850590940090418135201",
  "bankAlias": "juanperez.mp",
  "output_concept_id": "retiros billetera libre opcion"
}

```

**Criterios de aceptación:**

- El endpoint debe aceptar los nuevos campos indicados.


- Los valores deben ser validados y almacenados correctamente en la base de datos o vinculados a través de una relación con la tabla `[PendingCashOut]`.


- La estructura de respuesta no debe romper compatibilidad con integraciones actuales.


- El campo `output_concept_id` debe poder ser utilizado tanto como ID numérico como texto literal (caso: "retiros billetera libre opcion").


- Debe mantenerse trazabilidad de qué usuario (`userIdLo`) realizó la operación.


- Si se provee `clientsBankAccountId`, deben persistirse o vincularse también los datos `bankCBU` y `bankAlias`.



Revisa la historia completa y avisame si consideras que requiere algún cambio
