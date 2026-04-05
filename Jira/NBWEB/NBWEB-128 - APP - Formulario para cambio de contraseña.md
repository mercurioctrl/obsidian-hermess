---
jira_key: "NBWEB-128"
aliases: ["NBWEB-128"]
summary: "APP - Formulario para cambio de contraseña"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-04-21 10:34"
updated: "2022-06-26 21:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-128"
---

# NBWEB-128: APP - Formulario para cambio de contraseña

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-21 10:34 |
| Actualizado | 2022-06-26 21:39 |
| Etiquetas | ninguna |
| Jira | [NBWEB-128](https://bluinc.atlassian.net/browse/NBWEB-128) |

## Relaciones

- **Padre:** [[NBWEB-126 - APP - Recuperar contraseña|NBWEB-126]] APP - Recuperar contraseña
- **is blocked by:** [[NBWEB-125 - API - Cambiar password|NBWEB-125]] API - Cambiar password

## Descripcion

Se debe crear un formulario en modal o en el contexto del sitio, en el que se ingresen dos veces un password para validar la coincidencia.

El passworde debe tener al menos 8 caracteres y poseer mayusculas y minusculas

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
