---
jira_key: "PED-352"
aliases: ["PED-352"]
summary: "API - Review - Algunos productos con stock, solo me los muestra cuando tildo \"sin stock\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-18 11:25"
updated: "2024-01-04 19:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-352"
---

# PED-352: API - Review - Algunos productos con stock, solo me los muestra cuando tildo "sin stock"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-18 11:25 |
| Actualizado | 2024-01-04 19:05 |
| Etiquetas | ninguna |
| Jira | [PED-352](https://bluinc.atlassian.net/browse/PED-352) |

## Relaciones

- **Padre:** [[PED-65]] Listado de productos
- **is blocked by:** [[PED-423]] API - Filtrado por stock no coincidente

## Descripcion

Ejemplo de producción:

Al buscar [(2936) FUENTE SFX 500W 20+4 SATA](https://www.nb.com.ar/fromPedidos_-_2936) me pasa que si hago

```
GET {API_URL}/v1/items?search=FUENTE+SFX+500W+20%2B4+SATA&stock=1
```

No aparece

Pero si cuando le pongo 

`stock=0`
