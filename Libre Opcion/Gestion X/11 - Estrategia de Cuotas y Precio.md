---
tipo: estrategia
proyecto: LibreOpción
area: Finanzas / Pricing
estado: decidido
creado: 2026-06-02
tags:
  - libreopcion
  - cuotas
  - pricing
  - financiacion
  - margen
---

# 11 · Estrategia de Cuotas y Precio

> [!abstract] Resumen
> Las cuotas son **la herida #1** de conversión (explican el −70% producto→carrito de mayo 2026). Hoy LibreOpción ofrece **máximo 6 cuotas y CON interés** (3 = +15%, 6 = +24%), mientras Compra Gamer ofrece **24 sin interés en el 100%** (ver [[09 - Estudio de Catálogo - Compra Gamer]]). Igualar esto es el **piso para competir**, no la jugada para ganar.

## El problema, con números

- Medio de pago hoy: **100% Mercado Pago**, recargo estándar, **sin acuerdos con bancos**.
- Margen bruto actual: **17%** (`grilla_ventas.csv`, mayo 2026).
- Costo de bancar sin interés por MP: ~6% (3 cuotas) · ~11–13% (6) · ~20%+ (12).

> [!danger] La matemática que prohíbe comerse las cuotas
> Con **17% de margen**, bancar **6 cuotas sin interés** de tu bolsillo (~11–13%) te deja 4–6% bruto — y de ahí todavía sale el **envío gratis** y la operación. **Te deja en pérdida.** Comerse el sin interés en todo el catálogo es matemáticamente imposible a 17%.

## Getnet como adquirente alternativo

Investigado el 2026-06-06. Tarifas oficiales: [getnet.com.ar/aranceles](https://www.getnet.com.ar/aranceles)

### Aranceles base Getnet

| Medio | Acreditación estándar |
|---|---|
| QR (dinero en cuenta) | 0,80% + IVA |
| Débito | Hasta 1% + IVA (1 día hábil) |
| Crédito 1 pago | **Hasta 2% + IVA** (8 días hábiles) |
| Crédito cuotas | **Hasta 2% + IVA** (2 días hábiles) |

> El arancel base de crédito 1 pago es **significativamente más barato que MP** (~3-4%).

### Plan Cuotas Getnet — diferencia estructural clave

**El interés lo paga el cliente, no el comercio.** La TNA se suma al precio de cada cuota.

| Cuotas | TNA |
|---|---|
| 2 | 8,60% |
| 3 | 11,36% |
| 4 | 14,01% |
| 6 | 18,99% |
| 9 | 27,04% |
| 12 | 33,23% |
| 18 | 43,53% |
| 24 | 51,65% |

### Plan Cuotas MiPyME (Getnet)

Solo 3 y 6 cuotas, para rubros habilitados. Tasas: **7,36% (3c) · 13,82% (6c)**. Verificar si el rubro tech/importación califica.

### Getnet vs Mercado Pago — comparativa

| | Getnet | Mercado Pago |
|---|---|---|
| **Quién paga el interés en cuotas** | El **cliente** | El **comercio** |
| **6 cuotas** | 18,99% TNA → el comprador paga más | ~11-13% → vos lo absorbés |
| **12 cuotas** | 33,23% TNA → el comprador paga más | ~20%+ → vos lo absorbés |
| **Sin interés** | No existe en plan estándar | Sí, pero sale de tu margen |
| **Arancel crédito 1 pago** | ~2% | ~3-4% |

> [!tip] Combinación óptima tentativa
> - **Getnet** para 1 pago y débito (arancel más bajo).
> - **MP** para promos subsidiadas por marca (sin interés que paga AMD/ASUS/etc.) — el "oro" sigue siendo MP en ese caso.
> - En líneas propias/importadas donde fijás precio: Getnet en cuotas (el costo va al cliente) o meter el interés en el precio.

## Por qué "acordar con bancos a lo bestia" no alcanza (todavía)

A ~USD 161k de GMV/mes no hay volumen para que un banco arme una promo a medida. Las vías reales, por poder:

| Vía | Costo para el comercio | Realidad para LibreOpción |
|---|---|---|
| **Promos MP subsidiadas por marca** ("24 sin interés", +300 marcas) | **~0%** (paga la marca/MP) | ✅ El oro. Aplica a **mainstream** (AMD, ASUS, Samsung). |
| **Meter el costo en el precio** | Sale del margen ampliado | ✅ Base, sobre todo en **líneas exclusivas/importadas** (vos fijás el precio). |
| **Getnet Plan Cuotas** | El cliente paga el interés (TNA 8,60%–51,65%) | ✅ Sin costo para el comercio. Útil en exclusivas. |
| **Getnet MiPyME** | 7,36% (3c) · 13,82% (6c) | ⚠️ Verificar si el rubro califica. |
| **Cuota Simple** (programa nacional) | 5,41% (3) · 10,31% (6) | ⚠️ Casi seguro **no calificás**: exige producción nacional y vos importás. |
| **Bancos / adquirentes** | Variable | 🟡 Relación a futuro. Getnet es el primer paso concreto. |

## 🎁 El "aire" de precio — análisis actualizado (2026-06-06)

### Caso 1: Auricular Genius (dato original)
LibreOpción **$22.257** vs. competencia **~$26.000** → **~14% más barato**. En este caso sí existe "aire" para meter el costo.

### Caso 2: AMD Ryzen 7 5700G — el aire NO existe ⚠️

Relevamiento real contra CompraGamer:

| | CompraGamer | LibreOpción |
|---|---|---|
| Precio contado estimado | ~$270.000–$290.000 | **$304.531** |
| 6 cuotas (Modo + Supervielle/Comafi/ICBC) | **$318.264** (6×$53.044) | — |
| 6 cuotas (resto de bancos) | $350.724 (6×$58.454) | — |
| 6 cuotas actuales | — | **$377.616** (6×$62.936) |
| 12 cuotas | $390.036 (12×$32.503) | — |

LibreOpción es **más cara en precio base** Y tiene **peores cuotas** — el peor escenario posible.

Si LibreOpción aplica "meter el costo en el precio" para ofrecer 6 cuotas sin interés:
- Precio ajustado: $304.531 × 1,1624 = **~$353.900**
- Cuota resultante: **~$58.983/mes**
- Resultado: similar a CompraGamer con banco común, pero **todavía 11% más caro** que su mejor opción ($53.044).

> [!danger] Revisión de la hipótesis original
> El "aire de precio" **no es universal**. Existe en algunas líneas (Genius) pero no en mainstream (AMD). En productos competidos el problema no es la estrategia de precio sino el acceso a **promos bancarias subsidiadas** que CompraGamer ya tiene (Supervielle, Comafi, ICBC vía MODO).

> [!tip] La palanca real en mainstream
> No subir el precio — **sumarse a las promos bancarias** que ya existen (banco paga el sin interés, costo 0 para el comercio). Esto es lo mismo que las promos MP subsidiadas por marca, pero del lado del banco.

## Decisión (2026-06-02): tres palancas combinadas

1. **Meter el costo en el precio** — palanca base, sobre todo en exclusivas/importadas.
2. **Que paguen las marcas** — sumarse a promos MP subsidiadas; co-funding directo. Aplica al mainstream. Se conecta con la idea de **retail media** ([[03 - Hoja de Ruta - Fase 2 Rentabilización y Profundidad]]).
3. **Negociar con bancos igual** — arrancar el proceso aunque sea chico, para construir relación y volumen futuros.

*(Se descartó el "sin interés selectivo" como eje: se busca sin interés amplio.)*

## Consecuencia estratégica

Meter el costo en el precio = **abandonar la bandera de "el más barato"**. Eso obliga al [[10 - Reposicionamiento - De Precio a Confianza|reposicionamiento]]: el precio baja a "competitivo" y la **confianza (garantía)** toma la punta de lanza.

## Pendientes

- [ ] Segmentar el catálogo: productos donde hay "aire" (exclusivas/importadas) vs. productos mainstream donde no lo hay — estrategia diferente para cada segmento.
- [ ] En mainstream (AMD, etc.): investigar cómo acceder a promos bancarias (Supervielle, Comafi, ICBC vía MODO) igual que CompraGamer.
- [ ] Activar cuotas sin interés en MP (definir hasta cuántas) y medir impacto en conversión.
- [ ] Mapear qué marcas mainstream del catálogo tienen promo MP subsidiada disponible.
- [ ] Iniciar conversaciones con Getnet (adquirente concreto, más barato que MP en 1 pago).
- [ ] Evaluar usar Getnet para 1 pago/débito + MP solo para promos de marca.
- [ ] **Tramitar Certificado MiPyME** en AFIP (24hs, renovación automática). Vale por sí solo: IVA a 90 días, compensación impuesto al cheque, contribuciones patronales diferenciales.
- [ ] Una vez obtenido el certificado: verificar si el rubro (importador/revendedor tech) está habilitado para Plan Cuotas MiPyME en Payway y Getnet.
- [ ] Si califica MiPyME: activar en Payway (desde Mi Payway) — tasas 6,91% (3c) y 13,52% (6c), con opción de pasarle el costo al cliente via coeficiente.

## Enlaces

- [[10 - Reposicionamiento - De Precio a Confianza]]
- [[09 - Estudio de Catálogo - Compra Gamer]]
- [[Informe Diagnostico Conversion - Mayo 2026]]
- [[00 - Índice Gestión X]]
</content>
