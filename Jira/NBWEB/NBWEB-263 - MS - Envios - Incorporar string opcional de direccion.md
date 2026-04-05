---
jira_key: "NBWEB-263"
aliases: ["NBWEB-263"]
summary: "MS - Envios - Incorporar string opcional de direccion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-06-16 12:53"
updated: "2022-06-26 20:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-263"
---

# NBWEB-263: MS - Envios - Incorporar string opcional de direccion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-16 12:53 |
| Actualizado | 2022-06-26 20:18 |
| Etiquetas | ninguna |
| Jira | [NBWEB-263](https://bluinc.atlassian.net/browse/NBWEB-263) |

## Relaciones

- **Padre:** [[NBWEB-76 - API - Implementar MS envios|NBWEB-76]] API - Implementar MS envios

## Descripcion

Incluir un nuevo parámetro de carácter OPCIONAL que sera un string para la cotización de nuestro propio transporte.

```
{{API_URL}}/cart/nb/8004029/cp/1439/{string_con_direccion_completa_opcional}
```

```
{{API_URL}}/pedido/414798/cp/1426/cphost/1229/{string_con_direccion_completa_opcional}
```

```
{{API_URL}}/bulk/size/15x15x15/weight/3.68/cp/1400/{string_con_direccion_completa_opcional}
```

El mismo llega en formato `Dirección Numero, Cp destino, Provincia`, pero puede no estar, y en ese caso no sera considerado.
