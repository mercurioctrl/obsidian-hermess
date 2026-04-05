---
jira_key: "EXP-202"
aliases: ["EXP-202"]
summary: "Feat - Pestaña comprobantes"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-02-07 12:35"
updated: "2024-01-16 03:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-202"
---

# EXP-202: Feat - Pestaña comprobantes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-02-07 12:35 |
| Actualizado | 2024-01-16 03:02 |
| Etiquetas | ninguna |
| Jira | [EXP-202](https://bluinc.atlassian.net/browse/EXP-202) |

## Relaciones

- **Padre:** [[EXP-116]] Devoluciones
- **Subtarea:** [[EXP-203]] API - Feat - Pestaña comprobantes
- **Subtarea:** [[EXP-204]] APP - Feat - Pestaña comproabantes
- **Subtarea:** [[EXP-213]] API - Review - Problema al hacer una busqueda de comprobantes
- **Subtarea:** [[EXP-276]] API - Refactor - Solo mostrar resultados del ultimo año (ultimos 365 dias), en todos los casos a menos que la fecha se explicite
- **Subtarea:** [[EXP-343]] API - Research - Se debe investigar sobre la eliminación del token en AFIP SDK para ámbitos productivos o vías de acción para solucionar su dependencia
- **Subtarea:** [[EXP-344]] API - Feat - Mis comprobantes -> Facturar operacion
- **Subtarea:** [[EXP-345]] API - Refactor - Se debe adaptar el servicio de comprobantes para utilizar multiples razones sociales (Distinto Cert,key))
- **Subtarea:** [[EXP-347]] API - Refector - Implemetar servicio para exportacion wsfexv1
- **Subtarea:** [[EXP-362]] Refactor - Parece no tener el voucherId, al menos en algunos casos
- **Subtarea:** [[EXP-476]] API - Refactor - Arreglo para evitar duplicaciones por sucursal en listado de comprobantes
- **is blocked by:** [[EXP-224]] Comprobantes - Página no encontrada
- **is blocked by:** [[EXP-225]] Comprobantes - Descarga fallida
- **is blocked by:** [[EXP-232]] Comprobantes - Filtro por fecha sin resultados
- **is blocked by:** [[EXP-231]] Comprobantes - Filtro por moneda resultados no coincidentes
- **is blocked by:** [[EXP-233]] Comprobantes - Buscador de texto por número de orden
- **relates to:** [[EXP-387]] API - Comprobantes - Error al buscar por entero

## Descripcion

La idea es tener la sección completa de comprobantes para que puedan utilizar tambien en expedicion, ya que muchas veces les piden comprobantes o necesitan los créditos que acaban de hacer.

 

- La aplicación debe mostrar todos los comprobantes fiscales en el listado de forma clara y ordenada.


- Los comprobantes fiscales deben estar ordenados por fecha.


- La aplicación debe permitir la búsqueda y filtrado de comprobantes fiscales de manera efectiva y eficiente.


- Se deben poder ver descargar e imprimir los comprobantes de manera sencilla.


- La aplicación debe cumplir con los requisitos de seguridad y privacidad para garantizar la protección de los datos fiscales del usuario. Es decir que el recurso a los documentos fiscales, no debe estar abierto a internet sin un token
