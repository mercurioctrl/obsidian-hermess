---
jira_key: "PED-1141"
aliases: ["PED-1141"]
summary: "API - MVP - Feat - Repositorio Almacén (Deposito)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-06 08:46"
updated: "2025-10-27 14:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1141"
---

# PED-1141: API - MVP - Feat - Repositorio Almacén (Deposito)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-06 08:46 |
| Actualizado | 2025-10-27 14:44 |
| Etiquetas | ninguna |
| Jira | [PED-1141](https://bluinc.atlassian.net/browse/PED-1141) |

## Relaciones

- **Padre:** [[PED-1107]] Almacenes Multiples
- **has action item:** [[PED-1108]] API - MVP - Refactor - Mostrar items con almacenes multiples, cuando existan, y agregar el parametro stockWarehouseId
- **has action item:** [[PED-1144]] APP - MVP - Feat - Filtro de deposito para el recurso items
- **has action item:** [[PED-1129]] APP - MVP - Refactor - Agregar lista de depósito a la descarga de lista de precio

## Descripcion

Exponer los recursos `GET` sobre `warehouses` permitiendo filtrarlo por `name` y `companyCode`

```
GET {API_URL}/v1/warehouses?search={name|code|id}&companyCode={companyCode}
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
         "companyCode": 9
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

- Cada elemento incluye todos los atributos definidos:
`id`, `code`, `name`, `address`, `cityCode`, `provinceCode`, `phone`, `default`, `cityId`, `provinceId`, `companyCode`.
