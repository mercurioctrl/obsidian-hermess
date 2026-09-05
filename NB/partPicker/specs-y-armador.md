# Specs, Matches y Armador

Estructura de tablas que vincula el catálogo de New Bytes con las especificaciones de hardware scrapeadas por `partPicker`, qué llega a SQL Server y qué no, y propuesta de proyecto para un armador de PC encima.

**Verificado:** 2026-09-05 · **Origen:** `~/www/partPicker/scraper.db` · **Destino:** `db-nb-massql-dev.blu.net.ar:4444` → `PRODUCTOS`

> No confundir con [[BluPartPicker]], que es otro proyecto: el agregador de mayoristas y resellers con `oracular_sku`. Este es el scraper de PCPartPicker que extrae specs para validar compatibilidad.

---

## 1. Qué hace el sistema

El catálogo de New Bytes tiene títulos y precios, pero no tiene **specs estructuradas**: no sabe que un disco es SATA de 3.5" ni que un motherboard es AM5 con 4 slots DDR5. Sin ese dato no se puede validar si dos componentes son compatibles.

`partPicker` llena ese hueco. Toma los SKUs del inventario, los matchea contra PCPartPicker y otras fuentes abiertas, extrae las specs de cada producto y las deja en una estructura consultable. El objetivo final declarado en `COMPATIBILIDAD.md` es alimentar un armador de PC.

### Pipeline

Un solo script Python (`scraper.py`), resumable, que persiste todo en SQLite. Las fases corren en orden y cada una puede cortarse y retomarse:

| Fase | Qué hace | Chrome |
|---|---|---|
| **0 · buildcores** | Matchea por `metadata.part_numbers` contra la Open DB de BuildCores. Solo rellena specs faltantes, nunca pisa. | no |
| **1 · index** | Selenium recorre los listados de 8 categorías de PCPartPicker → tabla `products`. | sí |
| **2 · match** | Cruza SKUs contra productos. Métodos: `exact_name`, `exact_slug_suffix`, `amd_core_digits`. Nunca substring fuzzy. | no |
| **2.5 · dataset** | Specs desde el dataset local `pc-part-dataset`. | no |
| **3 · scrape** | Entra a cada ficha matcheada sin specs y extrae la tabla de especificaciones. | sí |
| **4 · search** | Busca los SKUs sin match. Acepta solo si el SKU está en el slug o el Part# de la ficha coincide exacto. | sí |

Chrome se abre únicamente en las fases 1, 3 y 4, con `undetected-chromedriver` para pasar Cloudflare. Con `SKIP_PCPP=1` corre solo con fuentes offline y termina sin abrir el navegador.

Monitor Flask en el puerto 5050 con cinco pestañas: progreso, SKUs pendientes con match manual, listado de productos, editor de `spec_definitions` y resolución de discrepancias.

---

## 2. Las tablas

Hay dos mundos. **SQLite es la fuente de verdad**: ahí escribe el scraper y ahí está todo. **SQL Server es el destino de consumo**: recibe un subconjunto vía `sync_sqlserver.py`, para que las aplicaciones puedan joinear contra el catálogo sin salir del motor.

| Tabla | Qué guarda | Filas | En SQL Server |
|---|---|---:|---|
| `skus` | SKU del inventario: `id_interno` + `id_fabricante` (part number) | 13.998 | ✅ |
| `matches` | Vínculo SKU ↔ producto scrapeado, con `match_type` | 2.424 | ✅ |
| `product_specs` | Una fila por spec de cada producto | 26.243 | ✅ |
| `spec_definitions` | Catálogo de specs por categoría: `is_compat`, `nombre_es` | 179 | ✅ |
| `category_mapping` | Categoría PCPartPicker ↔ categoría del inventario (N:N) | 22 | ✅ |
| `products` | Productos indexados: `url`, `name`, `category` | 42.725 | ❌ |
| `spec_discrepancies` | Conflictos BuildCores vs. valor cargado | 260 | ❌ |
| `items` | Inventario del usuario (`sku`, nombre, categoría, marca) | 1.558 | ❌ |
| `categories` · `brands` | Taxonomía del inventario | — | ❌ |
| `progress` | Estado de resume del scraper | — | ❌ |

> [!warning] Hueco conocido
> `products` no se sincroniza, y es la tabla que tiene la **categoría** de cada producto. Del lado de SQL Server la categoría solo se puede derivar indirectamente vía `spec_definitions.category`. Funciona —no hay ningún `product_url` que caiga en dos categorías— pero es frágil: las **56 filas de `product_specs` sin `spec_def_id`** quedan sin categoría derivable. Para el armador conviene sincronizar `products`.

### Las tres claves

| Clave | Dónde | Qué es |
|---|---|---|
| `id_interno` | `skus`, `matches`, `CS.dbo.productos` | El ID numérico del artículo en el ERP. Es el pivote de todo. |
| `id_fabricante` | `skus` | Part number del fabricante (`WD10EZEX`). Es lo que se matchea contra PCPartPicker. |
| `product_url` | `matches`, `product_specs` | La ficha de origen. Clave natural de las specs. |

`id_interno` es el mismo número en los tres lugares donde vive el artículo: `NewBytes_DBF.dbo.articulo.ID_ARTICULO`, `NewBytes_DBF.dbo.articulo.codigo` y `CS.dbo.productos.id_interno`. `ID_ARTICULO` y `codigo` no difieren en ninguna de las 25.782 filas de `articulo`.

---

## 3. La cadena de joins

Para ir de un producto del catálogo a sus specs hay que atravesar tres saltos. `matches` es la bisagra: sin ella el `id_interno` y la `product_url` no se tocan.

```
┌──────────────────┐            ┌──────────────┐            ┌──────────────────┐            ┌────────────────────┐
│ CS.dbo.productos │            │ skus         │            │ matches          │            │ product_specs      │
│                  │ id_interno │              │ id_interno │                  │product_url │                    │
│ id_interno       ├───────────►│ id_interno PK├───────────►│ id_interno    PK ├───────────►│ product_url    ┐PK │
│ titulo           │            │ id_fabricante│            │ product_url      │            │ spec_name      ┘   │
│ precioFInal      │            │              │            │ match_type       │            │ spec_value         │
└──────────────────┘            └──────────────┘            └──────────────────┘            │ spec_def_id        │
                                                                                            └─────────┬──────────┘
                                                                                                      │ spec_def_id
                                                                                                      ▼
                                                                                            ┌────────────────────┐
                                                                                            │ spec_definitions   │
                                                                                            │ id             PK  │
                                                                                            │ name · nombre_es   │
                                                                                            │ category           │
                                                                                            │ is_compat          │
                                                                                            └────────────────────┘
```

Tres cosas de esta cadena que conviene no olvidar:

- **`matches` es 1:1 con el SKU** (`id_interno` es su PK), así que no multiplica filas. Un SKU apunta a lo sumo a un producto scrapeado.
- **Todos los joins deben ser `LEFT`** si querés que el artículo aparezca aunque no tenga specs. Con `INNER`, un producto sin match devuelve cero filas en lugar de sus datos.
- **El join a `spec_definitions` debe ser `LEFT` sí o sí**: las 56 filas con `spec_def_id` en NULL desaparecerían con `INNER`.

---

## 4. Qué es `is_compat`

Es el flag que separa las specs que **sirven para validar compatibilidad** de las que son solo informativas. No todas las specs valen lo mismo: el socket de un CPU determina si entra en un motherboard; su caché L3 no determina nada.

- **28** de 179 definiciones marcadas
- **7.620** de 26.141 filas
- **9** reglas que las consumen, en **8** categorías

El flag vive en dos lugares con roles distintos. `spec_definitions.is_compat` es **la definición canónica**, editable desde el monitor web. `product_specs.is_compat` es una **copia desnormalizada** en cada fila, para poder filtrar sin joinear.

> [!danger] Se desincronizan
> Si cambiás un flag desde el monitor se actualiza `spec_definitions`, pero las filas ya escritas en `product_specs` conservan el valor viejo. **Ante la duda, filtrá por `sd.is_compat`, no por `ps.is_compat`** — que es lo que hace la query canónica de `COMPATIBILIDAD.md`.

### Las 9 reglas y las specs que consumen

| # | Regla | Comparación |
|---|---|---|
| 1 | CPU ↔ Motherboard | `cpu.Socket == mobo."Socket / CPU"` · match exacto de string |
| 2 | Motherboard ↔ RAM · tipo | `mobo."Memory Type" == ram.Type` · DDR4 / DDR5 |
| 3 | Motherboard ↔ RAM · módulos | módulos del kit ≤ `mobo."Memory Slots"` · parsear `2 x 8GB` o `2 \| 8` |
| 4 | Motherboard ↔ Gabinete | jerarquía EATX > ATX > Micro ATX > Mini ITX contra `case.Type` |
| 5 | GPU ↔ Gabinete | `gpu.Length ≤ case."Maximum Video Card Length"` · en mm |
| 6 | Cooler ↔ Gabinete | `cooler.Height ≤ case."Maximum CPU Cooler Height"` · solo coolers de aire |
| 7 | Cooler ↔ CPU | `cpu.Socket ∈ split(cooler."CPU Socket", " \| ")` |
| 8 | PSU ↔ build completo | `psu.Wattage ≥ (cpu.TDP + gpu.TDP) × 1.25` |
| 9 | PSU ↔ Gabinete | case Mini ITX sugiere `psu.Type = SFX` · aproximada, no bloquea |

Las reglas 1 a 7 producen **errores** (incompatibilidad física real). La 8 produce error o warning según el margen. La 9 es solo un warning.

---

## 5. Queries modelo

### A · Desde el catálogo web, deduplicando

Es la que más se usa. Requiere el CTE porque `CS.dbo.productos` tiene una fila por revendedor.

```sql
WITH prod AS (
    SELECT id_interno, titulo, Id_fabricante, precioFInal,
           ROW_NUMBER() OVER (PARTITION BY id_interno ORDER BY id) AS rn
    FROM CS.dbo.productos
    WHERE id_interno = 3574          -- el filtro va acá adentro
)
SELECT  a.id_interno,
        a.titulo,
        s.id_fabricante,
        COALESCE(NULLIF(sd.nombre_es, ''), ps.spec_name) AS spec,
        ps.spec_value,
        sd.is_compat
FROM       prod                             a
LEFT JOIN  PRODUCTOS.dbo.skus               s  ON s.id_interno   = a.id_interno
LEFT JOIN  PRODUCTOS.dbo.matches            m  ON m.id_interno   = s.id_interno
LEFT JOIN  PRODUCTOS.dbo.product_specs      ps ON ps.product_url = m.product_url
LEFT JOIN  PRODUCTOS.dbo.spec_definitions   sd ON sd.id          = ps.spec_def_id
WHERE a.rn = 1
ORDER BY sd.is_compat DESC, spec;
```

Devuelve 9 filas para el `3574` (*DISCO HDD 1TB WD BLUE SATA*). Sin el CTE devuelve **477**: ese artículo tiene 53 filas en `productos` × 9 specs.

### B · Solo las specs, sin pasar por el catálogo

Mucho más barata si el título y el precio no interesan.

```sql
SELECT COALESCE(NULLIF(sd.nombre_es, ''), ps.spec_name) AS spec,
       ps.spec_value, sd.is_compat, sd.category
FROM       PRODUCTOS.dbo.matches          m
JOIN       PRODUCTOS.dbo.product_specs    ps ON ps.product_url = m.product_url
LEFT JOIN  PRODUCTOS.dbo.spec_definitions sd ON sd.id          = ps.spec_def_id
WHERE m.id_interno = 3574;
```

### C · Desde el ERP

`NewBytes_DBF.dbo.articulo` no tiene el problema de duplicación: `ID_ARTICULO` es único. Se joinea igual que en A pero sin CTE.

> [!info] Detalles del server que cuestan una hora si no se saben
> La instancia distingue mayúsculas en los nombres de base: es `NewBytes_DBF`, no `newbyted_dbf` — con el nombre mal escrito tira `Invalid object name`. La tabla del ERP es `articulo`, en **singular**. Y las bases están en la misma instancia, así que el cross-database join funciona sin linked server.

---

## 6. Trampas de los datos

Ninguna es un bug a arreglar: son propiedades del dato que cualquier consumidor tiene que respetar.

### 6.1 · `CS.dbo.productos` multiplica todo por revendedor

447.247 filas para 16.448 `id_interno` distintos. Cada revendedor (`id_usuario`) tiene su copia con su propio `precioFInal`; el título y el `Id_fabricante` son los mismos. Cualquier join sin deduplicar multiplica las specs por la cantidad de revendedores.

Peor: hay **1.253 pares `(id_interno, id_usuario)` duplicados**, así que filtrar por revendedor tampoco garantiza una sola fila. El `ROW_NUMBER` es obligatorio en los dos casos.

### 6.2 · Los valores no están normalizados

Las specs vienen de tres fuentes distintas (PCPartPicker, BuildCores, pc-part-dataset) y conservan el formato de origen:

| Caso | Ejemplos reales | Cómo resolverlo |
|---|---|---|
| Unidad presente o no | `850 W` · `850` · `300 mm` · `300` | regex `(\d+)` |
| Doble unidad | `420 mm \| 16.535"` | tomar lo previo al `\|` |
| Sockets del cooler | `AM4 \| AM5 \| LGA1700` | split por `" \| "` |
| Módulos de RAM | `2 x 8GB` · `2 \| 8` | regex `^(\d+)\s*[x\|]` |
| Tipo de gabinete | `ATX Mid Tower` · `MicroATX Mini Tower` | keywords, default ATX |
| Eficiencia PSU | `gold` · `80+ Gold` · `platinum` | upper, quitar `80+ ` |
| Capacidad | `1 TB` · `1000` · `512` | convertir todo a GB |

### 6.3 · En BuildCores, `0` significa «sin dato»

El 35% de los motherboards traen `sata_6_gb_s = 0` aunque la placa tenga puertos. El scraper ya lo cubre con `BC_ZERO_IS_MISSING`, pero si alguna vez se lee la Open DB directo, tenerlo presente.

### 6.4 · Hay 260 discrepancias sin resolver

Conflictos reales entre BuildCores y el valor ya cargado, ninguno resuelto todavía. Están en `spec_discrepancies` con UI de resolución en el monitor. **No están sincronizadas a SQL Server**, así que desde ahí no se ven: un valor puede estar en disputa sin que el consumidor lo sepa.

### 6.5 · El sync es manual

Nada dispara `sync_sqlserver.py`: ni cron, ni el scraper al terminar, ni un botón en el monitor. Se corre a mano. Además inserta fila por fila con commit cada 100, lo que hace que una carga completa tarde alrededor de **80 minutos**; con `executemany` por lotes baja a minutos.

---

## 7. Cobertura real

Este es el número que define si el armador es viable, y conviene mirarlo antes de escribir una línea.

- **13.998** SKUs cargados
- **2.413** con specs → **17%** de cobertura
- **2.399** con specs de compatibilidad

De los 25.782 artículos del ERP, 2.413 tienen specs. Repartidos por categoría:

| Categoría | Productos con specs de compat | Estado |
|---|---:|---|
| video-card | 563 | holgado |
| motherboard | 533 | holgado |
| internal-hard-drive | 372 | holgado |
| memory | 300 | holgado |
| cpu | 264 | holgado |
| case | 196 | justo |
| cpu-cooler | 90 | **cuello de botella** |
| power-supply | 81 | **cuello de botella** |

Un armado necesita las 7 categorías simultáneamente, así que **la categoría más pobre define el techo**. Con 81 fuentes y 90 coolers hay suficiente para que el armador funcione, pero no para que ofrezca variedad en esas dos. Subir la cobertura de PSU y cooler es el trabajo de datos de mayor impacto.

> [!success] Resuelto — el stock sale de otra tabla
> `CS.dbo.productos.stock_cliente` **no es la fuente de stock**: de los productos con specs, uno solo lo tiene en cero positivo. Ese campo refleja el catálogo web/marketplace, no la existencia real.
>
> **"En stock" = fila en `NewBytes_DBF.dbo.stocks` con `nstock > 0`** para cualquier almacén (`ID_ALMACEN`), vinculado por `stocks.ID_ARTICULO = id_interno`. Con esa fuente hay **2.869 artículos en stock, 243 de ellos con specs**. Detalle en [[operacion#Origen del stock dato clave]].

---

## 8. Proyecto: armador de PC

La idea: una pantalla donde el cliente elige componentes paso a paso y en cada paso solo ve lo que **encaja** con lo que ya eligió, con el precio de New Bytes y el total actualizándose. Todo sobre el catálogo real de `CS.dbo.productos`.

### La decisión de arquitectura que importa

La tentación es joinear y parsear en vivo. No conviene: las reglas necesitan comparar números (`Length ≤ Maximum Video Card Length`) sobre valores guardados como texto sin normalizar, y hacer ese parseo en cada request, contra una tabla de 447.247 filas que además hay que deduplicar, es caro y frágil.

**La normalización va una sola vez, a una tabla tipada.** Un job lee la cadena de joins, aplica las reglas de parseo de `COMPATIBILIDAD.md` y escribe una fila por `id_interno` con columnas ya tipadas:

```sql
CREATE TABLE armador_componentes (
    id_interno        INT PRIMARY KEY,
    categoria         VARCHAR(40),   -- cpu, motherboard, memory, ...
    titulo            VARCHAR(255),
    -- claves de compatibilidad, ya parseadas
    socket            VARCHAR(20),   -- cpu, motherboard
    socket_list       VARCHAR(300),  -- cooler: lista separada por |
    form_factor       VARCHAR(20),   -- motherboard, psu
    case_max_ff       VARCHAR(20),   -- gabinete: mayor ff que acepta
    memory_type       VARCHAR(10),   -- DDR4 / DDR5
    memory_slots      INT,
    memory_modules    INT,
    tdp_w             INT,           -- cpu, gpu
    wattage_w         INT,           -- psu
    length_mm         INT,           -- gpu
    max_gpu_len_mm    INT,           -- gabinete
    height_mm         INT,           -- cooler
    max_cooler_h_mm   INT,           -- gabinete
    -- comercial, refrescado aparte y más seguido
    precio            DECIMAL(12,2),
    stock             INT,
    activo            BIT,
    actualizado       DATETIME
);
```

Con eso, cada regla de compatibilidad se vuelve un `WHERE` sobre enteros, y el armador filtra 2.400 filas en vez de medio millón. Las specs crudas siguen disponibles en `product_specs` para mostrar la ficha completa.

> [!tip] Por qué separar precio y stock del resto
> Las specs cambian cuando corre el scraper (semanas). El precio y el stock cambian todo el día. Si van en el mismo refresh, o recalculás parseos innecesariamente o servís precios viejos. Dos jobs con cadencias distintas sobre la misma tabla.

### Fases

**Fase 0 — Cerrar el pipeline de datos.** Nada de lo que sigue tiene sentido sobre datos que no se actualizan solos.

- Agregar `products` al `SYNC_CONFIG` para tener la categoría de forma directa
- Pasar el sync a `executemany` por lotes: de ~80 minutos a minutos
- Automatizarlo — cron, o llamada al final de `scraper.py`
- Resolver las 260 discrepancias pendientes en el monitor
- **Averiguar dónde está el stock real**, que hoy en dev viene vacío

**Fase 1 — Tabla normalizada.** El job de parseo y la tabla `armador_componentes`. Es el corazón del proyecto y donde vive toda la fealdad del dato sin normalizar, encapsulada en un solo lugar.

Entregable verificable: contar cuántos productos quedan con cada columna en NULL. Un CPU sin `socket` parseado es un CPU que el armador no puede ofrecer, y ese número es la cobertura real, más honesta que los 2.413 de hoy.

**Fase 2 — Motor de reglas.** Las 9 reglas como funciones puras sobre la tabla tipada, devolviendo `error` / `warning` / `info` con un mensaje que explique *qué* no encaja: «el cooler mide 160 mm y en este gabinete entran 155». Es la única parte del sistema que merece tests unitarios de verdad, y son fáciles: entrada tipada, salida determinística.

**Fase 3 — API.** Laravel 11, siguiendo el patrón por dominio ya usado. Cuatro endpoints alcanzan:

```
GET  /api/armador/categorias      # categorías con conteo de disponibles
GET  /api/armador/componentes     # filtra por categoría y por lo ya elegido
POST /api/armador/validar         # recibe el build entero, devuelve errores y warnings
POST /api/armador/build           # persiste el armado y devuelve link compartible
```

**Fase 4 — Interfaz.** Nuxt 3. El orden sugerido en `COMPATIBILIDAD.md` es CPU → Motherboard → RAM → GPU → Gabinete → Cooler → PSU → Almacenamiento, porque cada paso restringe al siguiente.

Dos detalles que hacen la diferencia: mostrar los incompatibles **grisados con el motivo** en vez de ocultarlos —el cliente aprende por qué no puede elegirlos— y un medidor de consumo que se va llenando contra la PSU elegida.

**Fase 5 — Precio por revendedor.** Recién acá entra la dimensión `id_usuario`. El armador arranca con un precio de referencia; después se le agrega el precio del revendedor logueado, que es exactamente la fila que hoy el `ROW_NUMBER` descarta.

---

## 9. Riesgos

Ordenados por cuánto pueden hundir el proyecto.

| Riesgo | Impacto | Cómo se mitiga |
|---|---|---|
| ~~Stock vacío~~ — **resuelto** | — | El stock sale de `NewBytes_DBF.dbo.stocks.nstock`, no de `stock_cliente`. 243 artículos en stock con specs. Ver [[operacion]]. |
| **PSU y cooler escasos** — 81 y 90 productos | alto | Priorizar esas dos categorías en el scraper y en el match manual. Son las que cortan la variedad de armados. |
| **Parseo pierde productos** — formatos mixtos | medio | Medirlo explícitamente en la Fase 1: NULLs por columna. Lo que no parsea se arregla o se documenta, no se ignora. |
| **Sync manual** — nada lo dispara | medio | Fase 0. Barato de resolver y evita que el armador sirva datos viejos sin que nadie se entere. |
| **Reglas 6 y 9 aproximadas** — AIO sin dato de radiador | bajo | Ya marcadas como warning en la doc original. Mantenerlas así: avisar, no bloquear. |
| **Cloudflare corta el scraper** | bajo | El pipeline es resumable y las fuentes offline no dependen de Chrome. No bloquea el armador, solo frena el crecimiento de cobertura. |

### Por dónde empezar

La Fase 0 es media jornada de trabajo y desbloquea todo lo demás. La Fase 1 es donde está el riesgo real del proyecto: hasta no ver cuántos productos sobreviven al parseo, la cobertura de 2.413 es un techo teórico, no un número con el que se pueda planificar.

---

## Referencias

- Repo: `~/www/partPicker` · `scraper.py`, `monitor.py`, `sync_sqlserver.py`
- Reglas completas con ejemplos de parseo: `COMPATIBILIDAD.md` del repo
- Arquitectura del pipeline: `CLAUDE.md` del repo
- Credenciales de SQL Server: `.env` del proyecto

**Conteos verificados 2026-09-05:** spec_definitions 179 · matches 2.424 · product_specs 26.243 · skus 13.998 · category_mapping 22

## Ver también

- [[partPicker]] — índice del proyecto
- [[operacion]] — cómo correr, origen del stock, reconstruir `scraper.db`, cobertura in-stock
- [[changelog]] — historial de sesiones
- [[contexto]] — decisiones abiertas y próximos pasos
