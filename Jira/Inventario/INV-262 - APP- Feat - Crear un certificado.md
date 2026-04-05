---
jira_key: "INV-262"
aliases: ["INV-262"]
summary: "APP- Feat - Crear un certificado"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-01 08:01"
updated: "2025-12-05 06:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-262"
---

# INV-262: APP- Feat - Crear un certificado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-01 08:01 |
| Actualizado | 2025-12-05 06:00 |
| Etiquetas | ninguna |
| Jira | [INV-262](https://bluinc.atlassian.net/browse/INV-262) |

## Relaciones

- **Padre:** [[INV-260]] Certificados eléctricos por Qr
- **action item from:** [[INV-261]] API - Feat - Crear un certificado

## Descripcion

Se agregará en la sección **Inventario → Certificados** un **botón accionable “Nuevo certificado”** que permita crear un certificado eléctrico interno.

Al presionarlo, se abrirá un **modal/formulario simple** con un único campo obligatorio:

- **Nombre del certificado** (input texto)



Al confirmar:

- Se enviará el request a 

```
POST {API_URL}/electricalCertificate
```


- Si la creación es exitosa:

- Se mostrará confirmación visual.


- El certificado quedará visible inmediatamente en el listado.




- Si ocurre un error de validación:

- Se mostrará el mensaje retornado por la API 





---

### Criterios de aceptación

✅ Existe el botón **“Nuevo certificado”** visible en la vista de certificados.
✅ El formulario valida que el nombre esté completo.
✅ Se consume correctamente el endpoint de alta.
✅ Se notifican errores devueltos por la API.
✅ El certificado creado se refleja en el listado sin recargar la vista.
