# Memoria

Contexto acumulado de las sesiones con Claude sobre este proyecto.
Sincronizado desde `~/.claude/projects/-home-hermess-Descargas-brevo/memory/`.

## Proyecto

Base exportada de Brevo (~231.227 contactos de New Bytes) que Brevo pidió limpiar
para no perder reputación. Herramienta local Python `validar_emails.py`. Resultado:
**226.113 válidos + 5.114 a bloquear**. Listas en `salida/`.

Pendiente posible: reintento de reconfirmación DNS para estabilizar `a_only`/`no_dns`
entre corridas.

## Feedback / preferencias del usuario

- **No corregir emails automáticamente.** Los emails malos (typos incluidos) van a una
  lista de bloqueo en su **forma original**, no se reescriben.
  - *Por qué:* corregir y reimportar deja duplicados fantasma en Brevo; un corrector
    difuso agresivo escondía descartables (yopmail→hotmail).
  - *Cómo aplicar:* la detección de typos sólo MARCA (`is_typo_domain`), con guarda de
    "misma primera letra" para evitar falsos positivos.

## Ver también
- [[contexto]] · [[arquitectura]] · [[limpieza-contactos-brevo]]
