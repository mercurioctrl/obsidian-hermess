---
jira_key: "NBWEB-705"
aliases: ["NBWEB-705"]
summary: "APP - Feat - Agregar nuevos parametros a la explicacion de como se procesa el carrito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-04-12 10:53"
updated: "2024-04-15 04:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-705"
---

# NBWEB-705: APP - Feat - Agregar nuevos parametros a la explicacion de como se procesa el carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-12 10:53 |
| Actualizado | 2024-04-15 04:37 |
| Etiquetas | ninguna |
| Jira | [NBWEB-705](https://bluinc.atlassian.net/browse/NBWEB-705) |

## Relaciones

- **Padre:** [[NBWEB-636]] Documentacion publica
- **is blocked by:** [[NBWEB-703]] API - Refactor - Agregar parametros para guardar correo y nombre del cliente
- **is blocked by:** [[NBWEB-704]] APP - Refactor - Al "encender" el dropShipping en el carrito, mostrar 2 inputs para el nombre del cliente y su correo electronico

## Descripcion

```
{
    "codigoPostalFavorito": "1439",
    "mediodeEnvioId" : 4065,
    "medioDePagoId" : 3,
    "idDirCli" : 19201,
    "datosBulto": {
        "weightKg": 0.5,
        "sizeCm": "1.4x2.43x1.4",
        "amount": 1
    },
    "dropShipping": true,
    "dpPayload":{
        "clientName": "Moe Szyslak",
        "clientEmail" : "MoeSzyslak@gmail.com"
    }
}
```
