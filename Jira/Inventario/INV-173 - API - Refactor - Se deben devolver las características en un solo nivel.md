---
jira_key: "INV-173"
aliases: ["INV-173"]
summary: "API - Refactor - Se deben devolver las características en un solo nivel"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-20 12:17"
updated: "2025-01-30 02:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-173"
---

# INV-173: API - Refactor - Se deben devolver las características en un solo nivel

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-20 12:17 |
| Actualizado | 2025-01-30 02:57 |
| Etiquetas | ninguna |
| Jira | [INV-173](https://bluinc.atlassian.net/browse/INV-173) |

## Relaciones

- **Padre:** [[INV-35]] Importadores/ Scrappers

## Descripcion

Se debe modificar el objeto de respuesta para que esté todo dentro de un solo objeto y sin objetos dentro


```
{{API_URL}}/attributes/scrap
```



```
{
    "productId": 119762,
    "url" : "https://www.samsung.com/ar/monitors/flat/t35f-22-inch-ips-fhd-1080p-freesync-lf22t350fhlxzb/#specs"
}
```

```

{
    "success": true,
    "data": {
        "Resolución": "1,920 x 1,080",
        "Relación de aspecto": "16:9",
        "Brillo (Típico)": "250 cd/㎡",
        "Relación de contraste estática": "1000:1",
        "Tiempo de respuesta": "5 (GTG）",
        "Frecuencia de actualización Max": "75Hz",
        "Tamaño de pantalla activa (HxV)": "476.064 x 267.786 mm",
        "Brillo (Min)": "200 cd/㎡",
        "Contrast Ratio (Dynamic)": "Mega",
        "Color Gamut (NTSC 1976)": "72% (CIE 1931)",
        "Temperatura": "10℃~ 40℃",
        "Humedad": "10% ~ 80%, non-condensing",
        "Tamaño del conjunto con soporte": "488.8 x 396.9 x 232.0 mm",
        "Tamaño del conjunto sin soporte": "488.8 x 294.4 x 39.4 mm",
        "Peso del paquete": "3.5 kg",
        "Longitud del cable de alimentación": "1.5 m",
        "HDMI Cable": "Yes",
        "Manual del usuario y descargas": "User Manual ver 2410280 | 3.75 MB 2024-10-29 Multi-idiomas INGLÉS, FRANCÉS, ESPAÑOL, Portugués (Brasil)"
    }
}
```
