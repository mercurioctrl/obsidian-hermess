---
jira_key: "NBWEB-28"
summary: "Cambio de datos de usuario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-25 11:08"
updated: "2022-06-26 20:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-28"
---

# NBWEB-28: Cambio de datos de usuario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-25 11:08 |
| Actualizado | 2022-06-26 20:09 |
| Etiquetas | ninguna |
| Jira | [NBWEB-28](https://bluinc.atlassian.net/browse/NBWEB-28) |

## Descripción

***[Ver comentario](https://lioteam.atlassian.net/browse/NBWEB-28?focusedCommentId=10802)

Se trata del producto que sirve para agregar/editar/eliminar productos del carrito

 

```
PATCH {{API_URL}}/v1/miCuenta/usuario/{userId}
```

 

En la request se envía el objeto

 

```json
{
  "password": "xxxxxx",
  "name": "nombreDeUsuario",
  "email": "correo@delusuario.com",
  "showName": "Nombre para mostrar"
  "role": "Postventa",
  *"defaultCurrency":true,
  *"defaulIvas":false,
  *"defaulStock":false
}
```
