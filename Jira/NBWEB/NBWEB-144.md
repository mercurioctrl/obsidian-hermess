---
jira_key: "NBWEB-144"
summary: "MS - Envios - Dotar al servicio de su tabla y administrador correspondiente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-04-26 12:19"
updated: "2022-05-02 18:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-144"
---

# NBWEB-144: MS - Envios - Dotar al servicio de su tabla y administrador correspondiente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-26 12:19 |
| Actualizado | 2022-05-02 18:52 |
| Etiquetas | ninguna |
| Jira | [NBWEB-144](https://bluinc.atlassian.net/browse/NBWEB-144) |

## Descripción

Se debe crear una tabla espejo, de la que se encuentra en el enlace local

Se puede usar un dockerfile basado en el siguiente ejemplo

**docker-compose.example.yml**

```
version: '3.1'

# Docker Services

services:

  # PHP/Apache Service

  apirest:
    build:
      context: .
      dockerfile: ./docker/Dockerfile
    container_name: service-envios-api-rest
    restart: always
    ports:
      - "8040:80"
    volumes:
      - ./app/:/var/www/app
      - ./docker/php/local.ini:/usr/local/etc/php/conf.d/local.ini
    networks:
      - service-envios-network


  # MySQL Service
  
  mariadb:
    image: mariadb
    container_name: service-envios-api-rest-mariadb
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: 5#6So5DR7mdu 
      MYSQL_DATABASE: service-envios-api-rest-db
    ports: 
      - "3312:3306"
    volumes:
      - dbdata:/var/lib/mysql
      - ./docker/mysql/my.cnf:/etc/mysql/my.cnf
    networks:
      - service-envios-network

  
  # PHPMyAdmin Service
  
  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    container_name: service-envios-api-rest-phpmyadmin
    restart: always
    ports:
      - "8049:80"
    volumes:
        - /sessions
    environment:
      PMA_HOST: mariadb
      MYSQL_ROOT_PASSWORD: 5#3845DR7mdu
    depends_on:
      - mariadb
    networks:
      - service-envios-network

# Volumes

volumes:
  lo-dbdata:
    driver: local

# Docker Networks

networks:
  lo-service-envios-network:
    driver: bridge
```

**my.cnf**

./docker/mysql/my.cnf:/etc/mysql/my.cnf (se crea la carpeta, dentro de la carpeta docker)

```
[mysqld]
general_log = 1
general_log_file = /var/lib/mysql/general.log
default-time-zone=-03:00

```
