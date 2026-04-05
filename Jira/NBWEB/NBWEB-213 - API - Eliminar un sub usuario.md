---
jira_key: "NBWEB-213"
aliases: ["NBWEB-213"]
summary: "API - Eliminar un sub usuario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-31 16:12"
updated: "2022-06-26 20:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-213"
---

# NBWEB-213: API - Eliminar un sub usuario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-31 16:12 |
| Actualizado | 2022-06-26 20:15 |
| Etiquetas | ninguna |
| Jira | [NBWEB-213](https://bluinc.atlassian.net/browse/NBWEB-213) |

## Relaciones

- **Padre:** [[NBWEB-2]] API - Mi cuenta
- **blocks:** [[NBWEB-172]] APP - Mi cuenta - Mis ususarios
- **relates to:** [[NBWEB-227]] APP - MI cuenta - Mis usuario - Eliminar un ususario

## Descripcion

Se trata del recurso que sirve para eliminar

 

```
DELETE {{API_URL}}/v1/miCuenta/usuario/{userId}
```

 Validar por usuario administrador de las cuentas.
