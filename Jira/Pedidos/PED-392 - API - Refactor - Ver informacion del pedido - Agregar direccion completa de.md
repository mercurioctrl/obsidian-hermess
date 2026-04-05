---
jira_key: "PED-392"
aliases: ["PED-392"]
summary: "API - Refactor - Ver informacion del pedido -> Agregar direccion completa de envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-12-26 08:50"
updated: "2024-02-06 20:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-392"
---

# PED-392: API - Refactor - Ver informacion del pedido -> Agregar direccion completa de envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-26 08:50 |
| Actualizado | 2024-02-06 20:07 |
| Etiquetas | ninguna |
| Jira | [PED-392](https://bluinc.atlassian.net/browse/PED-392) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **relates to:** [[PED-537 - API - Refactor - Ver información del pedido - Agregar dirección de envío del|PED-537]] API - Refactor - Ver información del pedido -> Agregar dirección de envío del sitio web

## Descripcion

Refactorizaremos el recurso  

```
GET {API_URL}/v1/aboutOrder/{branch y order}
```

Para incluir debajo de  los totales (En caso de que tenga un envío en `pedclit.medioEnvioId` o `pedclit.idDirCliNbWeb`)

Lo haremos con el siguiente formato

{Medio de envio} - {Localidad} - {Provincia}

{Direccion} - {CodigoPostal}



Ejemplo:

Entregar - Ciudad de Buenos Aires - Buenos Aires

Av. Jujuy 1030 - CP: 2723
