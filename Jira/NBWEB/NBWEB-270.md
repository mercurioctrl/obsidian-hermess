---
jira_key: "NBWEB-270"
summary: "API - Feat - Enviar mensaje de contacto por correo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-23 10:39"
updated: "2022-06-26 21:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-270"
---

# NBWEB-270: API - Feat - Enviar mensaje de contacto por correo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-23 10:39 |
| Actualizado | 2022-06-26 21:10 |
| Etiquetas | ninguna |
| Jira | [NBWEB-270](https://bluinc.atlassian.net/browse/NBWEB-270) |

## Descripción

```
POST {{API_URL}}/contacto/process
```



```
{
  
  "user":  ,
  "phone":  ,
  "mail":  ,
  "companyAndPosition": ,
  "contactSchedule": ,
  "site" : sitio,
  "email": email,
  "body": contenido del mail
  
}
```
