---
jira_key: "NBWEB-212"
aliases: ["NBWEB-212"]
summary: "API - Crear nuevo sub usuario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-31 16:10"
updated: "2022-07-03 09:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-212"
---

# NBWEB-212: API - Crear nuevo sub usuario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-31 16:10 |
| Actualizado | 2022-07-03 09:27 |
| Etiquetas | ninguna |
| Jira | [NBWEB-212](https://bluinc.atlassian.net/browse/NBWEB-212) |

## Relaciones

- **Padre:** [[NBWEB-2]] API - Mi cuenta
- **blocks:** [[NBWEB-172]] APP - Mi cuenta - Mis ususarios
- **relates to:** [[NBWEB-226]] APP - Mi cuenta - Mis usuarios - Agregar un usuario nuevo

## Descripcion

Se trata del recurso que sirve para agregar un sub usuario

 

```
POST {{API_URL}}/v1/miCuenta/usuario/{userId}
```

 

En la request se envía el objeto

 

```
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

los parámetros son todos opcionales
