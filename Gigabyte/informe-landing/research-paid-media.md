# Research & Estrategia — Paid Media GIGABYTE (Familia GIGA40)

Dossier de investigación y estrategia para el pitch de paid media centralizado (Google Ads + Meta Ads) de GIGABYTE/AORUS con resellers en **AR / CL / UY**. Cada afirmación lleva su **fuente accesible (URL)** y el **razonamiento** explícito. Lo que no es verificable públicamente está marcado como tal, con el método para obtenerlo. Base para nutrir el deck [[informe-landing]] y la [[landing-ejemplo-ads]].

> **Fecha del research:** 2026-07-16. Los benchmarks y fechas comerciales cambian; revalidar antes de presentar.

---

## 0. Cómo leer este dossier (niveles de confianza)

- **[VERIFICADO]** — dato con fuente pública citada y accesible.
- **[REQUIERE CONSULTA]** — no es público por fetch; se da el método exacto para obtenerlo (Ad Library, Keyword Planner, analytics del reseller).
- **[ESTABLECIDO]** — documentado en fuente oficial de Google/Meta.
- **[RECOMENDACIÓN]** — práctica de industria de fuente reputada (no doctrina oficial).

**Regla de honestidad:** no se reporta ningún monto de inversión de competidores ni volumen de búsqueda absoluto, porque **no son públicos** para hardware gamer. Se documenta cómo obtenerlos.

---

## 1. Competencia (Meta Ads + Google Ads en AR/CL/UY)

### Hallazgo metodológico central
La **Biblioteca de Anuncios de Meta** (`facebook.com/ads/library`) y el **Centro de Transparencia de Google Ads** (`adstransparency.google.com`) son **apps JS-render: no se scrapean por fetch** (verificado — devuelven solo el header). El inventario exacto de anuncios activos, fechas y creatividades **[REQUIERE CONSULTA manual]**, país por país. La Ad Library API solo devuelve anuncios **políticos/sociales** en LATAM → inútil para comerciales.
Fuente: [transparency.meta.com/researchtools](https://transparency.meta.com/researchtools/ad-library-tools/) · [Google Ads Transparency help](https://support.google.com/adspolicy/answer/13733850?hl=en)

### Qué SÍ es público (para la auditoría manual)
- **Meta:** creatividad, texto, CTA, Página, plataformas, **fecha de inicio**, activo/inactivo, variantes A/B. NO: gasto/performance (solo en anuncios políticos). Los comerciales **desaparecen al pausarse** (sin archivo histórico).
- **Google:** anunciante, ubicación, histórico por período, filtro por fecha y región, formatos (Search/Display/Gmail/YouTube), verificación. NO: gasto (solo político).

### Hallazgos verificables
- **[VERIFICADO]** ROG/ASUS fija el estándar creativo: **video vertical corto + UGC + mecánica de hashtag** (#ROGWorthTheUpgrade, tag @asusrog). Fuente: [rog.asus.com/latin](https://rog.asus.com/latin/) · [ROG OLED](https://rog.asus.com/latin/content/best-oled-gaming-monitor/)
- **[VERIFICADO]** MSI opera cuentas locales por país (paid social geolocalizado): [MSI Argentina FB](https://www.facebook.com/MSIArgentina/), [@msigaming_latam](https://www.instagram.com/msigaming_latam/), [@msigaming_chile](https://www.instagram.com/msigaming_chile/).
- **[VERIFICADO]** El mensaje dominante del retail gamer en AR es **financiación (cuotas sin interés) + % OFF atado a Hot Sale / CyberMonday**, no specs de marca. Fuente: [CyberMonday AR](https://www.cybermonday.com.ar/) · [fhgamer CM 2025](https://fhgamer.ar/ofertas-cyber-monday-gamer-2025/) · [Hot Sale gaming](https://pressover.news/articulos/hot-sale-en-argentina-del-30-de-mayo-al-2-de-junio/)
- **[VERIFICADO]** GIGABYTE/AORUS es jugador establecido en el Cono Sur desde 2017, con AR+UY como unidad comercial y distribución oficial (Newbytes, Air Computers) → habilita co-op marketing. Fuente: [AORUS AR launch](https://tecnogaming.com/la-marca-aorus-desembarca-argentina/) · [Newbytes AORUS](https://www.nb.com.ar/AORUS)
- **[VERIFICADO]** En VGA, el "aire" publicitario lo empujan **AIBs vía distribuidores/retailers**, no las marcas directo. Los AIBs chicos (Zotac, Palit, PowerColor, XFX, Gainward) raramente pautan directo **[REQUIERE CONSULTA para confirmar]**.

### Implicancias estratégicas
1. **Competir en el terreno del mensaje real:** financiación + calendario, con branding AORUS (co-op con Newbytes/retailers) para que el reseller no se lleve todo el crédito de marca.
2. **Subir el piso creativo a video corto/UGC** (Reels/Shorts), sobre todo monitores (mostrar panel/refresh) y watercooling (producto en acción) — donde AORUS tiene diferencial visual. Correr solo estáticas queda atrás del estándar ROG.
3. **Auditar antes de presupuestar:** correr la auditoría manual (§Anexo A) sobre ASUS ROG, MSI, Acer, Lenovo y distribuidores, país por país, para medir share-of-voice real.
4. **Uruguay = espacio en blanco:** GIGABYTE ya trata AR+UY como unidad, pero el marketing visible se concentra en AR/CL. Si la auditoría confirma baja densidad en UY, es liderazgo de voz barato.

---

## 2. Demanda de búsqueda y estacionalidad

### Terminología por país (afecta directo los grupos de anuncios y el copy)
Evidencia = cómo nombran la categoría los propios retailers/fabricantes de cada país (proxy fuerte de la búsqueda; cuantificar con §Anexo B).

| Concepto | 🇦🇷 Argentina | 🇨🇱 Chile | 🇺🇾 Uruguay | Evidencia |
|---|---|---|---|---|
| GPU | **placa de video** | **tarjeta gráfica / tarjeta de video** | *sin dato público* (probable "placa de video") | Alta (AR/CL) · Nula (UY) |
| Motherboard | **placa madre** + motherboard | **motherboard** + placa madre | *sin dato público* | Media · Nula (UY) |
| Resto (PC, monitor, notebook, fuente, watercooler) | términos asumidos | ídem | ídem | Baja (validar) |

- **[VERIFICADO]** CL usa "tarjeta gráfica/de video": [PCFactory](https://www.pcfactory.cl/tarjetas-graficas-nvidia?categoria=378), [SP Digital](https://www.spdigital.cl/categories/view/379), [SoloTodo](https://www.solotodo.cl/tarjetas_de_video), y el propio [GIGABYTE Chile](https://www.gigabyte.com/cl/Graphics-Card/GeForce-RTX%E2%84%A2-50-Series).
- **[VERIFICADO]** AR usa "placa de video": [Maldito Hard](https://www.malditohard.com.ar/placasdevideo/), [CompraGamer](https://compragamer.com/productos?cate=6).
- **⚠️ Mismatch de copy:** [GIGABYTE Argentina](https://www.gigabyte.com/ar/Graphics-Card) titula "Tarjetas de Video" — desalineado con el usuario argentino que busca "placa de video". **Oportunidad de copy** (usar el término local en los anuncios, como ya hace la [[landing-ejemplo-ads]]).
- **UY sin evidencia pública** → correr Trends geo=UY explícitamente antes de decidir términos.

### Estacionalidad — NO se puede unificar en un calendario LATAM
| Mes | 🇦🇷 AR | 🇨🇱 CL | 🇺🇾 UY |
|---|---|---|---|
| Marzo | Back-to-school | Vuelta a clases | Vuelta a clases |
| Mayo | **Hot Sale (CACE)** | — | — |
| Junio | — | **CyberDay (CCS)** | **CIBERLUNES (CEDU)** |
| Octubre | — | **CyberMonday (CCS)** | — |
| Noviembre | **CyberMonday (CACE)** + Black Friday | Black Friday | **CIBERLUNES (CEDU)** |
| Diciembre | Navidad | Navidad | Navidad |

Fuentes: [CACE Hot Sale](https://cace.org.ar/pages/hot-sale) · [CACE CyberMonday](https://cace.org.ar/pages/cybermonday) · [CyberDay CL](https://enviame.io/cuando-es-el-cyber-day/) · [CEDU Ciberlunes UY](https://www.cedu.org.uy/ciberlunes/)
**Implicancia:** presupuesto por país por separado; los picos NO coinciden (Hot Sale AR mayo vs CyberDay CL junio).

- **[VERIFICADO]** Los lanzamientos RTX 50 (Blackwell) fueron un driver **escalonado** ene–jul 2025 (5090/5080 ene, 5070 mar, 5060 may, **5050 GIGABYTE 1-jul**). Cada uno genera spike de "modelo específico" (ej. "rtx 5070 gigabyte") → campañas siempre-activas con ajuste de pujas. Fuente: [NVIDIA 5090/5080](https://www.nvidia.com/en-us/geforce/news/rtx-5090-5080-out-now/) · [GIGABYTE RTX 5050](https://www.gigabyte.com/Press/News/2301)
- **[VERIFICADO]** "TI/electrónica" es la 3ª categoría por facturación del e-commerce AR (Estudio Anual CACE 2024/2025) — señal de tamaño, no de volumen de keyword. Fuente: [CACE 2024](https://cace.org.ar/blogs/news/estudio-anual-de-cace-2024-el-ecommerce-en-argentina-alcanzo-los-22-billones-en-facturacion)

---

## 3. Benchmarks (para setear expectativas realistas)

⚠️ La mayoría de benchmarks públicos son **US/global** (WordStream, Store Growers, Triple Whale). La data LATAM/AR granular por rubro está en **Statista (paywall)**. Los anclajes AR abiertos vienen de un **agregador (AdAmigo)** → orden de magnitud, no número exacto.

### Google Ads (e-commerce, US/global salvo aclaración)
| Métrica | Rango | Fuente |
|---|---|---|
| CPC Search ecom | ~US$1.16–2.69 | [Store Growers](https://www.storegrowers.com/google-ads-benchmarks/) |
| CPC Shopping ecom | ~US$0.63–0.66 | [Store Growers](https://www.storegrowers.com/google-ads-benchmarks/) |
| CVR Search / Shopping | 2.81% / 1.91% | [Store Growers](https://www.storegrowers.com/google-ads-benchmarks/) |
| ROAS ecom | ~2.96–3.68x | [Store Growers](https://www.storegrowers.com/shopping-ads-benchmarks/) |
| CPC electrónica **AR** = el más bajo del país | valor exacto **paywall** | [Statista AR](https://www.statista.com/statistics/1402572/search-advertising-cpc-argentina/) |

### Meta Ads
| Métrica | Rango | Región | Fuente |
|---|---|---|---|
| CPM ecom | US$13.48–16.80 | US/global | [Triple Whale](https://www.triplewhale.com/blog/facebook-ads-benchmarks) |
| CVR compra (electrónica = la más baja) | ~1.20% | US/global | [Triple Whale](https://www.triplewhale.com/blog/facebook-ads-benchmarks) |
| ROAS ecom (mediana) | ~1.93x | US/global | [Triple Whale](https://www.triplewhale.com/blog/facebook-ads-benchmarks) |
| **CPM Argentina** | **~US$3.80** (3.00–4.80) | AR | [AdAmigo](https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026) |
| **CPC Argentina** | **~US$0.38** | AR | [AdAmigo](https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026) |
| CPM referencia US / Global | ~US$23 / ~US$6.59 | US/Global | [AdAmigo](https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026) |

### Regla de ajuste US → AR
- **Costos (CPC/CPM/CPA):** ajustar **fuerte a la baja** (CPM Meta AR ≈ 1/6 del US).
- **CTR:** comparable (depende de creativo/segmentación).
- **CVR/ROAS:** trasladar con cautela (dependen de producto/precio/funnel, no de geo). **Electrónica = peor CVR y mayor CPA** (ticket alto, ciclo largo, comparación de precio).

### Expectativas por presupuesto (ilustrativo, anclas AR reales + CVR electrónica US como proxy conservador)
Con Meta AR CPC ~US$0.38 y CVR ~1.2%:
| Presupuesto/mes | Clics aprox | Conversiones aprox |
|---|---|---|
| US$270 | ~700 | ~8 |
| US$500 | ~1.300 | ~16 |
| US$1.000 | ~2.600 | ~31 |

**Conclusiones:**
1. El **cuello de botella son las conversiones**, no los clics. Con presupuestos chicos la muestra es ruidosa → el aprendizaje del algoritmo exige **meses, no semanas**.
2. En **US$270 conviene 1 objetivo**, no un funnel completo (~71.000 impresiones/mes en Meta = una audiencia/mensaje). El escalón **US$500→1.000** recién permite separar prospecting de retargeting.
3. Electrónica es el rubro más duro: **ROAS objetivo realista ~2–3x** (Shopping/Search de marca rinde mejor que prospecting frío). No prometer 5x+ en frío con US$270.
4. En Hot Sale/CyberMonday/Q4 los CPC suben ~30–35% y CPM ~25–66%. Comunicar en **rangos con banda de error** y recalibrar con data propia del 1er trimestre.

---

## 4. Estrategia de canales (por qué "mismo peso")

Razonamiento de fondo: **demand capture vs demand generation**. Google intercepta intención que YA existe; Meta la crea. Complementarios, no redundantes → por eso presupuesto parejo.

| Canal | Rol | Evidencia oficial | Fuente | Estatus |
|---|---|---|---|---|
| Google Search | **CAPTURA** | "reach customers at the exact moment they are looking… ready to make a purchase" | [Google Ads Search](https://business.google.com/en-all/ad-solutions/search/) | [ESTABLECIDO] |
| Google Shopping | **CAPTURA** (muestra foto/precio/**tienda del reseller**) | dispara con búsqueda de producto | [Google Ads Help](https://support.google.com/google-ads/answer/2454022?hl=en) | [ESTABLECIDO] |
| Performance Max | **CAPTURA/rendimiento** (goal-based, optimiza conversión) | "goal-based… conversions or conversion value" | [Google PMax](https://support.google.com/google-ads/answer/10724817?hl=en) | [ESTABLECIDO] |
| Google Demand Gen | **GENERACIÓN dentro de Google** | "reach new users… even if they aren't actively searching yet" | [Google Demand Gen](https://support.google.com/google-ads/answer/13695777?hl=en) | [ESTABLECIDO] |
| Meta (Feed/Stories/Reels) | **GENERACIÓN / full-funnel** | Awareness optimiza "reach and ad recall lift" | [Meta objectives](https://www.facebook.com/business/help/1438417719786914) | [ESTABLECIDO] |

**Por qué mismo peso:** Search/Shopping/PMax tienen **techo finito** (la gente que ya busca). Para crecer hay que **crear** demanda → Meta (y Demand Gen). Capturar sin generar se estanca; generar sin capturar desperdicia la intención. Fuente del límite estructural: [Search Engine Land](https://searchengineland.com/why-search-shopping-ads-stop-scaling-without-demand-467961) [RECOMENDACIÓN].

### Mapa de funnel (etapa → objetivo → formato → KPI → plataforma)
| Etapa | Plataforma | Objetivo | Formato | KPI |
|---|---|---|---|---|
| Awareness | Meta | Awareness | Reels, Stories, Video | Alcance, CPM, frecuencia, ad recall |
| Awareness | Google | Demand Gen | YouTube/Shorts, Discover, Gmail | Alcance, CPM, views |
| Consideración | Meta | Traffic/Engagement | Carrusel, Collection | CTR, CPC, LP views |
| Consideración | Google | Search no-brand | Search text | CTR, CPC, impression share |
| Conversión | Meta | Sales (Advantage+/Catálogo) | DPA, retargeting | CVR, CPA, ROAS |
| Conversión | Google | Shopping + PMax + Search marca | Shopping, PMax | CVR, CPA, ROAS |

**Nota reseller:** la conversión ocurre en el **sitio del reseller** (fuera del dominio de la marca) → la atribución por clic se rompe → medir por lift (§5).

---

## 5. Medición, KPIs y atribución

### KPIs por etapa
- Arriba: CPM, alcance, frecuencia, ad recall lift.
- Medio: CTR, CPC, coste por lead.
- Abajo: CVR, CPA, **ROAS**.

### Infraestructura
- **Google tag + GTM server-side + Consent Mode** (controla el comportamiento de tags según consentimiento). Fuente: [Consent mode](https://developers.google.com/tag-platform/security/concepts/consent-mode) · [server-side](https://developers.google.com/tag-platform/tag-manager/server-side/consent-mode) [ESTABLECIDO]. → Conecta con los 5 escenarios GTM del deck [[informe-landing]].

### Por qué last-click subestima a Meta (punto central del pitch)
- Google mismo abandona last-click: la atribución data-driven "calcula la contribución real de cada interacción". Fuente: [Google DDA](https://support.google.com/google-ads/answer/6394265?hl=en) [ESTABLECIDO].
- Meta hace demand-gen (toque temprano, sin clic, conversión días después en el reseller) → last-click acredita esas ventas al último clic (Brand Search/retargeting de Google) → **subvalúa el upper-funnel** [RECOMENDACIÓN].

### Incrementalidad / geo-lift (el árbitro correcto del reparto Google/Meta)
- **Meta Conversion Lift:** RCT test vs control, mide "el impacto incremental real". Fuente: [Meta Conversion Lift](https://www.facebook.com/business/measurement/conversion-lift) [ESTABLECIDO].
- **Google Conversion Lift geo-based:** separa regiones comparables, mide "el ROI incremental no atribuido". Fuente: [Google geo-lift](https://support.google.com/google-ads/answer/14097193?hl=en) [ESTABLECIDO].
- **Recomendación:** como (1) la conversión ocurre en resellers, (2) Meta genera demanda invisible a last-click y (3) LATAM permite separar mercados limpiamente → el **geo-lift es el método natural** para asignar el peso real entre canales y no sub-financiar la generación de demanda.

---

## 6. Próximos pasos (para cerrar las brechas de datos)

1. **Auditoría manual de competencia** (§Anexo A) — Ad Library de Meta + Transparencia de Google, país por país, sobre ASUS ROG, MSI, Acer, Lenovo, distribuidores. Salida: share-of-voice y huecos.
2. **Números duros de demanda** (§Anexo B) — Google Trends (relativo/estacional, gratis) + Keyword Planner (volumen absoluto + CPC, requiere cuenta Ads) por país separado. Salida: matriz keyword × país × volumen × estacionalidad.
3. **Baseline por reseller** — estado de pixel/GTM (el CSV ya marca "listo" vs "en setup"), tráfico y calidad del sitio → define quién convierte hoy.
4. **Plan de medición con geo-lift** desde el arranque, para probar el valor de Meta.
5. **Volcar este dossier al deck** como slides de estrategia (roles de canal, funnel, benchmarks con banda de error, calendario por país).

---

## Anexo A — Auditoría manual de competencia (pasos)
- **Meta:** `facebook.com/ads/library/` → filtro País (AR/CL/UY, uno por vez) → "Todos los anuncios" → buscar cada marca/distribuidor → anotar formato, fecha de inicio, mensaje/promo, plataformas.
- **Google:** `adstransparency.google.com/` → ajustar región (AR/CL/UY) → buscar anunciante/dominio → revisar formatos, rango de fechas, y comparar entre países.

## Anexo B — Números duros de demanda (método)
- **Google Trends** ([trends.google.com](https://trends.google.com)): comparar términos, fijar país (uno por consulta), ventana 5 años (estacional) + 12 meses (tendencia), categoría "Computadoras y electrónica", exportar CSV. Ayuda: [resultados por región](https://support.google.com/trends/answer/4355212?hl=es).
- **Keyword Planner** (cuenta Google Ads): Herramientas → Planificador → "Consigue métricas y previsiones" → cargar keywords → Ubicación por país separado → leer "Promedio de búsquedas mensuales" + "Puja parte superior" (proxy CPC) → exportar. Caveat: sin gasto activo muestra rangos amplios. Ayuda: [Keyword Planner](https://support.google.com/google-ads/answer/7337243?hl=es-419).

---

## Ver también
- [[informe-landing]] · [[landing-ejemplo-ads]] · [[contexto]] · [[changelog]]
- [[investigacion-notebooks]] — molde de investigación por país (competencia por tier de GPU, precios) replicable a toda la Familia GIGA40.
