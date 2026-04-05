---
jira_key: "LIO-171"
aliases: ["LIO-171"]
summary: "API - Feat - Agregar funcionalidad para manejar y retornar información del código postal en la APIv4"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-01-15 09:52"
updated: "2025-02-01 00:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-171"
---

# LIO-171: API - Feat - Agregar funcionalidad para manejar y retornar información del código postal en la APIv4

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-15 09:52 |
| Actualizado | 2025-02-01 00:33 |
| Etiquetas | ninguna |
| Jira | [LIO-171](https://bluinc.atlassian.net/browse/LIO-171) |

## Relaciones

- **Padre:** [[LIO-162 - Mejoras generales para envios|LIO-162]] Mejoras generales para envios
- **has action item:** [[LIO-163 - APP - Refactor - Cambiar herramienta para cotizacion|LIO-163]] APP - Refactor - Cambiar herramienta para cotizacion

## Descripcion

Como **usuario del sistema**, quiero que el sistema registre mi código postal cuando interactúo con el sitio para que la navegación por los productos sea completa respecto a los envios, para esto agregaremos un recurso especifico para setear el parámetro

```
POST {API_V4}/users/postal-code
```

**Criterios de Aceptación**:

- **Usuarios logueados**:

- Cuando un usuario autenticado realiza una solicitud que incluye su código postal, este debe guardarse en la tabla de `[LO].[dbo].[usuarios]` en la base de datos.


- La API debe retornar la provincia asociada al código postal enviado.




- **Usuarios no logueados**:

- Si el usuario no está autenticado, el código postal se guarda temporalmente en el front-end (almacenamiento local o sesión del navegador).


- La API sigue retornando la provincia asociada al código postal enviado.





**Devuelve algo similar a:**

```
{
  "province": "Ciudad de Buenos Aires"
  "postalCode" "1407"
}
```



Actulizado:

Recurso:

```
POST {API_V4}/users/postalCode
```

payload:

```
{ "postalCode": 7600 }
```

response:

```
{
   "province": "CAPITAL FEDERAL ( CAP. FED. )",
   "locality": "CIUDAD DE BUENOS AIRES",
   "postalCode": 1229
}
```
