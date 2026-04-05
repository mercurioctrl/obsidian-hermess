---
jira_key: "LIO-138"
aliases: ["LIO-138"]
summary: "APP - Refactor - Se deben transportar los objetos con informacion del paquete (pesos, medidas y bultos) dentro del checkout para poder enviarlo en el payload al procesar la compra"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-11-25 12:04"
updated: "2024-12-04 04:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-138"
---

# LIO-138: APP - Refactor - Se deben transportar los objetos con informacion del paquete (pesos, medidas y bultos) dentro del checkout para poder enviarlo en el payload al procesar la compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-25 12:04 |
| Actualizado | 2024-12-04 04:00 |
| Etiquetas | ninguna |
| Jira | [LIO-138](https://bluinc.atlassian.net/browse/LIO-138) |

## Relaciones

- **Padre:** [[LIO-133 - Ms Envios Libre Opcion|LIO-133]] Ms Envios Libre Opcion
- **action item from:** [[LIO-139 - API - Refactor - Cambiar el objeto en el recurso de cotización nativo (evaluar|LIO-139]] API - Refactor - Cambiar el objeto en el recurso de cotización nativo (evaluar migración a v4) para tener informacion del paquete disponible al front 

## Descripcion

Almacenaremos la informacion del paquete que proviene de [link](https://lioteam.atlassian.net/browse/LIO-139)  para poder enviarla en el ultimo paso del checkout de nuestro carrito usando

```
GET {API_URL}/pedidos/checkout/confirmar
```

```
{
  "id":673845,
    "bulk": {
        "weightKg": 0.5,
        "sizeCm": "16.82x16.82x16.82",
        "amount": 1
    }
}
```

Recordar revisar la ficha que tambien cotiza el envio


[adjunto]
