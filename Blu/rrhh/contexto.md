# Contexto — Iniciativa RRHH BLU

## Situación actual

Los CEOs de BLU Digital Agency llevaban personalmente toda la gestión de personas:
vacaciones, licencias, ausencias, feriados, cumpleaños, conflictos y seguimiento del equipo.
Esto generaba carga operativa que distraía de las decisiones estratégicas.

## Objetivo

Incorporar una consultora de RRHH externa para:
- **Descargar a los CEOs** de la gestión operativa del equipo
- Obtener asesoramiento y seguimiento organizacional continuo
- Diagnosticar el clima y la cultura actual
- Implementar procesos y políticas formales de RRHH

## Scope de la consultora

### Autonomía total (decide sola)
- Aprobación de vacaciones y ausencias
- Gestión del calendario interno (feriados, cumpleaños)
- Primera contención en conflictos interpersonales
- Coordinación de onboarding de nuevos ingresos

### Consulta antes de actuar
- Situaciones de conflicto escalado
- Procesos disciplinarios
- Cambios en beneficios o condiciones laborales

### Queda en los CEOs
- Aumentos y promociones (consultora asesora, CEOs deciden)
- Decisión final en contrataciones (ella lleva el proceso)
- Desvinculaciones (ella acompaña, CEOs deciden)

## Plan 90 días

| Período | Foco |
|---|---|
| Semanas 1–2 | Diagnóstico: entrevistas 1:1, relevamiento de procesos |
| Semanas 3–4 | Encuesta de clima, informe inicial con hallazgos |
| Mes 2 | Documentar políticas base (vacaciones, ausencias, home office) |
| Mes 3 | Primera evaluación de desempeño, plan de mejoras |

## Actividades que dejan de pasar por los CEOs

- Gestión de vacaciones y aprobaciones
- Registro de licencias (médicas, estudio, etc.)
- Recordatorios internos (cumpleaños, aniversarios)
- Primera contención en conflictos interpersonales
- Onboarding de nuevos ingresos

## Canal de comunicación

Los empleados contactan directamente a la consultora, no a los CEOs.
Se define un canal único (ej. Slack) para esa comunicación.

## Infraestructura RRHH armada (al 2026-05-16)

| Herramienta | Descripción |
|---|---|
| `equipo/` | 10 perfiles individuales con datos personales y perfil RRHH |
| [[alertas-gestion]] | Panel de señales de gestión por persona (callouts Obsidian) |
| [[cumpleanos]] | Calendario de cumpleaños con próximos 12 meses |
| `recordatorio-cumpleanos.sh` | Script cron — avisa 7 días antes de cada cumpleaños |
| Crontab sistema | `7 9 * * *` — corre diario, log en `recordatorios.log` |

## Ver también

- [[agenda-primera-reunion]]
- [[actividades-rrhh-it]]
- [[alertas-gestion]]
- [[cumpleanos]]
