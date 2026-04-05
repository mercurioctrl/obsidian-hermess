---
jira_key: "BLUWEB-55"
summary: "APP - O. Mejora - Detalles en la firmas y compatibilidades con distintos clientes"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-06-12 14:12"
updated: "2025-11-14 08:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-55"
---

# BLUWEB-55: APP - O. Mejora - Detalles en la firmas y compatibilidades con distintos clientes

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-12 14:12 |
| Actualizado | 2025-11-14 08:23 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-55](https://bluinc.atlassian.net/browse/BLUWEB-55) |

## Descripción

1- Algunos clientes toman los enlaces, y los convierten en hipervinculo con underline, si o si. La recomendacion es convertir en imagen ese fragmento.

[attachment]
2- Si ampliamos la imagen vamos a ver en la zona de redes sociales, que los espacios entre elementos son interpretados como espacio dentro del hipervinculo generando un defecto de subrayado sobre el espacio vacio.

Se sugiere comprimir parte de la cadena de este modo

```
<table cellpadding="0" cellspacing="0" border="0" width="530" style="color: #FFFFFF;background-color: #000000; font-family: Arial, sans-serif;"><!-- Fila con el icono de la esquina superior derecha --><tr><td colspan="4" align="right" style="padding: 15px 15px 0;"><img src="https://signature.blu.inc/detalle.png" width="20" height="20" alt="Grid" style="display: block;"></td></tr><tr><!-- Logo Blu --><td width="120" style="padding: 0 0 0 10px;"><img src="https://signature.blu.inc/logo.png" width="100" alt="Blu." style="display: block;"></td><!-- Info de contacto --><td width="205" style=" color: #FFFFFF; font-size: 14px;"><strong style="font-size: 16px;">Belén Ontivero</strong><br> Diseñadora Gráfica<br><a href="https://vcard-link.com" style="color: #FFFFFF; background-color: #ffffff; color: #000000; font-size: 12px; padding: 2px 6px; text-decoration: none; display: inline-block; margin-top: 5px;">vCard</a></td><!-- Iconos y sitio con línea divisoria incluida --><td width="205" style="padding: 0 10px; color: #FFFFFF; font-size: 14px;"><table cellpadding="0" cellspacing="0" border="0" width="100%" style="color: #FFFFFF;"><tr><!-- Línea divisoria vertical --><td width="1" bgcolor="#FFFFFF" style="padding: 0;"></td><!-- Contenido: sitio e iconos --><td style="padding-left: 10px;"><table cellpadding="0" cellspacing="0" border="0" width="100%"><tr><td colspan="5" style="padding: 5px 0px"><a href="https://blu.inc/" target="_blank" style="text-decoration: none; color: #FFFFFF; font-size: 14px;"><img src="https://signature.blu.inc/web.png" width="15" height="15" alt="Sitio" style="vertical-align: middle;margin-right: 4px;"><span style="vertical-align: middle;">Blu.inc</span></a></td></tr><tr><td colspan="5"><a href="https://www.facebook.com/profile.php?id=61574894222654" target="_blank" style="text-decoration: none;"><img src="https://signature.blu.inc/facebook.png" width="16" height="16" alt="Facebook" style="display: inline-block; margin-right: 5px;"></a><a href="https://x.com/Blustudioinc" target="_blank" style="text-decoration: none;"><img src="https://signature.blu.inc/x.png" width="16" height="16" alt="X/Twitter" style="display: inline-block; margin-right: 5px;"></a><a href="https://www.instagram.com/blustudioinc/" target="_blank" style="text-decoration: none;"><img src="https://signature.blu.inc/instagram.png" width="16" height="16" alt="Instagram" style="display: inline-block; margin-right: 5px;"></a><a href="https://www.youtube.com/@blustudioinc" target="_blank" style="text-decoration: none;"><img src="https://signature.blu.inc/youtube.png" width="16" height="16" alt="YouTube" style="display: inline-block; margin-right: 5px;"></a><a href="https://www.threads.net/@blustudioinc" target="_blank" style="text-decoration: none;"><img src="https://signature.blu.inc/threads.png" width="16" height="16" alt="threads" style="display: inline-block; margin-right: 5px;"></a><a href=" https://www.linkedin.com/company/blustudioinc/" target="_blank" style="text-decoration: none;"><img src="https://signature.blu.inc/linkedin.png" width="16" height="16" alt="LinkedIn" style="display: inline-block;"></a></td></tr></table></td></tr></table></td></tr><tr><td colspan="4" align="right" style="padding: 17.5px "></td></tr></table>
```

[attachment]
