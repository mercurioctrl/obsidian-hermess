# Contexto — muestra-fravega

## Qué es la activación
Evento en **Frávega**: se muestran **dos monitores**, uno a **200Hz** y otro a **60Hz**,
corriendo la misma animación. La gente los mira y **adivina cuál es cuál**. GIGABYTE es la
**marca** que hace la muestra; Frávega es el **retailer** ("Presentado en Frávega").
Sin premio, "solo la satisfacción de tener buen ojo gamer".

## Reglas / requisitos importantes
- **El copy final es 200Hz vs 60Hz** (arrancó como 144 y se corrigió a 200 en toda la web).
- Para que el test sea válido, el monitor rápido debe estar **realmente a 200Hz** en el SO
  y Chrome en **pantalla completa** (respeta el refresh). Si vsync fuerza 60, se ven iguales.
- **Verificación del operador**: tecla **I** muestra el **FPS real** en pantalla → confirmar
  que cada monitor marca ~200 y ~60 **antes** de arrancar (dejar oculto durante el juego).

## Decisiones tomadas en la sesión
- Se abandonó la estela con glow difuso (disimulaba el salto) → **objeto sólido nítido**.
- La instrucción al público pasó a **"seguí la bola/el personaje con la vista"** (smooth
  pursuit es lo que revela el juddering del 60Hz).
- El objeto puede ser una **bola** (`pura.html`) o el **personaje águila** que corre y deja
  la estela (`gemini-code-…html`).
- Logos agrandados 1.5× y logo Frávega cambiado al **oficial** procesado para dark.

## TODOs / cosas abiertas
- Definir **cuál versión se usa** finalmente en el evento: bola pura vs personaje.
- Evaluar dejar **`path=h` (horizontal)** por defecto — suele hacer más obvia la diferencia.
- (Opcional) botón visible de "otra vez" / contador de aciertos en `index.html`.

## Ver también
- [[arquitectura]] · [[muestra-fravega]]
