---
jira_key: "LOCAPP-66"
aliases: ["LOCAPP-66"]
summary: "APP - Refactor - Agregar percepciones diferenciadas (CABA / ARBA)"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-05-09 09:54"
updated: "2025-05-12 14:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-66"
---

# LOCAPP-66: APP - Refactor - Agregar percepciones diferenciadas (CABA / ARBA)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-09 09:54 |
| Actualizado | 2025-05-12 14:28 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-66](https://bluinc.atlassian.net/browse/LOCAPP-66) |

## Relaciones

- **Padre:** [[LOCAPP-21 - Mostrar PDF descargable|LOCAPP-21]] Mostrar PDF descargable

## Descripcion

- Agregaremos en el rotulo un nuevo item “Per. Ingresos Brutos ARBA”, remplazando “Per./Ret. de IVA”


- Cambiaremos el nombre “Per./Ret. Ingresos Brutos” por “Per. Ingresos Brutos CABA”



Los valores (ahora diferenciados en 2) los tomaremos de los nuevos parametros `perceptionCabaCharged` y `perceptionArbaCharged` 

[adjunto]
```
"precio": "12,08",
"subtotal": "120,79",
"internalTax": "0,00"
}
],
"totales": {
"moneda": "DOL",
"cotizacion": "1130,00",
"perIngresosBrutos": "3,62",
"importeTotal": "149,77",
"netoNoGravado": "120,79",
"importeTotalPalabras": "Ciento cuarenta y nueve dolares con setenta y siete centavos.",
"observacionMoneda": "El total de este comprobante expresado en moneda de curso legal  - dólares -  considerándose un tipo de cambio de 1130.0.",
"obsevacionMonedaTotal": "169240,10",
"neto21": "120,79",
"iva21": "25,36",
"neto105": "0,00",
"iva105": "0,00",
"neto0": "0,00",
"iva0": "0,00",
"iibbPerception": "3,62",
"perceptionCabaCharged": "3,92", <--- SE AGREGA
"perceptionArbaCharged": "2,92", <--- SE AGREGA
"internalTax": "0,00"
},
"pie": {
"cae": "75198378949536",
"vencimientoCae": "19/05/2025"
```
