---
jira_key: "COB-316"
aliases: ["COB-316"]
summary: "APP - Feat - Agregar proveedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-01-30 09:05"
updated: "2023-02-23 17:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-316"
---

# COB-316: APP - Feat - Agregar proveedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-30 09:05 |
| Actualizado | 2023-02-23 17:22 |
| Etiquetas | ninguna |
| Jira | [COB-316](https://bluinc.atlassian.net/browse/COB-316) |

## Relaciones

- **Padre:** [[COB-150]] Feat - Proveedores
- **is blocked by:** [[COB-291]] API - Feat - Listar provincias (para retención)
- **is blocked by:** [[COB-317]] API - Feat- Repositorio Localidades
- **is blocked by:** [[COB-318]] API - Feat- Repositorio Paises
- **blocks:** [[COB-319]] APP - Feat - Agregar accionable para carga rápida de proveedor

## Descripcion

En la pestaña proveedores agregaremos un boton para lanzar el modal “Agregar proveedor”

El mismo cuenta con los campos necesarios para generar la carga util:

Payload:

```
  {
    "id": 14646,
    "name": "TRENDSETTERS - DA PALACE SRL",
    "businessName": "TRENDSETTERS - DA PALACE SRL",
    "Addres": "CARLOS TEJEDOR 890",
    "countryId": 7,
    "provicenId": 2,
    "localitieId": 14233,
    "Contact": "",
    "SaldoInicialCTA": null,
    "AgentePercIVA": 0,
    "ivaPercepction": false,
    "correo": "",
    "aliquotIbb": 1
  }
```

y ejecuta el recurso

```
POST {{API_URL}}/v1/providers
```
