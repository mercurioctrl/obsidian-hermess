---
jira_key: "BULLY-7"
aliases: ["BULLY-7"]
summary: "API - Contenedor FastApi / uvicorn"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-06-21 18:41"
updated: "2023-06-22 17:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BULLY-7"
---

# BULLY-7: API - Contenedor FastApi / uvicorn

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-21 18:41 |
| Actualizado | 2023-06-22 17:05 |
| Etiquetas | ninguna |
| Jira | [BULLY-7](https://bluinc.atlassian.net/browse/BULLY-7) |

## Relaciones

- **Padre:** [[BULLY-5 - API - Stack|BULLY-5]] API - Stack
- **blocks:** [[BULLY-12 - Logins y autenticaciones|BULLY-12]] Logins y autenticaciones 

## Descripcion

Si bien el proyecto puede funcionar en casi cualquier host, esto hace que el despliegue sea mas dificultoso. Suele suceder que al momento de correrlo en un servidor faltan librerias en el host y a su vez estas tienen dependencias incumplidas que hay que instalar.

Por esto , dejaremos ya preparado un contenedor de despliegue rápido que ya tenga todo lo necesario y las versiones adecuadas que corren la aplicacion

Crearemos un directorio llamado `/container`dentro del repositorio [https://github.com/New-Bytes/api-rest-bully](https://github.com/New-Bytes/api-rest-bully)  

```
/App <- Nuestra api
/containers
|_ database 
  |_docker
  |_docker-compose.example.yml
|_ aplicacion <- Dentro de este direcotrio colocaremos los archivos para montar el contenedor
  |_docker
  |_docker-compose.example.yml
```

En el alojaremos el conjunto necesario para correr python3  y todas las librerias y dependencias necesarias para correr el proyecto. Adicionalmente dejaremos configurado uvicorn para servir la aplicación de modo sencillo

[link](https://gist.github.com/sbv-trueenergy/a9a6971778a01d1acd3c466719e690b8)
