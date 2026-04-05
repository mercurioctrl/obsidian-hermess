---
jira_key: "COM-235"
aliases: ["COM-235"]
summary: "API -  MVP - Refactor agregar atributo representante al ver/editar un Proveedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-10-17 09:52"
updated: "2025-11-26 02:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-235"
---

# COM-235: API -  MVP - Refactor agregar atributo representante al ver/editar un Proveedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-17 09:52 |
| Actualizado | 2025-11-26 02:21 |
| Etiquetas | ninguna |
| Jira | [COM-235](https://bluinc.atlassian.net/browse/COM-235) |

## Relaciones

- **Padre:** [[COM-98 - Repositorio de impuestos por posicionar arancelaria|COM-98]] Repositorio de impuestos por posicionar arancelaria
- **has action item:** [[COM-236 - APP - MVP - Refactor agregar atributo representante al creareditar un Proveedor|COM-236]] APP -  MVP - Refactor agregar atributo representante al crear/editar un Proveedor

## Descripcion

Se debe **refactorizar el recurso** para incorporar un **nuevo parámetro** en el payload que permita **guardar el representante del proveedor**.
También se debe agregar una **nueva columna** en la tabla `[NewBytes_DBF].[dbo].[FP_Proveedores]` para almacenar ese valor.

```
PATCH {API_URL}/v1/providers
```

```
{
  "id":16385,
  "businessName":"INGRAM MICRO INC.",
  "name":"INGRAM MICRO INC.",
  "address":"2000 NW 84TH AVE. MIAMI FL",
  "countryId":0,
  "locateId":0,
  "provinceId":0,
  "ccoddiv":"DOL",
  "representative": "John Doe"
}
```

**Detalles técnicos:**

- Agregar el nuevo campo `representative`  o equivalente según convención del sistema).


- Modificar el endpoint `PATCH /v1/providers` para recibir este nuevo parámetro y actualizarlo en la base de datos.



Lo mismo haremos al momento de obtener el repositorio con 

```
GET {API_URL}/v1/providers
```

```
{
    "response": [
        {
            "id": 16388,
            "providerCode": "002320",
            "name": "MSI COMPUTER CORP.",
            "businessName": "MSI COMPUTER CORP.",
            "address": "901 CANADA COURT. CITY OF INDUSTRY, CA",
            "countryId": 0,
            "prefixFlag": "",
            "countryDescription": "",
            "countryFlagId": 0,
            "provinceId": 0,
            "locateId": 0,
            "ccoddiv": "DOL",
            "locateDescription": "",
            "companyCode": 4,
            "representative": "John Doe"
        },
        ...
```
