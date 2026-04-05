---
jira_key: "INV-265"
aliases: ["INV-265"]
summary: "API - Feat - Adjuntar PDF a un certificado"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-01 08:02"
updated: "2025-12-04 11:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-265"
---

# INV-265: API - Feat - Adjuntar PDF a un certificado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-01 08:02 |
| Actualizado | 2025-12-04 11:11 |
| Etiquetas | ninguna |
| Jira | [INV-265](https://bluinc.atlassian.net/browse/INV-265) |

## Relaciones

- **Padre:** [[INV-260]] Certificados eléctricos por Qr
- **has action item:** [[INV-266]] APP - Feat - Adjuntar PDF a un certificado

## Descripcion

## Subir y asociar archivo a un certificado eléctrico

Se deberá crear un recurso que permita **subir un archivo PDF** a un servidor de archivos externo y **asociarlo a un certificado eléctrico** determinado.
La relación se almacenará en una **tabla anexa** vinculada al certificado.

---

### 1) Nuevo endpoint

```
POST {API_URL}/electricalCertificate/{id}/files
```

Función:

- Recibe un archivo (PDF) asociado al certificado `{id}`.


- Lo sube al servidor de archivos `static.nb.com.ar`.


- Si la subida es exitosa, persiste en una tabla anexa todos los datos devueltos por dicho servidor.



#### Request (ejemplo)

- Tipo: `multipart/form-data`


- Campos:

- `file` → archivo PDF (obligatorio)





---

### 2) Integración con servidor de archivos

El backend deberá realizar una llamada HTTP al servidor:

```
POST 'https://static.nb.com.ar/u?key=ULPA7I2Bvhew2r2whGmMbYtZPAwuGl4C' \
  --header 'Authorization: Basic PEJhc2ljIEF1dGggVXNlcm5hbWU+OjxCYXNpYyBBdXRoIFBhc3N3b3JkPg== ' \
  --form 'temp=0' \
  --form 'imagen=@"/ruta/local/disp1.pdf"'

```

*(En el código, la ruta del archivo será el stream recibido en el endpoint, no la ruta local del ejemplo.)*

El servidor de archivos devuelve un JSON similar a:

```
{
  "id": "416852",
  "filename": "7290717fe486d2c661ecef2d6fc8056a.pdf",
  "url": "http://static.nb.com.ar/img/7290717fe486d2c661ecef2d6fc8056a.pdf"
}

```

---

### 3) Nueva tabla anexa en SQL Server

Crear una tabla de relación para almacenar los archivos asociados a cada certificado.

**Tabla:** `ElectricalCertificateFiles` (o equivalente según convenciones)

Campos mínimos:

- `id` → INT IDENTITY, **PK**


- `electrical_certificate_id` → INT, **FK** a `ElectricalCertificates.id`


- `external_id` → NVARCHAR(50) **NOT NULL**
(campo `id` devuelto por el servidor de archivos)


- `filename` → NVARCHAR(255) **NOT NULL**
(campo `filename` devuelto)


- `url` → NVARCHAR(500) **NOT NULL**
(campo `url` devuelto)


- `created_at` → DATETIME **NOT NULL**



Regla de negocio clave:

> **Solo se crea un registro en esta tabla si la subida al servidor de archivos fue exitosa y se obtuvo un JSON válido.**
Si la subida falla, no se inserta nada en la tabla.


---

### 4) Flujo del endpoint

- Validar que el certificado `{id}` exista.


- Validar que se haya enviado un archivo `file`.


- Subir el archivo al servidor `static.nb.com.ar` con:

- Query param `key`


- Header `Authorization: Basic ...`


- Campos de formulario `temp=0` e `imagen` (archivo).




- Si la respuesta es exitosa y con JSON válido (`id`, `filename`, `url`):

- Insertar registro en `ElectricalCertificateFiles`.




- Devolver al cliente los datos guardados.



#### Response ejemplo

```
{
  "id": 3,
  "certificateId": 7,
  "external_id": "416852",
  "filename": "7290717fe486d2c661ecef2d6fc8056a.pdf",
  "url": "http://static.nb.com.ar/img/7290717fe486d2c661ecef2d6fc8056a.pdf",
  "created_at": "2025-12-01 11:45:20"
}

```

---

### 5) Manejo de errores

- Si el certificado no existe → `404 Not Found`.


- Si no se envía archivo → `400 Bad Request`.


- Si falla la subida al servidor de archivos (timeout, 4xx/5xx, JSON inválido) →

- No se inserta nada en la tabla anexa.


- Se responde con `502 Bad Gateway` o `500` (según política) indicando fallo en el servidor de archivos externo.





---

### 6) Criterios de aceptación

- ✅ Existe la tabla `ElectricalCertificateFiles` vinculada a `ElectricalCertificates` por FK.


- ✅ El endpoint `POST /electricalCertificate/{id}/files`:

- Valida certificado y archivo.


- Sube el archivo a `static.nb.com.ar` usando los parámetros dados.


- Solo crea el registro en BD si la subida es exitosa.




- ✅ Se guardan en BD los campos `external_id`, `filename`, `url` y la relación con el certificado.


- ✅ La respuesta del endpoint devuelve los datos persistidos.
