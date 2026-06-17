# Changelog

## 2026-06-16

- feat: Herramienta `validar_emails.py` para validar/clasificar la base de Brevo
  (~231k contactos de New Bytes). Normalización, sintaxis, descartables, typos,
  DNS paralelo y clasificación.
- feat: Verificación DNS con resolvers públicos (8.8.8.8/1.1.1.1) y caché por dominio
  para evitar rate-limiting del ISP.
- change: Se descartó la corrección automática de emails. A pedido del usuario, los
  emails malos (typos incluidos) se entregan **sin corregir** en una lista de bloqueo.
  Ver [[contexto]] y [[arquitectura]].
- fix: Bug del corrector difuso que escondía descartables (`yopmail.com` → `hotmail.com`).
  Solución: guarda de "misma primera letra" en `is_typo_domain`. Los descartables
  volvieron de 99 → 163.
- feat: Listas de salida `validos.csv`, `riesgosos.csv`, `bloquear.csv`
  (+ `bloquear_solo_emails.csv`) y `summary.json`.

**Resultado final:** 226.113 válidos + 5.114 a bloquear (incluidos los 1.741 `sin_mx`
que el usuario decidió sumar al bloqueo).

Archivos principales: `validar_emails.py`, `salida/bloquear.csv`, `salida/validos.csv`, `README.md`
