---
jira_key: "BLUWEB-15"
summary: "APP - Seccion vCard"
status: "LISTO"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-05-06 14:59"
updated: "2025-05-09 17:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-15"
---

# BLUWEB-15: APP - Seccion vCard

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-06 14:59 |
| Actualizado | 2025-05-09 17:18 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-15](https://bluinc.atlassian.net/browse/BLUWEB-15) |

## Descripción

Crearemos una nueva feature en la aplicación con la finalidad de mostrar los datos de contacto de los distintos ejecutivos y personas comerciales.

El mismo podrá accederse directamente a través de la URL del siguiente modo o similar

```
https://blu.inc/vcard/cmercurio@blu.inc
```

Ademas, agregaremos la posibilidad de descargar y generar su archivo para vCard

```
npm install vcf
```

En caso de tener problemas para generar el archivo, podemos ver si el back puede generarlo ya que existe una librería de Laravel para ese fin. 

Una **vCard** es un formato de archivo estándar para el intercambio de información de contacto digital. Es ampliamente utilizado para compartir y almacenar detalles de contacto como nombres, direcciones, números de teléfono, direcciones de correo electrónico, URL, fotos, y otra información relacionada.

Se deja adjunto a continuación el archivo de ejemplo obtenido en la aplicación de un competidor
