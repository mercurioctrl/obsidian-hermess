---
jira_key: "PEGA-193"
summary: "API - Feat - Registro de nuevo reseller"
status: "En curso"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-05-23 13:23"
updated: "2025-06-24 19:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-193"
---

# PEGA-193: API - Feat - Registro de nuevo reseller

| Campo | Valor |
|-------|-------|
| Estado | En curso (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-05-23 13:23 |
| Actualizado | 2025-06-24 19:05 |
| Etiquetas | ninguna |
| Jira | [PEGA-193](https://bluinc.atlassian.net/browse/PEGA-193) |

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
