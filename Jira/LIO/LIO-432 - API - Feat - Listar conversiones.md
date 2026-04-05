---
jira_key: "LIO-432"
aliases: ["LIO-432"]
summary: "API - Feat - Listar conversiones"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-27 08:52"
updated: "2025-09-02 16:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-432"
---

# LIO-432: API - Feat - Listar conversiones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-27 08:52 |
| Actualizado | 2025-09-02 16:37 |
| Etiquetas | ninguna |
| Jira | [LIO-432](https://bluinc.atlassian.net/browse/LIO-432) |

## Relaciones

- **Padre:** [[LIO-408 - Referidos|LIO-408]] Referidos
- **is blocked by:** [[LIO-443 - API - Review - SyncUp - Impactar tokens por conversión - Tabla inexistente|LIO-443]] API - Review - SyncUp - Impactar tokens por conversión -> Tabla inexistente

## Descripcion

GET {API_URL}/v4/referrals/{token}/visits

Actualizado:

```
GET {API_URL}/v4/referrals/{token}/conversions
```

Basándonos en la tabla `LO.dbo.referral_conversions` mostraremos informacion de las conversiones del token de referido para ese token especifico y de ser necesario haremos join con otra tabla usuarios u otras

```
{
  "data": [
    {
      "id": 1001,
      "usuarioID": 5645,
      "userName": "Lisa Simpson",
      "userEmail": "lista@simpsopn.com",
      "pedidoCabeceraId": 43433,
      "fee": 1500,
      "totalAmount": 15000.24,
      "location": "Buenos Aires, AR"
    },
    {
     "usuarioID": 5645,
      "userName": "Lisa Simpson",
      "userEmail": "lista@simpsopn.com",
      "pedidoCabeceraId": 43433,
      "fee": 1500,
      "totalAmount": 15000.24,
      "location": "Córdoba, AR"
    }
  ],
  ... paginado etc .... 
}

```

Este repositorio sirve para listar las conversiones en un esquema similar al siguiente del rectángulo rojo


[adjunto]
