---
jira_key: "COM-181"
aliases: ["COM-181"]
summary: "API - Refactor - Agregar providerOrderInboundId (de nnumalb) a recurso existente de órdenes entrantes de proveedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-06 08:29"
updated: "2025-05-19 13:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-181"
---

# COM-181: API - Refactor - Agregar providerOrderInboundId (de nnumalb) a recurso existente de órdenes entrantes de proveedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-06 08:29 |
| Actualizado | 2025-05-19 13:35 |
| Etiquetas | ninguna |
| Jira | [COM-181](https://bluinc.atlassian.net/browse/COM-181) |

## Relaciones

- **Padre:** [[COM-12]] Listar ingresos (despachos de compra)

## Descripcion

El recurso que consume el endpoint


```
GET {API_URL}/v1/providerOrderInbound?currentPage=1&itemsPerPage=15
```

```
{
  "id": 9745,
  "providerOrder": 11643,
  "providerId": "000002",
  "providerName": "CORCISA SA",
  "dispatchName": "",
  "userId": "14",
  "updated": 0,
  "dispatchDate": "2025-04-30 00:00:00.000",
  "numPed": 11643,
  "fullSerialized": true,
  "total": 2992793.832,
  "totalFinal": 3621280.53672,
  "iva": 0,
  "companyCode": 0,
  providerOrderInboundId: 15912 <--- Se agrega
}
```



- Incorporar el campo `providerOrderInboundId`, que debe mapearse desde el campo `nnumalb` de la tabla `[NewBytes_DBF].[dbo].[albprot]`.


- Permitir realizar búsquedas usando el parámetro `search` aplicando filtro sobre `nnumalb`.



**Ejemplo de búsqueda esperada:**

```
GET {API_URL}/v1/providerOrderInbound?currentPage=1&itemsPerPage=15&search=12345
```



**Criterios de aceptación:**

- El campo `providerOrderInboundId` aparece en las respuestas del recurso.


- El campo se obtiene correctamente desde la tabla `albprot.nnumalb`.


- El parámetro `search` permite filtrar por `nnumalb`ademas de lo que ya se podia que era nombre de proveedor y providerOrder.


- Se mantienen intactas las funcionalidades existentes del recurso.
