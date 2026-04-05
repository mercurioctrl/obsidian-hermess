---
jira_key: "BULLY-5"
aliases: ["BULLY-5"]
summary: "API - Stack"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2023-06-21 18:26"
updated: "2023-07-13 15:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BULLY-5"
---

# BULLY-5: API - Stack

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-21 18:26 |
| Actualizado | 2023-07-13 15:39 |
| Etiquetas | ninguna |
| Jira | [BULLY-5](https://bluinc.atlassian.net/browse/BULLY-5) |

## Relaciones

- **Padre:** [[BULLY-1]] Bases y repositorios
- **Subtarea:** [[BULLY-6]] API - Contenedor MariaDB / phpmyadmin
- **Subtarea:** [[BULLY-7]] API - Contenedor FastApi / uvicorn

## Descripcion

Se trata de el stack necesario para correr la aplicación.

Si bien es probable que en ámbito productivo la base de datos corra en modo host y no dentro de un contenedor, en terminos practicos y para desarrollo dejaremos armado completo el stack para que sea mas facil.

Crearemos un directorio llamado `/container`dentro del repositorio [https://github.com/New-Bytes/api-rest-bully](https://github.com/New-Bytes/api-rest-bully) 

```
/App <- Nuestra api
/containers
|_ database <- [[BULLY-6]]
  |_docker
  |_docker-compose.example.yml
|_ aplicacion <- [[BULLY-7]]
  |_docker
  |_docker-compose.example.yml
```

En ambos casos se deben dejar instrucciones basicas en el `readme.me`
