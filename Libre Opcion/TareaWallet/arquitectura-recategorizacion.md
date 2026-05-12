# Arquitectura — Sistema de Recategorización de Productos

Feature desarrollada por Franco (fcallipo). Asigna automáticamente `id_categoria_lo` a productos del marketplace que no tienen categoría.

## Endpoints

| Método | URL | Descripción |
|--------|-----|-------------|
| `POST` | `/v4/categorias-admin/recategorizar` | Lanzar una corrida |
| `GET` | `/v4/categorias-admin/recategorizar/runs` | Historial de corridas |
| `GET` | `/v4/categorias-admin/recategorizar/runs/{runId}` | Detalle + items procesados |

## Flujo

```
POST /v4/categorias-admin/recategorizar
  → RecategorizarDispatchController
  → RecategorizarDispatchService::dispatch()
      - Valida solo_con_stock=true (obligatorio, sino 422)
      - Verifica que no haya corrida activa en DB (sino 409)
      - Crea registro 'pending' en categorizacion_runs
      - Despacha RecategorizarProductosJob a queue 'categorizacion'
  → RecategorizarProductosJob::handle()  [async]
      - UPDATE atómico WHERE status IN ('pending','running') para marcar 'running'
      - Carga productos con stock > 0 desde CS.dbo.productos
      - Por cada producto → CategoriaMatcher::intentarCategorizar()
      - Actualiza CS.dbo.productos si hubo match
      - Persiste item en categorizacion_runs_items
      - Cada 50 productos → actualiza resumen parcial
      - Al terminar → snapshot global + marca 'done'
```

## CategoriaMatcher — Algoritmo actual

**Estado: hardcodeado en PHP.** No lee las tablas de DB (ver sección siguiente).

### Orden de resolución (por título):

1. ¿Es combo/kit? → descarta (muy ambiguo)
2. `resolverPorTitulo(titulo)` — reglas stripos en orden de prioridad:
   - Heladera, Lavarropas, Aire acondicionado
   - Disco externo / SSD / HDD (con exclusiones entre sí)
   - Notebook/laptop (excluye si menciona disco/ram/cargador/funda)
   - PC armada/gamer
   - Monitor, Mousepad, Mouse, Teclado
   - Consola, Auricular, Fuente, Celular, PowerBank, Red, Bicicleta eléctrica
   - Cable/adaptador (al final, muy genérico)
3. Si no matchea → `resolverPorFamiliaNb(id_familia_original)` — switch case que mapea familia del proveedor NB a categoría LO

**Los patrones tienen positivos y negativos:**
- Positivos: si contiene alguna de estas palabras → matchea
- Negativos: si contiene alguna de estas palabras → no matchea aunque haya positivo
  - Ej: "Disco SSD para notebook" → no matchea como notebook (tiene "disco" y "ssd")

## Tablas de DB para matcher (preparadas, no conectadas aún)

```sql
[LO].[dbo].[categoriasPrediccionMatchFree]     -- 545 filas — positivos (LIKE %token%)
[LO].[dbo].[categoriasPrediccionMatchRequired] --   8 filas — token obligatorio
[LO].[dbo].[categoriasPrediccionMatchExclude]  -- 581 filas — negativos (excluyen match)
```

Todas tienen: `id`, `id_categoria`, `string_match` (formato `%TOKEN%` o `%TOK1%TOK2%`)

`precargarMapas()` está vacío — es el punto de extensión para conectar estas tablas.

## Algoritmo propuesto para reemplazar el switch hardcodeado

Usar índice invertido sobre primer token de cada patrón Free:

```
precargarMapas():
  parsear %A%B% → tokens ['a','b']
  freeIndex[primer_token] = [(categoria, tokens[])]
  excludeMap[categoria] = [tokens[][]]
  requiredMap[categoria] = [tokens[][]]

intentarCategorizar(producto):
  para cada primer_token del freeIndex:
    si aparece en título:
      verificar patrón completo (tokens en orden con stripos)
      → colectar categorías candidatas
  aplicar excludeMap y requiredMap
  resolver conflicto por especificidad (más tokens = más específico)
```

Ventaja: agregar sinónimos es un INSERT en DB, sin deploy.

## Tablas de DB del sistema

| Tabla | Base | Descripción |
|-------|------|-------------|
| `categorizacion_runs` | LO | Registro de cada corrida (status, params, contadores, snapshot) |
| `categorizacion_runs_items` | LO | Detalle por producto (antes/después) |
| `productos` | CS | Tabla de productos (se actualiza `id_categoria_lo`) |
| `categoriasPrediccionMatchFree` | LO | Sinónimos positivos para el matcher |
| `categoriasPrediccionMatchRequired` | LO | Tokens obligatorios |
| `categoriasPrediccionMatchExclude` | LO | Sinónimos negativos |

## Ver también

- [[TareaWallet]]
- [[changelog]]
