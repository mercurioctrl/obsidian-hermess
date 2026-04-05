---
jira_key: "EXP-113"
aliases: ["EXP-113"]
summary: "API - Feat - Listar medios de envío"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-12-21 09:57"
updated: "2023-06-21 07:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-113"
---

# EXP-113: API - Feat - Listar medios de envío

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-21 09:57 |
| Actualizado | 2023-06-21 07:11 |
| Etiquetas | ninguna |
| Jira | [EXP-113](https://bluinc.atlassian.net/browse/EXP-113) |

## Relaciones

- **Padre:** [[EXP-1 - Base y Repositorios|EXP-1]] Base y Repositorios
- **blocks:** [[EXP-86 - API - Feat - Filtros listar pedidos envios|EXP-86]] API - Feat - Filtros listar pedidos envios

## Descripcion

Basandonos en el recurso del ms-envios

```
{{API_URL}}/medios-envio
```

Se debe obtener 

```
[
    {
        "id": 3030,
        "nombre": "Moto",
        "activo": 1,
        "eliminado": 0,
        "tipo": 2,
        "descripcion": "Moto (Capital Federal)",
        "plusDiasExtraMin": 0,
        "plusDiasExtraMax": 0
    },
    {
        "id": 4041,
        "nombre": "OCA",
        "activo": 1,
        "eliminado": 0,
        "tipo": 2,
        "descripcion": "OCA a domicilio",
        "plusDiasExtraMin": 1,
        "plusDiasExtraMax": 3
    },
    {
        "id": 4055,
        "nombre": "Combinar Envio",
        "activo": 1,
        "eliminado": 0,
        "tipo": 2,
        "descripcion": "Moto coordinada en otro pedido",
        "plusDiasExtraMin": 0,
        "plusDiasExtraMax": 0
    },
    {
        "id": 4065,
        "nombre": "Andreani",
        "activo": 1,
        "eliminado": 0,
        "tipo": 2,
        "descripcion": "Andreani a domicilio",
        "plusDiasExtraMin": 1,
        "plusDiasExtraMax": 3
    },
    {
        "id": 3031,
        "nombre": "Camioneta",
        "activo": 1,
        "eliminado": 0,
        "tipo": 2,
        "descripcion": "Camioneta",
        "plusDiasExtraMin": 0,
        "plusDiasExtraMax": 0
    }
]
```
