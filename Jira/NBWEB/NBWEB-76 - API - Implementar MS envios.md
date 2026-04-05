---
jira_key: "NBWEB-76"
aliases: ["NBWEB-76"]
summary: "API - Implementar MS envios"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-04-04 06:53"
updated: "2024-01-29 17:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-76"
---

# NBWEB-76: API - Implementar MS envios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-04 06:53 |
| Actualizado | 2024-01-29 17:00 |
| Etiquetas | ninguna |
| Jira | [NBWEB-76](https://bluinc.atlassian.net/browse/NBWEB-76) |

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web
- **Subtarea:** [[NBWEB-79]] Cotizador de ordenes de compra
- **Subtarea:** [[NBWEB-85]] Inicializar ms local de envios
- **Subtarea:** [[NBWEB-80]] Cotizador de carritos de compra
- **Subtarea:** [[NBWEB-81]] Crear Etiqueta / Orden de retiro
- **Subtarea:** [[NBWEB-83]] Obtener tracking
- **Subtarea:** [[NBWEB-82]] Obtener etiqueta OCA / Andreani
- **Subtarea:** [[NBWEB-86]] Ms - envios Integracion completa de Motos y Mini Flete
- **Subtarea:** [[NBWEB-118]] Agregar MiniFlete
- **Subtarea:** [[NBWEB-144]] MS - Envios - Dotar al servicio de su tabla y administrador correspondiente
- **Subtarea:** [[NBWEB-155]] MS Envios - Independizar la tabla envios y agregar el doble instanciado de db
- **Subtarea:** [[NBWEB-164]] MS - Envios - Cotizar por peso y medidas
- **Subtarea:** [[NBWEB-165]] MS Envios - Agregar sistema de login y token
- **Subtarea:** [[NBWEB-173]] MS - Envios - Feature para aplazar fecha de entrega
- **Subtarea:** [[NBWEB-176]] MS - Envios - Sincronizar Medios de envio
- **Subtarea:** [[NBWEB-177]] MS - Envios - Crear tabla transportistas
- **Subtarea:** [[NBWEB-178]] MS - Envios - Crear un transportista
- **Subtarea:** [[NBWEB-179]] MS - Envios - Crear tabla envios
- **Subtarea:** [[NBWEB-180]] MS - Envios - Crear Envio
- **Subtarea:** [[NBWEB-181]] MS - Envios -  Confirmar clave privada
- **Subtarea:** [[NBWEB-182]] MS - Envios - Leer datos de envio
- **Subtarea:** [[NBWEB-183]] MS - Envios - Confirmar pago a transportista
- **Subtarea:** [[NBWEB-191]] MS - Envios - Marcar despacho
- **Subtarea:** [[NBWEB-218]] MS - Entregar palabra clava de manera aleatoria
- **Subtarea:** [[NBWEB-231]] MS - Research integracion de Urbano
- **Subtarea:** [[NBWEB-239]] MS - Feat - Urbano - Cotizador de carritos de compra
- **Subtarea:** [[NBWEB-240]] MS - Feat - Urbano - Cotizar ordenes de compra
- **Subtarea:** [[NBWEB-241]] MS - Feat - Urbano - Crear Etiqueta / Orden de retiro
- **Subtarea:** [[NBWEB-246]]  Feat - Urbano - Cotizar bulk
- **Subtarea:** [[NBWEB-248]] MS - Feat - Urbano - Trackear pedido
- **Subtarea:** [[NBWEB-250]] MS - Research - Obtener la distancia entre dos puntos
- **Subtarea:** [[NBWEB-256]] MS - Feat - Integrar transporte con precio por KM
- **Subtarea:** [[NBWEB-261]] API - Feat -  Agregar un porcentaje mínimo de exclusión en la cotización 
- **Subtarea:** [[NBWEB-262]] MS - Envios - Mover credenciales para google maps al archivo de variables de entorno
- **Subtarea:** [[NBWEB-263]] MS - Envios - Incorporar string opcional de direccion
- **Subtarea:** [[NBWEB-272]] API - Feat Agregar String de direccion al final del Recurso calcularEnvioPara
- **Subtarea:** [[NBWEB-357]] API - Feat - Agregar un recurso para consumir el ms-envios para generar un nuevo paquete
- **Subtarea:** [[NBWEB-416]] API - Oportunidad de mejora - Agregar comentario con la direccion e informacion complemetaria del destino
- **Subtarea:** [[NBWEB-488]] MS - Envios - Refactor Cotizador del carrito de compra

## Descripcion

Dada la necesidad de dotar al sitio web de un servicio de envíos que se encuentre dentro de la lógica de negocio ya utilizada para libre opción, se debe integrar el sitio al mismo micro servicio para este fin: [link](https://github.com/LibreOpcion/microservicio-envios-v1)
