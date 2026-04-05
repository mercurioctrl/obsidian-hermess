---
jira_key: "NBWEB-963"
aliases: ["NBWEB-963"]
summary: "APP - Feat - Agregar un conmutador para mostrar u ocultar la cotización del dólar en el sitio web"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-04-15 08:42"
updated: "2025-04-16 00:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-963"
---

# NBWEB-963: APP - Feat - Agregar un conmutador para mostrar u ocultar la cotización del dólar en el sitio web

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-15 08:42 |
| Actualizado | 2025-04-16 00:53 |
| Etiquetas | ninguna |
| Jira | [NBWEB-963](https://bluinc.atlassian.net/browse/NBWEB-963) |

## Relaciones

- **Padre:** [[NBWEB-524]] CMS - Parametros varios
- **action item from:** [[NBWEB-962]] API - Feat - Habilitar o deshabilitar la cotización del dólar mediante el parámetro quoteSiteShow para el sitio web

## Descripcion

Quiero que exista un conmutador (switch) en la interfaz que permita activar o desactivar la visualización de la cotización del dólar, para tener un mayor control para cuando es un buen momento de mostrarla o no en el sitio.

- **Requerimientos/Objetivos:**

- Mostrar un conmutador en la pantalla de administración (o en la sección adecuada del sitio) para controlar el parámetro `quoteSiteShow`.


- Al cambiar el estado del conmutador, se invoque el servicio para actualizar el valor de `quoteSiteShow`

```
POST {API_URL}/v1/cms/defaultParameters
```


- Leer 

```
GET {API_URL}/v1/cms/defaultParameters
```

para leer el estado actual de quoteSiteShow al cargar la pantalla, reflejando si la cotización del dólar está activa o no.


- Si `quoteSiteShow` es `true`, se muestra la cotización del dólar; si es `false`, se oculta.





- **Criterios de aceptación:**

- Existe un conmutador visible que represente el estado de `quoteSiteShow`.


- El conmutador se inicializa de acuerdo con el valor obtenido de 

```
GET {API_URL}/v1/cms/defaultParameters
```


- Al interactuar con el conmutador, el Front-End realiza la llamada `POST` con el body `{"quoteSiteShow": true/false}` y actualiza la visualización de la cotización en la misma vista.


- Los cambios en el valor de `quoteSiteShow` se ven reflejados en la sección de “Cotizaciones” de forma inmediata (o según el flujo de refresco definido).





[adjunto]
