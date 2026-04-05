---
jira_key: "PEGA-38"
aliases: ["PEGA-38"]
summary: "API - Feat - Formulario de rastreo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-15 17:35"
updated: "2025-01-03 00:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-38"
---

# PEGA-38: API - Feat - Formulario de rastreo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-15 17:35 |
| Actualizado | 2025-01-03 00:35 |
| Etiquetas | ninguna |
| Jira | [PEGA-38](https://bluinc.atlassian.net/browse/PEGA-38) |

## Relaciones

- **Padre:** [[PEGA-37]] Feat - Formulario de rastreo
- **blocks:** [[PEGA-39]] APP - Feat - Formulario de rastreo
- **is blocked by:** [[PEGA-70]] API - Formulario de rastreo - Correo no enviado
- **relates to:** [[PEGA-130]] API - Formulario de rastreo - Sin respuesta al hacer la petición 
- **relates to:** [[PEGA-162]] API - Formulario de rastreo - Valores enviados y almacenados no coincidentes

## Descripcion

Se debe crear una tabla para almacenar la información recolectada mediante el formulario 

```
POST {API_URL}/v1/addMyInventory
```

 La información que se recolectará incluirá el correo de contacto, nombre de la persona de contacto, URL del sitio, API del sitio (opcional), URL de la documentación de la API (opcional), nombre de la tienda y un comentario adicional.

Al guardar los datos, se debe enviar un correo electrónico utilizando PHPMailer al "correo de contacto" con el siguiente mensaje: "Gracias por completar el formulario. Analizaremos su solicitud de alta en nuestro catálogo para poder agregarlo lo antes posible. Es posible que alguien de nuestro equipo se ponga en contacto con usted si se necesitan más detalles. ¡Saludos!"

Los datos de correo deben figurar en el archivo de variables de entorno:

Host, puerto, correo de salida y demás (pedir esta data por privado)
