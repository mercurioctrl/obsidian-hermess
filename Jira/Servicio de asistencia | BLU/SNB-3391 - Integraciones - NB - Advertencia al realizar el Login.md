---
jira_key: "SNB-3391"
aliases: ["SNB-3391"]
summary: "Integraciones - NB - Advertencia al realizar el Login"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Guillermo Avila"
created: "2025-09-11 14:22"
updated: "2025-09-15 16:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3391"
---

# SNB-3391: Integraciones - NB - Advertencia al realizar el Login

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Guillermo Avila |
| Creado | 2025-09-11 14:22 |
| Actualizado | 2025-09-15 16:46 |
| Etiquetas | ninguna |
| Jira | [SNB-3391](https://bluinc.atlassian.net/browse/SNB-3391) |

## Relaciones

*Sin relaciones*

## Descripcion

Por parte de integraciones nos reportan que al realizar el inicio de sesión les aparece una advertencia la cual les rompe la respuesta.

Te comparto aquí un resumen del hilo de correos.



Información del cliente:

```
Grupo Net-World Soluciones Informáticas
gruponetworld@gmail.com
```



Código de JavaScript:

```
const formdata = new FormData();
formdata.append("user", "xxxxxx@gmail.com");
formdata.append("password", "xxxxxxxxx");
formdata.append("mode", "api");

const requestOptions = {
  method: "POST",
  body: formdata,
  redirect: "follow"
};

fetch("https://api.nb.com.ar/v1/auth/login", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
```



Objeto de respuesta:

```
<br />
<b>Warning</b>:  Undefined array key 0 in <b>/var/www/app/src/Service/TokenService.php</b> on line <b>105</b><br />
{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NTc0NjA3ODEsImF1ZCI6ImIxZjk1ZjM3MDNjMTVjOWJmZmJkOGZlYmE3NGY2MzcyN2U5YzVjM2YiLCJ1c2VyIjp7ImlkIjo1MjU0OCwiY29kaWdvRlAiOiIwMzg5NDkiLCJyb2xlIjoxLCJjb3JyZW9Db25maXJtYWRvIjoxLCJjYXJyaXRvQWN0aXZvIjo4MjQ5ODU4LCJibGFja1VzZXIiOjAsInNob3dOYW1lIjoiZ3J1cG9uZXR3b3JsZCIsIm1vZGUiOiJhcGkiLCJkb21haW4iOm51bGx9LCJpYXQiOjE3NTc0NDk5ODEsIm5iZiI6MTc1NzQ0OTk4MX0.iRPlL8KEPHFSCLJwuHLnuvHppn6mFX523nhnflnjIkU"}
```
