---
jira_key: "BLUWEB-50"
summary: "APP - Refactor - Crearemos una rama del sitio para backgrounds de la sección inicial"
status: "LISTO"
type: "Subtarea"
priority: "Highest"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-06-05 08:39"
updated: "2025-08-25 09:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-50"
---

# BLUWEB-50: APP - Refactor - Crearemos una rama del sitio para backgrounds de la sección inicial

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-05 08:39 |
| Actualizado | 2025-08-25 09:40 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-50](https://bluinc.atlassian.net/browse/BLUWEB-50) |

## Descripción

Basándonos en la idea de los vídeos, pondremos un directorio o carpeta dentro del proyecto, de donde se puedan tomar directamente las imágenes.

- Deben leerse directo desde un directorio cualquier imagen jpeg, jpg o png


- Se debe agregar un controlador o accionable para cambiar de imagen en un un lugar no invasivo, o bien se debe poder pasar con la flecha del teclado directamente para que no moleste.


- Se debe agregar una imagen similar a la del sitio [link](https://founderz.com/es/)  donde la imagen inicia un pequeño recorrido y cuando llega al final de la imagen, rebota e inicia el recorrido en el sentido contrario y el **fondo se mueve lentamente recorriendo la imagen completa**, se puede usar solo CSS con una animación de `background-position` con algo asi:



```
.hero-bg {
  width: 100%;
  height: 500px; /* o lo que necesites */
  background-image: url('tu-imagen.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  animation: slowPan 30s ease-in-out infinite alternate;
  /* tip: podés usar `background-size: 120%` si querés que recorra más contenido */
}

@keyframes slowPan {
  0% {
    background-position: 50% 0%;
  }
  100% {
    background-position: 50% 100%;
  }
}

```

- `alternate`: hace que la animación vaya y vuelva.


- `ease-in-out`: hace que el movimiento se sienta más natural.


- `30s`: podés cambiarlo según cuán lento lo quieras.



[attachment]
[attachment]
[attachment]
