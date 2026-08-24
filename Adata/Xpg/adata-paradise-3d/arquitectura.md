# arquitectura

Pipeline para convertir una imagen de logo (`ada.jpeg`, 736×1600) en un modelo 3D **multicolor imprimible** en FDM. Todo programático, sin CAD manual.

## Pipeline general (imagen → 3MF)

1. **Recorte y limpieza** — bounding box de píxeles no-negros (`gray > 30`), se borra el iconito de "escanear" de la captura.
2. **Cuantización de color** — reducir a paleta de N colores.
   - Con `argmin` de distancia euclídea RGB a la paleta objetivo.
   - **Regla clave:** el negro solo se asigna al **fondo real** (`gray < 30`); todo lo que es logo (`gray >= 30`) se fuerza a un color no-negro. Si no, las zonas oscuras del degradado quedaban asignadas a negro → agujeros en el modelo. Ver [[contexto]].
3. **Máscara por color** — una máscara binaria por filamento, con `morphologyEx` (open+close) para quitar motas.
4. **Vectorización** — `cv2.findContours(RETR_CCOMP)` para obtener contornos externos + huecos, `approxPolyDP` para simplificar.
5. **Polígonos** — `shapely.Polygon(shell, holes)`, `unary_union`, y **`buffer(0.02).buffer(-0.02)`** para regularizar (arregla mallas no-estancas al triangular polígonos con huecos).
6. **Extrusión** — `trimesh.creation.extrude_polygon` por isla, apiladas en Z.
7. **Exportar 3MF a mano** (core-spec) — ver más abajo.

## Geometría multicolor (relieve por capas)

- **Base** (negro): prisma de todo el footprint, `z = 0 .. BASE`.
- **Caps de color** (blanco/rojo/azul/…): footprint de cada máscara, `z = BASE .. BASE+CAP` (relieve ~0,8–1,2 mm).
- El fondo negro queda al nivel de la base; texto y figuras suben en relieve. Espalda y cantos negros → limpio.
- El AMS cambia de filamento **por capa** dentro de la zona de relieve (automático hasta 4 colores).

## Exportador 3MF propio

`trimesh` exporta 3MF con la extensión *production* (`p:UUID`, namespaces extra) que **Bambu Studio a veces rechaza** ("no se puede cargar el archivo"). Solución: escribir el 3MF a mano como zip con:
- `[Content_Types].xml`, `_rels/.rels`, `3D/3dmodel.model`
- Solo core-spec + extensión *material*: `<basematerials>` con `displaycolor`, un `<object>` por color, y `<build>` con un `<item>` por objeto (transform identidad → todo alineado).
- Resultado: 1 objeto por color, ya coloreado; el usuario asigna filamento por pieza en Bambu.

## Variantes específicas

- **Posavasos** — base circular (`shapely Point.buffer`) + anillo/rim (diferencia de círculos) elevado; relieve blanco de texto+palmeras. Palmeras dibujadas proceduralmente (tronco curvo + fronds con droop + cocos) en `cv2.fillPoly`.
- **Posavasos arcoíris** — el degradado del logo se aplica a las palmeras dividiendo la silueta en 6 bandas diagonales (violeta→azul→verde→amarillo→naranja→rojo), una máscara/pieza por color.
- **Cartel maceta (calado)** — el fondo negro es un **dilate** fino (~1,8 mm) de las letras (contorno que las abraza); huecos internos abiertos = calado; **rieles** finos en la base de cada palabra + spine central mantienen 1 sola pieza; **pinche** triangular hacia abajo. Se pueden rellenar huecos concretos con `RETR_EXTERNAL`.

## Ver también
[[stack]] · [[contexto]] · [[changelog]] · [[adata-paradise-3d]]
