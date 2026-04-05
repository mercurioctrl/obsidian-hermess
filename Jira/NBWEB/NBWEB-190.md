---
jira_key: "NBWEB-190"
summary: "Chequear si el username exists"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2022-05-17 12:34"
updated: "2022-06-22 07:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-190"
---

# NBWEB-190: Chequear si el username exists

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2022-05-17 12:34 |
| Actualizado | 2022-06-22 07:44 |
| Etiquetas | ninguna |
| Jira | [NBWEB-190](https://bluinc.atlassian.net/browse/NBWEB-190) |

## Descripción

POST  {{API_URL}}/v1/miCuenta/usuario/checkIfUsernameExist



Request : 



```
{
username:'EzeCapo123'
}
```

Returns : 



```
Si existe : {'success':'El username ya existe en el sistema'}
Si no existe : {'success':'El username esta disponible'}
```
