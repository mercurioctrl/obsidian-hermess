# Estado

Parte de [[portal]]. Actualizado: **2026-08-29**

## Hecho

**Operación** — login con recuperación de contraseña · panel con KPIs · catálogo completo
(1.342 artículos, paginado en cliente) con búsqueda y filtros · ficha de artículo con galería y
specs · carrito persistente editable · checkout con OC, medio de pago, **cotización de envío por
transporte con precio y plazo** e interés desglosado · mis pedidos con detalle por línea y
"Repetir" · compras frecuentes derivadas del histórico.

**Comercial** — lista de precios con export Excel/CSV · comprobantes con PDF.

**Cuenta** — sub-usuarios · direcciones · postventa de consulta · mi cuenta · contacto.

**Transversal** — modo oscuro · preferencia USD/ARS y con/sin IVA · [[marca|marca completa]] ·
[[configuracion#Secciones activables|secciones activables por deploy]].

## Sin verificar

**Nada que escriba en el ERP fue probado**, por no tener credenciales de prueba:

- [ ] Agregar / editar / borrar en el carrito
- [ ] **Confirmar un pedido** — crea una nota de pedido real
- [ ] Cotización de envío con dirección real
- [ ] ABM de sub-usuarios y de direcciones
- [ ] Export de lista de precios (depende de permisos por rol)
- [ ] PDF de comprobantes (depende de `COMPROBANTES_URL` en el backend)

## Bloqueado por backend

### Almacén y sucursal hardcodeados — riesgo para NBE

`PedidoRepository::create()` tiene `'SAF' AS ccodalm`, `2 AS ID_ALMACEN`, `2 AS ID_Sucursal`, y
`ShoppingCartService::process()` pasa la sucursal como literal `'0002'`. Si la instancia de NBE
corre ese código sin parchear, los pedidos salen marcados como empresa 9 pero **entran al
almacén 2 y la sucursal 0002 de NB** — el de NBE es el 8.

No se puede confirmar desde afuera. **Revisar antes del primer pedido real.**

### Preflight de la raíz

`$app->options('/{routes:.+}')` no matchea la raíz, así que el preflight de `GET /v1/` da 404 en
cualquier cliente autenticado. El portal lo esquiva; otros consumidores no.
Ver [[api-nbe#La barra final]].

### Falta el dato

| Feature del spec | Qué falta |
|---|---|
| Cuenta corriente real | Saldo pendiente y vencimiento en `getComprobantes` |
| Promociones (4 tipos) | Todo el modelo de datos |
| Cotizaciones del vendedor | Todo el modelo de datos |
| Campo de orden de compra | Hoy va como prefijo del `note` |
| Filtros facetados | Atributos técnicos con conteo |
| Ítems frecuentes reales | Endpoint por cliente; hoy se deriva del histórico |
| Observación por línea | Columna en `contenidoCarritos` |
| Importación texto/Excel | Endpoints |
| Link de recuperación al portal | Cambiar `PASSWORD_RECOVERY_ENDPOINT` |

## Pendiente de frontend

- **Deploy**: falta Dockerfile, config de nginx y definir el dominio
- **Alta de RMA**: la API tiene `POST /postventa` con serial, fotos y mensajería. Es la pieza
  más grande que queda construible hoy
- **Seguridad**: el JWT vive en cookie legible por JS (inevitable en SPA)
- **Escalabilidad del catálogo**: hoy se trae entero

## Ver también

- [[api-nbe]] · [[configuracion]] · [[changelog]]
