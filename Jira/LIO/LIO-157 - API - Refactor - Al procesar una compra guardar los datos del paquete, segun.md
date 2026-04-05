---
jira_key: "LIO-157"
aliases: ["LIO-157"]
summary: "API - Refactor - Al procesar una compra guardar los datos del paquete, segun los nuevos recursos y persistencia del dato en el front"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-12-02 12:39"
updated: "2024-12-04 04:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-157"
---

# LIO-157: API - Refactor - Al procesar una compra guardar los datos del paquete, segun los nuevos recursos y persistencia del dato en el front

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-02 12:39 |
| Actualizado | 2024-12-04 04:33 |
| Etiquetas | ninguna |
| Jira | [LIO-157](https://bluinc.atlassian.net/browse/LIO-157) |

## Relaciones

- **Padre:** [[LIO-133 - Ms Envios Libre Opcion|LIO-133]] Ms Envios Libre Opcion

## Descripcion

Refactor en recurso de confirmacion de compra LO.

`POST URL/pedidos/checkout/confirmar`

payload:

```
{
    "id": 656089,
    "bulk": {
        "weightKg": 0.06,
        "sizeCm": "5.89x5.89x5.89",
        "amount": 4
    }
}
```



Esta informacion debe persistir en tabla **pedclit**. en los campos.

```
packageWeight
packageSize
amountPackages
```
