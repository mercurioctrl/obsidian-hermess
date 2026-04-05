---
jira_key: "PEGA-192"
aliases: ["PEGA-192"]
summary: "Envío de información de los resellers"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-05-23 13:19"
updated: "2025-07-07 06:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-192"
---

# PEGA-192: Envío de información de los resellers

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-05-23 13:19 |
| Actualizado | 2025-07-07 06:43 |
| Etiquetas | ninguna |
| Jira | [PEGA-192](https://bluinc.atlassian.net/browse/PEGA-192) |

## Relaciones

- **Padre:** [[PEGA-190 - Implementación del sistema de autenticación y panel de gestión para usuarios|PEGA-190]] Implementación del sistema de autenticación y panel de gestión para usuarios tipo reseller
- **Subtarea:** [[PEGA-196 - API - Feat - Implementar envío de datos por parte del reseller|PEGA-196]] API - Feat - Implementar envío de datos por parte del reseller
- **Subtarea:** [[PEGA-197 - API - Feat - Implementar historial de datos enviados|PEGA-197]] API - Feat -  	Implementar historial de datos enviados
- **Subtarea:** [[PEGA-201 - API - Feat - Crear Syncup para importar catalogo de resellers por feet xml|PEGA-201]] API - Feat - Crear Syncup para importar catalogo de resellers por feet xml

## Descripcion

Desarrollar e integrar todos los endpoints relacionados con la gestión del catálogo de productos para usuarios autenticados con rol de *reseller*. Estos endpoints permitirán administrar el catálogo desde archivos .xlsx y mediante una URL de feed XML. Incluye la descarga de una plantilla, la validacin previa y carga de archivos, así como la validación y sincronización de un feed remoto.

### **Endpoints a implementar:**

####  **Información del catálogo**

- `GET /reseller/catalog/url`: Obtener metadatos del feed del catálogo.


- `GET /reseller/catalog/entries`: Obtener las entradas actuales del repositorio del catálogo.



####  **Gestión vía Excel**

- `GET /reseller/catalog/template`: Descargar plantilla de catálogo en Excel.


- `POST /reseller/catalog/preview`: Enviar y previsualizar un catálogo cargado por archivo.


- `POST /reseller/catalog/upload`: Cargar el catálogo desde archivo Excel.



####  **Gestión vía URL (feed XML)**

- `POST /reseller/catalog/url`: Registrar una URL para el catálogo.


- `POST /reseller/catalog/url/validate`: Validar la URL de catálogo proporcionada.


- `POST /reseller/catalog/url/sync`: Sincronizar el catálogo automáticamente desde una URL válida.



### **Requisitos:**

- Todos los endpoints deben estar protegidos con middleware `auth:sanctum`.


- Validaciones exhaustivas en carga de archivos y sincronización.


- Devolución de respuestas claras y estructuradas en JSON.


- Manejo de errores para entradas inválidas y respuestas de terceros en sincronización de feeds.
