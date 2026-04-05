---
jira_key: "NBWEB-209"
aliases: ["NBWEB-209"]
summary: "MS - Envios - Cotizar carrito api nb, no trae moto"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-26 18:46"
updated: "2022-06-27 09:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-209"
---

# NBWEB-209: MS - Envios - Cotizar carrito api nb, no trae moto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-26 18:46 |
| Actualizado | 2022-06-27 09:18 |
| Etiquetas | ninguna |
| Jira | [NBWEB-209](https://bluinc.atlassian.net/browse/NBWEB-209) |

## Relaciones

- **Padre:** [[NBWEB-50 - Sitio Web|NBWEB-50]] Sitio Web

## Descripcion

Al ejecutar el recurso

```
GET {{API_URL}}/cart/nb/8004029/cp/1407
```

debería traer moto tambien, o en su defecto, mini flete.

[https://beta.ms-envio.lio.red/v1/cart/nb/8068594/cp/1407](https://beta.ms-envio.lio.red/v1/cart/nb/8068594/cp/1407)

El origen del problema parece ser el ms de envios.

Por ahi no es un error, sino una flag o algo asi, pero mejor prevenir que curar
