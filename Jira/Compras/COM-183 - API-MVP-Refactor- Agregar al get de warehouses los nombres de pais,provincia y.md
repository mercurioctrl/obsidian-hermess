---
jira_key: "COM-183"
aliases: ["COM-183"]
summary: "API-MVP-Refactor- Agregar al get de warehouses los nombres de pais,provincia y ciudad"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-05-06 13:04"
updated: "2025-09-30 10:16"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/COM-183"
---

# COM-183: API-MVP-Refactor- Agregar al get de warehouses los nombres de pais,provincia y ciudad

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-05-06 13:04 |
| Actualizado | 2025-09-30 10:16 |
| Etiquetas | MVPLaset |
| Jira | [COM-183](https://bluinc.atlassian.net/browse/COM-183) |

## Relaciones

- **Padre:** [[COM-178 - Depositos|COM-178]] Depositos
- **blocks:** [[COM-180 - APP - MVP - Feat - Implementar pestaña Depositos|COM-180]] APP - MVP - Feat - Implementar pestaña "Depositos"

## Descripcion

En el recurso REST `GET`,  sobre `warehouses`,
**Se agregarán nuevos campos**

```
GET {API_URL}/v1/warehouses?search={name|code|id}
```

```
{
   "response": [
      {
         "id": 1,
         "code": "DE1",
         "name": "DEPOSITO 1",
         "address": "",
         "cityCode": "BSAS",
         "provinceCode": 1,
         "phone": "",
         "default": true,
         "cityId": 2,
         "provinceId": 0,
         "provinceName":"nombre de la provincia", //--->Nuevo
         "cityName":"nombre de la ciudad/localidad",//--->Nuevo
         "countryDescription": "España",//--->Nuevo
         "countryId" :2,//--->Nuevo
         "prefixFlag":"ES",//--->Nuevo
      },
      {...
   ],
   "pagination": {
      "total": 9,
      "limit": 15,
      "offset": 0
   }
}
```
