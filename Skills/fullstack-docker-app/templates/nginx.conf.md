# nginx.conf

> Reverse proxy que unifica todos los servicios en un solo puerto. Parte del skill [[SKILL|fullstack-docker-app]].
> Ver [[architecture#Single Port Exposure]] y [[architecture#Nginx como Reverse Proxy]].

## Ruteo

| Path | Destino | Servicio |
|------|---------|----------|
| `/api/*` | backend:8000 | [[backend.Dockerfile\|Backend]] |
| `/sanctum/*` | backend:8000 | [[backend.Dockerfile\|Backend]] (CSRF) |
| `/storage/*` | backend:8000 | [[backend.Dockerfile\|Backend]] (uploads) |
| `/*` | frontend:3000 | [[frontend.Dockerfile\|Frontend]] (SSR) |

Montado en el servicio `nginx` de [[docker-compose.yml]].

## Template

```nginx
server {
    listen 80;
    server_name localhost;
    client_max_body_size 10M;

    # API requests → backend
    location /api/ {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        add_header Cache-Control "no-store";
    }

    # Sanctum CSRF cookie → backend
    location /sanctum/ {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Storage (uploads, PDFs) → backend
    location /storage/ {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Everything else → frontend (Nuxt SSR)
    location / {
        proxy_pass http://frontend:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        add_header Cache-Control "no-store";
    }
}
```
