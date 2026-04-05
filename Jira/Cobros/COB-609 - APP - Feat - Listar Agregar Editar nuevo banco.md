---
jira_key: "COB-609"
aliases: ["COB-609"]
summary: "APP - Feat - Listar  Agregar / Editar nuevo banco"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-02-04 07:11"
updated: "2026-02-13 10:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-609"
---

# COB-609: APP - Feat - Listar  Agregar / Editar nuevo banco

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-04 07:11 |
| Actualizado | 2026-02-13 10:51 |
| Etiquetas | ninguna |
| Jira | [COB-609](https://bluinc.atlassian.net/browse/COB-609) |

## Relaciones

- **Padre:** [[COB-9 - API - Feat - Listar bancos|COB-9]] API - Feat - Listar bancos
- **action item from:** [[COB-608 - API - Feat - Listar Agregar Editar nuevo banco|COB-608]] API - Feat - Listar / Agregar / Editar nuevo banco 
- **action item from:** [[COB-612 - API - Feat - Agregar recurso para crear banco con cuenta bancaria asociada|COB-612]] API - Feat - Agregar recurso para crear banco con cuenta bancaria asociada automáticamente   

## Descripcion

Ya que ahora tenemos tanto los movimientos de los bancos, como el repositorio de los bancos en si, es necesario crear un pestaña con doble sección como se hace en el caso de “clientes”.

En la segunda están “Movimientos de bancos” (el actual [https://caja.saftel.com/banks](https://caja.saftel.com/banks?)).

En la primera, esta nueva sección “ Cuentas Bancarias” para **listar, crear y editar cuentas bancarias** consumiendo el CRUD existente.

---

## Scope

Pantalla simple de administración que consume:

| Método | Endpoint |
| --- | --- |
| GET | `/bank-accounts` |
| POST | `/bank-accounts` |
| PUT | `/bank-accounts/{accountId}` |

Sin delete.

---

## Pantalla: Listado de cuentas bancarias

Tabla con columnas:

| Columna |
| --- |
| ID |
| Descripción |
| Banco |
| Empresa |
| Acciones (Editar) |

Orden inicial: `accountId DESC`.

Estado vacío: mensaje + botón **Nueva cuenta bancaria**.

---

## Filtros

La pantalla debe permitir filtrar usando query params del endpoint:

| Filtro | Query param |
| --- | --- |
| Empresa | `companyCode` |
| Banco (texto) | `bankName` |
| Banco (id) | `bankId` |

Ejemplo de llamada:

```
GET /bank-accounts?bankName=Galicia&companyCode=4&bankId=3
```

---

## Crear cuenta

Botón **Nueva cuenta bancaria** → abre modal.

Campos:

| Campo | Req |
| --- | --- |
| Banco (bankId) | si |
| Descripción | si |
| Empresa (companyCode) | opcional |

Submit → `POST /bank-accounts`

### Success

- Toast: *Cuenta bancaria creada exitosamente*


- Cierra modal


- Refresca listado



### Errores a mostrar

- 422 banco inválido


- 422 empresa inválida



---

## Editar cuenta

Botón **Editar** en cada fila → abre modal precargado.

Campos editables:

- description


- bankId


- companyCode



Submit → `PUT /bank-accounts/{accountId}`

### Success

- Toast: *Cuenta bancaria actualizada exitosamente*


- Refrescar listado



### Error

- 404 → mostrar mensaje y refrescar listado



---

## Acceptance Criteria

- Existe pantalla accesible desde cobros.


- Se pueden aplicar filtros y refrescar listado.


- Se pueden crear cuentas.


- Se pueden editar cuentas.


- Manejo de loading + errores estándar del backoffice.
