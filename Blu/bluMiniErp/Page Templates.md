# Page Templates

Plantillas de paginas completas que muestran como se ensamblan los [[Componentes UI]] dentro del [[Layout System]].

## 1. Dashboard Overview

Pagina principal tras login. KPIs + tendencias.

```
[Welcome back, User]
[KPI Card 1]  [KPI Card 2]  [KPI Card 3]
[Sales Trend Chart — full width]
[Recent Activity]  [Top Items]
```

### Domain mapping
| Generic | E-commerce | CRM | SaaS |
|---------|-----------|-----|------|
| KPI 1 | Total Revenue | Total Deals | MRR |
| KPI 2 | Total Orders | Active Contacts | Active Users |
| KPI 3 | New Customers | Pipeline Value | New Signups |

## 2. List Page

Tabla de datos con busqueda, filtros y paginacion.

```
[Page Title]                    [+ Add New]
[Search] [Filter 1] [Filter 2]   [Export]
+-- DataTable --+
|  Header  |  Header  |  Actions  |
|  Cell    |  Cell    |  [...]    |
+-- Pagination --+
```

### Botones
- **Primary:** `bg-[#1A1A1A] text-white rounded-lg hover:bg-[#333333]`
- **Secondary:** `border border-[#E8E8E3] text-[#6B6B63] hover:bg-[#F5F5F0]`

## 3. Detail / Edit Page

Vista y edicion de una entidad.

```
< Back to [List]     [Entity Name]    [Actions]
+-- Primary Info (2/3) --+  +-- Side Info (1/3) --+
|  Field: Value          |  |  Status: Active      |
|  Field: Value          |  |  Created: Date       |
+-- Related Items Table --+
```

## 4. Settings Page

Configuracion con secciones de formulario.

```
[Tab: General] [Tab: Notifications] [Tab: API]
+-- Section Title --+
|  Description      |
|  Label  [Input]   |
|  Label  [Toggle]  |
+-- Another Section --+
                [Cancel]  [Save Changes]
```

### Tab style
- Activo: `border-[#1A1A1A] text-[#1A1A1A] font-medium`
- Inactivo: `border-transparent text-[#9B9B93]`

## Composicion para cualquier dominio

1. Landing/home -> Dashboard Overview
2. Lista de entidades -> List Page
3. Entidad individual -> Detail/Edit Page
4. Configuracion -> Settings Page

### Mock data
- Usar 10-20 filas en tablas
- Estados variados (active, pending, completed)
- IDs realistas
- Moneda en formato local

Todos los colores y componentes segun [[Design Tokens]] y [[Componentes UI]].

---

## Ver tambien

- [[Componentes UI]] - Specs de cada componente usado
- [[Design Tokens]] - Tokens visuales aplicados
- [[Layout System]] - Shell donde viven estas paginas
- [[Dashboard UI Skill]] - Skill que genera estas paginas
