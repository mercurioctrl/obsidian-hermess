# Componentes UI — gigaErp

Componentes en `frontend/components/ui/` y `frontend/components/`. Por `pathPrefix: false`
en `nuxt.config.ts` se usan **sin prefijo de directorio**:
```vue
<FormField>   ✅
<UiFormField> ❌
```

## Modal — SIEMPRE con `v-model`

```vue
<Modal v-model="showModal" title="Nuevo" size="lg">
  <div class="space-y-4">
    <FormField label="Nombre" v-model="form.nombre" />
  </div>
  <template #footer>
    <button @click="showModal = false" class="px-4 py-2 text-sm text-[#6B6B63] hover:text-[#1A1A1A]">
      Cancelar
    </button>
    <button @click="guardar" class="px-4 py-2 text-sm font-medium bg-[#1A1A1A] text-white rounded-lg hover:bg-[#2D2D2D]">
      Guardar
    </button>
  </template>
</Modal>
```

**Sizes:** `sm` `md` (default) `lg` `xl` `2xl` `full`.
**NUNCA** usar `v-if` + `@close` — siempre `v-model`.

## DataTable

```vue
<DataTable
  :columns="[{ key: 'nombre', label: 'Nombre' }, { key: 'estado', label: 'Estado' }]"
  :rows="items"
  :loading="cargando"
  :pagination="paginacion"
  empty-message="No hay datos"
  @row-click="(row) => navigateTo(`/mi-modulo/${row.id}`)"
  @page-change="(p) => { pagina = p; cargar() }"
>
  <template #default="{ row }">
    <td class="px-4 py-3.5 text-sm text-[#1A1A1A]">{{ row.nombre }}</td>
    <td class="px-4 py-3.5"><StatusBadge :status="row.estado" /></td>
  </template>
</DataTable>
```

**Paginación:** el componente espera **camelCase** (`{ total, perPage, currentPage, lastPage, from, to }`).
Laravel devuelve snake_case en `res.meta` (`per_page`, `current_page`, etc.). **Mapear manualmente:**

```ts
paginacion.value = res.meta ? {
  total: res.meta.total,
  perPage: res.meta.per_page,
  currentPage: res.meta.current_page,
  lastPage: res.meta.last_page,
  from: res.meta.from,
  to: res.meta.to,
} : null
```

## FormField

```vue
<!-- input default -->
<FormField label="Nombre" v-model="form.nombre" :required="true" :error="errores.nombre" />

<!-- textarea -->
<FormField label="Notas" type="textarea" v-model="form.notas" />

<!-- select con slot -->
<FormField label="Estado" type="select" v-model="form.estado">
  <template #options>
    <option value="ACTIVO">Activo</option>
    <option value="INACTIVO">Inactivo</option>
  </template>
</FormField>

<!-- date -->
<FormField label="Fecha" type="date" v-model="form.fecha" />

<!-- override total via slot -->
<FormField label="Cliente">
  <select v-model="form.cliente_id" class="w-full px-3 py-2 ...">
    <option v-for="c in clientes" :key="c.id" :value="c.id">{{ c.nombre }}</option>
  </select>
</FormField>
```

## StatusBadge

Mapea status string → color + label. Status conocidos:

| Status | Color | Label |
|--------|-------|-------|
| `POR_HACER` / `EN_CURSO` / `READY_FOR_QA` / `LISTO` | varios | Tareas |
| `PENDIENTE` / `PAGADA` / `CANCELADA` | varios | Ventas |
| `BORRADOR` / `FACTURADA` / `ANULADA` | azul / verde / rojo | Órdenes de Venta |
| `ALTA` / `MEDIA` / `BAJA` | rojo / azul / gris | Prioridades |

```vue
<StatusBadge :status="row.estado" />
```

Para agregar uno nuevo, editar `components/ui/StatusBadge.vue` (no está en "no modificar").

## StatsCard

```vue
<StatsCard
  label="Ingresos"
  value="$450,000"
  unit="ARS"
  sublabel="últimos 30 días"
  :change="12.4"
  :sparkline="[40,55,30,70,65]"
/>
```

## Otros componentes

| Componente | Notas |
|------------|-------|
| `<Toast>` | Ya está en `app.vue`. Usar vía `useNotification()`. |
| `<NavItem to="/x" icon="lucide:..." label="..." />` | Solo en `layouts/default.vue`. |
| `<OrdenItems>` | Builder de ítems para [[modulos/ordenes-venta]] — top-level component. |

## Archivos que NO se deben modificar

- `frontend/middleware/auth.global.ts`
- `frontend/composables/useApi.ts`
- `frontend/layouts/auth.vue`
- `frontend/nuxt.config.ts` (no cambiar `pathPrefix` ni `ssr`)

## Ver también

- [[design-system]] — colores y tipografía
- [[arquitectura#Frontend]] — useApi, useAuthStore, useNotification
