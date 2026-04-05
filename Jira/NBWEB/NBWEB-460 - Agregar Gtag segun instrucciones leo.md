---
jira_key: "NBWEB-460"
aliases: ["NBWEB-460"]
summary: "Agregar Gtag segun instrucciones leo "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-08-12 16:04"
updated: "2022-08-23 14:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-460"
---

# NBWEB-460: Agregar Gtag segun instrucciones leo 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-12 16:04 |
| Actualizado | 2022-08-23 14:34 |
| Etiquetas | ninguna |
| Jira | [NBWEB-460](https://bluinc.atlassian.net/browse/NBWEB-460) |

## Relaciones

*Sin relaciones*

## Descripcion

```
Colocar ambos códigos en todas las páginas del sitio web

Colocar en el HEAD lo más arriba posible

<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-N4QR6D2');</script>
<!-- End Google Tag Manager -->

Colocar como primer elemnto del BODY

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N4QR6D2"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
```
