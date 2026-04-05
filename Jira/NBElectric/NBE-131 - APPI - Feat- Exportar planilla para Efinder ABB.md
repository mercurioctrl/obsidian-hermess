---
jira_key: "NBE-131"
aliases: ["NBE-131"]
summary: "APPI - Feat- Exportar planilla para Efinder ABB"
status: "Listo"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Alejandra Guidobono"
created: "2025-07-14 15:24"
updated: "2025-07-22 22:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBE-131"
---

# NBE-131: APPI - Feat- Exportar planilla para Efinder ABB

| Campo | Valor |
|-------|-------|
| Estado | Listo (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Alejandra Guidobono |
| Creado | 2025-07-14 15:24 |
| Actualizado | 2025-07-22 22:11 |
| Etiquetas | ninguna |
| Jira | [NBE-131](https://bluinc.atlassian.net/browse/NBE-131) |

## Relaciones

- **Subtarea:** [[NBE-157]] API - Feat - SyncUp para cargar el archivo efinderABB en el endpoint directamente

## Descripcion

Se requiere generar un nuevo catálogo específico para la empresa **efinderABB**, cuya estructura es similar al catálogo ya existente en la siguiente URL:

```
https://api.nbe.com.ar/v1/priceListExcel/4520348d5e5ab6d973b54aec33dcd3
```

El nuevo catálogo estará disponible en la siguiente ruta:

```
https://api.nbe.com.ar/v1/efinderABB/{token}
```

Solo que la composición es diferente (Se adjunta el ejemplo a replicar)

El mismo cuenta con 6 columnas

- item (Numeracion incremental)


- Codigo SAP (nuestro id interno `itemId`)


- Codigo Comercial (Nuestro SKU `ID_PRODUCTO`)


- Descripción Técnica del Equipamiento (Nuestro nombre `cDetalle`)


- CANT. STOCK (Nuestro stock real de la columna `nstock`)


- link (El link al sitio del tipo [https://nbe.com.ar/np2-bd23-llave-maneta-corta-selectora-de-2-posiciones-fija-2na_-_119656](https://nbe.com.ar/np2-bd23-llave-maneta-corta-selectora-de-2-posiciones-fija-2na_-_119656))
