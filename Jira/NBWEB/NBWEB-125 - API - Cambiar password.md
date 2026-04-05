---
jira_key: "NBWEB-125"
aliases: ["NBWEB-125"]
summary: "API - Cambiar password"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-21 09:31"
updated: "2022-06-26 21:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-125"
---

# NBWEB-125: API - Cambiar password

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-21 09:31 |
| Actualizado | 2022-06-26 21:39 |
| Etiquetas | ninguna |
| Jira | [NBWEB-125](https://bluinc.atlassian.net/browse/NBWEB-125) |

## Relaciones

- **Padre:** [[NBWEB-121 - API - Recuperar Contraseña a través de correo electrónico|NBWEB-121]] API - Recuperar Contraseña a través de correo electrónico
- **blocks:** [[NBWEB-128 - APP - Formulario para cambio de contraseña|NBWEB-128]] APP - Formulario para cambio de contraseña

## Descripcion

```
POST {{API_URL}}/v1/auth/passwordRecovery
```

**Payload:**



```
{
token:"9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2d"
email : "correo@ejemplo.com"
password : "nuevoPassword"
}
```
