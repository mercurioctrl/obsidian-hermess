# Arquitectura — microservicio-envios

## Flujo de request

```
HTTP → public/index.php
     → src/App/App.php  (bootstrap)
     → Routes.php       (match de ruta)
     → Middleware       (auth JWT opcional)
     → Controller       (extrae params HTTP)
     → Service          (lógica de negocio)
     → Repository       (queries PDO)
     → DB (MSSQL o MariaDB)
```

## Bootstrap (App.php)

El orden de carga importa:

1. DotEnv — variables de entorno
2. Container (Pimple) — registro de servicios
3. ErrorHandler — manejo de errores custom
4. Middlewares — Slim routing/parsing/error
5. CORS
6. Database — conexiones PDO (MSSQL + MariaDB)
7. Services — registro en contenedor
8. Repositories — registro en contenedor
9. Routes — definición de endpoints
10. NotFound — handler 404

## Capas

| Capa | Namespace | Responsabilidad |
|---|---|---|
| Controller | `App\Controller\` | Extrae params HTTP, llama Service, devuelve JSON |
| Service | `App\Service\v1\` | Orquesta Repositories y Helpers |
| Repository | `App\Repository\v1\` | Queries PDO, hereda BaseRepository |
| Helper | `App\Helper\` | Wrappers de APIs externas de curriers |
| Middleware | `App\Middleware\` | Validación JWT (`Authenticate`, `AuthenticateAdmin`) |
| Dto | `App\Dto\` | Objetos de transferencia de datos tipados |
| Support | `App\Support\` | TokenManager y utilidades internas |

## Traits de cotización

`Controller\Cotizacion` usa traits para modificar los precios de respuesta:

- `AlterQuoteTrait` — aplica ajuste porcentual (env: `MAX_QUOTE_LIMIT` / `MIN_QUOTE_LIMIT`)
- `AlterShippingBonus` — bonificación selectiva por transportista (env: `SHIPPING_BONUS_ENABLED`)
- `ShippingSuggestion` — sugiere el mejor envío por zona (env: `SHIPPING_SUGGESTION_ENABLED`)
- `QuotesFieldDetector` — detecta campos de cotización según estructura de respuesta del currier

## Endpoints

### Sin autenticación (legacy MSSQL)

```
GET /v1/medios-envio
GET /v1/item/{idItem}/cp/{cp}
GET /v1/item/{idItem}/cp/{cp}/cphost/{cpOrigen}
GET /v1/pedido/{idPedido}/cp/{cp}
GET /v1/cart/nb/{cartId}/cp/{cp}
GET /v1/order/nb/{branch}-{order}/cp/{cp}
GET /v1/paquete/{idPaquete}/tracking/{refTracking}
GET /v1/getLabel/{trackingNumber}/{type}
```

### Con JWT (MariaDB)

```
POST /auth/login
GET  /auth/logout
GET  /shippingMethods
GET  /shipping/getPrivateKey
POST /shipping               (admin)
PUT  /shipping/makePayment
GET  /bulk/size/{s}/weight/{w}/cp/{cp}
```

## Registro de dependencias

Para agregar Service, Repository o ruta:
- `src/App/Services.php` — registrar servicio
- `src/App/Repositories.php` — registrar repository
- `src/App/Routes.php` — definir endpoint
- `src/App/Container.php` — solo si requiere config especial del contenedor

## Ver también

- [[microservicio-envios]] · [[stack]] · [[contexto]] · [[changelog]]
