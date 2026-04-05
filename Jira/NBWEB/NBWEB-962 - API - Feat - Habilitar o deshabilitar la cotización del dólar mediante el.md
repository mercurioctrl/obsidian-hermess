---
jira_key: "NBWEB-962"
aliases: ["NBWEB-962"]
summary: "API - Feat - Habilitar o deshabilitar la cotización del dólar mediante el parámetro quoteSiteShow para el sitio web"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-15 08:39"
updated: "2025-04-16 00:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-962"
---

# NBWEB-962: API - Feat - Habilitar o deshabilitar la cotización del dólar mediante el parámetro quoteSiteShow para el sitio web

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-15 08:39 |
| Actualizado | 2025-04-16 00:53 |
| Etiquetas | ninguna |
| Jira | [NBWEB-962](https://bluinc.atlassian.net/browse/NBWEB-962) |

## Relaciones

- **Padre:** [[NBWEB-524]] CMS - Parametros varios
- **has action item:** [[NBWEB-963]] APP - Feat - Agregar un conmutador para mostrar u ocultar la cotización del dólar en el sitio web

## Descripcion

Se debe poder controlar la visualización de la cotización del dólar en el sitio web a través de un parámetro en la API, de modo que pueda activar o desactivar esta funcionalidad según las necesidades del negocio.

- Obtener el valor de `quoteSiteShow` utilizando el recurso 

```
GET {API_URL}/v1/cms/defaultParameters
```


- Actualizar el valor de `quoteSiteShow` a través de 

```
POST {API_URL}/v1/cms/defaultParameters
```

```
{
"quoteSiteShow": true/false
}
```


- Guardar los cambios en la tabla `[NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS]`, columna `quoteSiteShow`.



**Criterios de aceptación:**

- El endpoint de POST recibe correctamente la clave `quoteSiteShow` con valor booleano (true/false).


- Al modificar el valor de `quoteSiteShow`, se impacta en la base de datos (tabla `[NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS]`, columna `defaultParameters`).


- Si la operación se realiza con éxito, la API retorna una respuesta indicando el éxito de la actualización.
