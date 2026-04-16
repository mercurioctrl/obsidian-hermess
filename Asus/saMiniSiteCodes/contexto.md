# Contexto

## Estado de la promoción

La promoción de canje de códigos (Resident Evil / ROG) **finalizó el 2026-04-15**.
El sitio permanece online para:
- Consultar instrucciones de canje en Steam
- Enviar tickets de soporte si hay problemas con un código ya entregado

Para reabrir: cambiar `PROMO_CLOSED=false` en `.env` y recrear container PHP.

## Reglas de negocio

- **Un código por serial:** La tabla `claims` tiene índice único por `serial_number` y `customer_email`
- **Códigos race-condition safe:** `send_code.php` usa `SELECT FOR UPDATE` dentro de transacción
- **Admin sin migración:** `ensureAdminExists()` sincroniza credenciales desde env vars en cada request
- **Video obligatorio en tickets:** Para soporte, se exige video del problema como evidencia

## Decisiones importantes

- **SMTP puerto 465 (no 587):** El servidor `box.asus-sa.com` usa SSL/TLS implícito. Puerto 587 requeriría STARTTLS y no funciona con este host.
- **Timeout 15s en PHPMailer:** Obligatorio para evitar PHP-FPM workers colgados si el SMTP no responde.
- **Nginx no monta todo src:** Solo `public/` y `uploads/`. Bug real: videos de tickets se subían bien pero no se servían hasta agregar el volumen.

## Ver también

- [[Asus/saMiniSiteCodes/saMiniSiteCodes|saMiniSiteCodes]]
- [[Asus/saMiniSiteCodes/arquitectura|Arquitectura]]
- [[Asus/saMiniSiteCodes/memoria|Memoria]]