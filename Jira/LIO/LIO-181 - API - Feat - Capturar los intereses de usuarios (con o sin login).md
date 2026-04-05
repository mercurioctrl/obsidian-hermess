---
jira_key: "LIO-181"
aliases: ["LIO-181"]
summary: "API - Feat - Capturar los intereses de usuarios (con o sin login)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Catriel Mercurio"
created: "2025-01-27 09:57"
updated: "2025-09-04 10:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-181"
---

# LIO-181: API - Feat - Capturar los intereses de usuarios (con o sin login)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-27 09:57 |
| Actualizado | 2025-09-04 10:16 |
| Etiquetas | ninguna |
| Jira | [LIO-181](https://bluinc.atlassian.net/browse/LIO-181) |

## Relaciones

- **Padre:** [[LIO-180 - Intereses de usuario|LIO-180]] Intereses de usuario
- **is caused by:** [[LIO-190 - APP - Refactor - agregar el token v4 para los dos recursos de LIO-181|LIO-190]] APP - Refactor - agregar el token v4 para los dos recursos de LIO-181

## Descripcion

Haremos algunas refactorizaciones que nos permitan almacenar de manera mas clara los intereses de los usuarios en diferentes productos, **estén o no estén logueados.**

Lo que pretendemos es en principio crear una tabla para almacenar los datos. Luego refactorizar distintos recurso del sitio para poder guardar algunos datos que nos permitan configurar los intereses del visitante/usuario respecto al sitio.

## 1 - Crearemos una tabla similar

```
CREATE TABLE user_interests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NULL,                    -- ID del usuario logueado, NULL si no está logueado
    session_id VARCHAR(64) NULL,         -- ID único de sesión para usuarios no logueados
    product_id INT NULL,                 -- ID del producto (NULL si es solo una búsqueda)
    search_query VARCHAR(255) NULL,      -- Términos de búsqueda ingresados por el usuario
    category_id INT NULL,                -- ID de la categoría explorada (si aplica)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Fecha y hora del registro
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

- Esta tabla tiene los parámetros mas o menos necesarios y es flexible respecto a los criterios. Por ejemplo podemos guardar o no `user_id` según el usuario este o no logueado, en cambio `session_id` se guarda siempre. De esta forma siempre podemos buscar coincidencias tanto si esta uno como el otro.


- Algo similar pasa cuando no podemos obtener el `product_id` concreto mediante su impresión, pero si podemos obtener los términos de búsqueda `search_query`



## 2 - Refactorizando los recursos para almacenar los datos

```
GET {API_URL}/v4/search?search={terminosDeBusqueda}
```

Utilizaremos cada golpe al recurso, para generar la “huella” en nuestra tabla

```
GET {API_URL}/v4/item/{itemId}
```

Utilizaremos cada golpe al recurso, para generar la “huella” en nuestra tabla
