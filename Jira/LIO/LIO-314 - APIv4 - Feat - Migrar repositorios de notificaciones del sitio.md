---
jira_key: "LIO-314"
aliases: ["LIO-314"]
summary: "APIv4 - Feat - Migrar repositorios de notificaciones del sitio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-04 08:54"
updated: "2025-04-15 23:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-314"
---

# LIO-314: APIv4 - Feat - Migrar repositorios de notificaciones del sitio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-04 08:54 |
| Actualizado | 2025-04-15 23:41 |
| Etiquetas | ninguna |
| Jira | [LIO-314](https://bluinc.atlassian.net/browse/LIO-314) |

## Relaciones

- **Padre:** [[LIO-313 - Notificaciones|LIO-313]] Notificaciones

## Descripcion

Migrar los siguientes recursos actualmente disponibles bajo la API legacy hacia la nueva estructura de `apiv4`, manteniendo compatibilidad de funcionalidades y mejorando la estructura de respuesta.

```
GET /notifications/last/pendings
```

```
GET /notifications/number/pendings
```



**Respuesta esperada:**

- `/notifications/last/pendings`
Debe devolver un arreglo de notificaciones con el siguiente formato:



```
[
  {
    "url": "https://lio.plus/479917e8/n/0013f873",
    "text": "¡Gracias por tu Compra! Catriel Mercurioo. Has click y seguíla de cerca.",
    "view": false,
    "avatar": "https://lio.plus/ce62",
    "createdAt": "Hace 14 horas"
  }
  // ...
]

```

2.

`/notifications/number/pendings`
Actualmente devuelve un número entero. En `apiv4` se espera devolverlo con estructura estándar:

```
{
  "total": 42
}

```

**📌 Consideraciones técnicas:**

- Asegurarse de que la lógica de  que determina qué notificaciones están pendientes se mantenga sin cambios.



**✅ Criterios de aceptación:**

- Los endpoints existen bajo `apiv4/notifications/last/pendings` y `apiv4/notifications/number/pendings`.


- Devuelven las respuestas en formato JSON con estructura validada.


- Se mantuvo la lógica de selección de notificaciones pendientes.
