# Memoria del proyecto

Consolidado de la memoria de Claude (`~/.claude/projects/-var-www-d-link*/memory/`) al 2026-09-05.

## Proyecto (project)
Estudio [[contexto|Blu]] contratado por D-Link Argentina para reposicionar la marca (perdió
relevancia/top-of-mind en ~10 años; compite contra TP-Link). Entregables en `/var/www/d-link/`:
investigación → estrategia → campaña → pitch, + landings web + familia plan-trabajo +
**videos/clips con IA**.

**Estado al 2026-09-03:** los 4 entregables core completos, 3 planes por canal, piezas web
(`index.html`, `propuesta.html`, `brand-guidelines/`), la familia [[plan-trabajo]] (deployada en
`dlink.blu.net.ar`), y el **nuevo formato [[videos-clips-ia|videos/clips con IA]]** en
`/var/www/d-link/clips/` (explainer con presentadora + reel de producto). Ver [[changelog]] y
[[arquitectura]].

**3 variantes de presupuesto/alcance coexisten a propósito (no unificar sin pedido):**
- docs 01–04 → **solo Argentina, ~USD 2.000/mes**.
- [[landings|propuesta.html]] → **Argentina + Chile, USD 1.800/mes**.
- [[plan-trabajo]] → **Argentina + Perú + Chile, USD 2.300/mes** (incluye el 6º workstream Site).

## Usuario (user)
Tiene un estudio de marketing digital llamado **Blu** (`blustudioinc.com`) que arma propuestas web
token-gated con lockup co-branded "<Cliente> × Blu". Detalle en [[contexto]].

**Preferencias observadas:** numerar workstreams/slides secuencialmente sin saltos en piezas cara al
cliente; logo Blu **negro sobre claro / blanco sobre oscuro** (nunca el azul `#0474f4` en piezas D-Link);
íconos flat, no emojis a color; cuando cambia contenido de [[plan-trabajo]] pide regenerar los 4
artefactos juntos. En **[[videos-clips-ia|videos IA]]**: prefiere UGC "sin manos" full-bleed, esquemas
**animados** (no collage), máxima calidad (Veo 3), **voz argentina real clonada** (no TTS neutro),
badges redondeados y logos reales. Reglas de trabajo: pedir OK antes de conectarse/ejecutar (avisar lotes); nunca pisar recursos, versionar.

## Referencia (reference)
- Propuesta modelo (Gigabyte): `blustudioinc.com/propuestas/gigabyte?token=gbt-mkt-2026`.
- Sitio oficial D-Link LA: `la.dlink.com`. Paletas: azul insignia `#4481a7` (landings de campaña),
  teal `#0083A5`/`#0087A9` (m15-2, brand-guidelines, plan-trabajo), **azul real `#0187AA`** (videos/clips,
  muestreado de piezas oficiales).
- **Pipeline de video/PDF** de plan-trabajo y clips: `.claude/scripts/render_video.py` + motor
  `window.__seek(t)`. Gotcha: la ruta HTML debe ser absoluta.
- **Videos IA con fal.ai** (ver [[videos-clips-ia]]): Veo 3 (video), sync-lipsync/v2 (lip-sync),
  flux-pro (retrato), minimax/voice-clone (voz clonada), whisper (subtítulos). Key en `clips/.env.local`
  (⚠️ rotar). Kling `CFG=0.2` evita rayos de luz.
- Bóveda Obsidian local: `/var/www/obsidian-hermess`, carpeta `D-Link`.

## Pendiente
Cerrar gaps de data (scraping MercadoLibre + sell-through) antes de fijar metas numéricas. En videos:
**derechos de la voz clonada** antes de publicar; opcional aplicar el motor animado + placa al reel
y extender el pipeline a otros héroes (R15, M30, etc.).


## Videos IA (sep-2026) — resumen
Biblioteca `clips/biblioteca/` (avatares + voces clonadas reutilizables por `custom_voice_id` de MiniMax
+ casos). 3 comerciales de **animación pura** 30s (overview / EAGLE PRO AI / cobertura). **Paleta real
del PSD**: teal `#0CCBD7→#0587a2` + textura de líneas concéntricas (nunca el teal oscuro). Regla: no
generar video/voz sin preguntar. Detalle en [[videos-clips-ia]].

**Caso VLAN B2B (sep-2026):** primer contenido B2B (switches/VLAN), superando un video que rebotó
gerencia. Producto héroe **DGS-1210-28P**. Sumamos **gpt-image-1 (OpenAI vía fal)** para ilustración de
alta calidad (switch ilustrado, edificio, red plana, grupos de PCs) y **OmniHuman** para **presentadora
IA** (foto→habla) intercalada 3× con animaciones; subtítulos solo cuando ella habla. Nuevo avatar
`D-ojos-verdes-openai`. Reglas confirmadas: **pedir autorización antes de conectarse/ejecutar procesos**
(avisar si es en lote) y **nunca pisar recursos → versionar** (`-v2`).

## Ver también
[[D-Link]] · [[contexto]] · [[arquitectura]] · [[plan-trabajo]] · [[videos-clips-ia]]
