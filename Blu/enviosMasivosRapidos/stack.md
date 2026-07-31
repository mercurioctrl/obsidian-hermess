# Stack

Ver índice: [[enviosMasivosRapidos]] · Arquitectura: [[arquitectura]]

## Tecnologías

- **PHP** (CLI, sin framework)
- **PHPMailer** `^6.10` — única dependencia (`composer.json`), envío SMTP
- **Composer** — gestión de dependencias (`composer install` tras clonar)
- **ImageMagick** (`convert`) — optimización de los JPG de las newsletters

## SMTP

- Host: `box.lio.red`, puerto 465 (SSL / `ENCRYPTION_SMTPS`)
- Remitentes por campaña: `website@fontainebleau.ar` (FB), `website@nbe.com.ar` (NBElectric)

## Comandos

```bash
composer install                          # instalar PHPMailer en vendor/
php enviarFB.php                           # envío producción Fontaine Bleau
SEND_LIST=emails_testing.txt php enviarFB.php   # envío de prueba
php enviar.php                             # campaña NBElectric
php -l enviarFB.php                        # lint de sintaxis
```

No hay build ni test suite.

## Ver también

- [[arquitectura]]
