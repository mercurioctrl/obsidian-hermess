# Stack — microservicio-envios

## Core

| Tecnología | Versión | Rol |
|---|---|---|
| PHP | ^7.4 | Lenguaje principal |
| Slim Framework | 4.* | Microframework REST |
| Pimple | ^3.4 | Contenedor de dependencias (IoC) |
| vlucas/phpdotenv | ^5.3 | Variables de entorno |
| monolog/monolog | ^2.2 | Logging |
| firebase/php-jwt | ^6.1 | Autenticación JWT (HS256) |
| panique/pdo-debug | ^0.2 | Debugging de queries PDO |

## Bases de datos

| DB | Uso |
|---|---|
| **MSSQL Server 17** | Datos legacy: carritos, items, pedidos, paquetes |
| **MariaDB** | Datos v1: métodos de envío, usuarios, tokens |

Ambas accedidas vía PDO. Las conexiones se registran en `src/App/Database.php`.

## Curriers integrados

| Currier | Helper | Protocolo |
|---|---|---|
| OCA | `src/Helper/Oca.php` | XML/SOAP |
| Andreani | `src/Helper/Andreani.php` | REST API |
| Entregar | `src/Helper/Entregar/Entregar.php` | REST API fluente |
| Urbano | `src/Helper/Urbano.php` | REST |
| Moto / Camioneta / Miniflete | internos | lógica propia |
| NbE | `src/Helper/NbE/NbE.php` | interno |

## Infraestructura local (Docker)

- Apache 2 + PHP 8.0 (imagen Docker)
- Puerto servicio: `8089`
- Puerto PHPMyAdmin: `8049`
- Puerto MariaDB: `3312`

## Ver también

- [[microservicio-envios]] · [[arquitectura]] · [[contexto]]
