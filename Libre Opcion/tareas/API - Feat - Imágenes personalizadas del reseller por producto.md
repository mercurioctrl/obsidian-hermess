# API - Feat - Imágenes personalizadas del reseller por producto

**Proyecto:** [[Libre Opcion/Libre Opcion|Libre Opcion]]
**Estado:** Pendiente
**Fecha:** 2026-04-06

---

## Descripción

Permitir que los resellers suban sus propias imágenes a los productos de su inventario, sin que estas se mezclen con las fotos oficiales del catálogo.

Las imágenes oficiales viven en `[PRODUCTOS].[dbo].[fotos]` + `[CS].[dbo].[productosFotos]`. Las imágenes del reseller se almacenan en una **tabla nueva separada** en la base `[LO]`.

## Entregables

### 1. SQL — Nueva tabla `[LO].[dbo].[productosImagenesReseller]`

```sql
CREATE TABLE [LO].[dbo].[productosImagenesReseller] (
    id          INT IDENTITY(1,1) PRIMARY KEY,
    id_producto INT NOT NULL,           -- FK a [CS].[dbo].[productos].id
    vendedorID  INT NOT NULL,           -- FK a [LO].[dbo].[vendedores].id
    checksum    VARCHAR(255) NOT NULL,  -- nombre archivo en servicio estático
    orden       INT NOT NULL DEFAULT 0, -- orden de visualización
    activo      BIT NOT NULL DEFAULT 1, -- soft delete
    created_at  DATETIME NOT NULL DEFAULT GETDATE(),
    updated_at  DATETIME NOT NULL DEFAULT GETDATE()
);

CREATE INDEX IX_productosImagenesReseller_producto_vendedor
ON [LO].[dbo].[productosImagenesReseller] (id_producto, vendedorID, activo);
```

**¿Por qué en `[LO]`?** Las tablas de `[PRODUCTOS]` y `[CS]` son del catálogo oficial/compartido. Los datos propios del reseller (pedidos, carrito) están en `[LO]`.

### 2. Repository — `ProductImagesRepository.php`

Ubicación: `app/Repository/Inventory/Products/ProductImagesRepository.php`

Métodos:
- `getByProduct(int $productId, int $vendedorId): array` — listar imágenes activas, ordenadas por `orden ASC`
- `insert(int $productId, int $vendedorId, string $checksum, int $orden): void` — insertar registro
- `delete(int $imageId, int $vendedorId): void` — soft delete (`activo = 0, updated_at = GETDATE()`)
- `countByProduct(int $productId, int $vendedorId): int` — contar imágenes activas (para validar límite)

### 3. Service — `ProductImagesService.php`

Ubicación: `app/Service/Inventory/Products/ProductImagesService.php`

Lógica:
1. **Listar:** Obtener imágenes del reseller para un producto
2. **Subir:**
   - Validar que el producto pertenece al vendedor autenticado (usar `ProductsRepository::findById`)
   - Validar archivo: mime type (`jpg`, `png`, `webp`), tamaño máximo
   - Validar límite de imágenes por producto (máx 5)
   - Llamar a `UploadImage::uploadServer($file)` para subir al servicio estático
   - Llamar a `UploadImage::makePermanent($checksum)` para hacerla permanente
   - Insertar registro en la tabla
3. **Eliminar:**
   - Validar ownership (la imagen pertenece al vendedor)
   - Soft delete

### 4. Controllers

Ubicación: `app/Http/Controllers/Inventory/Products/`

| Controller | Método HTTP | Ruta |
|------------|-------------|------|
| `ProductImagesListController` | `GET` | `/inventory/products/{productId}/images` |
| `ProductImagesUploadController` | `POST` | `/inventory/products/{productId}/images` |
| `ProductImagesDeleteController` | `DELETE` | `/inventory/products/{productId}/images/{imageId}` |

Todos usan `__invoke` (patrón single-action del proyecto).

### 5. Rutas

En `app/routes/api.php`, dentro del grupo autenticado con middleware `token.auth`:

```php
Route::get('inventory/products/{productId}/images', ProductImagesListController::class);
Route::post('inventory/products/{productId}/images', ProductImagesUploadController::class);
Route::delete('inventory/products/{productId}/images/{imageId}', ProductImagesDeleteController::class);
```

## Respuestas esperadas

**GET** `/inventory/products/{productId}/images`
```json
{
  "success": true,
  "images": [
    {
      "id": 1,
      "checksum": "abc123def456.jpg",
      "orden": 0,
      "created_at": "2026-04-06T10:30:00"
    }
  ]
}
```

**POST** `/inventory/products/{productId}/images` (multipart/form-data con campo `file`)
```json
{
  "success": true,
  "message": "Imagen subida correctamente",
  "image": {
    "id": 2,
    "checksum": "def789ghi012.jpg",
    "orden": 1,
    "created_at": "2026-04-06T10:35:00"
  }
}
```

**DELETE** `/inventory/products/{productId}/images/{imageId}`
```json
{
  "success": true,
  "message": "Imagen eliminada"
}
```

## Criterios de aceptación

- [ ] Tabla `productosImagenesReseller` creada en `[LO]` con índice
- [ ] GET devuelve solo imágenes del reseller autenticado para ese producto
- [ ] POST sube imagen al servicio estático, la hace permanente, y la registra en la tabla
- [ ] POST valida: ownership del producto, mime type, tamaño, límite de 5 imágenes
- [ ] DELETE hace soft delete y valida ownership
- [ ] Las imágenes oficiales (`productosFotos`) NO se ven afectadas en ningún caso
- [ ] Todos los endpoints protegidos con middleware `token.auth`

## Notas técnicas

- Reutilizar `UploadImage` helper existente (`app/Helper/UploadImage.php`) para la subida
- Reutilizar `TokenManager::getUserFromToken()` para obtener el `vendedorID`
- Seguir patrón Controller → Service → Repository del proyecto
- SQL Server con `DB::select()` / `DB::statement()` (sin Eloquent)
- **DATEFORMAT**: usar formato ISO 8601 con T en cualquier fecha

## Ver también

- [[Libre Opcion/Libre Opcion|Libre Opcion]]
