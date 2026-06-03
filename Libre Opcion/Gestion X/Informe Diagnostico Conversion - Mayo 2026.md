# Informe de diagnóstico de conversión — LibreOpción

**Período:** 1–31 mayo 2026 · **Propiedad:** Libre Opción GA4 · **Fuente:** GA4 (100 % de los datos)

> [!note] Nota de reconciliación (importante)
> En GA4 mayo registra **454.393 visitas** (page_view) ≈ los 446.000 reportados, y **493,1 M ARS** de ingresos. Pero el evento de venta tiene un problema: `purchase` disparó **1.139 veces** sobre solo **820 compradores únicos** (≈ las 831 ventas reales). Es decir, **el evento `purchase` sobre-cuenta ~37 %** (probablemente se dispara al recargar la página de gracias). Existe además un evento `compra_finalizada` configurado pero con **0 registros**. Todas las tablas usan el dato de GA (`purchase`=1.139); donde es relevante se aclara el equivalente en compradores únicos (820).

---

## SECCIÓN 1 — CALIDAD DEL TRÁFICO

### 1.1 Por canal (agrupado en 6 buckets)

Conversión sobre visitas (definición del cliente) **y** sobre sesiones (estándar e-commerce, más revelador).

| Canal | Visitas | Sesiones | Ventas | Conv% s/visitas | Conv% s/sesiones | Ingreso ARS |
|---|--:|--:|--:|--:|--:|--:|
| Pago* | 336.616 | 123.347 | 770 | 0,23 % | 0,62 % | 335.802.257 |
| Orgánico** | 42.727 | 9.445 | 133 | 0,31 % | 1,41 % | 62.839.045 |
| Directo | 41.160 | 9.983 | 145 | 0,35 % | 1,45 % | 56.220.266 |
| Social (orgánico) | 13.294 | 5.527 | 9 | 0,07 % | 0,16 % | 5.725.155 |
| Referidos | 12.681 | 2.644 | 66 | 0,52 % | 2,50 % | 29.919.896 |
| Email (Brevo) | 3.836 | 1.119 | 7 | 0,18 % | 0,63 % | 1.016.850 |
| Sin asignar | 4.079 | 825 | 9 | 0,22 % | 1,09 % | 1.598.040 |
| **Total** | **454.393** | **155.611** | **1.139** | **0,25 %** | **0,73 %** | **493.121.509** |

\* Pago = Cross-network + Paid Search + Paid Social + Display + Paid Other + Paid Video.
\*\* Orgánico = Organic Search + Organic Video + Organic Shopping.

**Lectura clave:** el tráfico **Pago concentra el 74 % de las visitas pero convierte 0,62 %/sesión**, mientras Orgánico (1,41 %), Directo (1,45 %) y Referidos (2,50 %) convierten 2–4× mejor. El tráfico pago es de calidad muy inferior.

### 1.2 Métricas globales

| Métrica | Valor |
|---|--:|
| % de rebote | 46,78 % (interacción 53,22 %) |
| Tiempo de interacción medio / sesión | 45 s |
| Páginas por sesión | 2,92 |

### 1.3 Por dispositivo

| Dispositivo | Visitas | Ventas | Conv% s/visitas | Ticket promedio ARS |
|---|--:|--:|--:|--:|
| Mobile | 268.067 | 565 | 0,21 % | 482.093 |
| Desktop | 184.632 | 571 | 0,31 % | 384.562 |
| Tablet | 1.629 | 3 | 0,18 % | 384.657 |
| Smart TV | 65 | 0 | 0 % | — |
| **Total** | **454.393** | **1.139** | **0,25 %** | **432.943** |

**Lectura:** mobile trae 59 % de las visitas pero vende casi lo mismo que desktop (565 vs 571); **desktop convierte ~50 % mejor**. Mobile está sub-rindiendo.

### 1.4 Top 10 fuentes con MÁS visitas y MENOS ventas

| Fuente/medio | Visitas | Ventas | Conv% |
|---|--:|--:|--:|
| ig / paid | 12.495 | 0 | 0 % |
| fb / paid | 11.121 | 5 | 0,045 % |
| l.instagram.com / referral | 4.010 | 4 | 0,10 % |
| reddit.com / referral | 2.739 | 1 | 0,037 % |
| facebook.com / referral | 2.251 | 1 | 0,044 % |
| youtube.com / referral | 1.281 | 1 | 0,078 % |
| l.facebook.com / referral | 1.134 | 1 | 0,088 % |
| instagram.com / referral | 1.048 | 1 | 0,095 % |
| m.facebook.com / referral | 729 | 0 | 0 % |
| an / paid (audience network) | 724 | 0 | 0 % |

**El gran derroche está en paid social: `ig/paid` (12.495 visitas, 0 ventas) y `fb/paid` (11.121, 5 ventas).**

---

## SECCIÓN 2 — EMBUDO DE CONVERSIÓN (prioritario)

### 2.1 Embudo paso a paso (usuarios por evento)

| Paso | Usuarios | % del paso anterior | % del total inicial |
|---|--:|--:|--:|
| Vio producto (view_item) | 14.604 | — | 100 % |
| Agregó al carrito (add_to_cart) | 4.405 | 30,2 % | 30,2 % |
| Inició checkout (begin_checkout) | 3.284 | 74,6 % | 22,5 % |
| Completó compra (purchase) | 820 | 25,0 % | 5,6 % |

### 2.2 Abandono de checkout

- Iniciaron checkout: **3.284** · Compraron: **820** · **Abandonaron: 2.464 (75,0 %)**

| Sub-paso checkout | Usuarios | Caída vs anterior |
|---|--:|--:|
| Inició checkout (begin_checkout) | 3.284 | — |
| Datos de envío (add_shipping_info) | 1.341 | **−59,2 %** ← mayor fuga |
| Selección de pago (add_payment_info) | 428 | −68,1 % |
| Cuotas | NO DISPONIBLE | — |
| Confirmación (purchase) | 820 | — |

> [!warning] Anomalía de tracking
> `purchase` (820) > `add_payment_info` (428): el evento de pago sub-registra y ese sub-paso no es confiable. La fuga sólida y mayor del checkout está en **datos de envío** (−59 %).

---

## SECCIÓN 3 — DEMANDA INSATISFECHA

### 3.1 Top 20 búsquedas internas SIN resultados

**NO DISPONIBLE.** La búsqueda interna casi no está trackeada (`view_search_results` = 23 eventos en todo mayo) y GA4 no registra de forma nativa "búsquedas sin resultados" sin un evento `no_results` personalizado. Recomendación: instrumentar el buscador interno.

### 3.2 Top 20 productos MÁS VISTOS vs vendidos (ratio visto/vendido)

| Producto | Vistas | Unidades vendidas | Ratio visto/vendido |
|---|--:|--:|--:|
| AURICULAR + MIC HEADSET GENIUS HS-05A | 1.967 | 1 | 1.967 |
| MONITOR GAMER GIGABYTE 24.5 GS25F2 200HZ | 1.661 | 18 | 92 |
| PROCESADOR RYZEN 7 5700X (AM4) | 1.655 | 28 | 59 |
| PROCESADOR RYZEN 7 9800X3D (AM5) | 1.636 | 58 | 28 |
| COOLER MASTER HYPER 212 V3 RGB | 1.334 | 25 | 53 |
| **MOTHERBOARD ASUS ROG CROSSHAIR X670E HERO** | 1.182 | **0** | ∞ |
| PLACA RTX 5060TI AERO 8GB | 1.120 | 1 | 1.120 |
| GABINETE COOLER MASTER HAF 700 EVO | 1.059 | 1 | 1.059 |
| PLACA RTX 5060 EAGLE OC 8GB | 1.024 | 4 | 256 |
| MOTHERBOARD GIGABYTE A520M K V2 (AM4) | 991 | 54 | 18 |
| **MOTHERBOARD ASUS ROG STRIX B550-F (WI-FI) II** | 942 | **0** | ∞ |
| PROCESADOR RYZEN 9 9950X3D2 (AM5) | 906 | 17 | 53 |
| **NOTEBOOK LENOVO V15.6 I5 12450HX RTX4050** | 873 | **0** | ∞ |
| **PARLANTE BT GENIUS SP-HF520BT** | 818 | **0** | ∞ |
| **MICROFONO TRUST EXXO GXT 256** | 813 | **0** | ∞ |
| PROCESADOR RYZEN 5 5500 (AM4) | 752 | 20 | 38 |
| **ACER NOTEBOOK ASPIRE LITE CI9 13900H** | 721 | **0** | ∞ |
| PROCESADOR RYZEN 9 5900XT (AM4) | 713 | 1 | 713 |
| **PARLANTE BT GENIUS SP-915BT RGB** | 688 | **0** | ∞ |
| PROCESADOR RYZEN 7 7800X3D (AM5) | 660 | 15 | 44 |

**8 de los 20 productos más vistos vendieron 0 unidades** (motherboards de gama alta, notebooks, parlantes, micrófono) — fuerte señal de demanda insatisfecha (probable falta de stock, precio o ficha deficiente).

---

## ENTREGABLE — ¿Tráfico o embudo?

**Es de ambos, pero el cuello de botella dominante y más accionable es el EMBUDO, con un problema grave de calidad de tráfico encima en paid social.** El tráfico de calidad (orgánico, directo, referidos) convierte 1,4–2,5 %/sesión, mientras el Pago —74 % del volumen— convierte ~0,6 % y el paid social directamente cerca de 0 (`ig/paid`: 12.495 visitas, 0 ventas), o sea hay tráfico que no compra. **El paso donde se pierde más gente es producto→carrito: de 14.604 a 4.405 usuarios (−70 %, ~10.200 personas), y dentro del checkout, el paso de "datos de envío" (−59 %); del total que inicia checkout, el 75 % no completa la compra.**
