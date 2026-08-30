# Configuración

Parte de [[portal]].

Todo por **variables de entorno en el deploy**. No hay panel en vivo — ver
[[contexto#Configuración por deploy no por panel]].

| Variable | Default | Qué hace |
|---|---|---|
| `NUXT_PUBLIC_API_BASE` | `https://api.nbe.com.ar/v1` | Instancia de API |
| `NUXT_PUBLIC_SECTIONS` | vacía | Lista blanca de secciones; vacía = todas |
| `NUXT_PUBLIC_SECTIONS_OFF` | vacía | Lista negra, se aplica después |

## Secciones activables

Claves y rutas en `composables/useSections.ts`:

```
panel · pedido · catalogo · frecuentes · pedidos
comprobantes · precios · promociones
mi-cuenta · usuarios · direcciones · postventa · contacto
```

```env
NUXT_PUBLIC_SECTIONS=pedidos                    # solo el camino del pedido
NUXT_PUBLIC_SECTIONS_OFF=postventa,comprobantes # todo menos esas dos
```

Apagar una sección hace **tres** cosas, porque las tres salen del mismo registro:
la saca del menú, **bloquea su ruta** (quien tenga el link va al panel) y esconde los enlaces
que apuntan a ella desde otras páginas.

`panel`, `pedido`, `catalogo` y `mi-cuenta` son `required` y no se pueden apagar.
`promociones` es `pending`: se lista con chip "Pronto" y su ruta está bloqueada.

En **Mi cuenta → Módulos del portal** hay una vista de solo lectura para verificar la config.

## Empresa: NB vs NBE

El alcance por empresa **no es un parámetro de request**: la API lee `COMPANY_CODES` y
`WAREHOUSE_IDS` de su `.env` y los interpola en el SQL del catálogo, marcas, rubros, ficha,
precios y alta de pedidos. Por eso hay una instancia por empresa.

| Instancia | Empresa | Catálogo |
|---|---|---|
| `api.nb.com.ar/v1` | 1, 2, 4 (NB) | Informática — ~74 marcas |
| `api.nbe.com.ar/v1` | 9 (NBE) | Material eléctrico — 27 marcas, 50 rubros, 1.342 artículos |

La empresa 9 está confirmada en el código del backend (`src/Controller/Excel.php:924`):
*"los productos ABB/Netcomponent viven bajo companyCode 9 y se stockean en el depósito NBE
(almacén 8)"*.

## Deploy

`npm run build` (servidor Node) o `npm run generate` (estático para nginx). Al ser SPA, el
servidor tiene que devolver `index.html` para cualquier ruta, si no las URLs directas dan 404.
Todavía no hay Dockerfile ni config de nginx — ver [[estado]].

## Ver también

- [[stack]] · [[arquitectura]] · [[estado]]
