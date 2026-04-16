# Memoria

Consolidación de la memoria de Claude para este proyecto.

## Feedback

### Commits sin coautoría
Nunca agregar `Co-Authored-By` en commits. Los commits son del usuario.

### Emails en tema oscuro
Los correos del sistema siempre usan tema oscuro (fondo `#0d0d0d`/`#111`, textos claros). No usar fondos blancos.

### Textos literales
Cuando el usuario da un texto específico (botones, labels, títulos), usar exactamente esas palabras. No parafrasear.

### Iterar rápido
El usuario trabaja en ráfaga. Respuestas mínimas: hacer el cambio y decir "Listo." No resumir salvo que haya impacto de deploy.

## Proyecto

### Volúmenes Docker
Nginx solo monta `public/` y `uploads/`. Cualquier ruta nueva necesita volumen explícito + location en Nginx. Bug real pasado con videos.

### Precauciones de deploy
Avisar proactivamente si hay cambios de DB, env vars nuevas, o riesgo de romper producción.

### Promoción cerrada
Finalizó 2026-04-15. `PROMO_CLOSED=true` activo. Para reabrir: cambiar env var y recrear container PHP.

## Ver también

- [[Asus/saMiniSiteCodes/saMiniSiteCodes|saMiniSiteCodes]]
- [[Asus/saMiniSiteCodes/contexto|Contexto]]