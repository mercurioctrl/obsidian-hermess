# blu-web-v1

Sitio web corporativo de Blu Inc Studio — Nuxt 3 + Vue 3 + SCSS

## Notas

- [[base-de-conocimiento]] — Documentación completa del proyecto (componentes, patrones CSS, fondos, animaciones, JobBoard, catálogo de merch, admin panel)
- [[arquitectura]] — Contexto en el monorepo, páginas, layouts, i18n, auth, permisos, [[arquitectura#Catálogo de merch|catálogo de merch]] con [[arquitectura#Pipeline de normalización de imágenes|pipeline de normalización]], [[arquitectura#SEO y archivos de descubrimiento|SEO y archivos de descubrimiento]]
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

## Contexto no-obvio (leer antes de tocar)

- **Dominio canónico:** `blustudioinc.com` — NO `blustudiogroup.com` (ver [[memoria#Dominio canónico trampa no-obvia|memoria]])
- **HTML nativo en admin:** NO usar Nuxt UI en forms del admin panel — ver [[memoria#HTML nativo en admin|memoria]]
- **Perfil BIMI obligatorio:** SVG Tiny 1.2 Portable/Secure — ver [[arquitectura#Checklist del perfil BIMI|checklist]]

## Última sincronización

2026-04-15 — Sistema de permisos por sección del admin panel, migración a HTML nativo en forms, fix de cambio de contraseña. Ver [[changelog#2026-04-15 — Sistema de permisos por sección  fixes admin panel|changelog]].
