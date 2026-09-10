# contexto

Contexto del proyecto [[fire]] (no es código; es administración de un dispositivo físico).

## Caso de uso
- Tablet **Fire HD 10 (KFMUWI)** montada **fija, siempre enchufada**, como pantalla para **visualizar cámaras** de videovigilancia.
- App: **gDMSS Plus** (Dahua), no Hikvision como se pensó al inicio — los paquetes `com.mm.android.*` son de Dahua.
- Se administra por **ADB/USB** desde `hermess-pc`.

## Decisiones tomadas (2026-09-10)
- Mantener **solo gDMSS Plus** como app de cámaras; se desactivaron las otras 5 apps de CCTV instaladas.
- Se desactivaron apps personales (Rappi, PedidosYa, AirMirror, Chromecast) por no ser necesarias en un kiosco.
- Brillo llevado a 75% por pedido del usuario (aunque 27% ahorraba más calor).
- No rootear la tablet (equipo en producción).

## Aprendizajes / cosas que NO se pueden
- **No se puede** hacer que tome corriente directa sin pasar por la batería vía software: Fire sin root no expone bypass de power-path ni control de carga (no hay nodos `input_suspend`/`charging_enabled` en sysfs).
- El bloatware core de Amazon **no se desactiva sin root** (solo se puede estrangular).

## Próximos pasos
1. **Batería dummy / eliminator** para el modelo KFMUWI (solución de fondo del ciclo de apagados).
2. Mientras tanto: **smart plug** con carga cíclica 40–80% + buena ventilación.
3. Configurar cámaras en **substream/SD** dentro de gDMSS para bajar CPU/calor en tiempo real.

## Ver también
- [[fire]]
- [[diagnostico]]
- [[optimizaciones-adb]]
