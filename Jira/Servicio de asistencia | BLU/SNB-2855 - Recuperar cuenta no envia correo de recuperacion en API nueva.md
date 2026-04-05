---
jira_key: "SNB-2855"
aliases: ["SNB-2855"]
summary: "Recuperar cuenta no envia correo de recuperacion en API nueva"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-07 12:41"
updated: "2025-03-11 11:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-2855"
---

# SNB-2855: Recuperar cuenta no envia correo de recuperacion en API nueva

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-07 12:41 |
| Actualizado | 2025-03-11 11:43 |
| Etiquetas | ninguna |
| Jira | [SNB-2855](https://bluinc.atlassian.net/browse/SNB-2855) |

## Relaciones

- **relates to:** [[LIO-258 - Migrar cambiar pw|LIO-258]] Migrar cambiar pw 

## Descripcion

Recuperar cuenta no envia correo de recuperacion en API nueva

```
curl 'https://api.gamma.libreopcion.com/auth/solicitar-cambio-clave' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.libreopcion.com' \
  -H 'Referer: https://gamma.libreopcion.com/solicitar-contrasena-nueva' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"email":"cuentatesting@gmail.com"}'
```
