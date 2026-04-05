---
jira_key: "COB-600"
aliases: ["COB-600"]
summary: "APP - Refactor - Agregar filtrado por nombre, clientId y userIdLo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-29 09:16"
updated: "2026-01-09 13:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-600"
---

# COB-600: APP - Refactor - Agregar filtrado por nombre, clientId y userIdLo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-29 09:16 |
| Actualizado | 2026-01-09 13:58 |
| Etiquetas | ninguna |
| Jira | [COB-600](https://bluinc.atlassian.net/browse/COB-600) |

## Relaciones

- **Padre:** [[COB-581 - Repositorio y Gestión de Billeteras Libre Opción|COB-581]] Repositorio y Gestión de Billeteras Libre Opción
- **action item from:** [[COB-599 - API - Refactor - Agregar filtrado por nombre, clientId y userIdLo|COB-599]] API - Refactor - Agregar filtrado por nombre, clientId y userIdLo

## Descripcion

El backend va a incorporar filtros explícitos en el recurso de billeteras para permitir enlazar cuentas desde distintas pantallas de forma directa y consistente ([link](https://bluinc.atlassian.net/browse/COB-599) ). Además, se usará `search` para filtrar por nombre (hoy el buscador general falla, pero es esperable que se corrija al actualizar el backend con esta historia).

**Objetivo**
Actualizar el frontend para:

- agregar filtros **explícitos** por `clientId` (cliente capa 1) y `userIdLo` (usuario LO), y


- utilizar el **buscador general** para buscar por **nombre** vía `search`.



---

## Alcance

### Endpoint a consumir

```
GET {API_URL}/v1/wallets/{search}?currentPage=1&itemsPerPage=15&clientId={clientId}&userIdLo={userIdLo}
```

- `clientId`: ID de cliente capa 1 (NewBytes_DBF.dbo.clientes)


- `userIdLo`: ID de usuario LO (Lo.dbo.usuarios)


- `search`: **texto libre de búsqueda por nombre** (por ahora nombre; a futuro puede incluir otros campos)



---

## Requerimientos FE

### UI / Filtros

- Agregar **dos filtros explícitos** (inputs o select según UI existente):

- **ClientId** → envía `clientId`


- **UserIdLo** → envía `userIdLo`




- Los filtros deben poder **combinarse entre sí** y con `search`.


- Si un filtro **no está seteado**, **NO** debe enviarse en la querystring (para evitar condiciones innecesarias).



### 

---

## Criterios de aceptación

- **Filtrado por clientId:** al ingresar `clientId`, el listado se actualiza usando `&clientId=<valor>` (sin enviar el parámetro si está vacío).


- **Filtrado por userIdLo:** al ingresar `userIdLo`, el listado se actualiza usando `&userIdLo=<valor>` (sin enviar el parámetro si está vacío).


- **Combinación de filtros:** `search + clientId + userIdLo` funcionan en conjunto (se envían únicamente los que correspondan).


- **Búsqueda por nombre:** el buscador general dispara request contra `/v1/wallets/{search}` y filtra por nombre.
