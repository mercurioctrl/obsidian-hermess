---
jira_key: "PED-58"
aliases: ["PED-58"]
summary: "Agregar / Editar Envío en las ordenes de compra"
status: "Tareas por hacer"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2023-09-11 09:22"
updated: "2023-09-11 09:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-58"
---

# PED-58: Agregar / Editar Envío en las ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-11 09:22 |
| Actualizado | 2023-09-11 09:26 |
| Etiquetas | ninguna |
| Jira | [PED-58](https://bluinc.atlassian.net/browse/PED-58) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **Subtarea:** [[PED-59]] API - Feat - Cotizar envío a una orden de compra 
- **Subtarea:** [[PED-60]] APP - Feat - Cotizar envío a una orden de compra
- **Subtarea:** [[PED-73]] API - Feat - Agregar "item" envío a una orden de compra
- **Subtarea:** [[PED-97]] API - Review - Me muestra una direccion, pero no la cotiza porque dice que no la tiene
- **Subtarea:** [[PED-102]] APP - Feat - Cotizar envío de una orden de compra
- **Subtarea:** [[PED-106]] APP - Review - Al hacer clic en el pedido abierto, abrir el modal de pedido
- **Subtarea:** [[PED-111]] API- Review -  Al seleccionar un transportista ajustar datos de update/insert
- **Subtarea:** [[PED-114]] APP - Review en Clientes las acciones parametros y direcciones no responden correctamente
- **Subtarea:** [[PED-116]] API - Feat - Realizar seguimiento de una orden
- **Subtarea:** [[PED-140]] API - Feat - Agregar recurso para leer etiquetas
- **Subtarea:** [[PED-141]] API - Feat - Leer numeros de tracking
- **Subtarea:** [[PED-159]] API - Review - Al agregar un envio, tengo algunos problemas con la informacion que se muestar
- **Subtarea:** [[PED-183]] API - Review - En produ solo me aparecen cotizaciones de envio para entregar y camioneta
- **Subtarea:** [[PED-196]] API - Review - Permite guardar mas unidades de las "disponibles" dejando el valor "disponible" en negativo y no deberia
- **Subtarea:** [[PED-197]] APP - Review - Permite marcar mas unidades de las "disponibles" dejando el valor "disponible" en negativo y no debería poder aumentarse mas, para que no se bloque
- **Subtarea:** [[PED-229]] API - Feat - Editar precio, se debe poder ingresar un precio a mano para un item determinado
- **Subtarea:** [[PED-230]] APP - Feat - Editar precio, se debe poder ingresar un precio a mano para un item determinado
- **Subtarea:** [[PED-271]] APP - Review - Mantener consistencia entre modal de Nuevo Client y Editar Client
- **Subtarea:** [[PED-325]] API - Review - Listar tracking Numbers
- **Subtarea:** [[PED-441]] API - Feat - Eliminar envio de una orden
- **Subtarea:** [[PED-443]] APP - Feat - Eliminar envio de una orden
- **Subtarea:** [[PED-472]] API - Refactor - Al agregar un envio a sucursal 10, este debe entrar en pedclil con niva = 0
- **Subtarea:** [[PED-512]] API - Refactor - Tener en cuenta el costo del envio, para el momento en el que liquidemos
- **Subtarea:** [[PED-514]] APP - Refactor - Al agregar un envio se debe enviar costo por body
- **Subtarea:** [[PED-521]] APP - Review - Al hacer cambios en una direccion , parece no recotizar a menos que la selecciones
- **Subtarea:** [[PED-541]] APP - Feat - Maquetar cotizacion de "Destino final para el transporte"
- **Subtarea:** [[PED-543]] API - Feat - Agregar "Destinlo final para el transporte"
- **Subtarea:** [[PED-544]] API - Refactor - Cuando eliminamos un envio, debemos eliminar tambien el "destino final" que lo acompaña
- **Subtarea:** [[PED-566]] API - Feat - Bonificar envio
- **Subtarea:** [[PED-571]] APP - Feat - Bonificar Envio
- **Subtarea:** [[PED-663]] APP - Feat - Se pude agregar en este modal quien es el currier?
- **Subtarea:** [[PED-807]] API - Refactor - Agregar adicional de envió (sobre costos) para moto / camioneta
- **Subtarea:** [[PED-808]] APP - Refactor - Agregar adicional de envió (sobre costos) para moto/camioneta
- **Subtarea:** [[PED-811]] API - Refactor - Mejoras en recurso carrier obteniendo mas informacion del transportista asignado 
- **Subtarea:** [[PED-817]] APP - Refactor - Mostrar estimados de llegada en el cotizador de envio
- **Subtarea:** [[PED-876]] API - Refactor - Al hacer una orden de SUC3 esta debe solo mover el stock virtualmente como en los otros casos hasta el momento de generar el pedido
- **Subtarea:** [[PED-946]] APP - Refactor - Transportar y procesar "promesa de envio"
- **Subtarea:** [[PED-947]] API - Refactor - Transportar y procesar "promesa de envio"
- **Subtarea:** [[PED-1305]] API - Feat - Agregar informacion de confección de paquetes como lo hicimos ne expedicion, para que los vendedores esten informados y puedan dar pre aviso de problemas graves

## Descripcion

Crearemos una serie de recursos que sean capaces de (según su contenido) cotizar una orden para distintos currier, ademas de poder editarla y seleccionar distintas direcciones o bien agregar una nueva en el mismo contexto.
