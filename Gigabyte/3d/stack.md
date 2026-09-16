# Stack — 3d

Proyecto de generación de geometría 3D por código. No hay build system ni package
manager: son dos scripts de Python que se corren a mano.

```bash
python3 build_logo.py      # las dos versiones de una pieza
python3 build_2partes.py   # dos mitades + pasadores + placa conjunta
```

## Dependencias

| Paquete | Para qué |
|---|---|
| `numpy` 2.4 | transformaciones, análisis de mallas |
| `trimesh` | mallas, extrusión, booleanas, export STL |
| `shapely` 2.1 | polígonos 2D del logo, contraformas, erosión para medir trazos |
| `manifold3d` | motor de booleanas (unión base+letras, corte en dos, agujeros) |
| `mapbox_earcut` | triangulación de los polígonos al extruir |
| `matplotlib` | los `preview*.png` |

## Vendorizado en `vendor/`

Se incluyen en el repo para que los scripts corran sin `pip install` (el sistema tiene
`PEP 668`, no deja instalar con `--user`):

- **`svgelements` 1.9.6** — parseo del SVG y aplanado de curvas Bézier
- **`rtree` 1.4.1** — `trimesh` lo necesita para `mesh.contains()` y `mesh.section()`;
  sin él tira `ModuleNotFoundError` recién al usar esas funciones, no al importar

## Destino

**Bambu Lab A1 mini** — cama 180 × 180 × 180 mm. Se lamina en **Bambu Studio**.
Los STL se exportan **ya posicionados en la cama** (girados y centrados), así que se
cargan y no hay que mover nada.

## Ver también

[[arquitectura]] · [[3d]]
