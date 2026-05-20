# Changelog — RRHH BLU

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
