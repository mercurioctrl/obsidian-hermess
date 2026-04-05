---
jira_key: "COM-132"
aliases: ["COM-132"]
summary: "APP - Refactor - Agregar al modal del detalle de la orden los impuestos que son prorrateables abajo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-08-05 14:54"
updated: "2024-08-08 04:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-132"
---

# COM-132: APP - Refactor - Agregar al modal del detalle de la orden los impuestos que son prorrateables abajo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-05 14:54 |
| Actualizado | 2024-08-08 04:46 |
| Etiquetas | ninguna |
| Jira | [COM-132](https://bluinc.atlassian.net/browse/COM-132) |

## Relaciones

- **Padre:** [[COM-38]] Ver orden de compra
- **is blocked by:** [[COM-130]] API - Refactor - Agregar nuevo parametro al repositorio de impuestos

## Descripcion

Utilizando el refactor de la historia[link](https://lioteam.atlassian.net/browse/COM-130)  lo que haremos sera agregar abajo los impuestos que provienen del repositorio

```
GET {API_URL}v1/tariffTax?distribute=true
```

Estos son los impuestos que mostraremos aca abajo

[adjunto]
Solo mostraremos por el momento el nombre del impuesto y dejaremos un input para ingresar un monto total 

(mas adelante volveremos sobre este formulario para guardar el dato)
