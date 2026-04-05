---
jira_key: "BLUWEB-26"
aliases: ["BLUWEB-26"]
summary: "API - Feat - Recurso para construir las vCard dentro del sitio"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-19 07:49"
updated: "2025-05-19 15:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-26"
---

# BLUWEB-26: API - Feat - Recurso para construir las vCard dentro del sitio

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-19 07:49 |
| Actualizado | 2025-05-19 15:29 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-26](https://bluinc.atlassian.net/browse/BLUWEB-26) |

## Relaciones

- **Padre:** [[BLUWEB-13 - Sitio Web_Etapa 0|BLUWEB-13]] Sitio Web_Etapa 0
- **action item from:** [[BLUWEB-9 - Autenticación y Administracion de usuarios|BLUWEB-9]] Autenticación y Administracion de usuarios 

## Descripcion

Crearemos el recurso para construir nuestras vCard en el sitio basándonos en las estructuras de usuarios creadas en [link](https://bluinc.atlassian.net/browse/BLUWEB-9) 

- Este recurso no requiere login, es publico


- Solo muestra los datos para la vCard cuando recibe el atributo `email` sino no muestra nada


- Solo se muestran datos para los usuarios que están `"status": "active"`



```
GET {API_URL}/vCard?email=emanzano@blu.inc
```

```
{
  "id": 1,
  "first_name": "Ezequiel",
  "last_name": "Manzano",
  "email": "emanzano@blu.inc",
  "role": "staff",
  "job_title": "Developer",
  "phone": "",
  "whatsapp": "",
}
```
