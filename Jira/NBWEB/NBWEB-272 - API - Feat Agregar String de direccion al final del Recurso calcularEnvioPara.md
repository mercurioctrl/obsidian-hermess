---
jira_key: "NBWEB-272"
aliases: ["NBWEB-272"]
summary: "API - Feat Agregar String de direccion al final del Recurso calcularEnvioPara"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2022-06-23 13:13"
updated: "2024-05-03 13:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-272"
---

# NBWEB-272: API - Feat Agregar String de direccion al final del Recurso calcularEnvioPara

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2022-06-23 13:13 |
| Actualizado | 2024-05-03 13:14 |
| Etiquetas | ninguna |
| Jira | [NBWEB-272](https://bluinc.atlassian.net/browse/NBWEB-272) |

## Relaciones

- **Padre:** [[NBWEB-76 - API - Implementar MS envios|NBWEB-76]] API - Implementar MS envios
- **relates to:** [[NBWEB-729 - API - Recurso calcularEnvioPara - Validación al no enviar la dirección completa|NBWEB-729]] API - Recurso calcularEnvioPara - Validación al no enviar la dirección completa

## Descripcion

Para el metodo de la API

```
GET {{API_URL}}/v1/carrito/calcularEnvioPara/{cp}/
GET {{API_URL}}/v1/carrito/calcularEnvioPara/{cp}/{string_con_direccion_completa_opcional}

```

A) Debe agregarse ademas, un string opcional al final del recurso, quie contenga la direccion completa con el siguiente formato:

`Dirección Numero, Cp destino, Provincia`

Esta sera la que utilizaremos para rastrear la distancia en [link](https://lioteam.atlassian.net/browse/NBWEB-250) . En caso de presentarse dudas respecto a donde obtener la informacion, ya se hicieron metodos que utilizan los mismos datos consultar con 

B) Ademas, deben agregarse a las variables de entorno (.env) el parámetro para la url puntera del servicio de envíos (en este caso “beta.ms-envio.lio.red).

[adjunto]
