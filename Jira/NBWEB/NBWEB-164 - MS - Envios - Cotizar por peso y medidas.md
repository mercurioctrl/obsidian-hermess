---
jira_key: "NBWEB-164"
aliases: ["NBWEB-164"]
summary: "MS - Envios - Cotizar por peso y medidas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-02 12:09"
updated: "2022-06-26 20:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-164"
---

# NBWEB-164: MS - Envios - Cotizar por peso y medidas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-02 12:09 |
| Actualizado | 2022-06-26 20:18 |
| Etiquetas | ninguna |
| Jira | [NBWEB-164](https://bluinc.atlassian.net/browse/NBWEB-164) |

## Relaciones

- **Padre:** [[NBWEB-76]] API - Implementar MS envios
- **relates to:** [[NBWEB-246]]  Feat - Urbano - Cotizar bulk

## Descripcion

Se trata del recurso necesario para poder cotizar cualquier envios basandose en 5 parametros basicos y uno opcional

- Peso


- Alto


- Ancho


- Largo


- CP destino


- CP origen (opcional)



Adicionalmente puede agregarse un parámetro adicional para el CP de origen

```
GET {{API_URL}}/bulk/size/10x12x45/weight/500/cp/1426/cphost/1229
```

```
GET {{API_URL}}/bulk/size/10x12x45/weight/500/cp/1426
```

Este recurso, devuelve un objeto del siguiente tipo



```json
[
    {
        "costo": 439.01,
        "descripcion": "OCA a domicilio",
        "id": 4041,
        "precio": 0,
        "plazoEntrega": "entre el viernes 08 y el martes 12",
        "plazoEntregaNumero": 4,
        "total": 439.01
    },
    {
        "costo": 993.01,
        "descripcion": "Andreani a domicilio",
        "id": 4065,
        "precio": 993.01,
        "plazoEntrega": "entre mañana y el jueves 07",
        "plazoEntregaNumero": 1,
        "total": 993.01
    },
    {
        "costo": 300,
        "descripcion": "Moto (Capital Federal).",
        "id": 3030,
        "precio": 0,
        "plazoEntrega": "hoy",
        "plazoEntregaNumero": 0,
        "total": 300,
        "horaActual": "2022-04-04 07:07:36"
    }
]
```
