---
jira_key: "LIO-142"
aliases: ["LIO-142"]
summary: "API - Refactor - Patron de 5 calificaciones en el recurso calificar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-26 17:18"
updated: "2024-12-18 11:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-142"
---

# LIO-142: API - Refactor - Patron de 5 calificaciones en el recurso calificar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-26 17:18 |
| Actualizado | 2024-12-18 11:22 |
| Etiquetas | ninguna |
| Jira | [LIO-142](https://bluinc.atlassian.net/browse/LIO-142) |

## Relaciones

- **Padre:** [[LIO-124]] Calificaciones

## Descripcion

```
PATCH {{API_URL}}/v4/pedidos/comprasCalificacion
```

```
{
"pedidoCabecerVendedorId": 564098,
"calificacion": 5 <--- AHORA PUDE IR HASTA 5
"token": "9c587657fe4a578ed398d7992babb37dc26235700fa6df2b438d1325c538ac7b"
}
```

Todas las que estan en 3, ponerlas en 5 (esto es para produ a lo ultimo de terminada la feature)

Todas las que estan en 2 ponerlas en 4 (esto es para produ a lo ultimo de terminada la feature)
