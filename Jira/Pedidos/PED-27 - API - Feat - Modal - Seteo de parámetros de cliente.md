---
jira_key: "PED-27"
aliases: ["PED-27"]
summary: "API - Feat - Modal - Seteo de parámetros de cliente "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-08-10 14:10"
updated: "2023-08-14 12:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-27"
---

# PED-27: API - Feat - Modal - Seteo de parámetros de cliente 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-10 14:10 |
| Actualizado | 2023-08-14 12:51 |
| Etiquetas | ninguna |
| Jira | [PED-27](https://bluinc.atlassian.net/browse/PED-27) |

## Relaciones

- **Padre:** [[PED-16]] Listar clientes
- **blocks:** [[PED-25]] APP - Feat - Modal - Seteo de parámetros de cliente 

## Descripcion

Esta feature se vincula con [link](https://lioteam.atlassian.net/browse/PED-20)  y a [link](https://lioteam.atlassian.net/browse/PED-25) 

Básicamente se trata de dos recursos necesarios para levantar un modal en donde configurar los parámetros ([link](https://lioteam.atlassian.net/browse/PED-25) ).

En este modal, tendremos para configurar los siguientes datos para cada cliente

- Perfil (Select)


- Empresa (Select)


- Vendedor (Select)


- Divisa (Select)




En principio necesitamos poder leerlo para poder cargar los datos en el formulario y esto podemos hacerlo recortando este recurso o bien saltarnos el paso y reutilziar el ya existente [link](https://lioteam.atlassian.net/browse/PED-20) 


```
GET {API_URL}/v1/clientParameters/{clientId}
```

```
{
  "salespersonId"8,
  "currencyId":1
  "profile":1,
  "companyCode":4,
}
```



Por otro lado tenemos la edición, que podría hacerse con el recurso [link](https://lioteam.atlassian.net/browse/PED-19)  pero algunos de los parámetros requieren un trato particular.


```
PATCH {API_URL}/v1/clientParameters/{clientId}
```

```
{
  "salespersonId"8,
  "currencyId":1
  "profile":1,
  "companyCode":4,
}
```

### Perfil

Se trata del tipo de “`profile`” del cliente. En este esquema están basados los precios que reciben y algunos criterios fiscales.

Los perfiles son enteros del 0 al 4 (0,1,2,3,4) y cuya leyenda para cada caso es “perfil 0”, “perfil 1” y así.

**Primer bloque **`switch` (basado en `$profile`):

Se verifica el valor de la variable `$profile`. Dependiendo de su valor, se asignan diferentes valores a las variables `$NDTO`, `$NTARIFAPP` y `$PRECIOAMANO`.

- Si `$profile` es 0:

- `$NDTO` se establece en 0.


- `$NTARIFAPP` se establece en 1.


- `$PRECIOAMANO` se establece en 0.




- Si `$profile` es 1 o 2:

- `$NDTO` se establece en 1.


- `$NTARIFAPP` se establece en 1.


- `$PRECIOAMANO` se establece en 0.




- Si `$profile` es 3 o 4:

- `$NDTO` se establece en 3.


- `$NTARIFAPP` se establece en 5.


- `$PRECIOAMANO` se establece en 0.




- Si `$profile` no coincide con ninguno de los valores anteriores, no se hace nada




Con estos parámetros saeteamos el perfil del cliente

```
UPDATE [NewBytes_DBF].[dbo].[clientes]
SET
ndto = NDTO,
ntarifapp = NTARIFAPP,
precioAMano = PRECIOAMANO,
perfil = profile,
WHERE ID_CLIENTE = valor_id_cliente;
```

### Empresa

Esta basado en el repositorio [link](https://lioteam.atlassian.net/browse/PED-24)

Con estos parámetros saeteamos 

```
UPDATE [NewBytes_DBF].[dbo].[clientes]
SET
CODEMP = companyCode,
WHERE ID_CLIENTE = clientId
```

### Vendedor

Esta basado en el repositorio [link](https://lioteam.atlassian.net/browse/PED-23)
Con estos parámetros saeteamos 

```
UPDATE [NewBytes_DBF].[dbo].[clientes] SET ccodage = (SELECT ccodage
FROM [NewBytes_DBF].[dbo].[agentes]
where ID_VENDEDOR = salespersonId ),
ID_VENDEDOR = salespersonId 
WHERE ID_CLIENTE = clientId
```

### Divisa

Esta basado en el repositorio [link](https://lioteam.atlassian.net/browse/PED-26)

Con estos parámetros saeteamos 

```
UPDATE [NewBytes_DBF].[dbo].[clientes]
SET
ID_DIVISA = currencyId
CCODDIV = (SELECT CCODDIV
  FROM [NewBytes_DBF].[dbo].[FP_Monedas] where Id_Moneda = currencyId)
WHERE ID_CLIENTE = clientId
```
