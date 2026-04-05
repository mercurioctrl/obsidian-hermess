---
jira_key: "LIO-58"
aliases: ["LIO-58"]
summary: "APP - Refactor - Mover los recursos estáticos que se usan en la home para una carga mas rapida y evitar un servidor extra (static2)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-06-26 14:02"
updated: "2024-07-03 00:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-58"
---

# LIO-58: APP - Refactor - Mover los recursos estáticos que se usan en la home para una carga mas rapida y evitar un servidor extra (static2)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-26 14:02 |
| Actualizado | 2024-07-03 00:55 |
| Etiquetas | ninguna |
| Jira | [LIO-58](https://bluinc.atlassian.net/browse/LIO-58) |

## Relaciones

- **Padre:** [[LIO-6]] Diseño de una interfaz intuitiva y navegacion
- **is blocked by:** [[LIO-43]] API - Refactor - Mover los recursos estáticos que se usan en la home para una carga mas rapida y evitar un servidor extra (static2)

## Descripcion

Moveremos todos los siguientes recursos a la APIv4, según la historia
[link](https://lioteam.atlassian.net/browse/LIO-43) 

```
{{API_URL}}/v4/cabecera-categorias
```

```
{{API_URL}}/v4/home-productos-nuevos
```

```
{{API_URL}}/v4/home-productos-instant-flash
```

```
{{API_URL}}/v4/home-productos-mas-vendidos
```

```
{{API_URL}}/v4/home-marcas
```

```
{{API_URL}}/v4/home-categories
```

Con respecto a las imagenes, iconos y demas me gustaria que charlemos que posibilidades hay de usar el repo propio del proyecyo o bien static normal, avisame cuando lo veas y charlamos
