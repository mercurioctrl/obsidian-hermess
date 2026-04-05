---
jira_key: "COB-581"
aliases: ["COB-581"]
summary: "Repositorio y Gestión de Billeteras Libre Opción"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Catriel Mercurio"
created: "2025-10-02 09:57"
updated: "2025-10-14 08:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-581"
---

# COB-581: Repositorio y Gestión de Billeteras Libre Opción

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-02 09:57 |
| Actualizado | 2025-10-14 08:32 |
| Etiquetas | ninguna |
| Jira | [COB-581](https://bluinc.atlassian.net/browse/COB-581) |

## Relaciones

- **Padre:** [[COB-20 - Cuentas Corrientes|COB-20]] Cuentas Corrientes
- **Subtarea:** [[COB-582 - API - Feat - Crear repositorio de billeteras de libre opción, mostrando solo el|COB-582]] API - Feat - Crear repositorio de billeteras de libre opción, mostrando solo el saldo relativo a libre opción tal cual lo muestra la billetera para el cliente
- **Subtarea:** [[COB-583 - APP - Feat – Mostrar repositorio de billeteras en nueva pestaña|COB-583]] APP - Feat – Mostrar repositorio de billeteras en nueva pestaña
- **Subtarea:** [[COB-585 - API - Feat - Repositorio para ver lo detalles de una billetera de libre opción|COB-585]] API - Feat - Repositorio para ver lo detalles de una billetera de libre opción determinada (transactions)
- **Subtarea:** [[COB-586 - APP - Feat - Ver transacciones de billetera por usuario LO|COB-586]] APP - Feat - Ver transacciones de billetera por usuario LO
- **Subtarea:** [[COB-588 - API - Refactor - Agregar filtro de balance para saber si la cuenta tiene saldo|COB-588]] API - Refactor - Agregar filtro de balance para saber si la cuenta tiene saldo positivo, negativo o neutro (solo wallet, no cc)
- **Subtarea:** [[COB-589 - APP - Refactor - Agregar filtro de balance para saber si la cuenta tiene saldo|COB-589]] APP - Refactor - Agregar filtro de balance para saber si la cuenta tiene saldo positivo, negativo o neutro (solo wallet, no cc)
- **Subtarea:** [[COB-590 - API - Refactor - Mostrar en el detalle de la wallet el numero de pedido y su|COB-590]] API - Refactor - Mostrar en el detalle de la wallet el numero de pedido y su enlace para rastrearlo en la aplicacion de pedidos
- **Subtarea:** [[COB-591 - APP - Refactor - Mostrar en el detalle de la wallet el numero de pedido y su|COB-591]] APP - Refactor - Mostrar en el detalle de la wallet el numero de pedido y su enlace para rastrearlo en la aplicacion de pedidos
- **Subtarea:** [[COB-599 - API - Refactor - Agregar filtrado por nombre, clientId y userIdLo|COB-599]] API - Refactor - Agregar filtrado por nombre, clientId y userIdLo
- **Subtarea:** [[COB-600 - APP - Refactor - Agregar filtrado por nombre, clientId y userIdLo|COB-600]] APP - Refactor - Agregar filtrado por nombre, clientId y userIdLo

## Descripcion

### Resumen

Se implementará un nuevo **repositorio de billeteras** para consultar, mostrar y gestionar el saldo disponible relativo a Libre Opción.
El alcance incluye backend, frontend y futuras funcionalidades de detalle y visualización global.

### Objetivos

- Centralizar la información de billeteras y saldos de clientes.


- Exponer un endpoint paginado y seguro para consumo interno.


- Mostrar en el panel de Cobros una pestaña **Billeteras** junto a Clientes.


- Ampliar la funcionalidad con **detalle de movimientos, acciones sobre wallets** y un **dashboard del ecosistema**.



### Historias incluidas

- **Backend**

- Endpoint `GET /v1/wallets` con paginación y filtrado.


- Campos: `date`, `clientId`, `clientName`, `loUserId`, `loUsername`, `cuit`, `availableAmount`.


- Manejo de errores (`400, 401, 403, 500, 503`).




- **Frontend**

- Nueva pestaña **Billeteras** en módulo Cobros.


- Tabla paginada con saldos en ARS, resaltando en verde >0 y rojo =0.


- Manejo de errores con mensajes claros.




- **Pendientes / Próximas historias**

- Acceso al **detalle de movimientos** y operaciones por wallet.


- Acciones sobre billeteras (ej. transferencias internas, ajustes).


- **Dashboard global** con métricas e indicadores del ecosistema de billeteras.





### Criterios de aceptación del Epic

- Endpoint consolidado y paginado funcionando.


- Interfaz con pestaña **Billeteras** disponible en Cobros.


- Información consistente y filtrada (solo clientes con usuario LO).


- Futuras historias permitirán acceder a detalle, acciones y visualización global.
