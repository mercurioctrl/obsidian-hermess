# APP - Fix - Tooltip de código postal aparece al cargar el sitio

**Proyecto:** [[Libre Opcion/Libre Opcion|Libre Opcion]]
**Estado:** Pendiente
**Fecha:** 2026-04-08

---

## Descripción

Cuando un usuario entra al sitio sin tener un código postal confirmado (por ejemplo, primera visita o sesión limpia), aparece automáticamente un tooltip/popover con el texto **"Estamos calculando tus envíos a este código postal"** apenas hidrata el cliente.

Es un defecto visual molesto:

- Salta solo, sin que el usuario haga nada.
- Roba foco visual a la home (banner principal, productos destacados).
- Aparece encima del header, justo al lado del pin de "Recibílo en".
- Se dispara en cada visita nueva mientras no se confirme el CP o se postergue con "Más tarde".

**Cómo reproducirlo:** abrir el sitio en una ventana de **incógnito** (así no hay `localStorage` con `expiresShowModal` ni cookie de sesión) y observar cómo el tooltip aparece automáticamente al terminar de cargar la home.

## Criterios de aceptación

- [ ] Al entrar al sitio por primera vez (incógnito), el tooltip **no debe aparecer automáticamente** apenas carga la página.
- [ ] El usuario tiene que poder seguir confirmando su código postal cuando él lo decida (clic en el pin de "Recibílo en"), sin que esa funcionalidad se rompa.
- [ ] Si se decide mostrarlo de forma diferida (ej: a los X segundos, al hacer scroll, o solo en ciertas páginas), definirlo y dejar el criterio asentado.
- [ ] La solución no debe causar CLS extra ni reintroducir FOUC en el header.
- [ ] Probado en incógnito en desktop y mobile.

## Notas técnicas

- Componente involucrado: `app/components/Layouts/Cabecera/partials/Envios.vue`.
- El tooltip vive dentro de un `<ClientOnly>` y se renderiza con `v-if="isShowModal"`.
- `isShowModal` se calcula a partir de `expiresShowModal` del store `setting/zipCode`:
  - Si el usuario no está logueado y **no hay** `expiresShowModal` guardado → se muestra.
  - Si está logueado pero no tiene `codigoPostalDefault` y no hay `expiresShowModal` → se muestra.
  - El botón "Más tarde" setea `expiresShowModal = new Date()` y agrega 24h de gracia tras confirmar el CP.
- Por eso en incógnito siempre dispara: no hay nada persistido todavía.
- Posibles enfoques (a discutir antes de implementar):
  1. **Diferir la primera aparición:** no mostrar nunca en el primer pageview; recién mostrar a partir de la segunda navegación, o tras N segundos / scroll del usuario.
  2. **Sembrar `expiresShowModal` con un valor inicial corto** al primer load para que la primera visita no lo dispare.
  3. **Mover la decisión a un trigger explícito** (ej: solo cuando el usuario interactúa con el pin del header).
- Cuidado con el orden de hidratación: el componente está dentro del header, así que cualquier cambio de altura podría reabrir problemas de CLS recientes (ver [[06-fix-cls-tbt-ronda-2]] y [[07-fix-cls-mobile-h1-sr-only-ronda-3]]).
- Verificar también que no rompa la lógica del modal de confirmación de CP (`#modalDomicilioEnvio`), que comparte el mismo componente.

## Ver también

- [[Libre Opcion/Libre Opcion|Índice del proyecto]]
- [[00-resumen-diagnostico-seo-performance]]
- [[Libre Opcion/tareas/APP - Refactor - Migrar cotización de envíos de API legacy a v4|APP - Refactor - Migrar cotización de envíos de API legacy a v4]]
