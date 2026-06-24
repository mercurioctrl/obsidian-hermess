# blu-web-v1

Sitio web corporativo de Blu Inc Studio — Nuxt 3 + Vue 3 + SCSS

## Notas

- [[base-de-conocimiento]] — Documentación completa del proyecto (componentes, patrones CSS, fondos, animaciones, JobBoard, catálogo de merch, admin panel)
- [[arquitectura]] — Contexto en el monorepo, [[arquitectura#Build y deploy importante|build/deploy PM2]], páginas, layouts, i18n, auth, permisos, [[arquitectura#Catálogo de merch|catálogo de merch]] con [[arquitectura#Pipeline de normalización de imágenes|pipeline de normalización]], [[arquitectura#SEO y archivos de descubrimiento|SEO y archivos de descubrimiento]], [[arquitectura#Propuestas comerciales detrás de token|propuestas comerciales]]
- [[stack]] — Dependencias, colores de servicios, backend consumido
- [[changelog]] — Registro de cambios de assets, decisiones y actualizaciones fuera del código
- [[memoria]] — Facts, preferencias y gotchas cross-sesión

## Features destacadas

- [[arquitectura#Sitio público|Sitio público]] con 4 servicios (IT, Marketing, BI, Recruiting) + Landing + Nosotros + Contacto
- [[base-de-conocimiento#JobBoard Búsquedas activas de Recruiting|JobBoard]] en `/servicios/recruiting` — búsquedas activas con postulación
- [[arquitectura#Catálogo de merch|Catálogo de merch]] en `/catalogo-merch` — galería importada desde CSV con fotos normalizadas (ver [[changelog#2026-04-13 — Normalización de imágenes del catálogo|changelog 2026-04-13]])
- [[base-de-conocimiento#Admin Panel staffpanel|Panel admin]] — contactos, citas, horarios, catálogo, reclutamiento, usuarios
- [[arquitectura#Sistema de permisos por sección|Permisos por sección]] — cada usuario ve solo las secciones asignadas, admin siempre ve todo
- [[arquitectura#SEO y archivos de descubrimiento|SEO y archivos de descubrimiento]] — sitemap auto-generado, robots, llms.txt, security.txt, BIMI logo en dominio canónico `blustudioinc.com`
- [[arquitectura#Propuestas comerciales detrás de token|Propuestas comerciales]] en `/propuestas/[slug]?token=` — landings personalizadas por cliente, con render inline o delegado a componente vía `kind` (ver [[changelog#2026-05-06 — Propuestas comerciales detrás de token propuestasslug|changelog 2026-05-06]] y [[changelog#2026-06-12/13 — Landing del monitor Gigabyte MO27Q28G estética del sitio oficial|landing monitor 2026-06-12/13]])

## Contexto no-obvio (leer antes de tocar)

- **Build/deploy:** el front corre con PM2 (`BLUWeb`) en `:3008`, NO hay HMR — `npm run build && pm2 restart BLUWeb` para ver cualquier cambio (ver [[memoria#Build y deploy PM2 en 3008|memoria]])
- **Dominio canónico:** `blustudioinc.com` — NO `blustudiogroup.com` (ver [[memoria#Dominio canónico trampa no-obvia|memoria]])
- **HTML nativo en admin:** NO usar Nuxt UI en forms del admin panel — ver [[memoria#HTML nativo en admin|memoria]]
- **Perfil BIMI obligatorio:** SVG Tiny 1.2 Portable/Secure — ver [[arquitectura#Checklist del perfil BIMI|checklist]]
- **Propuestas confidenciales:** nunca mencionar competidores del cliente en `/propuestas/<slug>` — ver [[memoria#Propuestas comerciales 2026-05-06|memoria]]
- **Color Gigabyte = azul, no naranja:** el naranja `#FF6600` es de AORUS — ver [[memoria#Landing del monitor Gigabyte estética oficial|memoria]]
- **Sitios que bloquean bots (Gigabyte/AORUS):** verlos con Playwright + Chrome del sistema — ver [[memoria#Ver sitios que bloquean bots Gigabyte AORUS|memoria]]

## Última sincronización

2026-06-23 — **Propuesta de negocios Gigabyte** (`/propuestas/gigabyte-negocios?token=gbt-biz-2026`): nuevo componente `NegociosPresentation.vue` (`kind: 'negocios'`) con 3 líneas — ERP (+ panel de la **API BluPartPicker**, botón a la **demo del ERP** `gigaerp.blustudioinc.com`), Marketing (cards uniformes + editores `edit.to-aor.us`) y Ads (planes + pautas por país). Hero con **banda identitaria AORUS** ("Team up. Fight on.", naranja `#FF6600`). Además: nueva **doc interna de la API** en `/apis/blupartpicker` (ruta estática que gana sobre `[slug]`, requiere reiniciar el dev server; generada del OpenAPI real `partpicker.blustudioinc.com`). Fixes mobile en la tabla de Ads (1ra columna sticky + scroll) y cards de presentaciones. También quedó documentado el **onboarding de resellers** (`gigabyte-ads`, `ResellerAdsOnboarding`). Cerró con una **ronda de ajustes de copy** con el cliente (hero orientado a negocio, ERP regional Arg/Uy/Py/Chi, "Pauta.Argentina", implementación ERP como **pago único** USD 1.990) y la aclaración de que la **API BluPartPicker es propia de Blu** (no específica del ERP de Gigabyte). Ver [[changelog#2026-06-23 — Propuesta de negocios Gigabyte + doc interna de la API BluPartPicker|changelog 2026-06-23]] y [[changelog#2026-06-23 cont. — Ronda de ajustes de copy con el cliente|ronda de copy]].

2026-06-17 — Cierre de las propuestas. Se documentó el **toggle ojo del fee mensual** (`fc176ff`): el monto arranca enmascarado `*,***` y se revela con un botón, disparando el contador al revelar. Y el **gotcha de assets estáticos en dev**: `<img src="/...">` da 400 en SSR desde archivos de ruta con corchetes (`[slug].vue`) — fix con binding dinámico (`:src="bluLogo"`). Ver [[changelog#2026-06-17 — Toggle del fee + gotcha de assets estáticos en dev|changelog 2026-06-17]] y [[memoria#Assets estáticos rompen en dev desde rutas con corchetes|memoria]].

2026-06-13 — Landing del monitor Gigabyte MO27Q28G (`/propuestas/gigabyte-monitor?token=gbt-mo27-2026`): nuevo componente `MonitorPresentation.vue` con la estética de la página oficial del producto (azul Gigabyte `#00A0E9`/`#0446F2` en vez de naranja AORUS, tipografía Aldrich en mayúsculas, fondo negro plano, UI rectangular, textwall en outline). Mecanismo de dispatch por `kind` en `[slug].vue`. Varias rondas de ajustes de copy (todo el contenido vive en arrays del `<script setup>`). Documentado el workflow de build/deploy con PM2 en `:3008` y el truco de Playwright para ver sitios que bloquean bots. Ver [[changelog#2026-06-12/13 — Landing del monitor Gigabyte MO27Q28G estética del sitio oficial|changelog 2026-06-12/13]].
