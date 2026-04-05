---
jira_key: "LIO-46"
aliases: ["LIO-46"]
summary: "API - Refactor - Crear formularios de registro especifico para empresas e individuos - Añadir razón social"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-06-14 14:57"
updated: "2024-06-19 12:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-46"
---

# LIO-46: API - Refactor - Crear formularios de registro especifico para empresas e individuos - Añadir razón social

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-14 14:57 |
| Actualizado | 2024-06-19 12:06 |
| Etiquetas | ninguna |
| Jira | [LIO-46](https://bluinc.atlassian.net/browse/LIO-46) |

## Relaciones

- **Padre:** [[LIO-11 - Proceso de registro sencillo para los vendedoresCompradores|LIO-11]] Proceso de registro sencillo para los vendedores/Compradores
- **relates to:** [[LIO-34 - API - Feat - Crear formularios de registro especifico para empresas e individuos|LIO-34]] API - Feat - Crear formularios de registro especifico para empresas e individuos 
- **relates to:** [[LIO-47 - APP - Refactor - Crear formularios de registro especifico para empresas e|LIO-47]] APP - Refactor - Crear formularios de registro especifico para empresas e individuos - Añadir razón social al registrar

## Descripcion

1. Realizaremos un refactor para añadir el nuevo parámetro enviado por el front `businessName` el cual será la razón social.

Cabe mencionar que este parámetro no es obligatorio al ser propio del registro de empresa.

```
POST {{API_URL}}/v4/auth/register
```

```
{
    "document": "20331854493",
    "fullName": "ANCHOVERRI PONCE NICOLAS RODRIGO",
    "businessName" "" <----------------------------- Se agrega
    "email": "gprueba1212@nb.com.ar",
    "password": "wa23er234rdf23"
}
```



2. Adicional a esto realizaremos la modificación correspondiente para que se inserte correctamente el URI.

[adjunto]
