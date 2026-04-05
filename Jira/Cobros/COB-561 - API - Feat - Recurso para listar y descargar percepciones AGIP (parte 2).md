---
jira_key: "COB-561"
aliases: ["COB-561"]
summary: "API - Feat - Recurso para listar y descargar percepciones AGIP (parte 2)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-29 09:14"
updated: "2025-06-17 11:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-561"
---

# COB-561: API - Feat - Recurso para listar y descargar percepciones AGIP (parte 2)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-29 09:14 |
| Actualizado | 2025-06-17 11:16 |
| Etiquetas | ninguna |
| Jira | [COB-561](https://bluinc.atlassian.net/browse/COB-561) |

## Relaciones

- **Padre:** [[COB-559 - Listar y descargar percepciones|COB-559]] Listar y descargar percepciones
- **has action item:** [[COB-567 - APP - Feat - Agregar seccion percepciones para visualizar y filtrar y|COB-567]] APP - Feat - Agregar seccion percepciones para visualizar y filtrar y accionables de descarga

## Descripcion

Esto es una continuación de [link](https://bluinc.atlassian.net/browse/COB-560) ya que retoma el mismo recurso para todo, menos para la descarga del archivo que se explica a continuación para AGIP (caba)

El recurso es exactamente el mismo y entrega el mismo resultado a nivel `JSON`pero esta historia es para dar detalles sobre como generar el TXT que dado que son agencias tributarias diferentes, es ligeramente diferente

```
GET /v1/perceptionibb?type={agip|arba}&currentPage=1&itemsPerPage=15&between=01-05-2025_31-05-2025&download=1
```

```
{
  "pagination" :{"currentPage": 1,
  "itemsPerPage": 15,
  "totalItems": 2,
  "totalPages": 1},
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

**Formato del archivo .txt generado (si **`download=1`**):**

Debe cumplir con el diseño técnico e-ARCIBA:

- Campos de longitud fija.


- Encoding: **[[UTF-8]] sin BOM**.


- Separador decimal: punto.


- Ejemplo de línea (formato simplificado, los | no van son para que se note cada parte):



```
2|01|07/05/2025|01|A|00000001|07/05/2025|10000.00|12345678901|3|1|20304050607|1|3|Empresa Demo|300.00|0.00|0.00|3.00|300.00|300.00
```

Linea real

```
2012025012310012022050701200000102022050710000.002012345678930010203040506070103Empresa Demo       0300.00000.00000.003.00300.00300.00
```

- `operationType` será siempre `2` para percepciones.


- `taxCode` debe ser `"01"` según el instructivo AGIP.


- Si el cliente es monotributista o exento, campos como `vatAmount` deben ir en blanco o 0, según normativa.


- El archivo `.txt` debe ser descargado automáticamente con nombre:

- `AGIP_PERCEPTIONS_202505.txt`




- INSTRUCTIVO DE AGIP (CABA)  



También se adjunta un ejemplo del archivo como se genera en el sistema viejo que estamos deprecando
