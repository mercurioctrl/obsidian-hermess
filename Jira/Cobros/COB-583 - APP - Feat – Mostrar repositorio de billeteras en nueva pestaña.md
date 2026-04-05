---
jira_key: "COB-583"
aliases: ["COB-583"]
summary: "APP - Feat – Mostrar repositorio de billeteras en nueva pestaña"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-10-02 10:12"
updated: "2025-10-07 11:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-583"
---

# COB-583: APP - Feat – Mostrar repositorio de billeteras en nueva pestaña

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-02 10:12 |
| Actualizado | 2025-10-07 11:29 |
| Etiquetas | ninguna |
| Jira | [COB-583](https://bluinc.atlassian.net/browse/COB-583) |

## Relaciones

- **Padre:** [[COB-581 - Repositorio y Gestión de Billeteras Libre Opción|COB-581]] Repositorio y Gestión de Billeteras Libre Opción
- **action item from:** [[COB-582 - API - Feat - Crear repositorio de billeteras de libre opción, mostrando solo el|COB-582]] API - Feat - Crear repositorio de billeteras de libre opción, mostrando solo el saldo relativo a libre opción tal cual lo muestra la billetera para el cliente

## Descripcion

Agregar una nueva pestaña en la vista de “Clientes” llamada **Billeteras**, ubicada junto a la pestaña actual de clientes, que muestre la información de saldos relativos a Libre Opción, proveniente del endpoint de backend:


```
GET {API_URL}/v1/wallets?currentPage=1&itemsPerPage=15
```

**Requerimientos**

- La pestaña **Billeteras** debe mostrarse al mismo nivel que la pestaña **Clientes** en la sección de Cobros.


- El listado debe ser **paginado** con los mismos controles (navegación, tamaño de página, búsqueda).


- Debe mostrar las siguientes columnas, en el mismo estilo de tabla actual:

- **Fecha** (`date`)


- **Cliente (ID)** (`clientId`)


- **Nombre del Cliente** (`clientName`)


- **Usuario LO (ID)** (`loUserId`)


- **Usuario LO (Username)** (`loUsername`)


- **CUIT/Documento** (`cuit`)


- **Saldo Libre Opción** (`availableAmount`, en pesos argentinos)


- Accionable Para acceder a billetera




- El campo **Saldo Libre Opción** debe resaltarse en **verde si es mayor a 0**, y en **rojo si es 0** (siguiendo el estilo de la grilla de clientes).


- El campo **Fecha** debe mostrarse en formato local legible (ej: `02/10/2025 09:00 hs`).



**Manejo de Errores en UI**

- Si el backend devuelve `400 Bad Request` → mostrar mensaje: *"Parámetros inválidos en la consulta."*


- Si devuelve `401 Unauthorized` o `403 Forbidden` → redirigir a login o mostrar alerta de sesión expirada.


- Si devuelve `500` o `503` → mostrar mensaje: *"No es posible recuperar los saldos de billeteras en este momento. Intente nuevamente más tarde."*



**Criterios de aceptación**

- La nueva pestaña **Billeteras** se muestra junto a la de **Clientes** en el módulo Cobros.


- La tabla consume el endpoint `/v1/wallets` y respeta la paginación (`currentPage`, `itemsPerPage`).


- Se listan únicamente los campos: `date`, `clientId`, `clientName`, `loUserId`, `loUsername`, `cuit`, `availableAmount`.


- El saldo se muestra solo en pesos argentinos (ARS).


- Los usuarios sin cuenta en Libre Opción **no aparecen en la lista** (ya filtrados por backend).


- Los errores del backend se manejan en la UI con mensajes claros.
