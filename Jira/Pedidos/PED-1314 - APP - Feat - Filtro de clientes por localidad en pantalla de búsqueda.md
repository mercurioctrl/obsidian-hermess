---
jira_key: "PED-1314"
aliases: ["PED-1314"]
summary: "APP - Feat - Filtro de clientes por localidad en pantalla de búsqueda"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-02-20 07:50"
updated: "2026-02-26 17:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1314"
---

# PED-1314: APP - Feat - Filtro de clientes por localidad en pantalla de búsqueda

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-20 07:50 |
| Actualizado | 2026-02-26 17:04 |
| Etiquetas | ninguna |
| Jira | [PED-1314](https://bluinc.atlassian.net/browse/PED-1314) |

## Relaciones

- **Padre:** [[PED-1312]] Filtrar clientes por localidad

## Descripcion

Se debe incorporar en el frontend un filtro por **localidad** para la búsqueda/listado de clientes.

El frontend reutilizará el recurso ya existente para obtener localidades según provincia seleccionada:

```
GET {API_URL}/v1/places/{provinceId}
```

- Ejemplo: `{API_URL}/v1/places/4`



Una vez seleccionada la localidad, el frontend deberá enviar el filtro al recurso de clientes:

```
GET {API_URL}/v1/clients?localityId={localityId}
```

#### **Comportamiento esperado**

- Al seleccionar una provincia, se cargan sus localidades


- El usuario puede seleccionar una localidad específica


- La búsqueda/listado de clientes se filtra por `localityId`



### **Criterios de aceptación**

- **AC1:** Al seleccionar una provincia, se consultan y muestran las localidades usando `/v1/places/{provinceId}`.


- **AC2:** Al seleccionar una localidad, el frontend envía `localityId` en la consulta de clientes.


- **AC3:** Si no se selecciona localidad, el filtro por localidad no se aplica.


- **AC4:** La UI mantiene el comportamiento actual sin regresiones en filtros existentes.


- **AC5:** El usuario puede identificar claramente el filtro de localidad en la pantalla.
