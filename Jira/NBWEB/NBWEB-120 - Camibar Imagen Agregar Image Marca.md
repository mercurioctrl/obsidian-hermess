---
jira_key: "NBWEB-120"
aliases: ["NBWEB-120"]
summary: "Camibar Imagen / Agregar Image Marca"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-19 12:43"
updated: "2022-11-09 11:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-120"
---

# NBWEB-120: Camibar Imagen / Agregar Image Marca

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-19 12:43 |
| Actualizado | 2022-11-09 11:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-120](https://bluinc.atlassian.net/browse/NBWEB-120) |

## Relaciones

- **Padre:** [[NBWEB-73 - API - CMS - ABMS|NBWEB-73]] API - CMS - ABMS

## Descripcion

```
POST {{API_URL}}/v1/cms/brand
```

Request

```
{
  'image': '',
  'brandId' : 12
}
```

Return

```
{
  success: 'ok',
  image: 'bd470a4653ccf91cb73a09790b14f0f4.jpeg';
}
```



Se debe guardar en `[NB_WEB].[dbo].[marcas].[imagen]` utilizando un formato 

https://cache-static.nb.com.ar/img/be41a8a927fc7e0bf1de452ff191c39e.jpeg
