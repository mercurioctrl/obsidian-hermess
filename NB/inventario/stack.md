# Stack — inventario

## Frontend (inventario-web-app)

| Tecnología | Versión | Uso |
|-----------|---------|-----|
| Nuxt.js | ^2.15.8 | Framework SSR/SPA |
| Vue | ^2.6.14 | UI framework |
| Ant Design Vue | ^1.7.8 | Componentes UI |
| Vuex | (incluido en Nuxt 2) | Estado global |
| Vue Router | (incluido en Nuxt 2) | Routing |
| @nuxtjs/auth-next | — | Autenticación JWT |
| Axios | (via Nuxt) | HTTP client |
| Less | — | Estilos (preprocesador CSS) |

**Entorno de ejecución:** Node.js + pm2 en producción

## Backend (ms-metadata)

| Tecnología | Uso |
|-----------|-----|
| Python 3 | Lenguaje |
| FastAPI | Framework web |
| Pydantic | Validación y modelos |
| pyodbc | Conexión a SQL Server |
| ODBC Driver 18 for SQL Server | Driver DB (solo v18 instalada) |
| Scrapy | Web scraping |
| BeautifulSoup4 + lxml | Parsing HTML |
| OpenAI API | IA para descripciones |
| pandas | Procesamiento de datos (Excel import) |
| python-multipart | Uploads de archivos |
| uvicorn | ASGI server |
| pytz | Manejo de zonas horarias |

## Base de datos

- **Motor**: SQL Server
- **Host**: `190.210.23.97,4444`
- **Base**: `NB_WEB`
- **Acceso**: Raw SQL via pyodbc (sin ORM)

## Ver también

- [[inventario]] · [[arquitectura]] · [[contexto]]
