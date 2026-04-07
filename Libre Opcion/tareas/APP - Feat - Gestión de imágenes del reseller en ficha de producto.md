# APP - Feat - Gestión de imágenes del reseller en ficha de producto

**Proyecto:** [[Libre Opcion/Libre Opcion|Libre Opcion]]
**Estado:** Pendiente (depende de la tarea de API)
**Fecha:** 2026-04-06

		---

## Descripción

Agregar una sección en la ficha de edición de producto (inventario del reseller) que permita subir, ver y eliminar imágenes propias del reseller. Estas imágenes son independientes de las fotos oficiales del catálogo.

## Dependencia

- [[Libre Opcion/tareas/API - Feat - Imágenes personalizadas del reseller por producto|API - Feat - Imágenes personalizadas del reseller por producto]] — los endpoints deben estar disponibles antes de implementar el frontend.

## Entregables

### 1. Sección de imágenes en la ficha de edición

Dentro de la pantalla de edición de producto del inventario, agregar una sección **"Mis imágenes"** (o similar) que:

- Muestre las imágenes del reseller para ese producto (consumiendo `GET /inventory/products/{productId}/images`)
- Muestre las imágenes oficiales del catálogo como referencia (read-only, diferenciadas visualmente)
- Permita subir nuevas imágenes
- Permita eliminar imágenes propias

### 2. Componente de upload

- Input de tipo archivo con preview antes de subir
- Validación client-side: formatos aceptados (`jpg`, `png`, `webp`), tamaño máximo
- Indicador de progreso durante la subida
- Feedback de éxito/error
- Límite visual: mostrar cuántas imágenes quedan disponibles (máx 5)

### 3. Galería de imágenes del reseller

- Thumbnails de las imágenes subidas, ordenadas
- Botón de eliminar en cada imagen (con confirmación)
- Diferenciación clara entre imágenes propias e imágenes oficiales del catálogo
- Las imágenes oficiales deben verse pero **no** poder eliminarse ni editarse

### 4. Integración con API

Consumir los 3 endpoints nuevos:

| Acción | Endpoint | Método |
|--------|----------|--------|
| Listar mis imágenes | `/inventory/products/{productId}/images` | `GET` |
| Subir imagen | `/inventory/products/{productId}/images` | `POST` (multipart/form-data) |
| Eliminar imagen | `/inventory/products/{productId}/images/{imageId}` | `DELETE` |

Las URLs de las imágenes se construyen con: `{URL_SERVICIO_ESTATICO} + checksum`

## Criterios de aceptación

- [ ] La sección "Mis imágenes" aparece en la ficha de edición de producto
- [ ] Se pueden subir imágenes (jpg, png, webp) con preview
- [ ] Se muestran las imágenes ya subidas como thumbnails
- [ ] Se pueden eliminar imágenes propias con confirmación
- [ ] Las imágenes oficiales del catálogo se muestran aparte como referencia (read-only)
- [ ] Se muestra el límite de imágenes (ej: "3 de 5 imágenes")
- [ ] Feedback visual de carga, éxito y error
- [ ] No se puede subir si ya se alcanzó el límite de 5

## Notas técnicas

- La ficha de edición actual está en la app Flutter (`mobileAppForSellers/`) — verificar si también aplica para el frontend web (`sitio-web-app-v3/`)
- El checksum devuelto por la API es el nombre del archivo en el servicio estático
- Token de autenticación: se envía como Bearer en el header (JWT del reseller)

## Ver también

- [[Libre Opcion/tareas/API - Feat - Imágenes personalizadas del reseller por producto|API - Feat - Imágenes personalizadas del reseller por producto]]
- [[Libre Opcion/Libre Opcion|Libre Opcion]]
