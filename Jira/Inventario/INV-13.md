---
jira_key: "INV-13"
summary: "API - Login -  Ingreso a la cuenta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-03 17:20"
updated: "2022-06-09 11:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-13"
---

# INV-13: API - Login -  Ingreso a la cuenta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-03 17:20 |
| Actualizado | 2022-06-09 11:47 |
| Etiquetas | ninguna |
| Jira | [INV-13](https://bluinc.atlassian.net/browse/INV-13) |

## Descripción

```
POST {{API_URL}}/v1/auth/login
```

Retorna

```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTQyOTEyODEsImF1ZCI6IjhjMmQ4YzczMmZmNTg5NjJjOWVkMTdhZDBmYzM3MjMwY2FhN2EzMDUiLCJ1c2VyIjo0NywiaWF0IjoxNjU0Mjg3NjgxLCJuYmYiOjE2NTQyODc2ODEsImNtcyI6dHJ1ZX0.1JXYGR8qv8hbDF9J2-f4gnK8WdyPTkE-uMFH5Q_TpWw"
}
```
