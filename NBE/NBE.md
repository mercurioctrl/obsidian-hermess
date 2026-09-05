# NBE — NB Electric

Unidad de material eléctrico del grupo New Bytes. Opera como **companyCode 9** dentro del ERP
compartido, con su propia instancia de API (`api.nbe.com.ar`) y su propio depósito (almacén 8).

Catálogo: 1.342 artículos, 27 marcas (ABB, CHINT, LS Electric, Elibet, AEA, Macroled…) y 50
rubros de material eléctrico.

---

## [[portal/portal|Portal B2B]]
Portal de autogestión para clientes mayoristas: catálogo con precios propios, carrito
persistente, checkout con orden de compra y cotización de envío, y seguimiento del pedido línea
por línea. Nuxt 3 SPA sobre la API REST existente.

Repo: [New-Bytes/nbelectric-portal](https://github.com/New-Bytes/nbelectric-portal) (privado).
- [[portal/stack|Stack]] — Nuxt 3 · Tailwind · Pinia
- [[portal/arquitectura|Arquitectura]] — SPA, patrones, registro de secciones
- [[portal/api-nbe|La API]] — endpoints y **las trampas que costaron debugging**
- [[portal/contexto|Contexto]] — de dónde salió y qué se decidió
- [[portal/configuracion|Configuración]] — entorno, secciones activables, empresa
- [[portal/marca|Marca]] — logo, paleta y tipografía tomados de nbe.com.ar
- [[portal/estado|Estado]] — hecho, sin verificar, bloqueado por backend
- [[portal/changelog|Changelog]] · [[portal/memoria|Memoria]]

---

## Relación con [[NB]]

Comparten la misma base de datos del ERP, incluido el carrito (`contenidoCarritos`). Lo que las
separa es el `companyCode` que cada instancia de API lee de su `.env`, no un parámetro de
request. Ver [[portal/configuracion#Empresa NB vs NBE]].

---
Última sincronización: 2026-09-05
