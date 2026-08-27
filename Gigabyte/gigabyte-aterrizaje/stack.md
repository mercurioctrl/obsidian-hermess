# Stack

| Capa | Tech |
|------|------|
| Framework | Nuxt 3 (SSR) + Vue 3 |
| Estilos | Tailwind CSS vía **PostCSS nativo** (`nuxt.config` → `postcss.plugins`), **NO** el módulo `@nuxtjs/tailwindcss` |
| Datos | Server routes (`server/api/*`) como proxy contra [[api-partpicker|BluPartPicker]] |
| Runtime | Node **>= 20.11** (obligatorio) |

## Dependencias clave

- `nuxt` ^3.13 (resuelve a 3.17.x)
- `@vueuse/core` + `@vueuse/nuxt`
- `autoprefixer` (para PostCSS)
- `tailwindcss` 3.x

## Fuentes

Google Fonts en `nuxt.config.ts`: **Rajdhani** (`font-display`), **Chakra Petch** (`font-tech`), **Inter** (`font-sans`).

## Entorno / gotchas

- **Node 20 obligatorio**: el toolchain de Nuxt 3.17 usa `import.meta.dirname`; con Node 18 falla `nuxt prepare`. En este entorno hay un Node 20 portable en `~/.local/node20/bin` → `export PATH="$HOME/.local/node20/bin:$PATH"`.
- **Tailwind por PostCSS nativo**: el módulo `@nuxtjs/tailwindcss` disparaba `[postcss] Cannot use 'import.meta' outside a module`. Se removió y se configuró PostCSS a mano.
- **Pesos de fuente numéricos** (`font-600/700`) declarados en `tailwind.config.ts` (no existen por default).
- **Dev server en este entorno**: muere con exit 144 si el comando de Bash es multi-statement o usa `sleep` en foreground. Lanzar one-liner `nohup npm run dev > /tmp/nuxt-dev.log 2>&1 & echo $!` y verificar aparte con `curl --retry-connrefused`.

## Variables de entorno

`.env` (gitignoreado): `PARTPICKER_BASE_URL`, `PARTPICKER_API_KEY`. Leídas server-side vía `runtimeConfig`. La key nunca se expone al browser.

## Ver también

- [[arquitectura]] · [[design-system]] · [[gigabyte-aterrizaje]]
