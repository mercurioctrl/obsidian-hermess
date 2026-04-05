---
jira_key: "INV-36"
aliases: ["INV-36"]
summary: "API - Review - Problemas al buscar imagenes por string"
status: "CodeReview"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-10-18 21:58"
updated: "2023-10-19 11:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-36"
---

# INV-36: API - Review - Problemas al buscar imagenes por string

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-18 21:58 |
| Actualizado | 2023-10-19 11:18 |
| Etiquetas | ninguna |
| Jira | [INV-36](https://bluinc.atlassian.net/browse/INV-36) |

## Relaciones

- **Padre:** [[INV-35 - Importadores Scrappers|INV-35]] Importadores/ Scrappers

## Descripcion

Al ejecutar algo como

```
curl --location --request GET 'http://gamma.api.inventory.lio.red/getImages/string?title=MOUSE GAMER TT ESPORTS THERON PLUS SMART' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2OTc2Nzg0OTMsInVzdWFyaW8iOjU4fQ.k2A0Gcx4recfBRyGrWSDd5uxp24RynbBTkySWv5Tojw'
```

Me da una salida del siguiente tipo

```
2023-10-19 00:55:33 [urllib3.connectionpool] DEBUG: https://api.mercadolibre.com:443 "GET /sites/MLA/search?q=MOUSE%20GAMER%20TT%20ESPORTS%20THERON%20PLUS%20SMART HTTP/1.1" 200 None
https://www.newegg.com/p/pl?d=MOUSE+GAMER+TT+ESPORTS+THERON+PLUS+SMART
INFO:     190.189.96.222:0 - "GET /getImages/string?title=MOUSE%20GAMER%20TT%20ESPORTS%20THERON%20PLUS%20SMART HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/progweb/.local/lib/python3.9/site-packages/uvicorn/protocols/http/h11_impl.py", line 407, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
  File "/home/progweb/.local/lib/python3.9/site-packages/uvicorn/middleware/proxy_headers.py", line 78, in __call__
    return await self.app(scope, receive, send)
  File "/home/progweb/.local/lib/python3.9/site-packages/fastapi/applications.py", line 271, in __call__
    await super().__call__(scope, receive, send)
  File "/home/progweb/.local/lib/python3.9/site-packages/starlette/applications.py", line 118, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/progweb/.local/lib/python3.9/site-packages/starlette/middleware/errors.py", line 184, in __call__
    raise exc
  File "/home/progweb/.local/lib/python3.9/site-packages/starlette/middleware/errors.py", line 162, in __call__
    await self.app(scope, receive, _send)
  File "/home/progweb/.local/lib/python3.9/site-packages/starlette/middleware/cors.py", line 84, in __call__
    await self.app(scope, receive, send)
  File "/home/progweb/.local/lib/python3.9/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
    raise exc
  File "/home/progweb/.local/lib/python3.9/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
    await self.app(scope, receive, sender)
  File "/home/progweb/.local/lib/python3.9/site-packages/fastapi/middleware/asyncexitstack.py", line 21, in __call__
    raise e
  File "/home/progweb/.local/lib/python3.9/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "/home/progweb/.local/lib/python3.9/site-packages/starlette/routing.py", line 706, in __call__
    await route.handle(scope, receive, send)
  File "/home/progweb/.local/lib/python3.9/site-packages/starlette/routing.py", line 276, in handle
    await self.app(scope, receive, send)
  File "/home/progweb/.local/lib/python3.9/site-packages/starlette/routing.py", line 66, in app
    response = await func(request)
  File "/home/progweb/.local/lib/python3.9/site-packages/fastapi/routing.py", line 237, in app
    raw_response = await run_endpoint_function(
  File "/home/progweb/.local/lib/python3.9/site-packages/fastapi/routing.py", line 165, in run_endpoint_function
    return await run_in_threadpool(dependant.call, **values)
  File "/home/progweb/.local/lib/python3.9/site-packages/starlette/concurrency.py", line 41, in run_in_threadpool
    return await anyio.to_thread.run_sync(func, *args)
  File "/home/progweb/.local/lib/python3.9/site-packages/anyio/to_thread.py", line 31, in run_sync
    return await get_asynclib().run_sync_in_worker_thread(
  File "/home/progweb/.local/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 937, in run_sync_in_worker_thread
    return await future
  File "/home/progweb/.local/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 867, in run
    result = context.run(func, *args)
  File "/var/www/gamma_inventory/ms-metadata/./main.py", line 164, in getInfo
    aux = {'Meli': meli['Images'], 'NewEgg':newEgg[0]['Images']}
TypeError: 'NoneType' object is not subscriptable
```
