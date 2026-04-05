---
jira_key: "NBWEB-769"
aliases: ["NBWEB-769"]
summary: "EXTESION - Refactor - Agregar medidas a la importación que se hace con woocomerce "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-16 08:00"
updated: "2024-07-23 16:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-769"
---

# NBWEB-769: EXTESION - Refactor - Agregar medidas a la importación que se hace con woocomerce 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-16 08:00 |
| Actualizado | 2024-07-23 16:42 |
| Etiquetas | ninguna |
| Jira | [NBWEB-769](https://bluinc.atlassian.net/browse/NBWEB-769) |

## Relaciones

- **Padre:** [[NBWEB-682 - Productos|NBWEB-682]] Productos
- **is blocked by:** [[NBWEB-768 - API - Refactor - Agregar medidas al catalogo|NBWEB-768]] API - Refactor - Agregar medidas al catalogo

## Descripcion

Modificaremos [link](https://github.com/New-Bytes/woocommerce-newbytes)  para agregarle las medidas según vimos tanto para la carga como para la actualización.

Ver como se hace en el archivo adjunto que obtuvimos de la competencia 

```
...

			$product->set_weight($row['peso']);
				if(!empty($row['dimensiones'])) {
					$product->set_width($row['dimensiones']['ancho']);
					$product->set_length($row['dimensiones']['largo']);
					$product->set_height($row['dimensiones']['alto']);
				}
				$product->save();

				if (is_plugin_active('featured-image-from-url/featured-image-from-url.php') || is_plugin_active('fifu-premium/fifu-premium.php')) {
					fifu_dev_set_image($id, $row['imagenes'][0]);
				}
				
...
```
