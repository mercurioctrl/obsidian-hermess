# frontend.Dockerfile

> Imagen Node 20 multi-stage para Nuxt 3 SSR. Parte del skill [[SKILL|fullstack-docker-app]].
> Ver [[architecture#Multi-stage Frontend Build]].

## Características

- **Stage 1 (builder)**: Instala deps, compila Nuxt con `NUXT_PUBLIC_API_BASE` como build arg
- **Stage 2 (runtime)**: Solo `.output/`, imagen mínima

Usado por el servicio `frontend` en [[docker-compose.yml]].
Nginx rutea `/*` a este container — ver [[nginx.conf]].
Deploy siempre requiere rebuild — ver [[conventions#Deploy frontend (siempre rebuild)]].

## Template

```dockerfile
# Stage 1: Build
FROM node:20-slim AS builder

WORKDIR /app

ARG NUXT_PUBLIC_API_BASE
ENV NUXT_PUBLIC_API_BASE=${NUXT_PUBLIC_API_BASE}

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Stage 2: Runtime (only the built output)
FROM node:20-slim

WORKDIR /app

COPY --from=builder /app/.output ./.output

EXPOSE 3000

CMD ["node", ".output/server/index.mjs"]
```
