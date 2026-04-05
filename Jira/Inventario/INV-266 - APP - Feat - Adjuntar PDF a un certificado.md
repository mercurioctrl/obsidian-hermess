---
jira_key: "INV-266"
aliases: ["INV-266"]
summary: "APP - Feat - Adjuntar PDF a un certificado"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-01 08:02"
updated: "2025-12-04 11:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-266"
---

# INV-266: APP - Feat - Adjuntar PDF a un certificado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-01 08:02 |
| Actualizado | 2025-12-04 11:12 |
| Etiquetas | ninguna |
| Jira | [INV-266](https://bluinc.atlassian.net/browse/INV-266) |

## Relaciones

- **Padre:** [[INV-260 - Certificados eléctricos por Qr|INV-260]] Certificados eléctricos por Qr
- **action item from:** [[INV-265 - API - Feat - Adjuntar PDF a un certificado|INV-265]] API - Feat - Adjuntar PDF a un certificado

## Descripcion

En el **listado de certificados eléctricos** se deberá agregar un **accionable por registro** para permitir **subir y asociar el archivo PDF del certificado** usando el endpoint:

```
POST /electricalCertificate/{id}/files
```

**UI / Acceso**

- El accionable puede ser:

- Opción en el **menú de botón derecho** del certificado (“Adjuntar certificado”), y/o


- Un **botón dentro del modal** del certificado.




- Al activarlo se abrirá un selector de archivo (solo **PDF**).



**Comportamiento**

- El usuario selecciona el PDF y confirma la carga.


- Se envía el archivo vía `multipart/form-data` al endpoint.


- En éxito:

- Se muestra confirmación con nombre/URL del archivo.


- Se actualiza el estado visual del certificado (ej: “PDF adjunto”).




- En error:

- Se muestra mensaje claro según respuesta del backend (404, 400, 502/500).





**Criterios de aceptación**

- ✅ Cada certificado del listado tiene un accionable para adjuntar PDF.


- ✅ El archivo se envía correctamente al endpoint de carga.


- ✅ En éxito se refleja visualmente que el certificado tiene archivo asociado.


- ✅ Se muestran errores de forma consistente si falla la operación.
