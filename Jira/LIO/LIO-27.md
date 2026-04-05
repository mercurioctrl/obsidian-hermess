---
jira_key: "LIO-27"
summary: "API - Feat - Agregar en la ficha de los productos la descripción generada por IA de los mismos como hicimos en \"capa 1\" "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-03 17:51"
updated: "2024-06-11 16:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-27"
---

# LIO-27: API - Feat - Agregar en la ficha de los productos la descripción generada por IA de los mismos como hicimos en "capa 1" 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-03 17:51 |
| Actualizado | 2024-06-11 16:19 |
| Etiquetas | ninguna |
| Jira | [LIO-27](https://bluinc.atlassian.net/browse/LIO-27) |

## Descripción

Se debe agregar un recurso en la APIv4 para obtener la descripción generada automáticamente en caso de que este disponible.

```
GET {{API_URL}}/v4/item/579703/iaDescription
```

```
[
  {
    "id": 142,
    "description": "El monitor Philips LED 24 241V8L 241V8L/77 es un monitor de 24 pulgadas con tecnología LED que ofrece una alta calidad de imagen y un diseño elegante. Tiene una resolución Full HD de 1920 x 1080 píxeles y un tiempo de respuesta de 4 ms, lo que lo hace ideal para ver películas, jugar videojuegos y trabajar con gráficos de alta definición.\n\nEste monitor cuenta con tecnología SmartContrast que ajusta automáticamente los colores y la intensidad de la retroiluminación para obtener imágenes más nítidas y colores más vibrantes. Además, tiene tecnología Flicker-Free que ayuda a reducir la fatiga visual al minimizar el parpadeo de la pantalla.\n\nEn cuanto a la conectividad, el monitor Philips LED 24 241V8L 241V8L/77 cuenta con puertos HDMI, VGA y DisplayPort, lo que permite una fácil conexión con dispositivos externos como computadoras, consolas de videojuegos y reproductores de medios.\n\nEn resumen, el monitor Philips LED 24 241V8L 241V8L/77 es una excelente opción para aquellos que buscan un monitor de alta calidad con una excelente calidad de imagen y diversas funciones útiles para el entretenimiento y el trabajo.",
    "itemId": 117789,
    "accepted": 1,
    "refused": 0
  }
]
```

Query orientativa:

```
SELECT TOP (1000) [id]
      ,[description]
      ,[itemId]
      ,[accepted]
      ,[refused]
  FROM [PRODUCTOS].[dbo].[iaDescriptions]
  WHERE itemId =  {id del producto capa 1}
```
