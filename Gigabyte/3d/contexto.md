# Contexto — 3d

## Decisiones del usuario

### El logo va centrado en la placa, aunque lleve soportes

Le propuse mover las letras al ras de la cara trasera para poder imprimir acostado sin
soportes. Respondió: *"el tema es que a mi me gustaba que quede centrado"*.

**La versión centrada es la principal.** La variante al ras existe solo como alternativa
en un archivo aparte (`gigabyte_logo_sinsoportes.stl`), nunca como reemplazo. El costo
real de los soportes son ~1,5 g sobre 27 g de pieza. Ver [[memoria]].

### El "TM" se descarta

En el SVG flota arriba a la derecha de la E **sin tocar ninguna letra**: en 3D quedaría
suspendido en el aire (imprimible solo con soporte, y se caería) y sus trazos miden
~0,5 mm a escala real. Se controla con `DROP_TM` en `build_logo.py`.

### El corte de la versión en dos partes va en el hueco A|B

Nunca partiendo una letra. Es el hueco entre glifos más cercano al centro; el centro
exacto (165 mm de 330) caería dentro de la A.

---

## Por qué la versión centrada lleva soportes

Análisis capa por capa, rasterizado a 0,2 mm igual que hace el slicer. Con las letras
centradas y el cartel de pie hay **6 techos planos a 90°**:

| Letra | Voladizo | Altura | Apoyo |
|---|---|---|---|
| E, brazo superior | 9,8 mm | 28,2 mm | 1 lado |
| E, brazo medio | 9,2 mm | 19,0 mm | 1 lado |
| G y G, la lengüeta horizontal | 9,0 mm c/u | 27,4 mm | 1 lado |
| T, alas del travesaño | 5,2 y 5,4 mm | 28,0 mm | 1 lado |
| A y B, contraformas | 8,0 / 2,8 mm | — | **puente — salen bien** |

Las contraformas de la A y la B **no son problema**: están ancladas de los dos lados, el
slicer las hace como puente. Los que se descuelgan son los 6 anclados de un solo lado.

Costo: 1.492 mm² de contacto, altura media 8 mm (máx. 18,6), prisma de 12 cm³ →
**~1,5 g con soporte tipo árbol**. Todas las marcas quedan en caras que miran al piso.

**No se puede arreglar con chaflanes** sin romper la tipografía: los voladizos están en
el plano X-Z, que es exactamente la silueta frontal del logo. Cualquier material que los
sostenga se ve de frente. Por eso la única salida sin soportes es cambiar la orientación
de impresión, y eso exige mover las letras al ras (que es lo que se descartó).

---

## Lo que se probó y se descartó

- **Acostar la versión centrada** — da menos área de voladizo pero deja las letras
  flotando 5 mm sobre la cama. Peor, no mejor.
- **Chaflanes bajo los voladizos** — rompen la silueta frontal del logo (ver arriba).
- **Panel de fondo detrás de las letras** para poder acostarlo manteniendo el centrado —
  taparía las contraformas y los huecos entre letras; deja de ser un cartel de letras
  sueltas y pasa a ser un relieve.
- **Partir en dos por el medio exacto** — cae dentro de la A.
- **Poner las dos mitades a 45° en la misma placa** — a 45° cada una ocupa ~162 × 162 mm
  y entra una sola. A 0° miden 169 × 61 y entran las dos sin achicar nada.

---

## Límites de tamaño en la A1 mini

- **Una pieza:** 180 mm de largo es el máximo, y solo entra **girada 45°** (huella
  150,7 × 150,7 mm en la cama de 180 × 180).
- **Dos partes:** 330 mm. El límite lo pone la mitad izquierda (169,1 mm, el 51,2% del
  total por dónde cae el corte A|B). El máximo teórico son ~349 mm; se dejó en 330 para
  tener margen de brim.
- **Las dos en una tirada:** 169,1 × 139,4 mm a 0°, con 5,5 mm de margen en X y 20,3 en Y.
  **No necesita brim** — cada mitad apoya más de 10.000 mm² de placa base, y justamente
  por eso alcanzan los 5,5 mm. Si se quiere más aire: `TOTAL_LEN = 320` → 8 mm de margen.

---

## TODOs / próximos pasos

- [ ] **Imprimir y validar la junta.** Los pasadores son Ø7,3 en agujero Ø7,7 (0,4 mm de
      holgura diametral). El ajuste real no está probado: si quedan flojos o duros, tocar
      `PIN_CLEAR` en `build_2partes.py`.
- [ ] Confirmar que los 5,5 mm de margen en X de la placa conjunta no molestan con la
      línea de purga de la A1 mini.
- [ ] Si se quiere multicolor (el usuario ya hizo piezas de 4 colores para otras marcas),
      habría que separar el logo de la base en cuerpos distintos o pensar un encastre.

## Ver también

[[arquitectura]] · [[changelog]] · [[memoria]] · [[3d]]
