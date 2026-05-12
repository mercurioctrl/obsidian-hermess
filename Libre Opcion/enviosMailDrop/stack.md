# Stack — enviosMailDrop

## Runtime

- **Python 3.12** — sin virtualenv, dependencias del sistema

## Dependencias Python

| Librería | Uso |
|---|---|
| `smtplib` + `ssl` | Envío SMTP SSL (stdlib) |
| `email.mime.*` | Construcción del mensaje MIME multipart (stdlib) |
| `email.utils.formataddr` | Formateo correcto del header `From` (RFC 5322) |
| `email.header.Header` | Codificación UTF-8 del nombre del remitente |
| `pyodbc` | Conexión a SQL Server (requiere ODBC Driver 18) |
| `uuid` | Generación de `Message-Id` único por envío |

## Infraestructura

| Servicio | Detalle |
|---|---|
| SMTP | `box.lio.red:465` SSL, con OpenDKIM activo |
| SQL Server | `190.210.23.97:4444`, DB `LO`, usuario `web` |
| DKIM | Selector `mail`, clave RSA publicada en DNS de `libreopcion.com` |
| SPF | `v=spf1 mx a ip4:190.210.23.98 ?all` (pendiente mejorar a `~all`) |

## Plantillas HTML

Diseño de email responsive en tabla HTML puro (compatible con Gmail, Outlook).
Imágenes en `static.libreopcion.com`. Sin CSS externo.

## Ver también

- [[arquitectura]] — flujo y decisiones
- [[enviosMailDrop]] — índice
