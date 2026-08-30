# Stack

Parte de [[portal]].

## Frontend (`portal/`)

| Pieza | Versión / elección | Para qué |
|---|---|---|
| Nuxt | 3.x, `ssr: false` | SPA: todo el portal es autenticado, no hay nada que prerenderizar |
| Vue | 3.5 | |
| Tailwind CSS | 3.x, `darkMode: 'class'` | Sin librería de UI, componentes propios |
| Pinia | 2.x | Sesión, carrito y preferencias de visualización |
| Work Sans | Google Fonts | Tipografía de nbe.com.ar |

**Node 20 o superior** — Nuxt 3 no corre en 16. Hay `.nvmrc`. Ojo: el `node` por defecto del
sistema es el 16 de nvm; el bueno es el de Homebrew (`/opt/homebrew/bin/node`).

Sin librería de íconos: `AppIcon.vue` tiene ~25 paths de Lucide inline.
Sin librería de componentes: todo propio, ~5.100 líneas entre `.vue` y `.ts`.

## Backend (referencia, no se modifica)

`sitio-api-rest-v3/` — PHP 8 + Slim 4 + SQL Server, con Phinx para migraciones.
Es la API productiva que sirve también al sitio de NB. Ver [[api-nbe]].

## Servicios externos

- **API de envíos** (`API_MS_ENVIOS`) — cotiza el envío por transporte. Si no responde, el
  checkout cae a la lista plana de transportes sin precios.
- **static.nb.com.ar** — imágenes de producto y de marca.

## Ver también

- [[arquitectura]] — cómo se organiza el código
- [[configuracion]] — variables de entorno
