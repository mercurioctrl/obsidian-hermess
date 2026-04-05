---
jira_key: "PED-40"
aliases: ["PED-40"]
summary: "Login automático como cliente"
status: "Tareas por hacer"
type: "Historia"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Catriel Mercurio"
created: "2023-08-21 19:48"
updated: "2023-09-12 08:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-40"
---

# PED-40: Login automático como cliente

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-21 19:48 |
| Actualizado | 2023-09-12 08:24 |
| Etiquetas | ninguna |
| Jira | [PED-40](https://bluinc.atlassian.net/browse/PED-40) |

## Relaciones

- **Padre:** [[PED-15]] Clientes
- **Subtarea:** [[PED-41]] API - Feat - Crear autorizacion en la api de ordenes
- **Subtarea:** [[PED-42]] API - Feat - Login mediante autorizacion en el sitio web 
- **Subtarea:** [[PED-43]] APP - Feat - Pedir autorizacion y redirigir 
- **Subtarea:** [[PED-44]] APP - Feat - Login meidante autorizacion en el sitio web
- **Subtarea:** [[PED-1290]] APP - Refactor - Agregar al menú "clic derecho" el acceso automático al sitio de NBE
- **blocks:** [[SNB-1154]] sumar andreani/ oca

## Descripcion

Crearemos una feature que nos permita hacer login con la cuenta de un cliente en el sitio web de NB.

Esto se hace para que puedan visualizar como un cliente, para asistir mejor o bien entender que cosas ve y como el cliente. Así tambien, sirve para poder aprovechar todas las herramientas del sitio.

Primero crearemos una autorización de un solo uso[link](https://lioteam.atlassian.net/browse/PED-43)  |  [link](https://lioteam.atlassian.net/browse/PED-41) 

Y redirigiremos al recurso del sitio 

Luego la utilizaremos para ingresar el sitio y expiraremos [link](https://lioteam.atlassian.net/browse/PED-42)
