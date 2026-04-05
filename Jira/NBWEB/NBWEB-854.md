---
jira_key: "NBWEB-854"
summary: "APP - Feat - Poner vCard Online para vendedores"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-08-29 07:43"
updated: "2024-09-02 10:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-854"
---

# NBWEB-854: APP - Feat - Poner vCard Online para vendedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-29 07:43 |
| Actualizado | 2024-09-02 10:58 |
| Etiquetas | ninguna |
| Jira | [NBWEB-854](https://bluinc.atlassian.net/browse/NBWEB-854) |

## Descripción

Crearemos una nueva feature en la aplicación de NB con la finalidad de mostrar los datos de contacto de los distintos ejecutivos y personas comerciales.

El mismo podrá accederse directamente a través de la URL del siguiente modo o similar

```
https://nb.com.ar/vcard/aaltamiranda@nb.com.ar
```

Ademas, agregaremos la posibilidad de descargar y generar su archivo para vCard

```
npm install vcf
```

En caso de tener problemas para generar el archivo, podemos ver si el back puede generarlo ya que existe una librería de Laravel para ese fin. 

Una **vCard** es un formato de archivo estándar para el intercambio de información de contacto digital. Es ampliamente utilizado para compartir y almacenar detalles de contacto como nombres, direcciones, números de teléfono, direcciones de correo electrónico, URL, fotos, y otra información relacionada.

Se deja adjunto a continuación el archivo de ejemplo obtenido en la aplicación de un competidor
