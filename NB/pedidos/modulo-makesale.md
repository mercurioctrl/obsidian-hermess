# MakeSale — Ejecución de pedidos

Convierte un pedido de estado **P** (pendiente) a **S** (procesado), creando un remito (albarán).

## Flujo (MakeSaleService::executeOrder)

1. **Fix warehouses** — `assignDefaultWarehouseToItems()`: UPDATE que asigna almacén default de la empresa a items sin `ID_ALMACEN`
2. **Validate** — Verifica que el pedido existe (estado 'P'), tiene items, y hay stock suficiente
3. **Create header** — Inserta en `albclit` (remito) con número auto-incremental por sucursal
4. **Build queries** — Acumula SQL strings para: UPDATE stock, INSERT registro_stock, INSERT albclil (detalle)
5. **Execute queries** — Ejecuta en orden: inserts registro → updates stock → updates registro → inserts detalle
6. **Update state** — Cambia `pedclit.cestado` de 'P' a 'S'
7. **Update reserve** — Recalcula `nstock_reserva_pedidos` para los artículos afectados

Todo dentro de `DB::transaction()` — si algo falla, rollback automático.

## Casos especiales

- **Pedido Libre Opción:** descuenta primero de `nstock_lo` y el resto de `nstock` (método `setAmountToDiscount`)
- **Sucursal 0003 (Postventa):** usa `nstock_postventa` en vez de `nstock`

## Archivos clave

- `app/Services/MakeSale/MakeSaleService.php`
- `app/Repositories/MakeSale/MakeSaleRepository.php`
- `app/Http/Controllers/MakeSale/`

## Precauciones

Las queries se construyen concatenando SQL como strings PHP. Ver [[contexto#Gotcha SQL concatenado en MakeSale/RemoveSale|gotcha de SQL concatenado]].

## Ver también

- [[modulo-removesale]] — Flujo inverso (revertir remito)
- [[contexto]] — Gotchas de base de datos
- [[arquitectura]] — Estructura general
