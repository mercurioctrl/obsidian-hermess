# Arquitectura

Parte de [[portal]].

## Por qué SPA

`ssr: false` porque **todo el portal es autenticado**: no hay nada que prerenderizar ni indexar.
Simplifica el deploy (estático detrás de nginx) y evita proxear el token por servidor.

## Estructura

```
portal/
├── components/       UI propia: tablas, precios, stock, cantidad, estados, logo
├── composables/
│   ├── useApi.ts        Cliente HTTP + token
│   ├── useFormat.ts     Moneda, fechas, números
│   └── useSections.ts   Registro de secciones
├── layouts/          default (sidebar + topbar), blank (login/recuperación)
├── middleware/       auth.global, sections.global
├── pages/            Una por sección
├── stores/           auth, cart, ui
└── types/api.ts      Tipos espejados de los DTO del backend
```

## Patrones

### Todo pasa por `useApi()`

Único punto de entrada a la API: adjunta el `Bearer`, normaliza errores (la API devuelve
**strings JSON planos**, no objetos) y maneja el 401. Tiene un método aparte, `catalogue()`,
por la trampa de la barra final — ver [[api-nbe#La barra final]].

### Tipos espejados, no renombrados

`types/api.ts` replica los DTO del backend **con sus nombres originales**, para que todo sea
rastreable contra `src/Dto/` del PHP. Cuando un nombre confunde (`amountInCart` es la cantidad
de la línea) va un comentario al lado, no un rename.

### Registro único de secciones

`composables/useSections.ts` es la fuente de la navegación. De ahí salen el menú, el middleware
que bloquea rutas y los enlaces cruzados entre páginas. Agregar una página = crear el `.vue` +
agregar la entrada ahí. Ver [[configuracion#Secciones activables]].

### Moneda e IVA como preferencia de vista

La API cotiza **siempre en dólares** y expone la cotización. El portal convierte a pesos solo
para mostrar; el TC real se congela al confirmar, del lado del backend.

### `DataState` para listados

Un componente envuelve los cuatro estados —cargando, error, vacío, datos— para no repetir la
estructura en diez páginas y para que el vacío siempre tenga texto útil y una acción.

## El carrito vive en la API

No en el navegador: es una tabla del ERP (`contenidoCarritos`), así que sobrevive sesiones y
equipos. El store de Pinia es un espejo — cada mutación recarga el carrito completo en vez de
actualizar el estado local. Una request de más, pero garantiza que lo que se muestra es lo que
la API va a usar al confirmar.

> **Ojo:** las instancias de NB y NBE comparten base de datos, así que el carrito es el mismo.
> Probar apuntando a una y después a la otra deja artículos de una empresa con precios de la otra.

## Ver también

- [[stack]] · [[api-nbe]] · [[configuracion]] · [[marca]]
