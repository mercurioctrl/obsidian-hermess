---
jira_key: PEGA-193
status: En curso
assignee: Emanuel Jesus Ferreyra
assignee_email: null
reporter: Emanuel Jesus Ferreyra
priority: Medium
issuetype: Subtarea
project: PEGA
updated: "2025-06-24T19:05:52.444-0300"
created: "2025-05-23T13:23:34.147-0300"
url: "https://bluinc.atlassian.net/browse/PEGA-193"
tags: [jira, PEGA, en-curso]
---

# PEGA-193 · API - Feat - Registro de nuevo reseller

[PEGA-193 en Jira](https://bluinc.atlassian.net/browse/PEGA-193)

## Descripción

Se debe poder registrar un nuevo reseller (campos: `name`, `company_name`, `email`, `password`, `password_confirmation`)

```
POST v1/reseller/register
```

Payload:

```json
{
  "name": "Katech",
  "company_name": "Katech S.A.",
  "email": "katech@Katech.com",
  "password": "Katech1241",
  "password_confirmation": "Katech1241"
}
```



Response: 201 Created

```json
{
   "message": "Registro exitoso",
   "data": {
      "id": 4,
      "reseller_code": null,
      "name": "Katech",
      "company_name": "Katech S.A.",
      "email": "katech@Katech.com",
      "created_at": "2025-05-27T22:34:47.815000Z",
      "updated_at": "2025-05-27T22:34:47.815000Z"
   },
   "token": "102|c0Ze4TfU1HkAnHgddiHUAZ0oyKl6gsoRqyfZzvab194e583b"
}
```



Tabla necesaria para este caso de uso.

```sql
CREATE TABLE PEGA.dbo.reseller_users
(
    id            INT IDENTITY (1,1) PRIMARY KEY,
    reseller_code INT                  NULL, -- posteriormente se utilizara para asignar el codigo de reseller actual
    name          NVARCHAR(255)        NOT NULL,
    company_name  NVARCHAR(255)        NULL,
    email         NVARCHAR(255) UNIQUE NOT NULL,
    password      NVARCHAR(255)        NOT NULL,
    created_at    DATETIME DEFAULT GETDATE(),
    updated_at    DATETIME DEFAULT GETDATE()
);
```

## Comentarios (2)

### @Guillermo Avila — 2025-06-10 10:51:23

1. La fecha no coincide con la actual.
2. Recomendaría guardar la fecha de actualización únicamente cuando se realicen modificaciones, en lugar de al momento de crearla, para así poder identificarlas en el futuro.

### @Guillermo Avila — 2025-06-24 10:18:02

1. El objeto de respuesta debe tener la siguiente estructura:

```
{
  "success": true,                    // true o false
  "message": "Operación exitosa",     // Descripción opcional
  "data": {}                          // Objeto con datos devueltos o null
}
```

1. Recomendaciones anteriores

---
_Sincronizado por jira-sidecar el 2026-06-07 22:27:20 UTC._
