# Dashboard UI Skill

Skill para generar interfaces de admin dashboard con **Nuxt 3 + Vue 3 + Tailwind CSS**, siguiendo un sistema de diseno preciso.

## Cuando usar

Cuando el usuario pida construir un dashboard, panel de control, interfaz de gestion, o cualquier pagina de administracion interna.

## Archivos de referencia

Antes de escribir codigo, leer:
1. [[Design Tokens]] - Paleta de colores, tipografia, espaciado
2. [[Layout System]] - Sidebar + contenido principal, responsive
3. [[Componentes UI]] - Specs de cada componente
4. [[Page Templates]] - Plantillas de paginas completas

## Arquitectura

- **Nuxt 3** con file-based routing
- **Vue 3** Composition API con `<script setup>`
- **Tailwind CSS** para todo el styling
- **Pinia** para estado

## Filosofia de diseno

- **Whitespace generoso**: padding y margins amplios
- **Monospace accents**: labels de KPIs en mono uppercase
- **Paleta muted con verde accent**: neutrals + `#2D8C5A` solo para positivos
- **Cards con bordes sutiles**: sin sombras (o muy sutiles)
- **Flat design**: minimo uso de sombras

## Proceso de generacion

1. **Entender el dominio**: mapear a patrones conocidos (e-commerce, CRM, SaaS)
2. **Leer [[Design Tokens]]**: aplicar tokens consistentemente
3. **Construir layout**: empezar con `layouts/default.vue`. Ver [[Layout System]]
4. **Construir componentes bottom-up**: atoms -> moleculas -> organismos
5. **Ensamblar paginas**: seguir [[Page Templates]]
6. **Conectar datos**: Pinia stores con mock data realista

## Quality checks

- Colores exactos de [[Design Tokens]]
- Tipografia correcta por contexto
- Sidebar con seccionamiento correcto
- KPI cards con label mono, valor grande, sparkline, badge YoY
- Iconos con prefijo `lucide:`. Ver [[Frontend#Iconos]]

---

## Ver tambien

- [[Design Tokens]] - Especificacion visual completa
- [[Componentes UI]] - Specs de componentes
- [[Layout System]] - Estructura de layout
- [[Page Templates]] - Plantillas de paginas
- [[Frontend]] - Contexto del frontend del proyecto
