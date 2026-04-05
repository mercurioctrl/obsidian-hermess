---
jira_key: "LIO-524"
aliases: ["LIO-524"]
summary: "APP - Refactor - Implementar evento add_to_cart en Google Analytics con métricas de ingresos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-02-02 08:55"
updated: "2026-02-12 13:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-524"
---

# LIO-524: APP - Refactor - Implementar evento add_to_cart en Google Analytics con métricas de ingresos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-02 08:55 |
| Actualizado | 2026-02-12 13:58 |
| Etiquetas | ninguna |
| Jira | [LIO-524](https://bluinc.atlassian.net/browse/LIO-524) |

## Relaciones

- **Padre:** [[LIO-344 - Adwords y Analytics|LIO-344]] Adwords y Analytics

## Descripcion

Se requiere implementar el tracking del evento `add_to_cart` de Google Analytics cuando los usuarios agregan productos al carrito. Actualmente el componente `AgregarComprar.vue` emite un evento `@trackADS` pero los componentes padres no lo capturan ni procesan, por lo que el evento nunca llega a Google Analytics.


**Contexto actual**
Actualmente ya existen implementaciones funcionales de eventos de e-commerce:

- `purchase` en /app/pages/mi-compra/confirmar.vue


- `view_item` en /app/pages/producto/_id.vue


- `view_item_list` y `view_search_results` en /app/pages/busquedas/general.vue

El componente `AgregarComprar.vue` emite `this.$emit("trackADS", "add_to_card")` (notar el typo: dice "card" en lugar de "cart"), pero ningún componente padre tiene el listener @trackADS para capturar este evento y enviarlo a GA.





**Alcance**

- Capturar y procesar el evento add_to_cart en todos los componentes padres donde se usa AgregarComprar:

- /app/pages/producto/_id.vue


- /app/components/Productos/ModuloC.vue


- /app/components/Productos/ModuloB.vue


- /app/components/Productos/VendedorInformacion.vue


- /app/components/Productos/VerMasCuotas.vue


- /app/pages/producto/partials/SellerOption.vue




- Corregir el nombre del evento de "`add_to_card`" a "`add_to_cart`"


- Enviar datos completos del producto al evento GA:

- `currency`: "ARS"


- `value`: precio × cantidad (para métricas de ingresos)


- `items`: array con `item_id`, `item_name`, `quantity`, `price`





- Habilitar métricas de ARPU en Google Analytics mediante la correcta implementación del evento con valor monetario





**Consideraciones técnicas**

- El componente `AgregarComprar.vue` actualmente solo recibe `productoId` y cantidad. Se debe evaluar cómo obtener el resto de los datos necesarios (precio, nombre, `idFabricante`) - ya sea pasándolos como props adicionales u obteniéndolos de otra forma.


- Revisar la consistencia de nombres de propiedades (idFabricante vs ID_fabricante) según el contexto donde se use.


- El evento `purchase` ya implementado debe seguir funcionando correctamente para el cálculo de ingresos totales.
