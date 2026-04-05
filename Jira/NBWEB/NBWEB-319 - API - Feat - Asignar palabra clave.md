---
jira_key: "NBWEB-319"
aliases: ["NBWEB-319"]
summary: "API - Feat - Asignar palabra clave"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-29 14:13"
updated: "2022-07-11 15:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-319"
---

# NBWEB-319: API - Feat - Asignar palabra clave

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-29 14:13 |
| Actualizado | 2022-07-11 15:12 |
| Etiquetas | ninguna |
| Jira | [NBWEB-319](https://bluinc.atlassian.net/browse/NBWEB-319) |

## Relaciones

- **Padre:** [[NBWEB-308 - API - Enviar correo de compra|NBWEB-308]] API - Enviar correo de compra

## Descripcion

Utilizando 

```
{{API_URL}}/auth/login
```

y

```
{{API_MS_ENVIOS}}/shipping/getPrivateKey
```

Se debe obtener un palabra clave aleatoria



```
email: testing@nb.com.ar

password: password
```

*estos datos deben estar en el .env
