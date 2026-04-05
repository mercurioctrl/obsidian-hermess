---
jira_key: "COB-575"
aliases: ["COB-575"]
summary: "API - Feat - Repositorio vendedores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-20 08:02"
updated: "2025-08-21 15:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-575"
---

# COB-575: API - Feat - Repositorio vendedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-20 08:02 |
| Actualizado | 2025-08-21 15:16 |
| Etiquetas | ninguna |
| Jira | [COB-575](https://bluinc.atlassian.net/browse/COB-575) |

## Relaciones

- **Padre:** [[COB-573]] Clientes
- **has action item:** [[COB-576]] APP - Refactor - Agregar filtros "vendedor" y "deudores" al repositorio de clientes

## Descripcion

Basándose en `[LO].[dbo].[vendedores]` se debe generar el repositorio de vendedores del sitio

```
GET {API_URL}/v1/agents
```

Devuelve:

```
[
    {
        "id": 5,
        "ccodage": "05 ",
        "description": "Contardi Patricio"
    },
    {
        "id": 6,
        "ccodage": "06 ",
        "description": "Baldisera Christian"
    },
    {
        "id": 7,
        "ccodage": "07 ",
        "description": "Blanco Insua Galo"
    },
    {
        "id": 8,
        "ccodage": "08 ",
        "description": "Altamiranda Andrea"
    },
    {
        "id": 12,
        "ccodage": "12 ",
        "description": "Sistema Web"
    },
    {
        "id": 20,
        "ccodage": "20 ",
        "description": "Fayela Alejandro"
    },
    {
        "id": 13,
        "ccodage": "13",
        "description": "Altamiranda Dario"
    },
    {
        "id": 14,
        "ccodage": "14",
        "description": "Lopez Daniel"
    },
    {
        "id": 27,
        "ccodage": "27",
        "description": "Carpintieri Carla"
    },
    {
        "id": 30,
        "ccodage": "30",
        "description": "Albarracin Julian"
    },
    {
        "id": 34,
        "ccodage": "34",
        "description": "Vommaro Valeria"
    },
    {
        "id": 35,
        "ccodage": "35",
        "description": "Melograna Sofia"
    },
    {
        "id": 36,
        "ccodage": "36",
        "description": "Sin Vendedor "
    },
    {
        "id": 38,
        "ccodage": "38",
        "description": "Hernandez Diego"
    },
    {
        "id": 100,
        "ccodage": "100",
        "description": "Opcion Libre"
    },
    {
        "id": 41,
        "ccodage": "41",
        "description": "Natalia Sheridaim"
    },
    {
        "id": 47,
        "ccodage": "47",
        "description": "Antonella Garcia"
    },
    {
        "id": 48,
        "ccodage": "48",
        "description": "Camila Garcia"
    },
    {
        "id": 45,
        "ccodage": "45",
        "description": "Juan De Bello"
    },
    {
        "id": 46,
        "ccodage": "46",
        "description": "Adriana Speranza"
    },
    {
        "id": 49,
        "ccodage": "49",
        "description": "Diego Bordon"
    },
    {
        "id": 50,
        "ccodage": "50",
        "description": "Pablo Valenti"
    },
    {
        "id": 51,
        "ccodage": "51",
        "description": "Lautaro Soto"
    },
    {
        "id": 52,
        "ccodage": "52",
        "description": "Juan Jose Tamagnone"
    },
    {
        "id": 55,
        "ccodage": "55",
        "description": "Lucas Mena"
    },
    {
        "id": 56,
        "ccodage": "56",
        "description": "Matias Rebreg"
    },
    {
        "id": 57,
        "ccodage": "57",
        "description": "Eloy Passarella"
    },
    {
        "id": 69,
        "ccodage": "69",
        "description": "Ariel Accme"
    },
    {
        "id": 70,
        "ccodage": "70",
        "description": "Eduardo Quinteros"
    },
    {
        "id": 67,
        "ccodage": "67",
        "description": "Agustin Carou"
    },
    {
        "id": 71,
        "ccodage": "71",
        "description": "Matias Rebreg"
    }
]
```

```
SELECT  
       [ccodage] as ccodage
      ,[capeage]+' '+[cnbrage] as description
      , id_vendedor as id
  FROM [NewBytes_DBF].[dbo].[agentes]
   
```
