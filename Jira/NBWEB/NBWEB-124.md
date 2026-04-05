---
jira_key: "NBWEB-124"
summary: "API - Pedir recuperacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-21 09:31"
updated: "2022-06-26 21:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-124"
---

# NBWEB-124: API - Pedir recuperacion

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
| Jira | [NBWEB-124](https://bluinc.atlassian.net/browse/NBWEB-124) |

## Descripción

```
PUT {{API_URL}}/v1/auth/passwordRecovery
```

**Payload:**

```
{email: "correo@ejemplo.com"}
```



Este recurso genera un token que expira en 20 minutos y que se envía por correo junto al mensaje

Hola, Tim Alegria:

Hemos recibido una solicitud para restablecer la contraseña de su cuenta. Haga clic en el botón que hay más abajo para cambiarla.

El botón de restablecimiento de la contraseña caducará a las {hora exacta}

[CAMBIAR LA CONTRASEÑA] ← esta boton se agrega después cuando maquetemos bien esto.

La solicitud se ha enviado desde un dispositivo Linux con el navegador Chrome. Si no solicitó restablecer la contraseña, ignore este e-mail o contacte con nuestro equipo de asistencia si tiene alguna duda.

Si el botón no funciona, copie y pegue la siguiente dirección URL directamente en su navegador web.

[enlace en texto plano]

El enlace en texto plano, estará compuesto de un recurso (que es esta parametrizado en .env como PASSWORD_RECOVERY_ENDPOINT) y un token.

**Ejemplo:**

http://www.nb.com.ar/passwordRecovery/
