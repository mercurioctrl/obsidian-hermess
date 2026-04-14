# blu-web-v1

Sitio web corporativo de Blu Inc Studio — Nuxt 3 + Vue 3 + SCSS

## Notas

- [[base-de-conocimiento]] — Documentación completa del proyecto (componentes, patrones CSS, fondos, animaciones, JobBoard, catálogo de merch, admin panel)
- [[arquitectura]] — Contexto en el monorepo, páginas, layouts, i18n, auth, [[arquitectura#Catálogo de merch|catálogo de merch]] con [[arquitectura#Pipeline de normalización de imágenes|pipeline de normalización]]
- [[stack]] — Dependencias, colores de servicios, backend consumido
- [[changelog]] — Registro de cambios de assets, decisiones y actualizaciones fuera del código

## Features destacadas

- [[arquitectura#Sitio público|Sitio público]] con 4 servicios (IT, Marketing, BI, Recruiting) + Landing + Nosotros + Contacto
- [[base-de-conocimiento#JobBoard Búsquedas activas de Recruiting|JobBoard]] en `/servicios/recruiting` — búsquedas activas con postulación
- [[arquitectura#Catálogo de merch|Catálogo de merch]] en `/catalogo-merch` — galería de productos importada desde CSV con fotos normalizadas sobre fondo blanco (ver [[changelog#2026-04-13 — Normalización de imágenes del catálogo|changelog 2026-04-13]])
- [[base-de-conocimiento#Admin Panel cmsadmin|Panel admin]] en `/cmsadmin` — contactos, citas, horarios, catálogo, usuarios

## Última sincronización

2026-04-13 — normalización de imágenes del catálogo (pipeline GD + refinamiento visual del front)
