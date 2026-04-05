---
jira_key: "PED-220"
aliases: ["PED-220"]
summary: "API - Review - Ver detalle de una orden de compra (0002-10314846)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-11-02 20:21"
updated: "2023-11-03 09:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-220"
---

# PED-220: API - Review - Ver detalle de una orden de compra (0002-10314846)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-02 20:21 |
| Actualizado | 2023-11-03 09:52 |
| Etiquetas | ninguna |
| Jira | [PED-220](https://bluinc.atlassian.net/browse/PED-220) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra

## Descripcion

```
curl 'https://gamma.api.orders.lio.red/v1/orders/0002-10314846' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Connection: keep-alive' \
  -H 'Origin: <ORIGIN_URL>' \
  -H 'Referer: <REFERER_URL>' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: <USER_AGENT>' \
  -H 'sec-ch-ua: "<BRAND_INFO>"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed

```

Me da un error

```
{
    "message": "Cannot assign null to property App\\Dto\\Order\\OrderDetailDto::$sellerIdCreator of type string",
    "exception": "TypeError",
    "file": "/var/www/app/app/Dto/Order/OrderDetailDto.php",
    "line": 42,
    "trace": [
        {
            "file": "/var/www/app/app/Services/Order/OrderService.php",
            "line": 298,
            "function": "__construct",
            "class": "App\\Dto\\Order\\OrderDetailDto",
            "type": "->"
        },
        {
            "file": "/var/www/app/app/Http/Controllers/Order/OrderController.php",
            "line": 206,
            "function": "getDetail",
            "class": "App\\Services\\Order\\OrderService",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/Controller.php",
            "line": 54,
            "function": "getDetail",
            "class": "App\\Http\\Controllers\\Order\\OrderController",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/ControllerDispatcher.php",
            "line": 43,
            "function": "callAction",
            "class": "Illuminate\\Routing\\Controller",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/Route.php",
            "line": 259,
            "function": "dispatch",
            "class": "Illuminate\\Routing\\ControllerDispatcher",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/Route.php",
            "line": 205,
            "function": "runController",
            "class": "Illuminate\\Routing\\Route",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/Router.php",
            "line": 798,
            "function": "run",
            "class": "Illuminate\\Routing\\Route",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 141,
            "function": "Illuminate\\Routing\\{closure}",
            "class": "Illuminate\\Routing\\Router",
            "type": "->"
        },
        {
            "file": "/var/www/app/app/Http/Middleware/PermissionMiddleware.php",
            "line": 28,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 180,
            "function": "handle",
            "class": "App\\Http\\Middleware\\PermissionMiddleware",
            "type": "->"
        },
        {
            "file": "/var/www/app/app/Http/Middleware/CorsMiddleware.php",
            "line": 27,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 180,
            "function": "handle",
            "class": "App\\Http\\Middleware\\CorsMiddleware",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/Middleware/SubstituteBindings.php",
            "line": 50,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 180,
            "function": "handle",
            "class": "Illuminate\\Routing\\Middleware\\SubstituteBindings",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/Middleware/ThrottleRequests.php",
            "line": 126,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/Middleware/ThrottleRequests.php",
            "line": 92,
            "function": "handleRequest",
            "class": "Illuminate\\Routing\\Middleware\\ThrottleRequests",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/Middleware/ThrottleRequests.php",
            "line": 54,
            "function": "handleRequestUsingNamedLimiter",
            "class": "Illuminate\\Routing\\Middleware\\ThrottleRequests",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 180,
            "function": "handle",
            "class": "Illuminate\\Routing\\Middleware\\ThrottleRequests",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 116,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/Router.php",
            "line": 797,
            "function": "then",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/Router.php",
            "line": 776,
            "function": "runRouteWithinStack",
            "class": "Illuminate\\Routing\\Router",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/Router.php",
            "line": 740,
            "function": "runRoute",
            "class": "Illuminate\\Routing\\Router",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Routing/Router.php",
            "line": 729,
            "function": "dispatchToRoute",
            "class": "Illuminate\\Routing\\Router",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Foundation/Http/Kernel.php",
            "line": 190,
            "function": "dispatch",
            "class": "Illuminate\\Routing\\Router",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 141,
            "function": "Illuminate\\Foundation\\Http\\{closure}",
            "class": "Illuminate\\Foundation\\Http\\Kernel",
            "type": "->"
        },
        {
            "file": "/var/www/app/app/Http/Middleware/CorsMiddleware.php",
            "line": 27,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 180,
            "function": "handle",
            "class": "App\\Http\\Middleware\\CorsMiddleware",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/TransformsRequest.php",
            "line": 21,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/ConvertEmptyStringsToNull.php",
            "line": 31,
            "function": "handle",
            "class": "Illuminate\\Foundation\\Http\\Middleware\\TransformsRequest",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 180,
            "function": "handle",
            "class": "Illuminate\\Foundation\\Http\\Middleware\\ConvertEmptyStringsToNull",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/TransformsRequest.php",
            "line": 21,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/TrimStrings.php",
            "line": 40,
            "function": "handle",
            "class": "Illuminate\\Foundation\\Http\\Middleware\\TransformsRequest",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 180,
            "function": "handle",
            "class": "Illuminate\\Foundation\\Http\\Middleware\\TrimStrings",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/ValidatePostSize.php",
            "line": 27,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 180,
            "function": "handle",
            "class": "Illuminate\\Foundation\\Http\\Middleware\\ValidatePostSize",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/PreventRequestsDuringMaintenance.php",
            "line": 86,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 180,
            "function": "handle",
            "class": "Illuminate\\Foundation\\Http\\Middleware\\PreventRequestsDuringMaintenance",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Http/Middleware/HandleCors.php",
            "line": 49,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 180,
            "function": "handle",
            "class": "Illuminate\\Http\\Middleware\\HandleCors",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Http/Middleware/TrustProxies.php",
            "line": 39,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 180,
            "function": "handle",
            "class": "Illuminate\\Http\\Middleware\\TrustProxies",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php",
            "line": 116,
            "function": "Illuminate\\Pipeline\\{closure}",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Foundation/Http/Kernel.php",
            "line": 165,
            "function": "then",
            "class": "Illuminate\\Pipeline\\Pipeline",
            "type": "->"
        },
        {
            "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Foundation/Http/Kernel.php",
            "line": 134,
            "function": "sendRequestThroughRouter",
            "class": "Illuminate\\Foundation\\Http\\Kernel",
            "type": "->"
        },
        {
            "file": "/var/www/app/public/index.php",
            "line": 51,
            "function": "handle",
            "class": "Illuminate\\Foundation\\Http\\Kernel",
            "type": "->"
        }
    ]
}
```
