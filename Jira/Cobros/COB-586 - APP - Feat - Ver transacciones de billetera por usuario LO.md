---
jira_key: "COB-586"
aliases: ["COB-586"]
summary: "APP - Feat - Ver transacciones de billetera por usuario LO"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-10-03 08:40"
updated: "2025-10-06 11:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-586"
---

# COB-586: APP - Feat - Ver transacciones de billetera por usuario LO

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-03 08:40 |
| Actualizado | 2025-10-06 11:05 |
| Etiquetas | ninguna |
| Jira | [COB-586](https://bluinc.atlassian.net/browse/COB-586) |

## Relaciones

- **Padre:** [[COB-581 - Repositorio y Gestión de Billeteras Libre Opción|COB-581]] Repositorio y Gestión de Billeteras Libre Opción
- **action item from:** [[COB-585 - API - Feat - Repositorio para ver lo detalles de una billetera de libre opción|COB-585]] API - Feat - Repositorio para ver lo detalles de una billetera de libre opción determinada (transactions)

## Descripcion

Desde la pestaña **Billeteras**, agregar un accionable **“Ver transacciones”** por fila (cliente). Al hacer clic, abrir un **panel lateral/modal** que consume 

```
GET /v4/wallets/transactions/{loUserId}
```

con paginación y orden, mostrando el historial de movimientos.

### Mostraremos un esquema que tenga esta disposición, aunque se usen los elementos del modal clásico de cuentas corrientes porque lo que queremos es que se asuma como algo diferente, mas parecido a una billetera.

[adjunto]
