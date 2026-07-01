---
tipo: idea
proyecto: LibreOpción
area: Producto / Conversión
estado: en marcha
creado: 2026-06-02
tags:
  - libreopcion
  - armador
  - combos
  - configurador
  - comunidad
  - conversion
---

# 16 · Armador, Combos Dinámicos y Builds de la Comunidad

> [!abstract] Concepto
> Un **armador de PC** + **combos de actualización generados dinámicamente desde el stock** + **builds de la comunidad shoppables** (las máquinas que arma uno, las compran otros). Nace de observar que Compra Gamer le da máxima bola a kits de actualización y armado ([[09 - Estudio de Catálogo - Compra Gamer]]). **Ya está encaminado por el equipo.**

## Las tres capas

| Capa | Qué es | Complejidad |
|---|---|---|
| **Combos de actualización dinámicos** | CPU + mother + RAM que aparecen *solo si hay stock para armarlos*. El slice de más demanda y menos complejidad. | Media — empezar acá |
| **Armador completo** | "Armá tu PC" con fuente, gabinete, refrigeración, clearance. | Alta — después |
| **Builds de la comunidad** | Las configuraciones que arman usuarios/creadores quedan **públicas y comprables** por otros. | Alta — el diferenciador |

## Dinámico desde el stock = la clave

- Un combo/build aparece **solo si hay stock** de todas sus partes (sin combos fantasma).
- Se **re-precia y re-stockea solo**; si falta una parte, **sugiere el swap** compatible.
- Los builds de la comunidad salen del armador → **válidos por construcción** (el motor ya validó compatibilidad).

## 🎯 Por qué es un motor, no una feature: converge media estrategia

| Resuelve | Cómo |
|---|---|
| **Conversión** (problema #1) | Mata la parálisis de decisión. Rescata las **mothers de gama alta con muchas vistas y 0 ventas** (nadie compra una mother sola). → [[13 - El Verdadero Cuello de Botella es la Demanda]] |
| **Ticket alto** | Empaqueta 3-4 productos → mejor base para cuotas + garantía. → [[11 - Estrategia de Cuotas y Precio]] |
| **Liquidación de aging** | El motor **mete stock viejo en combos** junto a partes frescas y demandadas. → [[14 - Liquidacion de Aging como Motor de Demanda]] |
| **Comunidad / creadores** | Los builds de creadores son su producto a revender (+1-3%). → [[12 - Modelo Operativo - Importador-Mayorista con Red de Vendedores]] |
| **Contenido / SEO** (cubre el hueco de redes) | Los builds UGC son **contenido buscable** generado por la comunidad, no por LibreOpción. |
| **Confianza** | "Comprá el build que armó X" = elección guiada y segura. → [[10 - Reposicionamiento - De Precio a Confianza]] |

## 💰 Revisión (2026-06-11): el "para qué" de fondo — mercado de upgrade + co-funding de marcas

> [!important] Lo que casi se nos pasa
> El armador/combos no es solo una palanca de conversión: **ataca el mercado real argentino y destraba fondos de las marcas.** Esto lo eleva de feature a columna vertebral.

**1 · El mercado argentino es de upgrade, no de PC nueva.** Con el poder adquisitivo golpeado, lo normal es **actualizar** la PC que ya se tiene, no comprar una nueva. El catálogo de Compra Gamer lo confirma ([[09 - Estudio de Catálogo - Compra Gamer]]): **~46% son componentes sueltos** (el mercado de upgrade) vs. solo **7,4% equipos/PCs completas**, y **"Kits de actualización" es su 2ª subcategoría** (125 productos, casi empatada con Mothers AMD). El combo de actualización es el producto que ataca esa cancha.

**2 · El combo destraba fondos de las marcas (palanca de margen).** Al empaquetar CPU + mother + RAM, **cada marca del combo tiene incentivo para co-fundear esa venta**: se apilan bonificaciones de varias marcas sobre un mismo carrito y se concentra volumen en SKUs puntuales → habilita **rebates y fondos de marketing (MDF)** que comprando suelto no aparecen. Es la misma lógica de "que paguen las marcas" de las cuotas ([[11 - Estrategia de Cuotas y Precio]]), pero del lado del producto: **plata fresca que afloja la restricción del 17% de margen**. Esto, no solo el ticket, es la razón estratégica de fondo para priorizar combos.

**3 · App de vendedores (clonado de builds).** El armador alimenta una **aplicación para vendedores/creadores** donde **clonan builds y combos con un toque** y los ofrecen a su audiencia con su margen (+1–3%). Nosotros ponemos stock, precio, garantía, cuotas y logística; el vendedor no opera nada. Convierte el armador en un **canal de ventas distribuido** — cada creador es una tienda más. Se conecta con [[12 - Modelo Operativo - Importador-Mayorista con Red de Vendedores]].

## 🧩 Catálogo de arranque validado contra stock real (2026-07-01)

> [!success] Ya hay lista concreta para el día uno
> Se cruzaron los kits y PCs de Compra Gamer contra el catálogo real de la distribuidora (`items/catalogoDistribuidoraJulio.csv`) con el script `gen-combos-match.py`. Resultado en [[combos-armables]]: **31 combos** (26 CPU+Mother, 3 GPU+Fuente, 2 Gabinete+Fuente) y **15 PCs armadas** (oficina → gamer tope), cada uno con SKU y costo. El armador dinámico **arranca con vidriera**, no de cero.

- **Hallazgo para decidir compras:** hay un **hueco de gama media AM5** — la línea AM5 propia es toda alta gama X3D, así que los combos de Ryzen no-X3D (7600, 8500G/8600G/8700G, 9600X, 9700X) hoy solo se cubren con un 7800X3D (más caro). Conviene **sumar 1-2 CPUs AM5 baratos** para competir esos precios.
- Todo quedó listado en la landing [[Plan-Estrategico-LibreOpcion-Marca.html|Plan Estratégico (Marca)]] bajo "Qué combos/PCs armaría para arrancar ya".

## Dónde se ofrece

- **Sección propia** ("Armá tu upgrade / tu PC").
- **Embebido** en distintas partes del sitio (en la ficha de una mother, "armá el combo").
- **Links compartibles** de cada build (para que el creador lo difunda).

## Guardrails

- **Híbrido > 100% automático:** el motor genera el universo de combos válidos, pero se **destacan/promocionan los curados** (recomendados), para no mostrar combos subóptimos.
- **Swap automático** cuando falta stock, para no romper el build.
- Los builds comprables deben pasar siempre por el **motor de compatibilidad**.

## Encaje en el plan

Palanca central de demanda → ver [[15 - Plan de Accion - Proximos 6 Meses]]. Combos de actualización en **Tier 1** (alto ROI, rescata 0-ventas + liquida aging); armador completo + builds de comunidad en **Tier 2**.

## Enlaces

- [[09 - Estudio de Catálogo - Compra Gamer]] · [[13 - El Verdadero Cuello de Botella es la Demanda]] · [[14 - Liquidacion de Aging como Motor de Demanda]]
- [[12 - Modelo Operativo - Importador-Mayorista con Red de Vendedores]] · [[15 - Plan de Accion - Proximos 6 Meses]]
- [[00 - Índice Gestión X]]
</content>
