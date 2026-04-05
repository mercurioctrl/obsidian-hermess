---
jira_key: "COB-563"
aliases: ["COB-563"]
summary: "API - Refactor - Agregar informacion a las salidas pendientes necesaria para retiros de wallet (GET)"
status: "Finalizada"
type: "Tarea"
priority: "Low"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-06-02 14:41"
updated: "2025-07-14 10:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-563"
---

# COB-563: API - Refactor - Agregar informacion a las salidas pendientes necesaria para retiros de wallet (GET)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Low |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-02 14:41 |
| Actualizado | 2025-07-14 10:38 |
| Etiquetas | ninguna |
| Jira | [COB-563](https://bluinc.atlassian.net/browse/COB-563) |

## Relaciones

- **Padre:** [[COB-19]] Cola de salidas
- **has action item:** [[COB-564]] APP - Refactor - Agregar nuevos campos dentro del formulario de solicitud de salida de retiro (y precarga para generar la salida)

## Descripcion

Revisa la historia completa y avisame si consideras que requiere algún cambio

Actualmente el recurso 

```
GET /v1/pendingCashOut
```

 devuelve una lista paginada de retiros con campos básicos como `amount`, `agentId`, `paymentMethodId`, `outputConceptId`, etc de la siguiente forma

```
{
    "response": [
        {
            "date": "16-03-2025 23:02",
            "id": 54,
            "userId": "LO",
            "clientId": 3434 <-- Este es el cliente para NB
            "agentName": "SAF SAF            ",
            "agentId": 0,
            "amount": 1,
            "paymentMethodId": 1,
            "outputConceptId": 43,
            "reference": "",
            "currencyQuote": 927,
            "pending": false,
            "type": "cashOut",
            "agentIdCreator": 0,
            "agentNameCreator": "",
            "userBoxCreator": ""
        },
        {
            "date": "16-03-2025 23:35",
            "id": 55,
            "userId": "LO",
            "agentName": "SAF SAF            ",
            "agentId": 0,
            
....            
```

Se requiere **refactorizar este endpoint** para que también devuelva los siguientes campos, necesarios para precargar el formulario de retiro con información más completa:

```
{
    "response": [
        {
            "date": "16-03-2025 23:02",
            "id": 54,
            "userId": "LO",
            "agentName": "SAF SAF            ",
            "agentId": 0,
            "amount": 1,
            "paymentMethodId": 1,
            "outputConceptId": 43,
            "reference": "",
            "currencyQuote": 927,
            "pending": false,
            "type": "cashOut",
            "agentIdCreator": 0,
            "agentNameCreator": "",
            "userBoxCreator": "",
            "userIdLo": 32,  <--- NUEVO
            "clientsBankAccountId": 432, <--- NUEVO
            "bankCBU": "2850590940090418135201", <--- NUEVO
            "bankAlias": "juanperez.mp" <--- NUEVO
        },
        {
            "date": "16-03-2025 23:35",
            "id": 55,
            "userId": "LO",
            "agentName": "SAF SAF            ",
            "agentId": 0,
            
....     
```

Estos campos ya existen en la base de datos, posiblemente en la tabla `[NEW_BYTES].[dbo].[PendingCashOut]`, y deben integrarse correctamente en la respuesta.

**Criterios de aceptación:**

- El recurso debe incluir en cada item de la lista los campos: `userIdLo`, `clientsBankAccountId`, `bankCBU`, y `bankAlias`.


- Estos datos deben obtenerse directamente o mediante JOIN a las tablas correspondientes si no están en `PendingCashOut`.


- La respuesta debe mantener compatibilidad hacia atrás con el frontend actual.


- Los datos deben estar disponibles para todos los retiros que los tengan asociados.


- El campo `clientsBankAccountId` debe representar la cuenta bancaria del cliente asociada al retiro.


- Alguno de estos datos (los que no vienen de LO, sino por el formulario normal de cobros) pueden no tener estos datos presentes
