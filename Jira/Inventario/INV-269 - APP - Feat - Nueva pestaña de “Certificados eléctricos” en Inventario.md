---
jira_key: "INV-269"
aliases: ["INV-269"]
summary: "APP - Feat - Nueva pestaña de “Certificados eléctricos” en Inventario"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-01 09:10"
updated: "2025-12-05 06:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-269"
---

# INV-269: APP - Feat - Nueva pestaña de “Certificados eléctricos” en Inventario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-01 09:10 |
| Actualizado | 2025-12-05 06:00 |
| Etiquetas | ninguna |
| Jira | [INV-269](https://bluinc.atlassian.net/browse/INV-269) |

## Relaciones

- **Padre:** [[INV-260 - Certificados eléctricos por Qr|INV-260]] Certificados eléctricos por Qr
- **action item from:** [[INV-268 - API - Feat – Listar certificados eléctricos y sus ítems asociados|INV-268]] API - Feat – Listar certificados eléctricos y sus ítems asociados

## Descripcion

En el backend se exponen recursos de solo lectura para:

- Listar los certificados eléctricos creados.


```
GET {API_URL}/electricalCertificate
```


- Listar los ítems asociados a un certificado.


```
GET {API_URL}/electricalCertificate/{id}/items
```



Desde el módulo de **Inventario** del front necesitamos una nueva pestaña que permita a los usuarios **visualizar y navegar** estos certificados ya creados y los ítems que tienen asociados.

---

### Objetivo

Agregar una **nueva pestaña en el módulo de Inventario** llamada **“Certificados eléctricos”**, que permita:

- Ver un **listado paginado** de certificados eléctricos.


- Ver el **detalle de ítems asociados a un certificado** seleccionado.



*(Por ahora, sólo lectura. No se crean ni editan certificados desde el front en esta historia.)*

---

### Alcance funcional del Front

#### 1) Nueva pestaña en Inventario

- Agregar una pestaña más en el módulo de Inventario, junto a las pestañas existentes.


- Nombre sugerido: **“Certificados eléctricos”**.


- Al seleccionar esta pestaña, se muestra una vista de listado de certificados.



#### 2) Listado de certificados eléctricos

- La pestaña mostrará una **tabla** basada en el endpoint:

```
GET {API_URL}/electricalCertificate?currentPage=1&itemsPerPage=300
```


- Campos a mostrar en la tabla (mínimo):

- **ID** (id)


- **Nombre** (name)


- **Fecha de creación** (created_at, formateado legible)


- **PDF**:

- Si `pdf_path` tiene valor, mostrar un **icono/enlace** que abra el PDF en una nueva pestaña.


- Si `pdf_path` es `null`, mostrar un estado tipo “Sin archivo” o ícono deshabilitado.







#### 3) Detalle de ítems asociados a un certificado

- Al hacer clic en un certificado de la tabla (por ejemplo, en la fila o mediante un botón “Ver ítems”):

- Abrir un **panel lateral**, modal o sección debajo de la tabla con el detalle de ítems.


- Consumir el endpoint:

```
GET {API_URL}/electricalCertificate/{id}/items
```




- Mostrar:

- **ID del certificado** (certificateId).


- Una tabla de **ítems asociados**:

- **ID de ítem** (itemId).


- **Fecha de vinculación** (linked_at → formatear).


- (Opcional si ya existe en el sistema) link para abrir el detalle del ítem en Inventario, usando itemId.






- Comportamiento según respuesta:

- Si el certificado existe pero **no tiene ítems**:

- Mostrar `items: []` como tabla vacía, con mensaje tipo “Este certificado no tiene ítems asociados”.




- Si el backend responde **404 – Certificate not found**:

- Mostrar mensaje de error contextual (“El certificado no existe o fue eliminado”) y cerrar/limpiar el panel de detalle.







---

### Criterios de aceptación

- **Nueva pestaña visible**

- ✅ En el módulo de Inventario aparece una pestaña llamada **“Certificados eléctricos”**.




- **Listado de certificados**

- ✅ Al abrir la pestaña, el front llama a `GET /electricalCertificate` usando `page` y `limit` por defecto.


- ✅ Se muestra una tabla con `id`, `name`, `created_at` y el estado/enlace del `pdf_path`.


- ✅ Si `pdf_path` tiene URL válida, el usuario puede abrir el PDF en una nueva pestaña.


- ✅ La paginación funciona: cambiar de página y de límite de registros actualiza la tabla y la URL de la API.




- **Detalle de ítems de un certificado**

- ✅ Al seleccionar un certificado, el front llama a `GET /electricalCertificate/{id}/items`.


- ✅ Si la respuesta es exitosa y tiene ítems, se muestra la lista con `itemId` y `linked_at`.


- ✅ Si el certificado existe pero viene `items: []`, se muestra mensaje de “sin ítems asociados”.


- ✅ Si el backend responde 404, se muestra un mensaje claro y no se rompe la vista.




- **Manejo de errores y estados**

- ✅ Durante las llamadas a los endpoints se muestra estado de “cargando”.


- ✅ Ante errores de red o del servidor, se muestra un mensaje genérico de error y opción de reintentar.


- ✅ No se exponen datos adicionales diferentes a los entregados por la API (se respeta `id`, `name`, `pdf_path`, `created_at`, `items.itemId`, `items.linked_at`).




- **Consistencia**

- ✅ El estilo visual (tablas, textos, botones) es consistente con el resto del módulo de Inventario.


- ✅ Los nombres y estructuras de los datos mostrados coinciden con los responses de los endpoints descritos.
