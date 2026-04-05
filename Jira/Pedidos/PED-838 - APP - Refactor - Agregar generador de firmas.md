---
jira_key: "PED-838"
aliases: ["PED-838"]
summary: "APP - Refactor - Agregar generador de firmas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-10-02 07:34"
updated: "2024-10-04 03:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-838"
---

# PED-838: APP - Refactor - Agregar generador de firmas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-02 07:34 |
| Actualizado | 2024-10-04 03:44 |
| Etiquetas | ninguna |
| Jira | [PED-838](https://bluinc.atlassian.net/browse/PED-838) |

## Relaciones

- **Padre:** [[PED-132]] Feat - Login / Re Login
- **action item from:** [[PED-837]] API - Refactor - Agregar parametros al objeto user

## Descripcion

Agregaremos en alguna parte del menú superior un modal que nos permita acceder al generador de firmas. 
Lo que haremos sera crear una visualización que pueda ser copiada la firma directamente, así como tambien su respectivo código html de la firma (segun el cliente de correo algunos podes pegar directamente la firma y otros requieren el codigo)

Para obtener los parametros usaremos 

```
GET GET {API_URL}/v1/auth/user
```

[adjunto]


[adjunto]
