---
jira_key: "LIO-239"
aliases: ["LIO-239"]
summary: "APP - Refactor - Conectar los mini banners de productos destacados con el CMS unificando la obtencion de los banners con una sola peticion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2025-02-27 21:13"
updated: "2025-03-05 18:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-239"
---

# LIO-239: APP - Refactor - Conectar los mini banners de productos destacados con el CMS unificando la obtencion de los banners con una sola peticion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2025-02-27 21:13 |
| Actualizado | 2025-03-05 18:15 |
| Etiquetas | ninguna |
| Jira | [LIO-239](https://bluinc.atlassian.net/browse/LIO-239) |

## Relaciones

- **Padre:** [[LIO-105]] Home
- **action item from:** [[LIO-234]] API - Refactor - Usar backgrounds personalizados para los sectores personalizados de productos
- **action item from:** [[LIO-235]] API CMS - Refactor - Permitir que el recurso que lee los banner por zona, tambien los traiga todos juntos cuando no se le pasa el parámetro de zona

## Descripcion

Zonas de banners

```

[
  {
    "id": 1,
    "description": "Banner Home",
    "isSubBanner": 0
  },
  {
    "id": 2,
    "description": "Banner Home Mobile",
    "isSubBanner": 0
  },
  {
    "id": 3,
    "description": "Sub Banner",
    "isSubBanner": 1
  },
  {
    "id": 4,
    "description": "Sub Banner Mobile",
    "isSubBanner": 1
  },
  {
    "id": 5,
    "description": "Mini Banner Home",
    "isSubBanner": 0
  },
  {
    "id": 6,
    "description": "PR Fondo y Onomatopeya",
    "isSubBanner": 0
  },
  {
    "id": "8",
    "description": "Fondo sector personzalizado home",
    "isSubBanner": "0"
}
]
```

las zonas 1,2,4,5,6 y 8 se utilizan directamente en la home se puede hacer un llamado unico con `https://apic.libreopcion.com.ar/v1/cms/banner/` y poder unificar la obtencion en de los banners en una sola petición

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
