---
jira_key: "PEGA-195"
aliases: ["PEGA-195"]
summary: "API - Feat -  Obtener datos del reseller autenticado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-05-23 13:25"
updated: "2025-06-10 11:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-195"
---

# PEGA-195: API - Feat -  Obtener datos del reseller autenticado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-05-23 13:25 |
| Actualizado | 2025-06-10 11:01 |
| Etiquetas | ninguna |
| Jira | [PEGA-195](https://bluinc.atlassian.net/browse/PEGA-195) |

## Relaciones

- **Padre:** [[PEGA-191 - Autenticación para resellers|PEGA-191]] Autenticación para resellers

## Descripcion

Se debe poder obtener datos del reseller autenticado.

```
GET /v1/reseller/profile
```

pasando como AUTH el token como `Bearer`{token generado en login}

response: 200 ok

```json
{
   "data": {
      "id": 4,
      "reseller_code": null,
      "name": "Katech",
      "company_name": "Katech S.A.",
      "email": "katech@Katech.com",
      "created_at": "2025-05-27T22:34:47.000000Z",
      "updated_at": "2025-05-27T22:34:47.000000Z"
   }
}
```
