---
jira_key: "NBWEB-131"
aliases: ["NBWEB-131"]
summary: "Crear solicitud de alta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-22 15:11"
updated: "2022-06-26 21:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-131"
---

# NBWEB-131: Crear solicitud de alta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-22 15:11 |
| Actualizado | 2022-06-26 21:34 |
| Etiquetas | ninguna |
| Jira | [NBWEB-131](https://bluinc.atlassian.net/browse/NBWEB-131) |

## Relaciones

- **Padre:** [[NBWEB-130 - API - Registro y alta de cliente|NBWEB-130]] API - Registro y alta de cliente

## Descripcion

Este recurso genera una request a partir de un formulario

```
POST {{API_URL}}/v1/registrationRequest
```

Payload:

```json
  {
    "email": 'mail@ejemplo.com',
    "userName": 'nombreDeUsuario',
    "password": 'pass',
    "name": "Catriel",
    "lastName": "Marin",
    "fiscalName": "1236546546",
    "socialName": null,
    "formatFiscalId": 0,
    "personId": "00.000.000",
    "fiscalId": "33-46985233-3",
    "fiscalCategoryId": 1,
    "firstPhoneNumber": "03424089730",
    "secondPhoneNumber": null,
    "howDidYouMeetUsId": "Bucadores",
    "webSite": "www.-tecno.com.ar",
    "province": "17",
    "place": "H976"
  }
```

Donde cada columna corresponde a un parametro de la siguiente manera



```
usuarios_nb.UserEmail ->email
usuarios_nb.UserName ->userName
usuarios_nb.UserPass ->password
info_usuarios.nombre ->name
info_usuarios.apellido ->lastName
info_usuarios.RSocial ->fiscalName
info_usuarios.NFantasia ->socialName
info_usuarios.dniOcuit ->formatFiscalId
info_usuarios.dni ->personId
info_usuarios.cuit ->fiscalId
info_usuarios.catIva ->fiscalCategoryId
info_usuarios.telFi ->firstPhoneNumber
info_usuarios.telCel ->secondPhoneNumber
info_usuarios.comoNos ->howDidYouMeetUsId
info_usuarios.wwwEmpresa ->webSite
info_usuarios.provLeg ->province
info_usuarios.locaLeg ->town
```
