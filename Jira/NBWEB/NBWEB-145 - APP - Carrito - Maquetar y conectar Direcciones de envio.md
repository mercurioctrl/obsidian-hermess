---
jira_key: "NBWEB-145"
aliases: ["NBWEB-145"]
summary: "APP -  Carrito - Maquetar y conectar Direcciones de envio "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-04-26 15:26"
updated: "2022-06-26 21:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-145"
---

# NBWEB-145: APP -  Carrito - Maquetar y conectar Direcciones de envio 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-26 15:26 |
| Actualizado | 2022-06-26 21:33 |
| Etiquetas | ninguna |
| Jira | [NBWEB-145](https://bluinc.atlassian.net/browse/NBWEB-145) |

## Relaciones

- **Padre:** [[NBWEB-140 - APP - Conexión con el carrito|NBWEB-140]] APP - Conexión con el carrito
- **is blocked by:** [[NBWEB-142 - API - Traer direcciones de envío|NBWEB-142]] API - Traer direcciones de envío

## Descripcion

9/05/22 Se cambia la ruta para traer las direcciones de envio de la cuenta, ahora se usa

```
GET {{API_URL}}/v1/miCuenta/shippingAddress
```

---



Para el componente de calculo de envío, se deben cargar las direcciones disponibles para el cliente.

Maquetar y conectar.



Imagen de referencia como ayuda memoria:

[adjunto]
