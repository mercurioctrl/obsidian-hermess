---
jira_key: "LIO-581"
aliases: ["LIO-581"]
summary: "APP - Feat - Ficha de edición de producto -> Agregar descripción del producto"
status: "Ready for QA"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-03-25 09:12"
updated: "2026-03-31 09:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-581"
---

# LIO-581: APP - Feat - Ficha de edición de producto -> Agregar descripción del producto

| Campo | Valor |
|-------|-------|
| Estado | Ready for QA (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-25 09:12 |
| Actualizado | 2026-03-31 09:41 |
| Etiquetas | ninguna |
| Jira | [LIO-581](https://bluinc.atlassian.net/browse/LIO-581) |

## Relaciones

- **Padre:** [[LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **action item from:** [[LIO-580]] API - Feat - Ficha de edición de producto -> Agregar descripción del producto

## Descripcion

## Descripción

Como vendedor, quiero poder escribir y formatear una descripción personalizada de mi producto desde la ficha de edición, para agregar información destacada, estilo y hasta imágenes mediante URL.

---

## Contexto

Esta historia **continúa** la ficha de edición (`FichaProducto.vue`) ya tiene una sección "Descripción" con una maqueta deshabilitada y el badge "Próximamente":

El backend expone el siguiente endpoint (ya implementado en historia de backend correspondiente):

```
PATCH /api/v4/inventories/products/{id}/list
Authorization: Bearer <token>
​
Body: { "customDescription": "<p>HTML del editor</p>" }
      { "customDescription": null }   ← borra la descripción
```

El campo `customDescription` se puede combinar con otros campos del mismo PATCH (el endpoint lo soporta).

---

## Opciones de editor — Investigar antes de implementar

El dev asignado debe evaluar las siguientes opciones y elegir la más adecuada antes de escribir código. Se listan en orden de menor a mayor esfuerzo de integración.

---

### Opción A — `vue-quill-editor` (Quill 1.x)

**Estado:** ya instalado en `node_modules`. Cero instalación.

|  |  |
| --- | --- |
| **Pros** | Zero setup; funciona con Vue 2; ampliamente documentado; toolbar configurable |
| **Contras** | Quill 1.x está en mantenimiento desde 2019 (sin releases activos); el botón de imagen abre un `prompt()` nativo del browser, experiencia pobre; problemas conocidos de SSR en Nuxt que requieren `<client-only>` |
| **Output** | HTML estándar |
| **SSR** | Requiere `<client-only>` |
| **Npm** | `vue-quill-editor` + `quill` |

**Cuándo elegirla:** si el tiempo de entrega es prioritario y la UX del editor no es crítica para esta iteración.

---

### Opción B — `vue2-editor`

**Estado:** wrapper más simple sobre Quill 1.x, puede ya estar en node_modules (verificar).

|  |  |
| --- | --- |
| **Pros** | API más simple que `vue-quill-editor`; tiene prop `useCustomImageHandler` + evento `@image-added` que hace levemente más cómodo interceptar el click de imagen y mostrar UI propia (modal, input) en lugar de sobreescribir el handler de Quill directamente |
| **Contras** | También sobre Quill 1.x; la ventaja sobre Opción A es menor — en ambos casos hay que escribir código custom para insertar imagen por URL; menos configurable a nivel bajo |
| **Output** | HTML estándar |
| **SSR** | Requiere `<client-only>` |
| **Npm** | `vue2-editor` |

> **Nota:** en Quill, el botón de imagen por defecto abre un **file picker** (selector de archivo local), no un prompt de URL. Para insertar por URL en cualquiera de las dos opciones (A o B) hay que sobreescribir el handler. La diferencia es solo ergonómica: `vue2-editor` emite `@image-added`; `vue-quill-editor` requiere definir `modules.toolbar.handlers.image` manualmente.


**Cuándo elegirla:** si se quiere Quill y se prefiere la API de eventos sobre la configuración de handlers de Quill crudo. La diferencia con Opción A es mínima.

---

### Opción C — Tiptap v1 (para Vue 2)

**Estado:** no instalado, requiere `npm install tiptap tiptap-extensions`.

|  |  |
| --- | --- |
| **Pros** | Basado en ProseMirror (más robusto que Quill); extensible por diseño; buena comunidad activa; experiencia de edición más pulida; control total sobre la toolbar |
| **Contras** | Tiptap v2 (el actual) es solo para Vue 3; para este proyecto (Nuxt 2 / Vue 2) hay que usar Tiptap v1, que ya no recibe updates. Más código para armar la toolbar custom |
| **Output** | HTML o JSON (configurable) |
| **SSR** | Compatible con Nuxt 2 sin workarounds |
| **Npm** | `tiptap` + `tiptap-extensions` |

**Cuándo elegirla:** si se busca mejor UX y extensibilidad futura, y el dev tiene tiempo para armar los componentes de toolbar.

---

### Opción D — CKEditor 5 con componente Vue

**Estado:** no instalado.

|  |  |
| --- | --- |
| **Pros** | Editor más completo y conocido por usuarios no técnicos; soporte activo; toolbar rica out-of-the-box; inserción de imagen por URL incluida en la versión gratuita |
| **Contras** | Bundle pesado (~300KB+); licencia: la versión open-source (GPL) tiene restricciones si el proyecto no es open-source — **verificar licencia antes de usar**; integración con Vue 2 requiere `@ckeditor/ckeditor5-vue2` |
| **Output** | HTML |
| **SSR** | Requiere `<client-only>` |
| **Npm** | `@ckeditor/ckeditor5-vue2` + build de CKEditor elegido |

**Cuándo elegirla:** si el vendedor necesita una experiencia de edición tipo Word y el peso extra del bundle es aceptable.

---

### Opción E — Editor minimalista custom (textarea + ayudas)

**Estado:** sin dependencias externas.

|  |  |
| --- | --- |
| **Pros** | Cero dependencias; peso mínimo; control total; sin problemas de SSR |
| **Contras** | Hay que construir la toolbar manualmente (bold, italic, etc. via `document.execCommand` o rangos); `execCommand` está deprecado en navegadores modernos aunque aún funciona; no es una solución a largo plazo |
| **Output** | HTML |
| **SSR** | Sin problemas |
| **Npm** | Ninguno |

**Cuándo elegirla:** solo si ninguna librería es viable por restricciones del proyecto.

---

## Cambios requeridos en el frontend

### Archivos a modificar

| Archivo | Cambio |
| --- | --- |
| `app/components/Catalogo/FichaProducto.vue` | Principal: reemplazar maqueta + integrar editor |

> Los snippets de código de las secciones siguientes usan `vue-quill-editor` como referencia. Si se elige otra opción, adaptar el import, el nombre del componente y las props correspondientes — la lógica de datos no cambia.


---

### 1. Configuración del editor

La toolbar mínima requerida (adaptar a la API de la opción elegida):

- Encabezados H1 / H2 / H3 / texto normal


- Negrita, cursiva, subrayado, tachado


- Lista ordenada y lista con viñetas


- PROHIBIDO Insertar link


- Insertar imagen por URL


- Limpiar formato



### Estado visual del editor

| Estado | Comportamiento |
| --- | --- |
| Sin contenido previo | Editor vacío con placeholder "Escribí la descripción de tu producto..." |
| Con contenido guardado | Carga el HTML del campo `customDescription` del producto |
| Guardando (`saving: true`) | Editor bloqueado (`disabled`), toolbar deshabilitada |
| Cambio detectado | El botón "Guardar" se habilita (misma lógica que otros campos) |
| Sin cambios | El botón "Guardar" permanece deshabilitado |

### Toolbar disponible

- Encabezados H1 / H2 / H3 / texto normal


- Negrita, cursiva, subrayado, tachado


- Lista ordenada y lista con viñetas


- PROHIBIDO Insertar link


- Insertar imagen por URL (prompt nativo del browser)


- Limpiar formato



### Imagen por URL

Al hacer clic en el ícono de imagen en la toolbar, Quill abre un `prompt()` nativo del navegador pidiendo la URL. El vendedor pega la URL de la imagen (CDN propio, servicio externo, etc.) y se inserta como `<img src="...">` en el HTML.

---

## Criterios de aceptación

- La sección "Descripción" ya no muestra el badge "Próximamente" ni el textarea deshabilitado


- El editor Quill se monta correctamente en `FichaProducto.vue`


- Si el producto tiene `customDescription` guardado, el editor lo carga al abrir la ficha


- Si el producto no tiene `customDescription`, el editor aparece vacío con el placeholder


- Editar el contenido del editor marca `tieneCambios` como `true` y habilita el botón "Guardar"


- Al guardar, el campo `customDescription` se incluye en el PATCH solo si cambió


- Borrar todo el contenido del editor y guardar envía `customDescription: null`


- Durante el guardado (`saving: true`), el editor queda deshabilitado


- La toolbar permite: encabezados, negrita, cursiva, subrayado, listas, PROHIBIDO link e imagen por URL


- Al insertar imagen por URL, se inserta como `<img>` dentro del HTML del editor


- El campo `customDescription` participa en el `PopConfirm` de descarte (si se editó el editor y se cancela, pregunta confirmación)


- Funciona correctamente en mobile (toolbar accesible y editor scrolleable)


- No rompe el comportamiento existente de los demás campos de la ficha
