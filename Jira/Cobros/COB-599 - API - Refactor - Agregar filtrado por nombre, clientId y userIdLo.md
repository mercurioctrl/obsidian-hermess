---
jira_key: "COB-599"
aliases: ["COB-599"]
summary: "API - Refactor - Agregar filtrado por nombre, clientId y userIdLo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-12-29 09:09"
updated: "2026-01-09 13:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-599"
---

# COB-599: API - Refactor - Agregar filtrado por nombre, clientId y userIdLo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-29 09:09 |
| Actualizado | 2026-01-09 13:58 |
| Etiquetas | ninguna |
| Jira | [COB-599](https://bluinc.atlassian.net/browse/COB-599) |

## Relaciones

- **Padre:** [[COB-581]] Repositorio y Gestión de Billeteras Libre Opción
- **action item from:** [[COB-582]] API - Feat - Crear repositorio de billeteras de libre opción, mostrando solo el saldo relativo a libre opción tal cual lo muestra la billetera para el cliente
- **has action item:** [[COB-600]] APP - Refactor - Agregar filtrado por nombre, clientId y userIdLo

## Descripcion

Modificaremos el repositorio de billeteras para agregar dos filtros explícitos: `clientId` y `userIdLo`

Y agregaremos `search` para filtrar por nombre (y en el futuro tal vez otros string)

```
GET {API_URL}/v1/wallets/{search}?currentPage=1&itemsPerPage=15&clientId={clientId}&userIdLo={userIdLo}
```

De esta forma podremos usarlos para enlazar directamente cuentas desde distintos lugares haciendo que el sistema tenga mejor usabilidad y conexión entre las partes

En el caso de `clientId` se trata simplemente del ID de cliente de capa uno, el de la tabla `NewBytes_DBF.dbo.clientes`

En el caso de `userIdLo` se trata simplemente del ID de usuario, el de la tabla `Lo.dbo.usuarios`

En el caso de `search` se trata simplemente del NOMBRE, el de la tabla `Lo.dbo.usuarios` y `NewBytes_DBF.dbo.clientes`
