---
jira_key: "LIO-491"
aliases: ["LIO-491"]
summary: "APP - Maquetado - Sección “Las recomendaciones de Loki” (grid + vista Clips tipo ML)"
status: "En curso"
type: "Tarea"
priority: "Lowest"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-11 06:26"
updated: "2025-12-23 10:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-491"
---

# LIO-491: APP - Maquetado - Sección “Las recomendaciones de Loki” (grid + vista Clips tipo ML)

| Campo | Valor |
|-------|-------|
| Estado | En curso (En curso) |
| Tipo | Tarea |
| Prioridad | Lowest |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-11 06:26 |
| Actualizado | 2025-12-23 10:19 |
| Etiquetas | ninguna |
| Jira | [LIO-491](https://bluinc.atlassian.net/browse/LIO-491) |

## Relaciones

- **Padre:** [[LIO-481 - Recomendaciones de loki|LIO-481]] Recomendaciones de loki
- **action item from:** [[LIO-483 - API - Refactor - Obtener los vídeos desde la base de datos|LIO-483]] API - Refactor - Obtener los vídeos desde la base de datos
- **action item from:** [[LIO-492 - API - Refactor - Listar el repositorio de cortos de video - Agregar ultimos|LIO-492]] API - Refactor - Listar el repositorio de cortos de video -> Agregar ultimos parámetro sobre el objeto existente para modelar objeto enriquecido

## Descripcion

La idea básica es poder maquetar un apartedo para navegar las **recomendaciones de Loki** en formato catálogo de videos cortos y poder ver cada clip en una vista vertical full-screen, con la ficha del producto asociada, para descubrir y comprar tecnología de una forma más entretenida y similar a como la gente navega en tik-tok, ig o MercadoLibre Clips.

Solo que en este casoi tendré dos vistas posibles una mas pensada para navegar desktop y otra para navegar mobile ya que buscamos atacar una idea muy especifica de como la gente consume en cada dispositivos este tipo de catálogos de video cuidando que sea fluido y adaptado a cada tipo de dispositivo para poder retener su atención.

---

Como aun estamos trabajando en el recurso y el contenido, la idea es tener lista la maqueta  bien lograda, ya que es un buen desafió de UX que debe ser cuidado.
Podes obtener mientras ejemplos de la API de yt directamente aca 

curl -X GET "[https://www.googleapis.com/youtube/v3/playlistItems?key=AIzaSyDqHlYjxQ0TFKwvMJ2y30Y17004U6LwDMs&playlistId=PLsJlL8wo5JgaIoKUS9aZJ1DMK3WeO9Goc&part=snippet&maxResults=25](https://www.googleapis.com/youtube/v3/playlistItems?key=AIzaSyDqHlYjxQ0TFKwvMJ2y30Y17004U6LwDMs&playlistId=PLsJlL8wo5JgaIoKUS9aZJ1DMK3WeO9Goc&part=snippet&maxResults=25)"

### Ejemplo de como sera el recurso terminado:

```
{
  "data": [
    {
      "videoId": "3mLvnaSEaLE",
      "platform": "youtube",
      "url": "https://www.youtube.com/shorts/3mLvnaSEaLE",
      "title": "🖐️ ¡El Mouse MÁS CÓMODO que vas a Usar! | Trust Bayo II para Decir Adiós al Dolor 🖱️",
      "description": "¿Cansado de la Tendinitis?\nDurante años, arrastramos la costumbre de usar el mouse con la mano plana sobre la mesa, un hábito que viene desde los viejos mouse de bolita. Pero nuestra mano está diseñada para ir de costado, en una posición más natural.\n\nLa Revolución de la Ergonomía\n\nEl Trust Bayo II Ergonomic está aquí para cambiar eso. Con su diseño vertical, logra un ángulo de 57°, la inclinación exacta requerida por la certificación ergonómica Ergocert.Este ángulo es clave para reducir al mínimo la tensión en la muñeca. Si pasás horas trabajando frente a la PC, vas a notar una diferencia impresionante en tu comodidad\n\n🛍Podés adquirirlo 👉🏻https://libreopcion.com/\n\n🔎Seguinos en Nuestras Redes \n👉🏻http://www.instagram.com/libreopcion\n👉🏻http://www.facebook.com/libreopcion\n👉🏻http://www.twitter.com/libreopcioncom\n\n✅ Sucribite a Nuestro Canal \n👉🏻http://www.youtube.com/c/libreopcion\n\n🕹La Manera más Simple de Comprar Tecnología\n👉🏻http://www.libreopcion.com \n\n😁 te gustó el video Dale LIKE y Dejanos tu Comentario😁",
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
    },
...
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 5
  }
}


```

---

## A. Vista grid pensada para desktop: `/recomendaciones-de-loki`

**Objetivo:** que se vea parecido al grid de YouTube Shorts (primera y segunda imagen). Este catalogo tipo “desktop” si bien tiene vista mobile permite apreciar una grilla y reproducir el video sin salir de ella.

**Requerimientos:**

- Nueva ruta `https://libreopcion.com/recomendaciones-de-loki`.


- Título visible: **“Las recomendaciones de Loki”**.


- Debajo, un texto corto (ej. “Explorá en video las recomendaciones de Loki para tu próximo producto tech.”).


- Mostrar los videos en una **grilla de tarjetas verticales**:

- Mobile: 2 columnas.


- Desktop: 3–4 columnas.




- Cada tarjeta muestra:

- Thumbnail vertical (`high` o `maxres`).


- Título (truncado en 2 líneas).


- Badge de **“Envío gratis”** si esta disponible.


- Precio actual y, si corresponde, precio tachado y % off (descuento flash).


- Botones:

- **Corazón**: “Agregar a favoritos”.


- **Compartir**: abre el share nativo  o copia link.


- CTA (texto tipo **“Ver producto”**) que abre `productUrl` en nueva vista/pestaña.






- El orden por ahora puede ser el mismo de la lista o por “más recientes”.


- Al tocar/clickear una tarjeta:



[adjunto]
[adjunto]
## B. Vista Clips pensada para mobile (La mas importante): `/recomendaciones-de-loki/clips`

**Objetivo:** que se vea y se use como los Clips de Mercado Libre (tercera imagen), sobre todo en mobile.

**Requerimientos:**

- Nueva ruta `https://libreopcion.com/recomendaciones-de-loki/clips`.


- **Mobile first**:

- Cada clip ocupa **toda la altura disponible** (video en vertical).


- Gestos de **swipe vertical**:

- swipe arriba → siguiente video


- swipe abajo → video anterior




- Transición fluida, sin recargar toda la página (uso de slider/gestos JS).




- Estructura visual:

- Video vertical full-screen (background principal).


- Overlay central de mute/unmute (icono).


- En la parte inferior, una **card de producto** flotante estilo ML:

- Imagen del producto (si está disponible).


- Título del producto.


- Precio actual y, si corresponde, precio tachado y % off (descuento flash).


- Badge de **“Envío gratis”** si esta disponible.


- Botones:

- **Corazón**: “Agregar a favoritos”.


- **Compartir**: abre el share nativo o copia link.


- CTA (texto tipo **“Ver producto”**) que abre `productUrl` en nueva vista/pestaña.








- Si el usuario entra o va “swipeando” debe iniciar la reproducción del video.


- El video se debería **autoplay** (muteado) al entrar al clip, con loop o sólo reproducción normal; tap para pausar/reanudar.


- Precarga ligera:

- Cuando estoy viendo un clip, intentar tener el siguiente ya listo para que el swipe sea fluido (sin pantalla negra).





[adjunto]
