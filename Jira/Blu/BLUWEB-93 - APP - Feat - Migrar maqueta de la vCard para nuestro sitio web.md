---
jira_key: "BLUWEB-93"
aliases: ["BLUWEB-93"]
summary: "APP - Feat - Migrar maqueta de la vCard para nuestro sitio web"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-07-22 17:57"
updated: "2025-08-25 09:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-93"
---

# BLUWEB-93: APP - Feat - Migrar maqueta de la vCard para nuestro sitio web

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-22 17:57 |
| Actualizado | 2025-08-25 09:40 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-93](https://bluinc.atlassian.net/browse/BLUWEB-93) |

## Relaciones

- **Padre:** [[BLUWEB-13 - Sitio Web_Etapa 0|BLUWEB-13]] Sitio Web_Etapa 0

## Descripcion

Mudaremos la maqueta realizada en [link](https://bluinc.atlassian.net/browse/BLUWEB-15)  de tal forma que siguiendo el mismo principio, al ingresar a 

`https://gamma.blu.inc/vcard/cmercurio@blu.inc` se muestre la vCard

Recurso de la API

`API_URL = https://api.blu.inc/ ` (por ahora solo existe prod)

```
{{API_URL}}/api/vCard?email=cmercurio@blu.inc
```

```
{
    "id": 4,
    "first_name": "Catriel",
    "last_name": "Mercurio",
    "email": "cmercurio@blu.inc",
    "role": "admin",
    "job_title": "CTO (Chief Technology Officer)",
    "phone": "1130510267",
    "whatsapp": "1130510267"
}
```
