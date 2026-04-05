---
jira_key: "PEGA-203"
summary: "APP - Feta - Agregar GTM"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-08-22 09:06"
updated: "2025-08-26 11:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-203"
---

# PEGA-203: APP - Feta - Agregar GTM

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-22 09:06 |
| Actualizado | 2025-08-26 11:13 |
| Etiquetas | ninguna |
| Jira | [PEGA-203](https://bluinc.atlassian.net/browse/PEGA-203) |

## Descripción

Instalar Google Tag Manager

Copie el código que aparece a continuación y péguelo en todas las páginas de su sitio web.

- Pegue este código lo más arriba posible en la sección **<head>** de la página:



```
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-P8BPB2L2');</script>
<!-- End Google Tag Manager -->
```

- Pegue este código justo después de la etiqueta de apertura **<body>**:



```
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-P8BPB2L2"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
```
