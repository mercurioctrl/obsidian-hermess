---
jira_key: "NBWEB-542"
summary: "CMS - Permisos por seccion"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-05-08 09:05"
updated: "2023-09-06 09:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-542"
---

# NBWEB-542: CMS - Permisos por seccion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-08 09:05 |
| Actualizado | 2023-09-06 09:40 |
| Etiquetas | ninguna |
| Jira | [NBWEB-542](https://bluinc.atlassian.net/browse/NBWEB-542) |

## Descripción

Agregaremos un permiso por cada una de las secciones tal como hicieron el requerimiento

- [Marcas](https://cms-nbweb.saftel.com/brands)


- [Banners](https://cms-nbweb.saftel.com/banners)


- [Medios de pago](https://cms-nbweb.saftel.com/paymentMethods)


- [Personal](https://cms-nbweb.saftel.com/staffs)


- [Formas de Cobro](https://cms-nbweb.saftel.com/paymentMethodTrade)


- [Medios de envío](https://cms-nbweb.saftel.com/shippingMethods)


- [Cotización](https://cms-nbweb.saftel.com/currenciesQuote)


- [Parametros varios](https://cms-nbweb.saftel.com/defaultParameters)



**Para poder hacer esto se debe primero agregar el recurso user** (tal como lo hacemos en el sistema de caja, expedicion, etc) y devolver algo como esto

```
GET {API_URL}/v1/cms/user
```

```
{
    "user":{
    "id": 41,
    "userName": "dario",
    "email": "daltamiranda@nb.com.ar",
    "type": "administrador",
    "user_agent": null,
    "cms_lo": null,
    "cms_nb": null
  }
}
```

*Esta informacion debe estar contenido en el objeto de JWT*

Adicional mente agregaremos un permiso por cada sección

```
{
    "user":{
    "id": 41,
    "userName": "dario",
    "email": "daltamiranda@nb.com.ar",
    "type": "administrador",
    "user_agent": null,
    "cms_lo": true,
    "cms_nb": false,
    "banner": true, <--Se agrega
    "paymentMethods": true, <--Se agrega
    "categories": true, <--Se agrega
    "shippingMethods": false, <--Se agrega
    "currencyQuote": false, <--Se agrega
    "defaultParameters": true, <--Se agrega
    "staff": true
  }
}
```

Debemos agregar uno por cada una de las secciones.

El dataset, que tiene los permisos puede estar en la tabla de permisos que ya utilizamos antes, aunque yo preferiría usar para esto específicamente la tabla `[NB_WEB].[dbo].[permisos_admin]` 

Una vez que tenemos el objeto user, lo podemos utilizar para saber en el front que secciones debo mostrar y cuales no para cada caso, según el usuario.

[attachment]
[attachment]
Ademas, se debe bloquear cada recurso (patch,post,delete) que sea para cada recurso, segun este Middleware de admin

Repositorio: [link](https://github.com/New-Bytes/cms-nb-wep-app-v1)
