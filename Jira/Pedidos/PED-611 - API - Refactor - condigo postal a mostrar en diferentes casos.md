---
jira_key: "PED-611"
aliases: ["PED-611"]
summary: "API - Refactor - condigo postal a mostrar en diferentes casos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-03-14 12:19"
updated: "2024-03-18 17:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-611"
---

# PED-611: API - Refactor - condigo postal a mostrar en diferentes casos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-03-14 12:19 |
| Actualizado | 2024-03-18 17:18 |
| Etiquetas | ninguna |
| Jira | [PED-611](https://bluinc.atlassian.net/browse/PED-611) |

## Relaciones

- **Padre:** [[PED-65 - Listado de productos|PED-65]] Listado de productos
- **is blocked by:** [[PED-615 - API - Problema al cotizar un envío - Después de eliminar direcciones sus datos|PED-615]] API - Problema al cotizar un envío - Después de eliminar direcciones sus datos siguen apareciendo

## Descripcion

Una orden puede tener 3 posibles casos en cuanto a su Codigo Posta.

1 - CP: asignado debido a una cotizacion de envio - ( es la que tiene mas relevancia en el contexto de  la orden)

2- CP: asignada por defecto. (el cliente tiene una direccion creada y es la predeterminada)

3 - CP: null → este caso se da cuando el cliente fue creado recientemente o todas las direcciones fueron eliminadas.
