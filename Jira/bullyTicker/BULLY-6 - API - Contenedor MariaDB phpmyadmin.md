---
jira_key: "BULLY-6"
aliases: ["BULLY-6"]
summary: "API - Contenedor MariaDB / phpmyadmin"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-06-21 18:35"
updated: "2023-06-26 09:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BULLY-6"
---

# BULLY-6: API - Contenedor MariaDB / phpmyadmin

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-21 18:35 |
| Actualizado | 2023-06-26 09:34 |
| Etiquetas | ninguna |
| Jira | [BULLY-6](https://bluinc.atlassian.net/browse/BULLY-6) |

## Relaciones

- **Padre:** [[BULLY-5 - API - Stack|BULLY-5]] API - Stack
- **blocks:** [[BULLY-12 - Logins y autenticaciones|BULLY-12]] Logins y autenticaciones 

## Descripcion

Si bien la aplicacion no se trata de recopilacion de datos, siempre es necesario almacenar configuraciones, procedimientos y demas. Por esto la aplicacion debe estar provista de una base de datos. Se elije el stack en función de su velocidad y simpleza.

Crearemos un directorio llamado `/container`dentro del repositorio [https://github.com/New-Bytes/api-rest-bully](https://github.com/New-Bytes/api-rest-bully) 

```
/App <- Nuestra api
/containers
|_ database <- Dentro de este direcotrio colocaremos los archivos para montar el contenedor
  |_docker
  |_docker-compose.example.yml
|_ aplicacion
  |_docker
  |_docker-compose.example.yml
```

En el alojaremos el conjunto MariaDb (o mysql) \ phpMyAdmin  

[link](https://migueldoctor.medium.com/run-mysql-phpmyadmin-locally-in-3-steps-using-docker-74eb735fa1fc) 

[link](https://www.kirandev.com/mysql-phpmyadmin-docker-compose) 

[link](https://doc4dev.com/en/install-phpmyadmin-for-mysql-under-docker-with-docker-compose/)
