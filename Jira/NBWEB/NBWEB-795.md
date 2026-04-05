---
jira_key: "NBWEB-795"
summary: "EXTENSION - Refactor - En el primer login que hace la extensión, se debe registrar (de ser posible) el dominio putero para golpearlo posteriormente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-07-31 12:05"
updated: "2024-08-16 01:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-795"
---

# NBWEB-795: EXTENSION - Refactor - En el primer login que hace la extensión, se debe registrar (de ser posible) el dominio putero para golpearlo posteriormente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-31 12:05 |
| Actualizado | 2024-08-16 01:05 |
| Etiquetas | ninguna |
| Jira | [NBWEB-795](https://bluinc.atlassian.net/browse/NBWEB-795) |

## Descripción

Seria bueno que nuestro sistema registre automáticamente el dominio del cliente cuando hace login nuestra extensión de WooCommerce, para evitar tener que solicitarlo manualmente y asegurar un proceso más eficiente y preciso.

**Detalles:**

- **Registro Automático del Dominio**:

- Implementar un mecanismo que permita obtener automáticamente el dominio del cliente desde la base de datos de su WordPress al momento de la conexión.


- Este dominio debe ser guardado o actualizado en nuestro sistema durante el proceso de login de la extensión de WooCommerce.




- **Plan B - Solicitud Manual**:

- En caso de que el registro automático falle, se debe permitir que el cliente proporcione manualmente su dominio.


- Este dato manual también debe ser registrado y utilizado en nuestro sistema.
