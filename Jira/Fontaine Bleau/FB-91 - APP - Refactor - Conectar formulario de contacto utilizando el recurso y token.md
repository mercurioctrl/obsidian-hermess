---
jira_key: "FB-91"
aliases: ["FB-91"]
summary: "APP - Refactor - Conectar formulario de contacto utilizando el recurso y token de cliente"
status: "Listo"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-11-17 07:52"
updated: "2025-12-05 05:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/FB-91"
---

# FB-91: APP - Refactor - Conectar formulario de contacto utilizando el recurso y token de cliente

| Campo | Valor |
|-------|-------|
| Estado | Listo (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-17 07:52 |
| Actualizado | 2025-12-05 05:30 |
| Etiquetas | ninguna |
| Jira | [FB-91](https://bluinc.atlassian.net/browse/FB-91) |

## Relaciones

- **action item from:** [[BLUWEB-207 - API - Feat - Recurso para formularios de contacto para landings de clientes|BLUWEB-207]] API - Feat - Recurso para formularios de contacto para landings de clientes (partner contact forms)

## Descripcion

[adjunto]


El objetivo es conectar el formulario de contacto de cada cliente con el sistema centralizado de envío de mensajes definido en **[[[BLUWEB-207]]](https://bluinc.atlassian.net/browse/BLUWEB-207)**[.](https://bluinc.atlassian.net/browse/BLUWEB-207)
Para ello, cada cliente contará con una **apiKey/token** propio, que debe estar cargado en el archivo `.env` de su sitio para permitir una rotación o reemplazo sencillo sin afectar el código.

### **Implementación**

El frontend deberá invocar el recurso:

```
POST {API_URL}/partner/contact-forms/submit
```

#### **Payload esperado**

```
{
  "siteOrigin": "https://landing-cliente.com",
  "formIdentifier": "contacto-principal",
  "senderName": "Juan Pérez",
  "senderEmail": "juan@example.com",
  "senderPhone": "+54 11 1234-5678",
  "subject": "Consulta sobre producto",
  "message": "Hola, quería más información sobre el producto X.",
  "extraData": {
    "utm_source": "google-ads",
    "utm_campaign": "campania-abril"
  }
}

```

La petición debe incluir la **apiKey del cliente**, que se utilizará para autenticar la solicitud y asociar correctamente cada envío a su correspondiente partner dentro del sistema.

### **Criterios de aceptación**

- El formulario se envía correctamente al endpoint especificado.


- La apiKey se toma desde variables de entorno y nunca queda hardcodeada.


- El backend recibe, valida y registra el origen (`siteOrigin`), el identificador del formulario y todos los datos del remitente.


- Si faltan datos obligatorios o la apiKey es inválida, el sistema debe devolver un error claro y estandarizado.


- La integración debe permitir agregar campos adicionales mediante `extraData` sin requerir cambios en el backend.
