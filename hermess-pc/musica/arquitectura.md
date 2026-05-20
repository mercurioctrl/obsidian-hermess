# Arquitectura — musica

Descargador de playlists de YouTube a MP3. Un solo script Python sin dependencias pip.

## Flujo principal (`descargar_playlist.py`)

```
URL playlist
    ↓
get_playlist_info()      → yt-dlp --flat-playlist --dump-json
                           Obtiene todos los IDs sin descargar nada
    ↓
get_track_info()         → yt-dlp --dump-json (solo primer track)
                           Metadata completa para detectar artista/álbum
    ↓
extract_artist_album()   → Prioridad: artist > creator > uploader
                                       album > playlist_title > playlist
    ↓
Crea carpeta: base/Artista/Álbum/
    ↓
download_track() × N     → yt-dlp --no-playlist --extract-audio --audio-format mp3
                           --audio-quality 0 --embed-thumbnail --embed-metadata
```

## Estructura de salida

```
descargas/
  Artista/
    Álbum/
      01 - Título.mp3
      02 - Título.mp3
```

## Decisiones de diseño

- **`--flat-playlist` primero:** Evita descargar todo para saber cuántos tracks hay.
- **Metadata del primer track:** Solo se hace una consulta completa; el resto asume el mismo artista/álbum (playlist homogénea).
- **`--no-playlist` por track:** Evita que yt-dlp re-descargue la playlist entera al dar la URL individual de un video.
- **Sin paralelismo:** Procesamiento secuencial para no sobrecargar la conexión ni YouTube.
- **Solo stdlib:** No requiere pip; las dependencias son herramientas del sistema (yt-dlp, ffmpeg).

## Ver también

- [[hermess-pc/musica/musica|musica]] — Índice del proyecto
- [[hermess-pc/musica/stack|Stack]] — Dependencias del sistema
