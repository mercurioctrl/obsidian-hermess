---
jira_key: "LIO-235"
aliases: ["LIO-235"]
summary: "API CMS - Refactor - Permitir que el recurso que lee los banner por zona, tambien los traiga todos juntos cuando no se le pasa el parámetro de zona"
status: "Finalizada"
type: "Tarea"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-26 06:43"
updated: "2025-02-27 21:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-235"
---

# LIO-235: API CMS - Refactor - Permitir que el recurso que lee los banner por zona, tambien los traiga todos juntos cuando no se le pasa el parámetro de zona

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-26 06:43 |
| Actualizado | 2025-02-27 21:13 |
| Etiquetas | ninguna |
| Jira | [LIO-235](https://bluinc.atlassian.net/browse/LIO-235) |

## Relaciones

- **Padre:** [[LIO-1]] Experiencia del Usuario (UX)
- **has action item:** [[LIO-239]] APP - Refactor - Conectar los mini banners de productos destacados con el CMS unificando la obtencion de los banners con una sola peticion

## Descripcion

Actualmente, la API `https://apic.libreopcion.com.ar/v1/cms/banner/{zona}` permite obtener los banners de una zona específica pasando el ID de la zona como parámetro en la URL. Sin embargo, no existe una opción para recuperar todos los banners de todas las zonas en una sola solicitud.

Se requiere modificar el recurso para que, si no se pasa una zona específica, se devuelvan todos los banners agrupados por zona.

- Si el usuario consulta `https://apic.libreopcion.com.ar/v1/cms/banner/{zona}`, la API sigue devolviendo solo los banners de la zona solicitada (sin cambios en la funcionalidad actual).


- Si el usuario consulta `https://apic.libreopcion.com.ar/v1/cms/banner/` (sin especificar `{zona}`), la API debe responder con un objeto que contenga todas las zonas y sus respectivos banners.


- La respuesta debe estructurarse agrupando los banners bajo su zona correspondiente.


- Se debe mantener el mismo formato de los banners actuales en la respuesta.


- Si no hay banners disponibles en alguna zona, esta igualmente debe aparecer en la respuesta con un array vacío.



```
GET {API_CMS}/v1/cms/banner
```

```
{
  "1": [
    {
      "orden": "1",
      "url": "/gigabyte?o=rel&ver_mas_vendedores=1",
      "checksum": "8f931b98cf2923bd7402dd7ad1449b6c.jpg"
    },
    {
      "orden": "2",
      "url": "",
      "checksum": "0945ee7a0a6c866cfb08d7e2bb5b00f3.jpg"
    }
  ],
  "2": [
    {
      "orden": "1",
      "url": "",
      "checksum": "9d965b85a020d21ff1c4d90b479480a3.jpg"
    },
    {
      "orden": "2",
      "url": "",
      "checksum": "6e78a0b00f91dbdaabe82631d652276f.jpg"
    }
  ]
}

```

*ver con Marbe si este objeto se adapta a sus necesidades de la mejor manera
