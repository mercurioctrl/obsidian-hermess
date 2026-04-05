---
jira_key: "COB-560"
aliases: ["COB-560"]
summary: "API - Feat - Recurso para listar y descargar percepciones ARBA (parte 1)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-29 08:50"
updated: "2025-07-04 11:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-560"
---

# COB-560: API - Feat - Recurso para listar y descargar percepciones ARBA (parte 1)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-29 08:50 |
| Actualizado | 2025-07-04 11:11 |
| Etiquetas | ninguna |
| Jira | [COB-560](https://bluinc.atlassian.net/browse/COB-560) |

## Relaciones

- **Padre:** [[COB-559 - Listar y descargar percepciones|COB-559]] Listar y descargar percepciones
- **has action item:** [[COB-567 - APP - Feat - Agregar seccion percepciones para visualizar y filtrar y|COB-567]] APP - Feat - Agregar seccion percepciones para visualizar y filtrar y accionables de descarga
- **relates to:** [[COB-568 - API - Review - Recurso para descargar archivo ARBA, devolucion estudio contable|COB-568]] API - Review - Recurso para descargar archivo ARBA, devolucion estudio contable

## Descripcion

Se debe desarrollar un endpoint que permita obtener percepciones de Ingresos Brutos (IIBB) según jurisdicción **ARBA**  (en la próxima historia haremos el type **AGIP**) basándose en la tabla `[NewBytes_DBF].[dbo].[FP_FactWebCliEncabezado]`.

Este endpoint debe:

- Filtrar por un rango de fechas (`between`) aplicado sobre la fecha de emisión de los comprobantes.


- Soportar paginación (`currentPage`, `itemsPerPage`).


- Permitir descargar un archivo `.txt` formateado conforme a los lineamientos de ARBA  cuando `download=1`.


- O devolver los resultados como JSON cuando `download=0`.



```
GET /v1/perceptionibb?type=arba&currentPage=1&itemsPerPage=15&between=01-05-2025_31-05-2025&download=1
```

**Parámetros query:**

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| `type` | string | Tipo de percepción: `"arba"` o `"agip"` |
| `between` | string | Rango de fechas en formato `DD-MM-YYYY_DD-MM-YYYY` |
| `currentPage` | int | Página actual para la vista en JSON |
| `itemsPerPage` | int | Cantidad de ítems por página |
| `download` | int (0/1) | Si es `1`, genera archivo `.txt`. Si es `0`, devuelve JSON paginado |

**Reglas:**

- Si `type=arba`, filtrar comprobantes que tengan percepción ARBA (`jurisdicción = Buenos Aires`).


- Si `type=agip`, filtrar comprobantes con percepción AGIP (`jurisdicción = CABA`) (ESTO ES PARA DESPUES)


- Si `download=1`, generar `.txt` en formato oficial para presentación.


- El archivo debe descargarse directamente desde el navegador con nombre:

- `ARBA_PERCEPTIONS_202505.txt`


- `AGIP_PERCEPTIONS_202505.txt`




- Si `download=0`, devolver JSON estructurado como el siguiente ejemplo:



Ejemplo Salida con `donwload=0`

```
{
  "currentPage": 1,
  "itemsPerPage": 15,
  "totalItems": 2,
  "totalPages": 1,
  "data": [
    {
      "invoiceDate": "2025-05-07",
      "documentType": "F",
      "documentLetter": "A",
      "branchNumber": "0001",
      "documentNumber": "00001234",
      "clientCuit": "20123456789",
      "taxableAmount": 10000.00,
      "perceptionAmount": 350.00,
      "rate": 3.50,
      "jurisdiction": "ARBA"
    },
    {
      "invoiceDate": "2025-05-21",
      "documentType": "F",
      "documentLetter": "B",
      "branchNumber": "0005",
      "documentNumber": "00009876",
      "clientCuit": "20345987123",
      "taxableAmount": 20000.00,
      "perceptionAmount": 600.00,
      "rate": 3.00,
      "jurisdiction": "AGIP"
    }
  ]
}

```

**Notas técnicas:**

- La fecha de emisión debe mapearse a `invoiceDate`.


- El CUIT del cliente debe normalizarse sin guiones para exportación.


- El separador decimal debe respetarse según normativa en formato `.txt`.


- El TXT debe incluir solo percepciones válidas para la jurisdicción solicitada.


- Se adjunta el documento oficial donde están todas las especificaciones detalladas para componer el archivo  



Esta historia continua con el mismo archivo, pero generado para AGIP (CABA) en la historia [link](https://bluinc.atlassian.net/browse/COB-561)
