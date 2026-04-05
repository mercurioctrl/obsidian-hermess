---
jira_key: "BLUWEB-3"
aliases: ["BLUWEB-3"]
summary: "APP - Feat - Maquetar firmas para que se visualicen de forma correcta en todos los clientes"
status: "LISTO"
type: "Subtarea"
priority: "Highest"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-04-28 14:44"
updated: "2025-05-07 15:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-3"
---

# BLUWEB-3: APP - Feat - Maquetar firmas para que se visualicen de forma correcta en todos los clientes

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-28 14:44 |
| Actualizado | 2025-05-07 15:38 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-3](https://bluinc.atlassian.net/browse/BLUWEB-3) |

## Relaciones

- **Padre:** [[BLUWEB-2]] Firmas

## Descripcion

Se debe crear una maqueta estándar de nuestros correos se implemente en código HTML para que las firmas se vea correctamente en clientes web (Gmail, Outlook) y de escritorio (Thunderbird, Outlook).

Las mismas se maquetaran como un prototipo en código y luego sera integrada con un generador de firmas que toma los datos por cada uno desde la base de datos como ya hemos realizado para otras ocasiones.

## Criterios de Aceptación

- **Estructura HTML basada en tablas**

- Toda la plantilla debe construirse con tablas y CSS inline para garantizar máxima compatibilidad.




- **Fidelidad al diseño**

- La maquetación respeta tamaños, colores y espaciados definidos en la maqueta estándar adjunta en las imagenes para intentar la fidelidad maxima.




- **Compatibilidad cross-client**

- Render correcto y sin desplazamientos inesperados en:

- Gmail web (desktop y mobile)


- Outlook web (Office 365)


- Outlook Desktop (Windows)


- Thunderbird


- WerbMail Box.lio.red






- **Imágenes y accesibilidad**

- Todas las imágenes incluyen atributos `width`, `height` y `alt`.


- No se usan fondos con CSS `background-image` (usar `<img>`).




- **Uso de fuentes seguras**

- Sólo fuentes web-seguras (Arial, Helvetica, sans-serif) y declaradas en `style` inline.




- **Estilos permitidos**

- CSS inline soportado por la mayoría de clientes de correo (no floats complejos, no `position:absolute`, sin `@media` queries críticos).
