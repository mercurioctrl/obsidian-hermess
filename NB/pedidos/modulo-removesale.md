# RemoveSale — Reversión de remitos

Es el inverso de [[modulo-makesale|MakeSale]]. Convierte un pedido de estado **S** (remitido) a **P** (pendiente), eliminando el remito.

## Flujo (RemoveSaleService::revertSale)

1. **dataOrder** — Verifica que el pedido existe y está remitido
2. **headerOrder** — Obtiene cabecera del remito (albclit) via `MakeSaleRepository::getHeader`
3. **detailOrder** — Obtiene detalle via `MakeSaleRepository::getDetailOrder` (misma query que MakeSale, LEFT JOIN con stocks)
4. **Por cada item acumula SQL strings para:**
   - `revertStock` — UPDATE stocks SET nstock = nstock + cantidad
   - `revertDetail` — DELETE FROM albclil (detalle del remito)
   - `registerStock` — INSERT INTO registro_stock (log de auditoría)
5. **Ejecuta queries acumuladas** en orden: updates stock → deletes detalle → inserts registro → delete cabecera → delete condiciones
6. **updateOrderStatus** — Cambia `pedclit.cestado` de 'S' a 'P' y recalcula `nstock_reserva_pedidos`

## Archivos clave

- `app/Services/RemoveSale/RemoveSaleService.php`
- `app/Repositories/MakeSale/MakeSaleRepository.php` (comparte repo con MakeSale)
- `app/Http/Controllers/RemoveSale/`

## Precauciones

Usa el mismo patrón frágil que [[modulo-makesale|MakeSale]]: SQL concatenado como strings. Si un campo del item es null, genera SQL malformado para todo el batch. Ver [[contexto#Gotcha SQL concatenado en MakeSale/RemoveSale|gotcha]].

## Ver también

- [[modulo-makesale]] — Flujo directo (ejecutar pedido)
- [[contexto]] — Gotchas de base de datos
