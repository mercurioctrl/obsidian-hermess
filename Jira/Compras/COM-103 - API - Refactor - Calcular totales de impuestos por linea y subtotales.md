---
jira_key: "COM-103"
aliases: ["COM-103"]
summary: "API - Refactor - Calcular totales de impuestos por linea y subtotales"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-06-06 09:47"
updated: "2024-06-27 17:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-103"
---

# COM-103: API - Refactor - Calcular totales de impuestos por linea y subtotales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-06 09:47 |
| Actualizado | 2024-06-27 17:03 |
| Etiquetas | ninguna |
| Jira | [COM-103](https://bluinc.atlassian.net/browse/COM-103) |

## Relaciones

- **Padre:** [[COM-38]] Ver orden de compra
- **blocks:** [[COM-104]] APP - Refactor - Agregar totales impositivos al modal de la orden
- **is blocked by:** [[COM-108]] API - Calcular totales de impuestos por línea y subtotales - Valores no coincidentes

## Descripcion

Crearemos un recurso especifico para calcular el sobtotal por item de impuestos y a su vez, el subtotal de toda la orden.

Para esto obtendremos el total por item sumando los montos deducidos de los porcentajes 

AEC IIBB IVA IVA AD GAN TE DII DIE, aplicados sobre (cant+ingresado * costo)

```
GET {API_URL}/v1/totalTaxexProviderOrder/{order}
```

```
{
    "response": {
        "items": [
            {
                "id": 5325,
                "totalItemTax": 111770,
            },
            {
                "id": 233,
                "totalItemTax": 23424,
            }            
          ],
      "subtotalTaxPosition": {
        "aec": 353.3,
        "iibb": 6455.5,
        "iva": 234.4,
        "ivaAd": 3466.4,
        "ganancias": 63445.43
        "te": 534,
        "dii": 0,
        "die": 146,
        "ivaimp": 43.43
    },        
  }
 }         
```



[adjunto]
