---
jira_key: "PEGA-46"
aliases: ["PEGA-46"]
summary: "API - Feat - Subir banner"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-01-03 09:25"
updated: "2023-01-09 13:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-46"
---

# PEGA-46: API - Feat - Subir banner

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-03 09:25 |
| Actualizado | 2023-01-09 13:49 |
| Etiquetas | ninguna |
| Jira | [PEGA-46](https://bluinc.atlassian.net/browse/PEGA-46) |

## Relaciones

- **Padre:** [[PEGA-33 - Feat - Administrar sliders|PEGA-33]] Feat - Administrar sliders
- **blocks:** [[PEGA-35 - APP - Feat - Administrar sliders|PEGA-35]] APP - Feat - Administrar sliders

## Descripcion

Este recurso es muy parecido a [http://gamma.api.nb.com.ar/v1/cms/banner](http://gamma.api.nb.com.ar/v1/cms/banner) y lo que hace es subir la imagen al servidor, de forma tal que pueda luego guardarse para el slide

Se debe utilizar el recurso para subir imágenes al servidor y a su vez poder ordenarlas

```
POST {{API_URL}}/v1/cms/banner/{zoneId}
```

```


Request
{
  image: ''
}

```

Return

```
{
  success: 'ok',
  image: 'bd470a4653ccf91cb73a09790b14f0f4.jpeg';
}
```
