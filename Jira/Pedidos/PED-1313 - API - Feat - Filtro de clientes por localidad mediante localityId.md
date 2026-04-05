---
jira_key: "PED-1313"
aliases: ["PED-1313"]
summary: "API - Feat - Filtro de clientes por localidad mediante localityId"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-02-20 07:49"
updated: "2026-02-25 10:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1313"
---

# PED-1313: API - Feat - Filtro de clientes por localidad mediante localityId

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-20 07:49 |
| Actualizado | 2026-02-25 10:31 |
| Etiquetas | ninguna |
| Jira | [PED-1313](https://bluinc.atlassian.net/browse/PED-1313) |

## Relaciones

- **Padre:** [[PED-1312 - Filtrar clientes por localidad|PED-1312]] Filtrar clientes por localidad

## Descripcion

Se debe actualizar el repositorio y el recurso de clientes para aceptar el nuevo parámetro opcional `localityId`, permitiendo filtrar resultados por localidad.

#### **Endpoint**

```
GET {API_URL}/v1/clients?localityId={localityId}
```

#### **Requerimiento funcional**

- Si `localityId` está presente, el backend debe filtrar clientes por esa localidad.


- Si `localityId` no está presente, el comportamiento actual no debe cambiar.


- El filtro debe ser compatible con filtros existentes (si los hubiera).



#### **Cambios esperados**

- Agregar `localityId` al contrato del endpoint `GET /v1/clients`


- Incorporar `localityId` en el repositorio/query de clientes


- Validar que `localityId` sea numérico/ válido



### **Criterios de aceptación**

- **AC1:** Dado un `localityId` válido, el endpoint devuelve únicamente clientes de esa localidad.


- **AC2:** Si no se envía `localityId`, el endpoint mantiene el comportamiento actual.


- **AC3:** Si `localityId` es inválido, el endpoint responde con error de validación (según estándar actual de API).


- **AC4:** El cambio no rompe consumidores existentes del endpoint.
