# Contexto — qApp

Ver índice: [[qApp]] · relacionado: [[arquitectura]] · [[stack]]

## Origen del proyecto

Nace de la propuesta "Arquitectura de Automatización QA" para New Bytes: la
preparación manual de datos de prueba (pedidos en distintos estados) consume tiempo
y retrasa la validación de tareas de QA. La herramienta permite seleccionar un
escenario, definir parámetros, ejecutar y obtener un resultado reutilizable con
evidencia y trazabilidad.

## Decisiones tomadas en la sesión

- **Capa de datos:** SQL crudo con el driver `mssql`, **sin ORM** (elección del
  usuario).
- **Alcance del scaffold:** base ejecutable **end-to-end** (no solo esqueleto), con
  un demo autocontenido verificado corriendo en Docker.
- **Concurrencia configurable** desde el arranque: Playwright en `1` pero cambiable
  por `.env` — se contempló el cuello de botella marcado en la revisión de la propuesta.
- **Demo sin dependencias externas:** el escenario HTTP pega al endpoint interno
  `/demo/echo`; el de Playwright abre una URL con navegador real. Así el circuito se
  prueba sin Gamma ni internet.

## Gotchas (cosas que rompieron al ejecutar y su fix)

- **corepack + pnpm:** la imagen base traía un `corepack` con claves viejas que no
  podía verificar la firma de pnpm. Fix: `RUN npm install -g pnpm@9.12.0` en los
  Dockerfiles.
- **ValidationPipe:** activarlo exige el paquete `class-validator`; no se usan DTOs
  con decoradores, así que se removió el pipe.
- **Orden de hooks onModuleInit:** el migrador corría antes de que el pool de la DB
  conectara. Fix: la conexión arranca en el **constructor** del `DatabaseService` y
  `query`/`execute` esperan una promesa `ready` — el orden de init deja de importar.
- **Puerto 3000 ocupado** en el host de trabajo: el contenedor `web` no se pudo
  probar localmente por conflicto de puerto (específico de esa máquina, no del
  proyecto). Se cambia con `WEB_PORT` en el `.env`.

## Cómo correrlo

```
cp .env.example .env
make up          # build + up de db + api + web
```
Web en `:3000`, API en `:4000`, SQL en `:1433`. `make help` lista el resto.
Deploy en QA con SQL Server existente:
`docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build`.

## Próximos pasos / pendientes

- **Ciclo de vida del dato de prueba:** definir marcado/limpieza (idempotencia) de la
  data generada en Gamma para que no se acumule basura.
- **Anti-fragilidad de Playwright:** capa de *page objects* / selectores estables
  para no romper ante cambios de UI.
- **Seguridad:** mover credenciales de Gamma a un secreto gestionado (no `.env` plano).
- **Primer escenario real** contra Gamma (setear `GAMMA_BASE_URL` + migración con el
  `INSERT` del escenario).
- **Verificar `web`** resolviendo el puerto.
- Decidir si se commitea el `.claude/CLAUDE.md` (hoy sin commitear en el repo).

## Ver también

- [[arquitectura|Arquitectura]]
- [[stack|Stack]]
- [[changelog|Changelog]]
