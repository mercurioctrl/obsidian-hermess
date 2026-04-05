---
jira_key: "NBWEB-676"
aliases: ["NBWEB-676"]
summary: "API - Agregar agregar direccion, codigo postal y whatsapp en el registro de un cliente y que se pueda levantar en PED"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2024-03-28 12:00"
updated: "2024-04-15 17:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-676"
---

# NBWEB-676: API - Agregar agregar direccion, codigo postal y whatsapp en el registro de un cliente y que se pueda levantar en PED

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2024-03-28 12:00 |
| Actualizado | 2024-04-15 17:42 |
| Etiquetas | ninguna |
| Jira | [NBWEB-676](https://bluinc.atlassian.net/browse/NBWEB-676) |

## Relaciones

- **Padre:** [[NBWEB-498]] Oportunidades de mejora
- **relates to:** [[NBWEB-675]] APP - Refactorizar los pasos de registro de cliente y agregar direccion, codigo postal y whatsapp
- **relates to:** [[NBWEB-706]] API - Registro de usuario - Email invalido 
- **relates to:** [[NBWEB-710]] API - Registrar usuario - Fecha no guardada

## Descripcion

```json
{
    "email": "test2803@test.com",
    "username": "test2803",
    "password": "Marbe123456",
    "showName": "test2803",
    "fiscalName": "marbe test 2803",
    "socialName": "nombre fantasi",
    "formatFiscalId": 0,
    "fiscalId": "99885588",
    "fiscalCategoryId": "1",
    "province": 1,
    "place": 20891,
    "address": "CASTRO BARROS 10 5C",// <------ nuevo
    "postalCode": "1178",// <------ nuevo
    "name": "Marbe",
    "lastName": "Moreno",
    "personId": "95999988",
    "firstPhoneNumber": "01122533038",
    "secondPhoneNumber": "",
    "whaPhone": "5491122558899",// <------ nuevo
    "howDidYouMeetUsId": "weeb",
    "webSite": null
}
```
