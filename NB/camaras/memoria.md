# Memoria — CCTV MUGELLO

Contexto acumulado de las sesiones con Claude sobre el proyecto [[camaras]]. Ver también [[contexto]].

## Usuario

Dueño/responsable de **New Bytes – MUGELLO S.R.L.** (oficinas y depósitos). Valida presupuestos a fondo:
que las cuentas cierren, coherencia técnica, precios de mercado en Argentina y qué falta. Respuestas
concretas y accionables, en español.

## Proyecto

Revisión del presupuesto de CCTV de **C-Team Inc SRL** (~USD 19.645). Cuentas verificadas. Decisión de
subir cámaras a **4MP + audio**, lo que obliga a cambiar 2 NVR (2116HS→2216-4KS3) y recalcular discos.
Switches/PoE sobrados. Faltan UPS y confirmar puesta a tierra.

## Referencia técnica (verificada con datasheets)

- **NVR:** `NVR2116HS-S3` = 80 Mbps (se satura a 4MP) → cambiar. `NVR2216-4KS3` = 144 Mbps → se deja.
- **Switches:** `PFS4226-24ET-240` y `CS4226-24ET-240`, ambos PoE 24p 240W managed, uplinks gigabit.
- **Cámaras 4MP Dahua (Argentina):** general `HDW2449T-S-IL`/`HFW2449S-S-IL`; puerta `HDW3449H-AS-PV`
  (disuasión activa); varifocal `HFW3441T-ZAS` (2.7–13.5mm); recepción videoportero VTO.
- **Geometría rostro:** a 4m de altura, zona buena de caras a 5–9m; puerta de paso directo bajar a 2,2–2,5m.
- **Almacenamiento:** a 4MP ~2,6 TB/día (60 cám); 30 días ≈ 75–80 TB.

## Pendientes

Definir días de retención (discos), dimensionar UPS por rack, contar puertas por tipo, confirmar con C-Team
(distribución de switches, interconexión de racks, VLAN, garantía).
