---
title: Resumen coloquial de Julio 2026 — proyecto por proyecto
fecha: 2026-08-12
periodo: 2026-07-01 / 2026-07-31
tipo: reporte
fuente: Jira (todos los tableros)
---

# 🗣️ Julio 2026 en criollo — qué hizo cada equipo

Versión "para leer de corrido" del [[2026-07-reporte-detallado|reporte detallado]]. Sin tablas ni gráficos: qué se movió en cada proyecto y quién lo empujó.

---

## 🛒 Libre Opción — el proyecto más movido del mes

Fue, lejos, el que más laburo tuvo (87 tareas). El foco grande fue el **sistema de reputación y calificaciones**: **Franco** metió mano en todo el backend (API + CMS) y **Marbe** en las pantallas. Ahora se puede calificar tanto al **vendedor** como al **producto**, responder y replicar las opiniones (parecido a las preguntas y respuestas de la ficha), y se sumaron los "penales". Hubo bastante ida y vuelta de QA sobre esto: reseñas que se duplicaban, calificaciones que se "heredaban" entre compras y un campo obligatorio que faltaba.

En paralelo, **Marbe** se comió una tanda enorme de **A+ Content**: más de 25 fichas enriquecidas de **Gigabyte** (motherboards, monitores, fuentes, gabinetes, la RTX 5050), **Trust** y **AMD**. También arrancó la **Wallet / Billetera LO** con el QR "air drop" y la pantalla de aterrizaje. Y **Eze** sumó el login de PartPicker en inventario y dejó lista la actualización de la **app de Vendedores** para Google Play.

## 🏢 GIGA (el ERP nuevo) — arrancó y cerró todo

Todo **Eze**, y cerró el 100% de lo del mes (12 tareas). Se armó la sección **Contactos** (importar listas y dar de alta clientes), el **login de PartPicker**, las **etiquetas de cargo** con autocompletar, los **estados de proyecto configurables** (con color) más el estado "Pendiente de pago", el **calendario con hora**, el **"Mapa de Ploteos"** (mapa del país con las marcas) y mejoras en Fondos y acciones de marketing. Un mes redondo para el ERP.

## 📦 Pedidos — billetera, LASET y volanta

**Ema** y **Eze** laburaron la **Billetera LO** (movimientos y saldo, replicando lo de Cobros). Se corrigieron los datos de **clientes de LASET** que no cargaban bien en producción, y **Marbe** metió los ajustes de la **Volanta** (nombres en mayúscula y el logo de cada empresa). También se arregló el error al abrir el detalle de un pedido pagado con wallet.

## 🔧 Postventa — flujo de pre-ingreso terminado

Cinco tareas, todas cerradas (**Eze** + **Marbe**). Quedó redondo el flujo de **pre-ingreso**: rechazar con motivo, disparar el mail, mejorar el wording del correo de ingreso y los remitos.

## 🌐 NBWEB / NBElectric — postventa, banners y research

Se hizo el **detalle de postventa** (el "pase"), se mejoraron los **banners de aceleradores** y se sumó la marca **Cooler Master**. **Guillermo** arrancó un **research para generar casos de prueba automáticos** y actualizó la documentación de developers/sandbox. En NBE, ajustes de la web y cambio de logo.

## 🧾 Compras e Inventario — refactors finos

Refactors de **PartPicker** (meter la key en todos los recursos), el arreglo del **color de moneda** cruzado en las órdenes de compra, y mejoras de **Stock** (subir el buscador y resolver el mensaje del delta al filtrar por fecha).

---

## 🎨 BLU — Agencia y clientes (el músculo de Diseño y Marketing)

Acá está el grueso operativo del mes, sostenido por **Bárbara** y **Belu**:

- **Fontaine Bleau** (58): fue el cliente más cargado — **avance de obra** (fotos, ISO), triadas y un montón de **activaciones cargadas al ERP**.
- **ADATA** (42): mes intenso y muy "de coyuntura" — mucho contenido del **Mundial** (Argentina vs varios rivales), **Adata Rewards**, memes, banners, presupuestos del **Brand Tour** y toda la carga de activaciones.
- **LASET** (19): las **triadas de posteos** (ZOTAC, Patriot, Toshiba, ASUS, Genius) y ajustes al sitio (logo SVG, flechas en el slider de marcas).
- **Blu** (11): la **BluTriada 1-2-3**, posteos y cronograma de actividades.
- **CBL** (6): eventos **Microglobal Cisco-Brotek** y tarjetas.
- **LO Marketing** y **D-Link**: promos (NVIDIA) y material de marca.

> El equipo de diseño mantuvo un ritmo altísimo y muy variado: contenido de redes, activaciones, eventos y obra, para varias marcas a la vez.

---

## 🎧 Soporte (SNB) — el "impuesto" invisible al desarrollo

El equipo de dev atendió **46 pedidos** de las otras áreas. La mitad fueron **errores/bugs**, el resto consultas y pedidos de funciones nuevas. Lo cargó sobre todo **Eze** (20 tickets), con **Catriel** (12) y **Ema** (9). La semana 4 fue la más pesada (14 tickets). Es tiempo que el equipo técnico le saca al roadmap, así que vale tenerlo a la vista.

---

## En una frase

**Julio fue un mes de empuje fuerte de producto (LIO y el ERP GIGA), con Diseño/Marketing a pleno sosteniendo todas las marcas, y un soporte que pesó sobre el equipo de desarrollo.**
