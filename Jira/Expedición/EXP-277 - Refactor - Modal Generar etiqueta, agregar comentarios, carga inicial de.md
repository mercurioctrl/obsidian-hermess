---
jira_key: "EXP-277"
aliases: ["EXP-277"]
summary: "Refactor - Modal \"Generar etiqueta\", agregar comentarios, carga inicial de dirección, dirección completa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-05-08 08:24"
updated: "2023-06-08 06:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-277"
---

# EXP-277: Refactor - Modal "Generar etiqueta", agregar comentarios, carga inicial de dirección, dirección completa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-08 08:24 |
| Actualizado | 2023-06-08 06:38 |
| Etiquetas | ninguna |
| Jira | [EXP-277](https://bluinc.atlassian.net/browse/EXP-277) |

## Relaciones

- **Padre:** [[EXP-12 - Feat - Listar pedidos para envio|EXP-12]] Feat - Listar pedidos para envio
- **blocks:** [[SNB-807 - mejoras para oca y andreani|SNB-807]] mejoras para oca y andreani 

## Descripcion

Vamos a hacer un refactor sobre el modal “Generar Etiqueta” para solucionar algunos issues y mejorar la experiencia.

El refactor consta de tres partes

**1- Arreglar cargar inicial de la dirección**

[adjunto]
Como se ve en la imagen de arriba, siempre que abrís un modal de un pedido sin dirección y tenes que seleccionar aparece un cero. Mismo en todos los casos no aparece el string con la dirección, sino un id. 

**2 - La direccion se ve sin la localidad**

[adjunto]
El string de dirección aparece como {direccion}-{provincia}-{cp}

Debería ser {direccion}-{localidad}{provincia}-{cp}

**3 - Agregar comentarios.**

Como a veces la dirección no fue cargada, es muy útil tener los comentarios que tiene el pedido y era parte del requerimiento original, pero parece que no se ven.

Estaría bueno agregar debajo los comentarios que se obtienen de 

Los comentarios deberían poder obtenerse en el momento que se abre el modal con el recurso [link](https://lioteam.atlassian.net/browse/EXP-240)
