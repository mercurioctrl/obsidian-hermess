# Arquitectura — 3d

## Pipeline SVG → STL

1. **Parseo** del SVG con `svgelements` (`reify=True`, aplica transforms). Las curvas
   Bézier se aplanan a 48 segmentos.
2. **Cada glifo → polígono de Shapely.** Un glifo es *anillo exterior XOR contraformas*:
   se ordenan los anillos por área descendente y se hace `symmetric_difference`. Así
   salen bien los huecos de la A, la B y las dos G.
3. **Limpieza** (`clean_polygon`): quita vértices duplicados. Ver [[#Gotchas]].
4. **Normalización**: escala al ancho objetivo e invierte Y (el SVG mira hacia abajo).
5. **Extrusión** de cada glifo en Z, después rotación +90° sobre X para que el alto del
   logo pase a ser Z y la extrusión quede en Y → letras **de pie**.
6. **Unión booleana** (`manifold`) de las letras con la placa base. Las letras se hunden
   0,6 mm dentro de la placa para garantizar la fusión: el glifo "I" del SVG tiene la
   base 0,23 unidades más arriba que las demás letras y si no quedaría flotando.
7. **Posicionado en la cama** y export.

## Reglas de proporción (derivadas de `muestra.stl`)

`muestra.stl` es la referencia del cliente: un cartel "HP" de pie, 180 × 58,51 × 58,41 mm,
exportado ya girado 45°. De ahí salen las reglas que replica todo el proyecto:

| Regla | Valor |
|---|---|
| Fondo de extrusión de las letras | **= alto de las letras** (en la muestra, ratio 1,002) |
| Fondo de la placa | fondo de letras + 10 mm (5 mm de margen adelante y atrás) |
| Espesor de la placa | largo total / 18 |
| Margen del logo a los extremos | 5 mm |
| Orientación de export | ya girado 45° y centrado en la cama |

La muestra además tiene dos pasadores de Ø4 × 4 mm sobre la placa, de propósito poco
claro. **No se replicaron.**

## Los dos scripts

### `build_logo.py` — versiones de una pieza (180 mm)

`build(flush_back, nombre, maestro)` genera el cartel completo. Con `flush_back=False`
las letras van **centradas** en la placa (5 mm adelante y atrás); con `True` van al ras
de la cara trasera, que es lo que habilita imprimirlo acostado sin soportes.

Elige la orientación de laminado sola: acuesta la pieza **solo si el voladizo da
exactamente cero**, si no la deja de pie. Ver [[contexto#Por qué la versión centrada lleva soportes|contexto]].

### `build_2partes.py` — versión de 330 mm en dos mitades

- `make_sign(total_len)` — el cartel completo escalado.
- `corte_entre_letras()` — elige el **hueco entre glifos más cercano al centro** de la
  placa. Con GIGABYTE da el hueco **A|B** (el centro exacto caería dentro de la A), así
  que la junta es un corte recto en la base y **no parte ninguna letra**.
- Los agujeros de los pasadores se restan **antes** de partir, con un prisma que cruza el
  plano de corte: al cortar quedan automáticamente ciegos y simétricos en las dos mitades.
- `teardrop()` — los agujeros tienen perfil de **lágrima** (círculo + punta triangular
  arriba), no redondo. Se imprimen acostados y un agujero redondo se descuelga en el
  techo; después el pasador no entra.
- `placa_conjunta()` — pone las dos mitades a **0°** (no 45°), una detrás de la otra, con
  los pasadores en el hueco del medio.

## Verificaciones automáticas

Los scripts **verifican y reportan antes de exportar**. Si algo falla, abortan:

- `is_watertight` / `is_volume` de cada malla, y de cada letra al extruirla
- `check_overhangs()` — área de caras que miran hacia abajo a más de 45°, excluyendo la cama
- huella al girar 45° y margen al borde de la cama
- en la placa conjunta: que ninguna pieza se pise y que todas apoyen en z=0

## Gotchas

- **Vértices duplicados del SVG rompen la triangulación.** La "B" traía dos puntos
  idénticos (segmento de 1,4e-14 mm) y `extrude_polygon` devolvía una malla **no cerrada
  sin avisar**. Lo arregla `clean_polygon()`; el script aborta si una letra no queda estanca.
- **Centrar en la cama por caja envolvente, nunca por centroide.** Con el centroide la
  mitad izquierda daba 7,9 mm de holgura en vez de 8,8.
- **Elegir orientación por "menor área de voladizo" es engañoso.** Acostar la versión
  centrada daba *menos* área que de pie, pero deja las letras flotando 5 mm sobre la cama.
- `trimesh` necesita `rtree` para `contains()` y `section()`, y falla recién al usarlas.

## Ver también

[[contexto]] · [[stack]] · [[changelog]] · [[3d]]
