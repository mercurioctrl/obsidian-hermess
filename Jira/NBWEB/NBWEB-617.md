---
jira_key: "NBWEB-617"
summary: "APP - Feat - Mi cuenta - Credenciales"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-01-22 09:22"
updated: "2024-01-26 05:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-617"
---

# NBWEB-617: APP - Feat - Mi cuenta - Credenciales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-22 09:22 |
| Actualizado | 2024-01-26 05:29 |
| Etiquetas | ninguna |
| Jira | [NBWEB-617](https://bluinc.atlassian.net/browse/NBWEB-617) |

## Descripción

Crearemos una nueva secccion dentro de Mi cuenta, en ella usaremos el recurso

```
GET {{API_URL}}/v1/miCuenta/readToken
```

Para mostrar un input con la herramienta “copiar” donde se visualiza el token.

Y agregaremos un “accionable” de regenerar usando el recurso

```
PATCH {API_URL}/v1/miCuenta/hardToken
```



Adicionalmente distribuiremos en esta seccion un texto similar a este de la forma mas clara posible

```
Para poder a utilizar algunos recursos es necesario que puedas desarrollar los procesos de Autenticación.
De esta manera, podrás trabajar con los recursos privados del usuario cuando tengas un "hard token" sin necesidad de hacer login.
Tambien puede regenerarlo cuando sea necesario y asi evitar que todas tus aplicaciones vionculadas a ese token lo sigan utilizando.
Tene en cuenta que al regenerarlo tus aplicaciones quedaran sin conexion hasta que vuelvas a vincularlas con el nuevo token.
```

Adicionalmente mostraremos tambien la fecha de generacion en base al refactor realizado en [link](https://lioteam.atlassian.net/browse/NBWEB-618)
