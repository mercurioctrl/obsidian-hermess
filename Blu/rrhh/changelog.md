# Changelog — RRHH BLU

---

## 2026-08-31 — Registro de salarios

- Creada [[salarios]] con la foto de salarios base vigentes del equipo (8 personas, total mensual **$14.390.000 ARS**).
- Agregada tabla de **historial de aumentos** para trackear ajustes de acá en adelante (fecha, personas, monto/%, motivo).
- No consta ningún aumento cargado en la bóveda durante 2026 → esta foto queda como línea base.
- Pendiente: verificar traslado de la paritaria Comercio CCT 130-75 (abr-jun 2026).

---

## 2026-08-07 — Vacaciones + onboarding ERP (sync desde Slack `#talento`)

### Política de vacaciones
- Creada [[politica-vacaciones]] con la política formal comunicada el 2026-08-06:
  vacaciones en **días hábiles** como beneficio Blu, escala por antigüedad (14/21/28/35),
  regla de **períodos continuos** (sáb/dom/feriados cuentan para la extensión máxima aunque no descuenten saldo),
  condiciones de uso y administración en el ERP.
- Comunicada por mail (hoja membretada, correo RRHH de Blu) + Slack `#blu-team` + mensajes individuales.

### ERP y ausencias
- Creada [[ausencias]] — registro operativo de ausencias/vacaciones cargadas.
- Alta de accesos al ERP para 6 colaboradores (Eze, Marbe, Emanuel, Guille, Franco, Belén).
  Credenciales distribuidas por Slack — **no se persisten en la bóveda**.
- Ausencias cargadas: Ezequiel (completas), Marbe (11/08, día ganado en el prode),
  Guillermo (todas revisadas y OK; pendientes de NB no se trasladan).
- Integración con Google Calendar funcionando (ausencias con color).

### Datos del equipo
- Emails corporativos unificados a `@blustudioinc.com` en [[rrhh]] (los perfiles individuales ya estaban actualizados).
- Resuelta la alerta de email faltante de [[equipo/franco-callipo|Franco Callipo]] → `fcallipo@blustudioinc.com`.

---

## 2026-05-15 — Sesión de arranque

### Primera reunión con consultora RRHH
- Incorporación formal de consultora RRHH externa para diagnóstico organizacional
- Definición del scope: qué decide sola, qué consulta, qué queda en los CEOs
- Objetivo central: descargar a los CEOs de la gestión operativa del equipo

### Documentación creada
- `agenda-primera-reunion.md` — Agenda estructurada para la primera meet (90 min, 8 bloques)
- `contexto.md` — Objetivo estratégico, scope de la consultora, plan 90 días
- `actividades-rrhh-it.md` — Referencia de actividades típicas RRHH en empresas IT

### Perfiles del equipo
- Importados datos de 10 empleados desde CSV (formulario "Bienvenidos a BLU")
- Creados 10 perfiles individuales en `equipo/` con datos personales + perfil RRHH:
  - catriel-mercurio · alejandra-guidobono · belu-ontivero · ezequiel-manzano
  - guillermo-avila · marbe-moreno · emanuel-ferreyra · sebastian-fontan
  - barbara-carrillo · franco-callipo

### Alertas y calendario
- `cumpleanos.md` — Calendario de cumpleaños por mes con tabla de próximos 12 meses
- `alertas-gestion.md` — Panel de alertas por persona (danger/warning/tip/info) con resumen de criticidad

### Automatización
- `recordatorio-cumpleanos.sh` — Script bash que revisa diariamente si hay cumpleaños en 7 días
- Crontab del sistema: `7 9 * * *` — se ejecuta todos los días a las 9:07am
- Log en `/var/www/blu/rrhh/recordatorios.log`

---

## 2026-05-16 — Primera alerta automática

- Recordatorio disparado correctamente: **Guillermo Avila** cumple el 23/05
- Entrada en log: `[2026-05-16 09:07] 🎂 CUMPLEAÑOS EN 7 DÍAS: Guillermo Avila (23/05)`
- Sistema de recordatorios funcionando

---
