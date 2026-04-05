---
jira_key: "PED-412"
aliases: ["PED-412"]
summary: "APP - Refactor - Desactivar selectores en ambas pestañas del dashboard segun el rol"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-12-29 09:38"
updated: "2024-01-03 11:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-412"
---

# PED-412: APP - Refactor - Desactivar selectores en ambas pestañas del dashboard segun el rol

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-29 09:38 |
| Actualizado | 2024-01-03 11:31 |
| Etiquetas | ninguna |
| Jira | [PED-412](https://bluinc.atlassian.net/browse/PED-412) |

## Relaciones

- **Padre:** [[PED-149 - Reportes|PED-149]] Reportes
- **blocks:** [[PED-426 - APP - Review - Parece que al hacer cambios sobre los selectores de fechaperiodo|PED-426]] APP - Review - Parece que al hacer cambios sobre los selectores de fecha/periodo deje de ver el selector de "agente"

## Descripcion

Segun el objeto

```
GET /v1/auth/user
```

```
{
    "user": {
        "id": 7463,
        "codeFP": 19227,
        "username": "master",
        "email": "hermess87@gmail.com",
        "codeAgent": 12,
        "showName": "catriel2",
        "usuIdentificacion": "Seba",
        "pedidos": true,
        "pm": false,
        "roleDescription": "Administrator" <-----
    }
}
```

Usaremos el parámetro `roleDescription` 

Los únicos que pueden hacer cambios en el selector de agentes son 

- Administrador


- Gerente General


- Product Manager
