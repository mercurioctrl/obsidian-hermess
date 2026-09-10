# fire

Tablet **Amazon Fire HD 10** (modelo `KFMUWI`, 11ª gen 2021, Fire OS / Android 9) usada como **kiosco fijo 24/7 para monitorear cámaras** con la app **gDMSS Plus** (Dahua).

Se administra por **ADB/USB** desde la PC (`hermess-pc`). Directorio del proyecto: `/var/www/fire`.

## Problema principal
Se apagaba y reencendía sola. Diagnóstico: **batería degradada (~50% de salud)** que colapsa bajo picos de consumo → apagado por protección → el USB/cargador la reenciende → ciclo. Ver [[diagnostico]].

## Notas
- [[diagnostico]] — Causa raíz de los apagones y evidencia de los logs.
- [[optimizaciones-adb]] — Todos los cambios ADB aplicados y **cómo revertir cada uno**.
- [[contexto]] — Caso de uso, decisiones y próximos pasos.

## Stack / herramientas
- **Dispositivo:** Fire HD 10 (KFMUWI), Fire OS 7 / Android 9, sin root.
- **App de cámaras:** gDMSS Plus — `com.mm.android.direct.gdmssphone` (Dahua).
- **Gestión:** ADB (`/home/hermess/Android/Sdk/platform-tools/adb`) por USB.

Última sincronización: 2026-09-10
