---
jira_key: "NBWEB-424"
aliases: ["NBWEB-424"]
summary: "API - Feat - Enviar correo al generar la etiqueta"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-22 09:29"
updated: "2022-08-01 12:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-424"
---

# NBWEB-424: API - Feat - Enviar correo al generar la etiqueta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-22 09:29 |
| Actualizado | 2022-08-01 12:37 |
| Etiquetas | ninguna |
| Jira | [NBWEB-424](https://bluinc.atlassian.net/browse/NBWEB-424) |

## Relaciones

- **Padre:** [[NBWEB-423 - Logistica Envios|NBWEB-423]] Logistica Envios

## Descripcion

Esta recurso se trata sobre como deben recibir en el sector “expedición” interno de la empresa la informacion sobre los pedidos que salen despachados.

En principio se usara una bandeja electrónica (que simplemente es un correo que todos reciben) que simula un proceso que antes se realizaba en el mundo físico: Que un administrativo prepare todos los pedidos acumulados los imprima y los baje y deposite en una bandeja para que quienes arman paqueteria los armen y y peguen etiquetas.

Vamos a modificar el recurso [link](https://lioteam.atlassian.net/jira/software/c/projects/NBWEB/boards/34?modal=detail&selectedIssue=[[NBWEB-357]]) 

```
POST {{API_URL}}/v1/miCuenta/ordenesDeCompra/0002/10217260/addTrackingOrder
```

Para que en caso de ser exitoso, envié un correo al sector de deposito (correo receptor: [prepararpaquete@nb.com.ar](mailto:prepararpaquete@nb.com.ar))

#### ¿como debe ser el correo?

[adjunto]
Esos son los elementos básicos. Tomamos el contenido del correo que se genera cuando se hace una compra, agregamos numero de orden y pedido y  le adjuntamos la etiqueta.

#### ¿como obtengo la etiqueta?

Haciendo uso el el micro servicio de envíos, mas precisamente el recurso:

```
GET {{API_URL}}/getLabel/{trackginNumber}/pdf
```

Este archivo debe obtenerse y guardarse como un adjunto en el correo.

---

Cualquier duda me consultas!
