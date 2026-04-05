---
jira_key: "LIO-245"
aliases: ["LIO-245"]
summary: "API - Feat - Editar archivo css dinamico"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-05 15:33"
updated: "2025-03-10 23:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-245"
---

# LIO-245: API - Feat - Editar archivo css dinamico

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-05 15:33 |
| Actualizado | 2025-03-10 23:02 |
| Etiquetas | ninguna |
| Jira | [LIO-245](https://bluinc.atlassian.net/browse/LIO-245) |

## Relaciones

- **Padre:** [[LIO-198 - CMS|LIO-198]] CMS
- **has action item:** [[LIO-246 - APP - Feat - Agregar sección para editar CMS remoto|LIO-246]] APP - Feat - Agregar sección para editar CMS remoto

## Descripcion

Crearemos un recurso que sirve para poder escribir un archivo CSS que luego llamaremos desde el sitio web, esto nos permite reescribir estilos para acciones y eventos especiales sin tener que re-compilar el sitio por cada cambio.

## Escribir archivo 

```
POST {API_CMS}/v1/dynamicStyles
```

Esto escribe un archivo que debe poder ser accesible desde

**Carga útil**

```
{
  "cssContent": "body { background-color: #000; color: #fff; }"
}
```

**Devuelve**

```
{
  "success": true,
  "message": "Estilos guardados correctamente."
}
```

## Leer archivo de forma remota para el sitio

```
 {API_CMS/css/dynamicStyles.css
```

Este debe ser un archivo puro, cacheable y por eso debe ser un archivo que se puede escribir (si no tiene nada escrito, simplemente esta vacio)

## Leer archivo para poder editarlo desde el front del CMS

```
GET {API_CMS}/v1/dynamicStyles
```
