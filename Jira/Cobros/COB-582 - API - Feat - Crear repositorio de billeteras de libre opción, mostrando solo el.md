---
jira_key: "COB-582"
aliases: ["COB-582"]
summary: "API - Feat - Crear repositorio de billeteras de libre opción, mostrando solo el saldo relativo a libre opción tal cual lo muestra la billetera para el cliente"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-10-02 09:58"
updated: "2025-12-29 09:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-582"
---

# COB-582: API - Feat - Crear repositorio de billeteras de libre opción, mostrando solo el saldo relativo a libre opción tal cual lo muestra la billetera para el cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-02 09:58 |
| Actualizado | 2025-12-29 09:10 |
| Etiquetas | ninguna |
| Jira | [COB-582](https://bluinc.atlassian.net/browse/COB-582) |

## Relaciones

- **Padre:** [[COB-581]] Repositorio y Gestión de Billeteras Libre Opción
- **has action item:** [[COB-583]] APP - Feat – Mostrar repositorio de billeteras en nueva pestaña
- **has action item:** [[COB-599]] API - Refactor - Agregar filtrado por nombre, clientId y userIdLo

## Descripcion

Exponer un endpoint paginado que liste billeteras de clientes mostrando **solo el saldo relativo a Libre Opción**, tal como lo ve el cliente en su billetera en PESOS ARGENTINOS.

## Objetivo

Crear un repositorio/endpoint de consulta que consolide información de billeteras y devuelva únicamente los campos requeridos:

- `date` (fecha de corte/última actualización de saldo)


- `clientId`(es el id del cliente en capa 1 `[NewBytes_DBF].[dbo].[clientes]`)


- `clientName` (El nbombre del cliente en capa 1 `[NewBytes_DBF].[dbo].[clientes]`)


- `loUserId` (userId de Libre Opción `[LO].[dbo].[usuarios]`)


- `loUsername` (username de Libre Opción `[LO].[dbo].[usuarios]`)


- `cuit` (este es el cuit o documento en capa 1 `[NewBytes_DBF].[dbo].[clientes]`)


- `availableAmount` (monto disponible relativo a Libre Opción)


- `currency` (indica si son pesos o dolares)



## Endpoint

```
GET {API_URL}/v1/wallets?currentPage=1&itemsPerPage=15
```

### Query params

- `currentPage` (int, default: 1, min: 1)


- `itemsPerPage` (int, default: 15, min: 1, max: 100)



### Respuesta (200)

```
{
  "response": [
    {
      "date": "2025-10-02T12:00:00Z",
      "clientId": 93365,
      "clientName": "Matias",
      "loUserId": 120345,
      "loUsername": "matias.g",
      "cuit": "20-44372018-3",
      "availableAmount": 0.0
    },
    {
      "date": "2025-10-02T12:00:00Z",
      "clientId": 93364,
      "clientName": "Simes",
      "loUserId": 120346,
      "loUsername": "simes.t",
      "cuit": "27-45484685-1",
      "availableAmount": 0.0
    },
    {
      "date": "2025-10-02T12:00:00Z",
      "clientId": 93363,
      "clientName": "Agustín Ortega",
      "loUserId": 120347,
      "loUsername": "aortega",
      "cuit": "20-42083003-9",
      "availableAmount": 0.000008
    }
  ],
  "pagination": {
    "total": 88838,
    "current": 1,
    "pageSize": 15
  }
}

```

### Errores

- `400 Bad Request`: parámetros inválidos (`currentPage`, `itemsPerPage`)


- `401 Unauthorized`: token inválido/ausente


- `500 Internal Server Error`: error inesperado


- `503 Service Unavailable`: dependencia de billeteras caída/timeout



#### **Citeriores de acpetacion:**

- El endpoint debe devolver únicamente los campos:

- `date`


- `clientId`


- `clientName`


- `loUserId`


- `loUsername`


- `cuit`


- `availableAmount`




- El resultado debe estar paginado con `total`, `current` y `pageSize`.


- El campo `availableAmount` debe mostrar **solo el saldo relativo a Libre Opción**.


- Si el cliente no tiene usuario en Libre Opción → `loUserId` y `loUsername` = `null`, y `availableAmount = 0.0` no aparece en la lista.


- Si se envían parámetros inválidos (`itemsPerPage=0` o `currentPage=0`) → devolver `400 Bad Request`.


- Si no hay token válido → devolver `401 Unauthorized`.


- Si el token no tiene permisos suficientes → devolver `403 Forbidden`.


- El campo `date` debe mostrar la última fecha/hora de actualización del saldo (en UTC).
