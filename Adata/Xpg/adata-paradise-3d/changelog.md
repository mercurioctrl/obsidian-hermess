# changelog

## 2026-08-22

- Placa plana **multicolor 4 colores** del logo ADATA PARADISE (negro/blanco/rojo/azul), 170×139,6×2,8 mm. Pipeline imagen→cuantización→vectorización→relieve. Archivos: `ADATA_PARADISE_4color.3mf`, `ADATA_PARADISE.3mf`, `part_*.stl`.
- **Fix carga en Bambu:** era el sandbox de Flatpak (solo lee `home`) → copiar entregables a `~/Descargas/adata_3d/`.
- **Exportador 3MF propio** core-spec (Bambu rechazaba el 3MF de trimesh por la extensión *production*).
- **Fix "parte faltante":** el cuerpo del colibrí quedaba con agujeros → forzar foreground a color, negro solo al fondo.
- Versión **encastre A1 mini** (`ADATA_PARADISE_A1_MINI_encastre.3mf`, `ADATA_PARADISE_encastre/`).

## 2026-08-23

- **Posavasos redondo** Ø95 mm, negro + blanco, con 3 palmeras procedurales + texto (`ADATA_POSAVASO.3mf`).
- Reemplazado el texto tipeado por el **lettering original** del logo (extraído de `mask_white.png` / `part_white.stl`); quitado el subtítulo "BRASIL 2026".
- **Posavasos arcoíris** — degradado del logo aplicado a las palmeras en 6 bandas, 8 filamentos (`ADATA_POSAVASO_RAINBOW.3mf`).
- **Cartel para maceta** — fondo negro que copia la forma de las letras + pinche (`ADATA_MACETA.3mf`).
- Iterado a **calado fino**: contorno ~1,8 mm que abraza las letras, huecos internos abiertos, rieles para mantener 1 pieza.
- Rellenados los huecos de la **D** y las dos **A** junto a la **T** (base negra).
- Palito rehecho: **2,3× más largo (138 mm)** y **más angosto (14 mm base)**. Alto total 180 mm (límite A1 mini → imprimir en diagonal).

Archivos principales: `/var/www/adata/*.3mf`, entregables en `~/Descargas/adata_3d/`.

## Ver también
[[changelog]] ← [[arquitectura]] · [[contexto]] · [[adata-paradise-3d]]
