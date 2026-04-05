---
jira_key: "LIO-492"
aliases: ["LIO-492"]
summary: "API - Refactor - Listar el repositorio de cortos de video -> Agregar ultimos parámetro sobre el objeto existente para modelar objeto enriquecido"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2025-12-11 07:01"
updated: "2026-02-02 08:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-492"
---

# LIO-492: API - Refactor - Listar el repositorio de cortos de video -> Agregar ultimos parámetro sobre el objeto existente para modelar objeto enriquecido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-11 07:01 |
| Actualizado | 2026-02-02 08:10 |
| Etiquetas | ninguna |
| Jira | [LIO-492](https://bluinc.atlassian.net/browse/LIO-492) |

## Relaciones

- **Padre:** [[LIO-481 - Recomendaciones de loki|LIO-481]] Recomendaciones de loki
- **has action item:** [[LIO-491 - APP - Maquetado - Sección “Las recomendaciones de Loki” (grid + vista Clips|LIO-491]] APP - Maquetado - Sección “Las recomendaciones de Loki” (grid + vista Clips tipo ML)
- **has action item:** [[LIO-523 - API - Refactor - Utilizar informacion real de productos, con clip (video)|LIO-523]] API - Refactor - Utilizar informacion real de productos, con clip (video) vinculado 

## Descripcion

Actualmente el recurso:

```
GET {API_URL}/v4/yt/shorts?label=recomendaciones-de-loki
```

responde con un objeto simple por cada short:

```
{
  "data": [
    {
      "id": 1,
      "url": "https://www.youtube.com/shorts/jvaQbXXIa-k",
      "thumbnail": "https://img.youtube.com/vi/jvaQbXXIa-k/hqdefault.jpg"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 5
  }
}

```

Necesitamos refactorizar la respuesta para modelar un objeto más completo, pensando en la integración futura con datos reales de catálogo.

---

### Objetivo

Refactorizar **solo la estructura de la respuesta JSON** del endpoint, manteniendo la misma URL y comportamiento de paginación, pero devolviendo un objeto enriquecido por cada video.
En esta primera etapa **todos los campos nuevos estarán hardcodeados con datos de fantasía** (no hace falta conectarse a base de datos ni a otras APIs).

---

### Nuevo contrato de respuesta

La estructura final esperada es:

```
{
  "data": [
    {
      "videoId": "3mLvnaSEaLE",
      "platform": "youtube",
      "url": "https://www.youtube.com/shorts/3mLvnaSEaLE",
      "title": "🖐️ ¡El Mouse MÁS CÓMODO que vas a Usar! | Trust Bayo II para Decir Adiós al Dolor 🖱️",
      "description": "…",
      "thumbnailUrl": "https://i.ytimg.com/vi/3mLvnaSEaLE/maxresdefault.jpg",
      "publishedAt": "2025-12-11T09:03:07Z",
      "item": {
        "id": 731425,
        "sku": "TRUST-BAYO-II",
        "title": "Mouse Ergonómico Trust Bayo II",
        "url": "https://libreopcion.com/",
        "image": "https://libreopcion.com/path/to/bayo-ii.jpg",
        "price": {
          "listPrice": 25344.39,
          "discount": 0,
          "finalPrice": 25344.39
        },
        "sellerId": 53,
        "sellerName": "UltraBytes",
        "freeShipping": true,
        "instantFlash": false
      }
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 5
  }
}

```

---

### Detalle de cambios

**Campos antiguos (por cada item):**

- `id`


- `url`


- `thumbnail` (puede ser `null`)



**Campos nuevos (por cada item):**

Reemplazar / ampliar el objeto actual por:

- `videoId` **(nuevo, lo agregaremos en **`[LO].[dbo].[yt_videos]` ya que puede obtenerse de la API de google**)**


- `platform` **(nuevo)** – por ahora siempre `"youtube"`.


- `url` – se mantiene semántica, pero ahora dentro del objeto enriquecido.


- `title`  **(nuevo, lo agregaremos en **`[LO].[dbo].[yt_videos]` ya que puede obtenerse de la API de google**)**


- `description`  **(nuevo, lo agregaremos en **`[LO].[dbo].[yt_videos]` ya que puede obtenerse de la API de google**)**


- `thumbnailUrl` **(nuevo)** – reemplaza a `thumbnail`.


- `publishedAt`  **(nuevo, lo agregaremos en **`[LO].[dbo].[yt_videos]` ya que puede obtenerse de la API de google**)** 



Objeto anidado `item` **(completamente nuevo por ahora harcodeado con info falsa, ya veremos como conectarlo al repositorio de productos)**:

- `item.id` **(nuevo, poner un dato fantasía cualquiera, luego conectaremos al repositorio de productos)**


- `item.sku` **(nuevo, poner un dato fantasía cualquiera, luego conectaremos al repositorio de productos)**


- `item.title` **(nuevo, poner un dato fantasía cualquiera, luego conectaremos al repositorio de productos)**


- `item.url` **(nuevo, poner un dato fantasía cualquiera, luego conectaremos al repositorio de productos)** – link al producto.


- `item.image` **(nuevo, poner un dato fantasía cualquiera, luego conectaremos al repositorio de productos)**


- `item.price.listPrice` **(nuevo, poner un dato fantasía cualquiera, luego conectaremos al repositorio de productos)**


- `item.price.discount` **(nuevo, poner un dato fantasía cualquiera, luego conectaremos al repositorio de productos)**


- `item.price.finalPrice`**(nuevo, poner un dato fantasía cualquiera, luego conectaremos al repositorio de productos)**


- `item.sellerId` **(nuevo, poner un dato fantasía cualquiera, luego conectaremos al repositorio de productos)**


- `item.sellerName` **(nuevo, poner un dato fantasía cualquiera, luego conectaremos al repositorio de productos)**


- `item.freeShipping` **(nuevo, poner un dato fantasía cualquiera, luego conectaremos al repositorio de productos)**


- `item.instantFlash` **(nuevo, poner un dato fantasía cualquiera, luego conectaremos al repositorio de productos)**



---

### Reglas para esta primera versión

- **Todos los campos nuevos se deben completar con datos hardcodeados de fantasía.**

- Podés basarte en el ejemplo del ticket.


- No hace falta que coincidan exactamente, lo importante es que respeten **nombres de campos y tipos**.




- Mantener **tipos de datos coherentes**:

- `string` para `videoId`, `platform`, `url`, `title`, `description`, `thumbnailUrl`, `publishedAt`, `sku`, `sellerName`, etc.


- `number` para `id`, `listPrice`, `discount`, `finalPrice`, `sellerId`.


- `boolean` para `freeShipping`, `instantFlash`.




- Si hoy `thumbnail` puede venir `null`, asegurarse de que `thumbnailUrl` también pueda venir `null` en caso de necesitarlo.
