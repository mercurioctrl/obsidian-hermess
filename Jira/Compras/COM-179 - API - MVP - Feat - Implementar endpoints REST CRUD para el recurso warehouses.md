---
jira_key: "COM-179"
aliases: ["COM-179"]
summary: "API - MVP - Feat - Implementar endpoints REST CRUD para el recurso warehouses basado en la tabla [FP_Almacen]"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-05 08:17"
updated: "2025-05-19 13:34"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/COM-179"
---

# COM-179: API - MVP - Feat - Implementar endpoints REST CRUD para el recurso warehouses basado en la tabla [FP_Almacen]

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-05 08:17 |
| Actualizado | 2025-05-19 13:34 |
| Etiquetas | MVPLaset |
| Jira | [COM-179](https://bluinc.atlassian.net/browse/COM-179) |

## Relaciones

- **Padre:** [[COM-178 - Depositos|COM-178]] Depositos
- **has action item:** [[COM-180 - APP - MVP - Feat - Implementar pestaña Depositos|COM-180]] APP - MVP - Feat - Implementar pestaña "Depositos"

## Descripcion

Exponer los recursos REST `GET`, `POST`, `PATCH`, `DELETE` sobre `warehouses`,
**para** permitir la gestión completa (listar, crear, editar, eliminar) de los depósitos físicos y virtuales donde se almacena el stock.

```
GET {API_URL}/v1/warehouses?search={name|code|id}
```

```
{
   "response": [
      {
         "id": 1,
         "code": "DE1",
         "name": "DEPOSITO 1",
         "address": "",
         "cityCode": "BSAS",
         "provinceCode": 1,
         "phone": "",
         "default": true,
         "cityId": 2,
         "provinceId": 0
      },
      {...
   ],
   "pagination": {
      "total": 9,
      "limit": 15,
      "offset": 0
   }
}

```

```
POST {API_URL}/v1/warehouses
```

```
  {
    "id": 1,
    "code": "ALM001",
    "name": "Depósito Central"
  }
```

- Crea un nuevo depósito con los campos requeridos (Como minimo debo agregar campo `id,code,name` aunque puedo incluirlos todos)


- Devuelve `201 Created` con el depósito creado.



```
DELETE {API_URL}/v1/warehouses
```

- Elimina (SOFT) un depósito.


- Devuelve `204 No Content` si se elimina correctamente



```
PATCH {API_URL}/v1/warehouses
```

```
 {
    "id": 1,
    "code": "ALM001",
    "name": "Depósito Central",
    "cityCode": "XYZ",
    "provinceCode": 3,
  }
```

- Mientras incluya el `id` (obligatorio) el resto de los campos que estén presentes, son los que son editables.



### Tabla SQL

```
SELECT * FROM [NewBytes_DBF].[dbo].[FP_Almacen]
```

| Campo SQL | Atributo JSON (camelCase) |
| --- | --- |
| `ID_ALMACEN` | `id` |
| `CCODALM` | `code` |
| `CNOMBRE` | `name` |
| `CDIRECC` | `address` |
| `CCODPOBL` | `cityCode` |
| `NCODPROV` | `provinceCode` |
| `CTFNO` | `phone` |
| `Predeterminado` | `default` |
| `ID_CIUDAD` | `cityId` |
| `ID_Provincia` | `provinceId` |

### ✅ Criterios de Aceptación: Recurso `/v1/warehouses`

---

#### 🔹 `GET /v1/warehouses`

- Cada elemento incluye todos los atributos definidos:
`id`, `code`, `name`, `address`, `cityCode`, `provinceCode`, `phone`, `default`, `cityId`, `provinceId`.


- Responde con código **200 OK**.


- Debe estar paginado si se define un límite superior de resultados.



---

#### 🔹 `POST /v1/warehouses`

- Crea un nuevo depósito con los campos enviados en el cuerpo del request.


- Campos obligatorios:

- `code` (string, único)


- `name` (string)


- `default` (boolean)




- El resto de los campos son opcionales pero deben validarse si se proveen.


- En caso de éxito, responde con:

- Código **201 Created**


- El objeto creado en formato JSON.




- Si `code` ya existe, devuelve **409 Conflict** con mensaje de error.



---

#### 🔹 `PATCH /v1/warehouses`

- Acepta un **array de objetos JSON** donde cada objeto debe tener el campo `id`. → **modificado**: se manda un objeto json.


- Solo se actualizan los campos que están presentes en el objeto.


- Si el `id` no existe, debe devolver error


- Responde con:

- **200 OK** si todas las actualizaciones son exitosas.


- **207 Multi-Status** si hay una mezcla de éxitos y errores (por ejemplo: 2 actualizados, 1 fallido).


- **400 Bad Request** si falta el campo `id` en alguna entrada.




- Los campos que pueden actualizarse:
`code`, `name`, `address`, `cityCode`, `provinceCode`, `phone`, `default`, `cityId`, `provinceId`. 



---

#### 🔹 `DELETE /v1/warehouses/{id}`

- Elimina un depósito por su `id`.

- Puede ser eliminación lógica (por ejemplo, marcando como inactivo).




- Si el `id` existe y se elimina correctamente:

- Devuelve **204 No Content**




- Si el `id` no existe:

- Devuelve **404 Not Found**
