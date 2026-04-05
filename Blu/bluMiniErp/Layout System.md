# Layout System

Layout de dos columnas fijas: sidebar persistente + area de contenido scrolleable.

## Estructura

```
+------------------+------------------------------------------------+
|                  |  Breadcrumb Bar (h-14, border-bottom)          |
|     Sidebar      +------------------------------------------------+
|     (w-[280px])  |                                                |
|     fixed left   |  Main Content Area                             |
|     full height  |  (p-8, overflow-y-auto, bg-[#F5F5F0])         |
|     bg-[#F7F7F2] |                                                |
+------------------+------------------------------------------------+
```

Colores de [[Design Tokens]].

## Template - layouts/default.vue

```vue
<template>
  <div class="flex h-screen overflow-hidden">
    <aside class="w-[280px] flex-shrink-0 bg-[#F7F7F2] border-r border-[#E8E8E3] flex flex-col overflow-y-auto">
      <DashboardSidebar />
    </aside>
    <div class="flex-1 flex flex-col min-w-0">
      <header class="h-14 flex-shrink-0 bg-white border-b border-[#E8E8E3] flex items-center justify-between px-8">
        <DashboardBreadcrumb />
        <SearchInput placeholder="Search..." />
      </header>
      <main class="flex-1 overflow-y-auto bg-[#F5F5F0] p-8">
        <slot />
      </main>
    </div>
  </div>
</template>
```

## Sidebar Anatomy

### 1. Organization Switcher (top)
- Logo 36x36px, label `text-[11px] text-[#9B9B93]`, org name `text-sm font-semibold`

### 2. Navigation Sections
- Section title: `text-[11px] font-medium tracking-[0.05em] uppercase text-[#9B9B93]`
- Nav items: ver [[Componentes UI]]

### 3. Nav Item States
- **Inactivo:** `text-[#4A4A43] hover:bg-[#EEEEE9]`
- **Activo:** `text-white bg-[#1A1A1A] font-medium`

## Breadcrumb Bar

- Height: 56px, background white, bottom border `#E8E8E3`
- Left: breadcrumb path
- Right: search input

## Responsive

| Breakpoint | Sidebar | Contenido |
|-----------|---------|-----------|
| >= 1280px | Visible, 280px fijo | Llena el resto |
| 768-1279px | Colapsable (hamburger) | Full width colapsado |
| < 768px | Overlay drawer | Full width |

## Grid del contenido

### KPI Cards
```html
<div class="grid grid-cols-3 gap-6">
  <KpiCard v-for="kpi in kpis" v-bind="kpi" />
</div>
```

### Full-width sections
```html
<div class="mt-6">
  <SalesTrendChart :data="salesData" />
</div>
```

### Two-column split
```html
<div class="grid grid-cols-2 gap-6 mt-6">
  <RecentOrders />
  <TopProducts />
</div>
```

---

## Ver tambien

- [[Design Tokens]] - Colores y espaciado aplicados
- [[Componentes UI]] - Componentes dentro del layout
- [[Page Templates]] - Composiciones de paginas completas
- [[Frontend#Navegacion]] - Sidebar del proyecto actual
