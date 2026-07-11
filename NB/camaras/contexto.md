# Contexto — CCTV MUGELLO

Revisión del presupuesto de **C-Team Inc SRL** para instalar CCTV en oficinas y depósitos de
**MUGELLO S.R.L.** (7 ubicaciones/racks). Ver índice: [[camaras]] · datos técnicos en [[memoria]].

## Presupuesto original (proformas C-Team, jun-2026)

- **Productos:** USD 13.848,58 (TC billete Nación 1.318,78) ≈ $18,26M ARS. Cuentas **verificadas, cierran**.
- **Mano de obra:** $7.643.717,08 ARS (≈ 30% del total).
- **Total proyecto:** ≈ **USD 19.645 / ~$25,9M ARS**.
- **Base original:** 60 cámaras 2MP (HDW1239), 4 NVR (2×2116HS-S3 + 2×2216-4KS3), 14 switches PoE
  (7 CS4226 + 7 PFS4226), 4×4TB SkyHawk, 7 racks 6U + 7 canales de tensión, cable CAT6.

## Decisión: subir cámaras a 4MP + audio

Esto obliga a tres cambios en el presupuesto:

1. **Cámaras nuevas (Dahua 4MP, PoE, IP67, se consiguen en Argentina):**
   - General: `IPC-HDW2449T-S-IL` (domo) / `IPC-HFW2449S-S-IL` (bullet exterior). Full-color + mic.
   - Puerta (default): `IPC-HDW3449H-AS-PV` — starlight + mic + **disuasión activa** (sirena/luz).
   - Portón/varifocal: `IPC-HFW3441T-ZAS` (2.7–13.5mm motorizada, starlight, IR40m).
   - Recepción: videoportero IP **VTO** (audio 2 vías + facial opcional).
2. **NVR:** reemplazar 2× `NVR2116HS-S3` (80 Mbps, se saturan a 4MP) → 2× `NVR2216-4KS3` (144 Mbps).
3. **Discos:** recalcular. A 4MP el consumo se duplica (~2,6 TB/día); 16TB actuales ≈ 6 días; 30 días ≈ 75–80 TB.

## Verificado: switches y PoE quedan SOBRADOS

Ambos switches son PoE 24p **240W** managed. Cámaras 4MP ~6–7W, puerta ~10–11W → 24 cám ≈ 168W < 240W
(peor caso 70%; real ~30%). Puertos 100Mbps + uplink gigabit → caudal sobrado. Sirven para VLAN de CCTV.
**No hay que tocar nada de switches/PoE/tensión por pasar a 4MP.** Incluso parece haber switches de más
(14 PoE / 336 puertos para ~65 cámaras).

## Pendientes / faltantes detectados

- ⚠️ **UPS por rack** — no está presupuestado; sin él, un corte deja sin grabación. Dimensionar VA/autonomía.
- ⚠️ **Puesta a tierra** — la RMA de Dahua la exige; confirmar en cada rack.
- ⚠️ **Garantía 6 meses** (de C-Team, no de fábrica) — corta para CCTV; negociar.
- ⚠️ **VLAN separada** para CCTV — verificar que la mano de obra la incluya (no agrega APs, son cableadas PoE).
- ⚠️ **Interconexión de los 7 racks** — confirmar mismo predio (cable/fibra) o edificios separados (¿fibra/PtP?).

## Nota técnica: altura vs captura de rostro

Para identificar caras (~250 px/m) la resolución 4MP + varifocal da de sobra; el limitante es el **ángulo**.
Cámara a **4m** → zona buena de caras a **5–9m** de distancia (ángulo ≤30°, ideal ~15°). Justo debajo/<3m se ve
la coronilla. Puerta de paso directo: bajar a **2,2–2,5m** o montar enfrentada. Acceso con recorrido: 4m + zoom OK.

## Próximos pasos

1. Definir **días de retención** → calcular discos/TB.
2. Dimensionar **UPS por rack**.
3. Contar **puertas/accesos** por tipo (peatonal/portón/recepción) → desglose de modelos de puerta.
4. Confirmar con C-Team: distribución de switches, interconexión de racks, VLAN, garantía.
