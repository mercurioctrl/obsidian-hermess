# Contexto — Desafío personal N950

## Origen del proyecto

El usuario recibió por donación un POS Newland N950 (MercadoPago Point Smart 2) con OS dañado. Originalmente intención: reflashear con OS funcional para reutilizar el hardware (impresora térmica + pantalla + batería) en una escuelita.

## Pivot — 2026-05-22

Después de agotar el vector software fastboot, el usuario decidió:

> "olvidate de la escuelita, ahora es un desafío personal. Documenta todo, guarda memoria y contexto, arquitectura y todo lo que consideres necesario para trabajar de forma más precisa y rápida en el futuro."

**Cambio de framing:** uso utilitario → desafío personal de reverse engineering / hacking hobby.

**Implicaciones:**
- Vale la pena explorar TODOS los vectores técnicos, no solo los rápidos
- Hardware (test points, chip-off, JTAG) está sobre la mesa si software no alcanza
- No hay deadline rígido — sesiones pueden ser largas y exploratorias
- Documentación exhaustiva crítica para retomar sesiones futuras eficientemente

## Restricciones técnicas

- **NO tenemos firmware FIRMADO** del N950 — todas las búsquedas exhaustivas dieron negativo
- **NO podemos obtenerlo por canales oficiales** (Newland no responde a particulares; programa developer NPT requiere acuerdo comercial)
- **Bootloader excepcionalmente blindado** — no es un Qualcomm vanilla, Newland sumó defense-in-depth
- **Anti-tamper SE presumido** — abrir el POS puede invalidar el SE (Secure Element)

## Decisiones acumuladas durante las sesiones

| Fecha | Decisión | Justificación |
|---|---|---|
| 2026-05-22 | Documentación completa antes de continuar | Sesiones largas, no querer re-investigar |
| 2026-05-22 | Crear fuzzer raw masivo en vez de probar 1-by-1 | Eficiencia para descartar definitivamente el namespace |
| 2026-05-22 | Vincular proyecto con bóveda Obsidian | Persistencia + grafo de conocimiento entre sesiones |
| 2026-05-23 | Estrategia chunks de fuzz visibles en vez de background | Usuario quería ver progreso en vivo |
| 2026-05-23 | Skipear `oem-nl` y `oem-mp` (redundantes con `oem-dev`) | Honestidad técnica vs cobertura exhaustiva |
| 2026-05-23 | Generar fake_boot.img propio en vez de buscar imagen real | Más rápido y suficiente para caracterizar verify |
| 2026-05-23 | Tirar Test C (300 MB) aunque resultado esperado fuera similar | Vale la pena confirmar comportamiento con imagen grande |

## Cosas que se intentaron y NO funcionaron (resumen para no repetir)

Ver [[vectores]] sección "agotados". Highlights:

- Búsqueda de firmware en 5+ idiomas en 10+ comunidades — nada
- Payment Product Tools v2.3.4 chino — no soporta N950
- Exploit Qualcomm GBL 2026 — chipset entry-level no tiene etapa GBL
- CVE-2023-42134 PAX — `oem paxassert` no existe
- Fuzz raw masivo 5.701 strings — 0 hits
- 5 experimentos de verify pipeline — todos rebotan en verify centralizado

## TODOs / próximos pasos

Ordenados por costo creciente y probabilidad decreciente:

1. **Inspección USB descriptors profunda** en download mode (`ioreg -p IOUSB -l` completo) — buscar interfaces alternativas no estándar
2. **Análisis estático bootloader bengal de otros vendors** (Nokia C20, Moto E20) — entender qué fields valida Newland vs hardware
3. **Buscar firmware en canales especializados privados** (Telegram POS modding, XDA semi-private) — único vector de obtener imagen firmada
4. **Email a Newland Payment Argentina** — pedir firmware como researcher (improbable pero gratis)
5. **Hardware: test points EDL** — abrir el POS, identificar test points, cortocircuitar para forzar EDL 9008. Riesgo anti-tamper SE
6. **eMMC chip-off** — soldar fuera el eMMC, dumpear con programador. Costo ~USD 300, alta dificultad técnica

## Ver también

- [[n950-research]] — índice
- [[arquitectura]] — qué descubrimos del hardware
- [[verify-pipeline]] — el último hallazgo
- [[vectores]] — exhaustivo de qué falta probar
- [[changelog]] — historial de sesiones
