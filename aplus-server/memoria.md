# Memoria

Consolidación de la memoria persistente de Claude para este proyecto. Los archivos fuente viven en `~/.claude/projects/-Users-hermess-www-aplus-server/memory/` y se cargan automáticamente en cada sesión. Esta nota es un espejo navegable — la fuente de verdad sigue siendo la carpeta `memory/`.

## Proyecto

### Estrategia de migración — full migration, no hybrid

**Decisión (2026-04-16):** migrar **todos** los micrositios de Libre Opción desde `/micrositios-files/` a `aplus.tudominio.com`. No hay hybrid, no hay reverse proxy.

**Por qué:** el punto de [[aplus-server/aplus-server|aplus-server]] es protección per-retailer. Un hybrid dejaría al retailer más importante con la menor protección. Ver [[aplus-server/migracion-libreopcion|migración]] para el detalle de las 3 opciones y por qué se descartaron las otras.

**Cómo aplicar:** si en futuras sesiones alguien propone re-abrir el debate (hybrid, proxy), referenciar esta decisión. Solo re-evaluar si cambian constraints (ej: SEO que requiera same-origin, cookies agregadas al microsite).

### Estado de deploy (2026-04-16)

- Scaffold local completo en `/Users/hermess/www/aplus-server`
- **No es git repo todavía**
- Productos: `tuf-rtx5080` (scaffold, sin assets reales procesados)
- **No deployado a VPS** — `Caddyfile` tiene placeholder `aplus.tudominio.com` + email `cambiar@tudominio.com`
- `.env` tiene ejemplo de `ALLOWED_REFERERS` (Fravega, ML, Compragamer) — falta agregar Libre Opción
- `TOKEN_SECRET` todavía es placeholder (se autogenera en primer `./start.sh`)

**Cómo aplicar:** antes de recomendar comandos que asumen estado deployado (`rsync ... user@vps:...`), **preguntar el dominio real y el VPS**. Antes de migrar nada, pedirle al usuario que elija dominio + levante CF + edite Caddyfile.

## Referencia

### Integración actual de Libre Opción — `.syndication-iframe`

Observado en DevTools de `gamma.libreopcion.com` (2026-04-16):

```html
<div class="syndication-iframe-wrapper">
  <iframe src="/micrositios-files/<slug>/index.html"
          class="syndication-iframe"
          loading="lazy" frameborder="0"
          style="height: 7891px;"></iframe>
</div>
```

Claves:
- Micrositios servidos **same-origin** desde `public/micrositios-files/<slug>/index.html` del repo Nuxt de LO
- Classes CSS `.syndication-iframe-wrapper` + `.syndication-iframe` con estilos propios — **preservarlas** en el snippet post-migración
- El `style="height: 7891px"` es medido → LO ya tiene iframe-resizer (o equivalente) parent-side
- Slugs kebab-case (ej: `asus-sindicate-limited-edition`) — compatibles con la regex de aplus-server
- Ambientes: `gamma.libreopcion.com` (staging), `libreopcion.com` + `www.libreopcion.com` (prod)
- Componente a modificar: `SyndicationIframe.vue` (o equivalente) — agregar `APLUS_WHITELIST` durante Fase 2

Ver proyecto relacionado: [[Libre Opcion/Libre Opcion|Libre Opción]].

## Feedback

### Recomendaciones decisivas cuando se comparan opciones

Cuando el usuario pide "qué es lo mejor?" / "what's best?" después de ver N opciones, **elegir una** y justificarla, explicando por qué las otras no.

**Por qué:** patrón observado en esta sesión (2026-04-16) — ante 3 opciones de migración, responder decisivamente ("**(a) — full migration**") con reasoning de por qué NO las otras produjo alineamiento inmediato y un próximo paso concreto. Respuestas tipo "depende de X/Y" estancan la sesión.

**Cómo aplicar:**
- Al presentar opciones, tener ya una preferida — no un menú neutral
- Respuesta: pick en **bold** → reasoning → explícito "por qué no" para cada rechazada
- Incluir trade-offs del pick elegido (costos, no solo beneficios)
- Si genuinamente es un empate, preguntar **una** pregunta específica que rompa el empate, no devolver incertidumbre

Consistente con global preferences: *"Iterar rápido"* + *"Preferir simplicidad sobre complejidad"*.

## Ver también

- [[aplus-server/aplus-server|aplus-server]] — índice
- [[aplus-server/migracion-libreopcion|Migración desde /micrositios-files/]] — decisión estratégica completa
- [[aplus-server/contexto|Contexto]] — gotchas operativas y reglas del proyecto
