---
jira_key: "BLUWEB-7"
summary: "API - Feat - Instalar entorno Docker para Laravel con MySQL, phpMyAdmin y Redis"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-28 16:43"
updated: "2025-05-06 10:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-7"
---

# BLUWEB-7: API - Feat - Instalar entorno Docker para Laravel con MySQL, phpMyAdmin y Redis

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-28 16:43 |
| Actualizado | 2025-05-06 10:16 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-7](https://bluinc.atlassian.net/browse/BLUWEB-7) |

## Descripción

Crear un entorno Docker funcional con **MySQL**, **phpMyAdmin** y **Redis** ya preconfigurado para que la aplicación Laravel corra correctamente, facilitando el desarrollo y testing en infraestructura remota.

**Acceder con (pedir certificado):**

```
ssh -i "SP-A.pem" root@ec2-54-94-237-109.sa-east-1.compute.amazonaws.com
```

- Instalar Docker y Docker Compose (si no están instalados).


- Crear los contenedores necesarios:

- MySQL con persistencia de datos.


- phpMyAdmin vinculado al contenedor de MySQL.


- Redis.


- Contenedor para Laravel si se desea levantar la app directamente en Docker.




- Configurar el archivo `docker-compose.yml` con los servicios.


- Montar correctamente volúmenes y variables de entorno (`.env`) para conexión desde Laravel.


- Probar que Laravel puede conectarse a MySQL y Redis exitosamente.


- Documentar en el README del repo los pasos para levantar el entorno localmente.



### 📤 Repositorio

Guardar todo el código y configuración en:

> [link](https://github.com/BluIncStudio/sitio-api-rest-v1-laravel) 


---

### ✅ Criterios de Aceptación

- El comando `docker-compose up -d` levanta todos los servicios sin errores.


- Laravel se conecta correctamente a MySQL y Redis.


- Se puede acceder a phpMyAdmin desde el navegador.


- Toda la configuración está subida al repositorio indicado.


- El README explica cómo levantar el entorno local en desarrollo.
