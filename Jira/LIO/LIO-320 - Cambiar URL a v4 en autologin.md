---
jira_key: "LIO-320"
aliases: ["LIO-320"]
summary: "Cambiar URL a v4 en autologin "
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Ezequiel manzano"
created: "2025-04-11 09:49"
updated: "2025-04-14 11:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-320"
---

# LIO-320: Cambiar URL a v4 en autologin 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Ezequiel manzano |
| Creado | 2025-04-11 09:49 |
| Actualizado | 2025-04-14 11:17 |
| Etiquetas | ninguna |
| Jira | [LIO-320](https://bluinc.atlassian.net/browse/LIO-320) |

## Relaciones

- **has action item:** [[SNB-2979]] Libre Opción - Autologin desde pedidos fallido 

## Descripcion

Se migró el recurso de autologin de v3 legacy a v4. 

url v4

```
{{API_URL}}/v4/auth/autologin
```

body

```
{
    "token": "18d5f830786bbfc08ec545d992f9517e"
}
```

Se necesita cambiar el mismo cuando hacemos 

[https://libreopcion.com.ar/login?access_token_admin=6233bddb1d4b5ea4e1adb5c9888c9267](https://libreopcion.com.ar/login?access_token_admin=6233bddb1d4b5ea4e1adb5c9888c9267)
