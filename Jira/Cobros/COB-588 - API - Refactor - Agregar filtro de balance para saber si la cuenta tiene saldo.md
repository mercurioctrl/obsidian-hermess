---
jira_key: "COB-588"
aliases: ["COB-588"]
summary: "API - Refactor - Agregar filtro de balance para saber si la cuenta tiene saldo positivo, negativo o neutro (solo wallet, no cc)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-11-26 08:58"
updated: "2025-12-08 14:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-588"
---

# COB-588: API - Refactor - Agregar filtro de balance para saber si la cuenta tiene saldo positivo, negativo o neutro (solo wallet, no cc)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-26 08:58 |
| Actualizado | 2025-12-08 14:14 |
| Etiquetas | ninguna |
| Jira | [COB-588](https://bluinc.atlassian.net/browse/COB-588) |

## Relaciones

- **Padre:** [[COB-581]] Repositorio y Gestión de Billeteras Libre Opción
- **has action item:** [[COB-589]] APP - Refactor - Agregar filtro de balance para saber si la cuenta tiene saldo positivo, negativo o neutro (solo wallet, no cc)

## Descripcion

Parecido a como realizamos en las cuentas corrientes comunes, agregaremos el filtro para las wallet (solo saldo wallet)

```
GET {API_URL}/v1/wallets?balanceState={credit|debt|none|null}
```
