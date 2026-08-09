# 404 Videos Page

Página de error **404** con fondo de videos rotando en loop, estética "touch some grass".
Hecha para [[Blu|BLU Studio]] (usa su logo). Los clips los fue pasando **Catriel M.** por WhatsApp (posts de X/Twitter, arte generativo/motion).

## Qué es

- `index.html` autónomo (sin build ni servidor): abre con `file://` y anda.
- Fondo: los `.mp4` a pantalla completa (`object-fit: cover`), en **orden aleatorio** y encadenados — al terminar un clip arranca el siguiente. Loop infinito sobre toda la lista.
- **Crossfade** entre clips con doble buffer de `<video>` (`vidA`/`vidB`, fundido de 0.8s), fondo cálido `#0d0b09` de respaldo (nunca negro puro).
- Overlay estilo referencia: logo **BLU** (SVG inline, blanco) arriba, un **404** grande y etéreo (`mix-blend-mode`), divisor con puntito, subtítulo *"Before you head back, touch some grass."* y botón **Go Back** (`history.back()`).
- Abajo a la derecha muestra el **@usuario** del clip que está sonando (sacado del nombre de archivo). Puramente cosmético.
- Va **muteado** (autoplay del navegador no permite audio).

## Ubicación

- Carpeta local: `~/Descargas/x-videos/`
- 30 videos (.mp4), ~113 MB. Un poster (frame `.jpg`) por video en `posters/`, mismo nombre base; el HTML los usa como placeholder durante el crossfade.
- `urls.txt` — enlaces originales de X (histórico del batch inicial).
- `blu-logo-orig.svg` — logo vectorial de BLU (también incrustado inline en el HTML).
- **`CLAUDE.md`** en la carpeta — tiene el workflow completo, las convenciones (no romper) y la config de Obsidian. Leerlo antes de tocar; con eso `/sincronizar-boveda` detecta esta carpeta sola (no re-pregunta).

## Cómo agregar un video (workflow)

`yt-dlp` con plantilla `%(uploader_id)s_%(id)s.%(ext)s`. El nombre lleva la cuenta que **posteó** el tweet (metadato de X), que no siempre es el autor original — cuando el tweet cita/repostea, yt-dlp baja el video fuente (por eso hay nombres con ID distinto al del tweet). No genera duplicados aunque el mismo uploader aparezca varias veces con ids distintos.

```bash
cd ~/Descargas/x-videos
# 1. bajar
yt-dlp -o "%(uploader_id)s_%(id)s.%(ext)s" --no-warnings "<url-del-tweet>"
# 2. generar poster (mismo nombre base, frame representativo)
f="NOMBRE.mp4"; ffmpeg -y -i "$f" -vf thumbnail -frames:v 1 "posters/${f%.mp4}.jpg"
# 3. agregar el nombre del .mp4 al final del array `videos` en index.html
```

## Créditos (uploaders)

basepaint_xyz · Blondie23LMD · Bombadiluss · doortodivinity · dr_version_ · ex_mortal_ · hal_chemy · _hoodLink_ · ingi_erlingsson · JteveSob · _juanrg92 · kattlatte · leonardofed · luizandregama · MaNiCArt_ · nebulica · neomechanica · ojovivoMotion · PERFECTL00P · sinusoidalsnail · TTTVVV666 · xeriesjame_art

## Para verla

```bash
xdg-open ~/Descargas/x-videos/index.html
```

## Ver también

- [[Catirel]]
