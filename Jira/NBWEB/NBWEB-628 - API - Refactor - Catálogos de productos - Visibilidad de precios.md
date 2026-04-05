---
jira_key: "NBWEB-628"
aliases: ["NBWEB-628"]
summary: "API - Refactor - Catálogos de productos - Visibilidad de precios"
status: "Tareas por hacer"
type: "Subtarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2024-01-31 00:58"
updated: "2024-01-31 01:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-628"
---

# NBWEB-628: API - Refactor - Catálogos de productos - Visibilidad de precios

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-31 00:58 |
| Actualizado | 2024-01-31 01:20 |
| Etiquetas | ninguna |
| Jira | [NBWEB-628](https://bluinc.atlassian.net/browse/NBWEB-628) |

## Relaciones

- **Padre:** [[NBWEB-4]] API - Catalogos de productos

## Descripcion

Hemos recibido comentarios frecuentes de clientes que reportan el no poder ver los precios de los productos. Esta situación ocurre cuando los usuarios aún no han iniciado sesión en sus cuentas. Es importante destacar que, aunque los productos son visibles sin iniciar sesión, los precios no son accesibles hasta que los usuarios han iniciado sesión en sus cuentas. 
Es por esta razón que surge la necesidad de buscar una forma de mejorar la experiencia de los usuarios y disminuir estos reportes que son frecuentes.

Aquí comento algunas opciones:

- **Actualización de la Documentación:**

- Actualizar de manera clara y detallada la documentación del sitio, especificando que la visualización completa de precios requiere la iniciación de sesión. Esto proporcionará una guía clara para los usuarios y reducirá la confusión.




- **Requerir Inicio de Sesión para Precios Completos:**

- Implementar una restricción que exija a los usuarios iniciar sesión para acceder a la información completa de precios. Esta medida garantiza que solo los usuarios autenticados tengan acceso total a los detalles de los productos.




- **Identificación de Consultas Directas a la API:**

- Establecer un sistema para identificar cuando las consultas se realizan directamente a la API, sin pasar por el sitio web. Esto permitirá detectar posibles problemas y tomar medidas correctivas.




- **Mensajes de Error para Usuarios No Autenticados:**

- Configurar mensajes de error informativos que se muestren cuando usuarios no autenticados intenten consultar productos y los precios no estén visibles. Estos mensajes explicarán la necesidad de iniciar sesión para acceder a esta información.
