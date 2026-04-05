---
jira_key: "NBWEB-127"
aliases: ["NBWEB-127"]
summary: "APP - Formulario de recuperacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-04-21 10:34"
updated: "2022-06-26 21:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-127"
---

# NBWEB-127: APP - Formulario de recuperacion

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
| Jira | [NBWEB-127](https://bluinc.atlassian.net/browse/NBWEB-127) |

## Relaciones

- **Padre:** [[NBWEB-126]] APP - Recuperar contraseña
- **is blocked by:** [[NBWEB-124]] API - Pedir recuperacion

## Descripcion

Se trata  de un formulario para recuperar contraseña donde se debe poder ingresar un correo electrónico que al submitear, ejecuta el recurso descrito en [link](https://lioteam.atlassian.net/browse/NBWEB-124) 

El mismo puede estar en una ruta

```
{{APP_URL}}/passwordRecovery/
```

 o puede encontrase en un modal, según el criterio de usabilidad que se crea mas adecuado

Recursos API necesarios

```
PUT {{API_URL}}/v1/auth/passwordRecovery
```

**Payload:**

```
{email: "correo@ejemplo.com"}
```
