# contexto

## Objetivo
Llevar el logo **ADATA PARADISE — Brasil 2026** a impresión 3D multicolor en una **A1 mini + AMS lite**, y derivar objetos (posavasos, cartel de maceta).

## Impresora / restricciones
- Cama **180×180 mm**. AMS lite = **4 filamentos automáticos**; >4 → pausas manuales.
- Piezas planas: se imprimen acostadas, relieve hacia arriba, **sin soportes**.

## Gotchas descubiertos (importante para retomar)
- **Flatpak sandbox:** Bambu (Flatpak) solo accede a `home`. Archivos en `/var/www/adata` **NO cargan** ("no se puede cargar el archivo"). → Copiar entregables a **`~/Descargas/adata_3d/`** e importar desde ahí con el diálogo (no arrastrar).
- **3MF de trimesh:** mete la extensión *production* (`p:UUID`) y Bambu lo rechaza. → Usar el **exportador 3MF propio** core-spec (ver [[arquitectura]]).
- **Cuantización:** incluir negro en la paleta metía agujeros en las zonas oscuras del degradado del colibrí. → Forzar el foreground (`gray>=30`) a color; negro solo para el fondo real.
- **int16 overflow:** al cuadrar diferencias RGB (245²) desborda `int16` y da colores basura. → `int32`.
- **Mallas no-estancas:** polígonos con huecos fallan al triangular. → `buffer(0.02).buffer(-0.02)`.
- **Bambu no auto-asigna filamentos** desde el 3MF: hay que asignar filamento por objeto/pieza a mano.

## Piezas y medidas
- **Placa plana 4 colores** (negro/blanco/rojo/azul) — 170×139,6×2,8 mm. El arcoíris del colibrí se resuelve como rojo+azul.
- **Encastre A1 mini** — versión partida/encastrable.
- **Posavasos redondo** — Ø95 mm, base 3 mm + rim 1,5 mm, relieve 1,2 mm. Negro + blanco. Lettering original del logo (sin "BRASIL 2026") + 3 palmeras proc.
- **Posavasos arcoíris** — palmeras con el degradado del logo en 6 bandas → **8 filamentos** (negro, blanco, violeta, azul, verde, amarillo, naranja, rojo). No es 100% automático en AMS lite.
- **Cartel maceta** — fondo negro **calado** que copia la forma de las letras + **pinche**. Huecos de la **D** y las dos **A** junto a la **T** rellenos (base negra). Palito final **138 mm** (2,3× el original) × **14 mm** de base. **Alto total 180 mm** = límite de la cama → imprimir **en diagonal**.

## Próximos posibles ajustes
- Reforzar el pinche (más grosor 5–6 mm o nervadura) si flexa.
- Variante del posavasos con menos colores para AMS 100% automático.

## Ver también
[[arquitectura]] · [[stack]] · [[changelog]] · [[adata-paradise-3d]]
