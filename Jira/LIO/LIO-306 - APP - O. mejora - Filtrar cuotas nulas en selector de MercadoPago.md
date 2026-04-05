---
jira_key: "LIO-306"
aliases: ["LIO-306"]
summary: "APP - O. mejora - Filtrar cuotas nulas en selector de MercadoPago"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-03-31 07:21"
updated: "2025-04-07 01:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-306"
---

# LIO-306: APP - O. mejora - Filtrar cuotas nulas en selector de MercadoPago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-31 07:21 |
| Actualizado | 2025-04-07 01:45 |
| Etiquetas | ninguna |
| Jira | [LIO-306](https://bluinc.atlassian.net/browse/LIO-306) |

## Relaciones

- **Padre:** [[LIO-8]] Proceso pago sencillo y competitiva a nivel financiamiento

## Descripcion

Durante el desarrollo de la feature que permite obtener dinámicamente las cuotas para la pasarela de pago de MercadoPago, se definió que aquellas cuotas cuyo valor venga como `null` no deben ser mostradas en el selector del formulario.

Sin embargo, se detectó que al consumir el endpoint (no se si lo haces así, sino corregime)

```
{API_URL}/pedidos/checkout/{numeroDePedido}
```

y recibir respuestas como las siguientes:

```
...
{
  "id": 5076,
  "key": 5076,
  "activo": true,
  "nombre": "Tarjeta de Credito / Debito",
  "descripcion": "Tarjeta de credito",
  "interes": 0,
  "soloSucursal": false,
  "cuotas": 4,
  "total": 0,
  "interes1": 0,
  "interes3": 6.83,
  "interes6": 12.83,
  "interes9": null,
  "interes12": null
}
...
```

Las opciones de 9 y 12 cuotas **siguen apareciendo** en el selector, a pesar de tener su valor en `null`. Esto parece estar ocurriendo debido a la lógica actual del método `updateInstallments` ubicado en:
`pages/mi-compra/partials/FormPagoTarjetaCreditoDebitoMP.vue`.

**Criterios de aceptación:**

- Las cuotas con valor `null` no deben ser incluidas en el selector de cuotas..


- Se debe revisar y ajustar el método `updateInstallments` para que realice este filtrado correctamente.


- Validar con ejemplos reales que las cuotas `null` efectivamente desaparezcan del frontend.



**Checklist para QA:**

- Simular checkout con cuotas válidas (1, 3, 6) y cuotas nulas (9, 12) y verificar que sólo se muestren las válidas.


- Simular respuesta con **todas** las cuotas en `null` y verificar que el selector no se muestre o se muestre un mensaje informativo.


- Verificar que no se rompa el flujo de pago ni haya errores en consola.


- Validar en navegadores modernos (Chrome, Firefox, Edge) que el comportamiento sea consistente.


- Confirmar que al seleccionar una cuota válida, el calculo de intereses y total sea correcto
