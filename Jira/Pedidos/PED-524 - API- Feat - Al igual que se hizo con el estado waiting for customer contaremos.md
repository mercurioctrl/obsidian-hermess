---
jira_key: "PED-524"
aliases: ["PED-524"]
summary: "API- Feat - Al igual que se hizo con el estado \"waiting for customer\" contaremos aquellso reportes que estan en otros estados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-02 08:23"
updated: "2024-02-19 15:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-524"
---

# PED-524: API- Feat - Al igual que se hizo con el estado "waiting for customer" contaremos aquellso reportes que estan en otros estados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-02 08:23 |
| Actualizado | 2024-02-19 15:58 |
| Etiquetas | ninguna |
| Jira | [PED-524](https://bluinc.atlassian.net/browse/PED-524) |

## Relaciones

- **Padre:** [[PED-255 - Notificaciones|PED-255]] Notificaciones
- **blocks:** [[PED-525 - APP - Feat - Devolver debajo de la burbuja, otra burbuja que sean los Work in|PED-525]] APP - Feat - Devolver debajo de la burbuja, otra burbuja que sean los "Work in progres"
- **is blocked by:** [[PED-532 - API - Pendientes, incluir reportes de otros estados - Cantidades no coincidentes|PED-532]] API - Pendientes, incluir reportes de otros estados - Cantidades no coincidentes

## Descripcion

Agregaremos el contador para “work in progres” tambien. 

Y si no demora mucho el recurso, tambien para “done”

```
GET {{API_URL}}/v1/pendings
```

Para esto debemos cambiar el nombre del parámetro o bien los devolveremos como un array (consultar con front)
