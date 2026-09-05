# Memoria del proyecto

Parte de [[portal]].

Lo que hay que saber antes de retomar. Espeja el `CLAUDE.md` del repo.

## Reglas

**El backend no se modifica.** `sitio-api-rest-v3/` está en el repo solo como referencia: es la
API productiva que también sirve al sitio de NB. Lo que no se puede resolver desde el frontend
queda documentado en [[estado]], no se parchea.

**La API no tiene documentación.** Ante una duda: buscar el DTO en `src/Dto/`, el repositorio en
`src/Repository/`, y **verificar contra la API real con curl**. No asumir.

**Confirmar un pedido escribe en el ERP.** `POST /carrito/process` crea una nota de pedido real.

**El backend no se versiona en este repo.** `sitio-api-rest-v3/` está en el `.gitignore` de la
raíz: es un repo aparte y su `.env-example` tiene credenciales reales. Si alguna vez hay que
mover el `.gitignore`, verificar que siga excluido antes de commitear.

## Trampas que ya costaron tiempo

1. **La barra final** — `GET /v1?query` da 404; el preflight también, y el navegador aborta con
   `Failed to fetch`. Usar `useApi().catalogue()`, nunca `get('/')`.
2. **Dólares vs pesos** — los precios vienen en dólares, el envío en pesos.
3. **El carrito es compartido entre NB y NBE** — misma base de datos.

Detalle en [[api-nbe#Trampas]].

## Convenciones

- Nuxt 3 SPA, Node 20+ (el `node` del sistema es el 16 de nvm; usar el de Homebrew)
- `types/api.ts` espeja los DTO **sin renombrar** — comentarios, no renames
- Toda llamada HTTP por `useApi()`
- La navegación sale de `composables/useSections.ts`, no del sidebar
- Sin librerías de UI ni de íconos
- Listados con `DataState`

## Criterio de producto

**Donde la API no da el dato, se dice en pantalla.** Sin columnas vacías ni números inventados.
Ver [[contexto#Donde la API no da el dato se dice en pantalla]].

## Entorno

Repo: [New-Bytes/nbelectric-portal](https://github.com/New-Bytes/nbelectric-portal) (privado).

```bash
cd portal && npm run dev -- --port 3400
```

El puerto 3000 suele estar ocupado por otro proyecto. La extensión de Chrome de Claude no logra
cargar `localhost` fuera del 3000, así que **la verificación visual la hace el usuario**.

## Ver también

- [[contexto]] · [[api-nbe]] · [[estado]] · [[arquitectura]]
