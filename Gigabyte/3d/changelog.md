# Changelog — 3d

## 2026-09-16 — Documentación y sincronización

- `README.md` y `CLAUDE.md` del repo: pipeline, reglas de proporción, los tres modelos,
  el análisis de voladizos y las trampas encontradas.
- Memoria del proyecto (4 notas) → ver [[memoria]].
- Primera sincronización de la bóveda. Se detectó que la **API de Obsidian volvió a
  responder 200**; el `CLAUDE.md` de [[../gigaErp/gigaErp|gigaErp]] la daba por caída
  (`000`) desde agosto de 2026.
- Se regeneraron `gigabyte_2p_pasadores.stl` y `gigabyte_2p_placa.stl`, que habían
  desaparecido del directorio entre sesiones.

## 2026-09-15 — Del SVG al STL: tres modelos y la versión en dos partes

**Análisis de `muestra.stl`.** Se descubrió que es un cartel "HP" de pie (180 × 58,51 ×
58,41 mm, ya girado 45°) y se derivaron las reglas de proporción que replica todo el
proyecto. Ver [[arquitectura#Reglas de proporción (derivadas de `muestra.stl`)|arquitectura]].

**Generador `build_logo.py`.** Pipeline SVG → polígonos Shapely → extrusión → unión
booleana → STL, con `svgelements` y `rtree` vendorizados para no depender de `pip`.

**Versión de una pieza (180 mm).** Logo de 170 × 23,1 mm, extrusión 23,1, base
180 × 33,1 × 10. Malla estanca, 106,9 cm³, trazo más fino ~4 mm. Se descarta el **TM**
(flota en el aire y mide ~0,5 mm).

**Análisis de voladizos.** Se había afirmado que imprimía sin soportes; al verificarlo
capa por capa aparecieron **6 techos planos a 90°** (brazos de la E, lengüetas de las G,
alas de la T). Las contraformas de la A y la B sí salen bien, son puentes. Costo real:
~1,5 g de soporte sobre 27 g de pieza. Ver [[contexto#Por qué la versión centrada lleva soportes|contexto]].

**Variante sin soportes.** Con las letras al ras de la cara trasera se puede imprimir
acostado: 0 mm² de voladizo, verificado sobre la malla. **El usuario prefirió el
centrado**, así que la variante quedó como alternativa en archivo aparte.

**Versión en dos partes (330 mm, 1,83×).** Corte en el hueco **A|B**, sin partir ninguna
letra. Junta con dos pasadores Ø7,3 × 23 mm y agujeros ciegos de 12 mm con perfil de
**lágrima** para que no se descuelgue el techo. Cada mitad entra girada 45°.

**Placa conjunta.** Las dos mitades **a 0°** (no 45°) entran las dos en la misma cama:
169,1 × 139,4 mm, con los 3 pasadores en el hueco del medio. **Sin achicar nada.**

**Bugs corregidos en el camino:**
- Vértices duplicados en la "B" → `extrude_polygon` devolvía malla no cerrada sin avisar.
- Centrado en la cama por centroide en vez de por caja envolvente → desperdiciaba margen.
- El selector de orientación elegía "acostado" para la versión centrada porque el área de
  voladizo daba menor, pero eso deja las letras flotando 5 mm sobre la cama.

## Ver también

[[arquitectura]] · [[contexto]] · [[3d]]
