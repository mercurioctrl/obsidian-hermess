---
jira_key: "NBWEB-709"
aliases: ["NBWEB-709"]
summary: "APP - Registrar usuario - Teléfono invalido"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-04-15 17:16"
updated: "2024-04-17 20:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-709"
---

# NBWEB-709: APP - Registrar usuario - Teléfono invalido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-15 17:16 |
| Actualizado | 2024-04-17 20:27 |
| Etiquetas | ninguna |
| Jira | [NBWEB-709](https://bluinc.atlassian.net/browse/NBWEB-709) |

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web
- **relates to:** [[NBWEB-675]] APP - Refactorizar los pasos de registro de cliente y agregar direccion, codigo postal y whatsapp
- **relates to:** [[NBWEB-710]] API - Registrar usuario - Fecha no guardada
- **relates to:** [[NBWEB-714]] API - Refactor - whatsapp telefono 1 y 2 que no sean obligatorios
- **relates to:** [[PED-672]] App - Quitar obligatorio los telefonos (telefono, telefono 2 y whatsapp)

## Descripcion

- Resultado obtenido: 



1. Cuando descargo la solicitud de un cliente y trato de crearlo, no puedo de avanzar debido a que los números telefónicos son inválidos. Si bien esto es cierto, como cliente intentando registrarme en el sitio, no debería ser permitido continuar si los números telefónicos no son válidos.

[adjunto]
2. No se visualiza el teléfono.

[adjunto]
- Pasos para replicar error: 



Realizar el registro de un usuario nuevo en el sitio de NB con números telefónicos inválidos.

- Datos de la prueba: 



```
    {
        "requestId": 54143,
        "username": "Gprueba_bremer2",
        "email": "bremer2@nb.com.ar",
        "emailConfirmed": false,
        "socialReason": "Bremer company sa de cv",
        "fantasyName": "Bremer comp",
        "dni": 87654321,
        "name": "Bremer",
        "cuit": "12345678",
        "telephone": "0011234567",
        "cellPhone": "0011234567",
        "secondaryEmail": "",
        "companyWebsite": "",
        "howYouKnowUs": "",
        "requestDate": "",
        "provinceId": "9",
        "taxType": 3,
        "zipCode": "2024",
        "whaPhone": "5201123456787",
        "address": "Lopez mateos",
        "dniOcuit": 4,
        "localityId": "416"
    } 
```

- Resultado esperado: 



Al descargar la solicitud del cliente en el sistema de Pedidos, pueda crearla sin necesidad de intervenir en los datos capturados por el cliente.

- Posible solución:



Validar los datos ingresados del cliente antes de registrarlo en el sitio.
