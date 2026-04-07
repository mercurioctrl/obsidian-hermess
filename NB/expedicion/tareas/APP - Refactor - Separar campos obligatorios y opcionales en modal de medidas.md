# APP - Refactor - Separar campos obligatorios y opcionales en modal de medidas

**Proyecto:** [[NB/expedicion/expedicion|Expedición]]
**Estado:** Pendiente
**Fecha:** 2026-04-06

---

## Descripción

El modal "Cargar código universal asociado y medidas" (`UniversalCodeForm.vue`) muestra muchos campos juntos (GTIN, EAN, UPC, ISBN, peso, largo, ancho, alto, cantidad por caja) sin una separación clara entre lo que es obligatorio y lo que no. Esto genera confusión al usuario.

Se necesita que el modal distinga **visualmente** qué campos son obligatorios y cuáles opcionales, basándose en los permisos de bypass que ya vienen en el objeto `user`:

- Si el usuario **tiene** permiso de bypass de barcode → los campos GTIN, EAN, UPC, ISBN se muestran como **opcionales**
- Si el usuario **tiene** permiso de bypass de medidas → peso, largo, ancho, alto se muestran como **opcionales**
- Si el usuario **tiene** permiso de bypass de PPU → cantidad por caja se muestra como **opcional**
- Si el usuario **no tiene** el permiso → esos campos se muestran como **obligatorios** (comportamiento actual vía `errorFields`)

### Problema actual

Actualmente la obligatoriedad se determina por el array `errorFields` que viene del backend cuando el producto no tiene esos datos cargados. No hay separación visual entre los grupos de campos — todo se muestra en un solo bloque con un mensaje genérico: *"Introduzca al menos uno de los siguientes campos"*.

## Criterios de aceptación

- [ ] Los campos del modal se agrupan visualmente en 3 secciones: **Códigos de barras**, **Medidas**, **Unidades por caja**
- [ ] Cada sección indica claramente si es obligatoria u opcional para el usuario actual
- [ ] La obligatoriedad se determina combinando `errorFields` (del backend) con los permisos de bypass del `user`
- [ ] Si el usuario tiene permiso de bypass, los campos de esa sección se marcan como opcionales aunque `errorFields` los incluya
- [ ] Los campos opcionales no bloquean el submit del formulario
- [ ] No se rompe el comportamiento actual para usuarios sin permisos de bypass

## Notas técnicas

### Componente principal

`expedicion-web-app-v1/app/components/Providers/UniversalCodeForm.vue`

- El modal se abre desde `SerialsForm.vue` (línea 53) cuando el backend retorna `errorFields`
- La prop `formProps.errorFields` (array de strings) determina qué campos son required
- Campos de barcode: `gtin`, `ean`, `upc`, `isbn` (líneas 19-90)
- Campos de medidas: `weightAverage`, `lengthAverage`, `widthAverage`, `highAverage` (líneas 100-190) — usan `ValidationProvider` con `:rules="{required: formProps.errorFields.includes('...')}"`
- Campo PPU: `packagePerUnit` (línea 196)
- Ya existe lógica de placeholder condicional con `(Opcional)` (ej: línea 113)

### Componente padre

`expedicion-web-app-v1/app/components/Providers/SerialsForm.vue`

- Línea 722: captura `err.errorFields` de la respuesta del backend
- Pasa los errorFields como prop a `UniversalCodeForm`

### Implementación sugerida

1. Leer los permisos de bypass del usuario desde el store/auth (`$auth.user`)
2. Filtrar `errorFields` quitando los campos para los cuales el usuario tiene permiso de bypass
3. Agrupar visualmente los campos en 3 secciones con títulos/separadores
4. Cada sección muestra un tag o indicador: "Obligatorio" / "Opcional"
5. Usar estilos diferenciados (ej: borde, fondo, o badge) para distinguir secciones obligatorias de opcionales

## Ver también

- [[NB/expedicion/tareas/API - Feat - Permisos por agente para saltear validaciones de serials|Tarea: Permisos por agente para saltear validaciones]]
- [[NB/expedicion/tareas/API - Feat - Incluir permisos de bypass en objeto user|Tarea: Incluir permisos de bypass en objeto user]]
- [[NB/expedicion/arquitectura|Arquitectura]]
