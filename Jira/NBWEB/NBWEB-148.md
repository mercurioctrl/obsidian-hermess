---
jira_key: "NBWEB-148"
summary: "API - Opciones medios envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-28 12:27"
updated: "2022-06-26 21:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-148"
---

# NBWEB-148: API - Opciones medios envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-28 12:27 |
| Actualizado | 2022-06-26 21:33 |
| Etiquetas | ninguna |
| Jira | [NBWEB-148](https://bluinc.atlassian.net/browse/NBWEB-148) |

## Descripción

Usando el recuso del micro servicio de envíos [link](https://lioteam.atlassian.net/browse/NBWEB-76)  

```
GET {{API_URL}}/medios-envio
```

Se debe generar un recurso analogo para nuestra api, en la ruta

```
GET {{API_URL}}/mediosEnvio
```

Se debe retornar una respuesta como la siguiente, solo para los casos que estén activos (eso esta en el parametro que entrega el micro servicio)

```
[
    {
        "id": "3030",
        "nombre": "Moto                                              ",
        "tipo": "2",
        "descripcion": "Moto (Capital Federal)",
    },
    {
        "id": "4041",
        "nombre": "OCA                                               ",
        "tipo": "2",
        "descripcion": "Envio OCA a domicilio",
    },
    {
        "id": "4055",
        "nombre": "Combinar Envio                                    ",
        "tipo": "2",
        "descripcion": "Moto coordinada en otro pedido",
    },
    {
        "id": "4056",
        "nombre": "Miniflete (Capital Federal)                       ",
        "tipo": "2",
        "descripcion": "Miniflete (Capital Federal)",
    },
    {
        "id": "4065",
        "nombre": "Andreani                                          ",
        "tipo": "2",
        "descripcion": "Andreani a domicilio",
    }
]
```
