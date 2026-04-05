---
jira_key: "ADATA-357"
summary: "API - Feat - Modelo de datos (Usuarios, Clientes, Compras, Aceleradores)"
status: "Listo"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-02-19 11:17"
updated: "2026-02-23 12:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ADATA-357"
---

# ADATA-357: API - Feat - Modelo de datos (Usuarios, Clientes, Compras, Aceleradores)

| Campo | Valor |
|-------|-------|
| Estado | Listo (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-19 11:17 |
| Actualizado | 2026-02-23 12:40 |
| Etiquetas | ninguna |
| Jira | [ADATA-357](https://bluinc.atlassian.net/browse/ADATA-357) |

## Descripción

Crear tablas y relaciones para soportar la lógica de XPG.

#### Tablas requeridas

**usuarios**

- id (auto)


- correo (unique)


- clave (hash)


- nombre


- telefono (opcional)


- createdAt, updatedAt



**clientes**

- id (auto)


- nombreParaMostrar


- cuit (ideal unique)


- nombre (razón social opcional)


- userId (FK [usuarios.id](http://usuarios.id))


- createdAt, updatedAt



**compras**

- id (auto)


- clientId (FK [clientes.id](http://clientes.id))


- sku (opcional)


- nombreProducto (requerido)


- cantidad (requerido >0)


- precio (opcional)


- montoTotal (requerido >0)


- facturaCompra (opcional)


- fechaCompra (opcional)


- fechaCarga (requerido)


- createdAt, updatedAt



**aceleradores**

- id (auto)


- match (string; match parcial “contiene”)


- sku (string; match exacto)


- fechaInicial


- fechaFinal


- acelerador (multiplicador: x2, x3, etc.)


- createdAt, updatedAt



*(Recomendado pero opcional MVP)* **compra_puntos** (auditoría)

- purchaseId, multiplicadorAplicado, aceleradorId, puntosBase, puntosFinales, calculatedAt



### Acceptance Criteria

AC

Criterio

AC1

Existen las 4 tablas principales con FKs correctas (clientes.userId, compras.clientId).

AC2

Validaciones mínimas de integridad: cantidad > 0, montoTotal > 0, nombreProducto requerido.

AC3

Un usuario puede tener múltiples clientes asociados por userId.

AC4

Aceleradores permiten match por `sku` exacto y/o por `match` parcial.
