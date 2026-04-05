# Memoria

Contexto acumulado de sesiones de trabajo con Claude en este proyecto.

## Usuario

Desarrollador/tech lead argentino. Maneja frontend (Nuxt/Vue) y backend (Laravel). Prefiere iteración rápida, soluciones directas, y que se verifique que las cosas funcionan antes de declarar listo.

## Feedback

### Siempre probar cambios
Después de cada fix, verificar con requests reales (curl, npm run dev). No asumir que un cambio funciona sin probarlo.

### SQL concatenado — cuidado con nulls
Las queries en MakeSaleService y RemoveSaleService se construyen concatenando strings. Un campo null genera SQL inválido que rompe todo el batch. Siempre verificar propiedades interpoladas, especialmente las que vienen de LEFT JOINs. Ver [[contexto#Gotcha SQL concatenado en MakeSale/RemoveSale|detalle]].

## Proyecto

### Node.js + OpenSSL
Frontend necesita `NODE_OPTIONS=--openssl-legacy-provider` con Node v17+ (la máquina tiene Node v25.5.0).

### Firebase en local
No configurado. Plugin usa stub vacío. Verificar guards antes de llamar a `getMessaging()`. Ver [[contexto#Firebase local|detalle]].

### Docker setup
- Backend: container `api-rest-pedidos-apirest-laravel`, puerto 8093
- Frontend: local, puerto 3002, proxy `/v1/` → localhost:8093
- DB: SQL Server externo

---
*Sincronizado: 2026-04-04*
