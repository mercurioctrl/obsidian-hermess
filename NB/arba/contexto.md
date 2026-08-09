# Contexto

## Rol fiscal

- **Agente de recaudación** de IIBB (Ingresos Brutos) — Provincia de Buenos Aires
- Razón social: **NB DISTRIBUIDORA MAYORISTA** · CUIT `30-70924663-8`
- Presenta DDJJ periódicas de percepciones por la vía web de ARBA
- Método habitual: **devengado mensual** (actividad `D7`)

## Reglas de negocio / advertencias

- **El nombre del archivo fuente NO define el período.** El sistema contable lo nombra con el mes de exportación (ej. `202607`) pero el contenido puede ser de otro mes. Siempre verificar las fechas **dentro** del archivo y usar el período real en `--periodo`.
- **Notas de crédito** (tipo `C`): importes negativos → es correcto según el diseño ARBA.
- **Hash MD5**: se calcula sobre el ZIP completo. Si se modifica el ZIP después de generarlo, el hash deja de servir y ARBA lo rechaza por "Error de integridad".
- **No se pueden subir lotes** si hay operaciones rechazadas pendientes del lote anterior.
- **Alícuotas**: la fuente de verdad es el padrón de ARBA, no el sistema contable. Ver [[proceso-correccion-padron]].

## Decisiones tomadas

- **2026-08-06** — Ante CUIT que el padrón marca a 0%, se decidió **quitar esas líneas del lote** (no informarlas en 0). El reintegro al cliente, si ya se le cobró, se gestiona por contabilidad aparte.
- El lote corregido se resube como **nuevo número de lote** con el archivo completo (criterio de junio 2026).

## Ver también

- [[arba]]
- [[arquitectura]]
- [[memoria]]
