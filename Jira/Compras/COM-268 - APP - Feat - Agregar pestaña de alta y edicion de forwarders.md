---
jira_key: "COM-268"
aliases: ["COM-268"]
summary: "APP - Feat - Agregar pestaña de alta y edicion de forwarders"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-08 09:39"
updated: "2026-01-22 11:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-268"
---

# COM-268: APP - Feat - Agregar pestaña de alta y edicion de forwarders

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-08 09:39 |
| Actualizado | 2026-01-22 11:00 |
| Etiquetas | ninguna |
| Jira | [COM-268](https://bluinc.atlassian.net/browse/COM-268) |

## Relaciones

- **Padre:** [[COM-265 - Forwarders|COM-265]] Forwarders
- **action item from:** [[COM-267 - API - Feat - Leer repositorio forwarders|COM-267]] API - Feat - Leer repositorio forwarders
- **action item from:** [[COM-266 - API - Feat - CrearEditarEliminar forwarder|COM-266]] API - Feat - Crear/Editar/Eliminar forwarder

## Descripcion

Agregar una nueva pestaña **Forwarders** en la sección de para poder **listar, filtrar y dar de alta forwarders**.

### Alcance

- Crear pestaña **Forwarders**


- Mostrar grilla/listado


- Agregar **filtros** (mínimos) y un **accionable** para crear



### UI / Funcionalidad

- **Filtro General**:

- `name` (texto, búsqueda parcial)


- `code` (texto, exacta o parcial según implementen)


- `id`




- **Filtro Empresa**


- **Acción**: botón **“Agregar forwarder”**

- Abre modal / drawer / pantalla de alta


- Campos del form:

- name (requerido)


- code (requerido)


- address


- phone


- email






- **Listado**: columnas sugeridas

- Code, Name, Phone, Email





### Integración API

- Listado: `GET /v1/forwarders?name=...&code=...`


- Alta: `POST /v1/forwarders`



### Criterios de aceptación

- Existe la pestaña **Forwarders**


- Los filtros actualizan el listado usando el GET


- El botón **Agregar forwarder** permite crear y al éxito:

- cierra el modal/pantalla


- refresca el listado


- muestra mensaje de confirmación




- Se muestran errores de validación del backend (ej. code duplicado / campos requeridos)
