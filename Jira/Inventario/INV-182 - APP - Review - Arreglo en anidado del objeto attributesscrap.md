---
jira_key: "INV-182"
aliases: ["INV-182"]
summary: "APP - Review - Arreglo en \"anidado\" del objeto attributes/scrap"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-03-27 09:55"
updated: "2025-03-29 16:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-182"
---

# INV-182: APP - Review - Arreglo en "anidado" del objeto attributes/scrap

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-27 09:55 |
| Actualizado | 2025-03-29 16:52 |
| Etiquetas | ninguna |
| Jira | [INV-182](https://bluinc.atlassian.net/browse/INV-182) |

## Relaciones

- **Padre:** [[INV-177]] Atributos

## Descripcion

Actualmente, al consumir el endpoint 

```
GET {API_URL}/attributes/scrap
```

 la respuesta contiene los atributos reales (como por ejemplo `Socket`, `Ranuras RAM`, `Tipo de RAM`, etc.) dentro de la clave `"data"`, así:

```
{
  "success": true,
  "data": {
    "Socket": "Z890M AORUS ELITE WIFI7",
    "Ranuras RAM": 4,
    "Tipo de RAM": "DDR5",
    "Factor de forma": "EEB/E-ATX/ATX/microATX/mini-ITX"
  }
}

```

Sin embargo, en el frontend, al cargar esta información en el formulario de atributos (ver imagen adjunta), se interpreta `data` como si fuera un atributo más, en lugar de desestructurar correctamente los atributos internos.

[adjunto]
**Tareas:**

-  Ajustar el parsing de la respuesta del endpoint `/attributes/scrap` en el frontend.


-  Validar que se desestructure correctamente el contenido del campo `data` y que los atributos internos (Socket, RAM, etc.) se asignen como campos individuales del formulario.


-  Verificar que el formulario se complete correctamente y sin errores con atributos oficiales.


-  Pruebas con otros productos para asegurar robustez del fix.



** **
