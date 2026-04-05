---
jira_key: "NBWEB-79"
summary: "Cotizador de ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-04-04 07:09"
updated: "2022-06-26 20:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-79"
---

# NBWEB-79: Cotizador de ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-04 07:09 |
| Actualizado | 2022-06-26 20:17 |
| Etiquetas | ninguna |
| Jira | [NBWEB-79](https://bluinc.atlassian.net/browse/NBWEB-79) |

## Descripción

```
GET {{API_URL}}/order/nb/{branch}-{order}/cp/1426/cphost/1229
```



```
GET {{API_URL}}/order/nb/{branch}-{order}/cp/1426
```

Se debe crear un recurso para poder cotizar una orden de compra completa, según los distintos métodos de envío.



El mismo retorna un array de objetos del siguiente tipo:



```json
[
    {
        "costo": 439.01,
        "descripcion": "OCA a domicilio",
        "id": 4041,
        "precio": 0,
        "plazoEntrega": "entre el viernes 08 y el martes 12",
        "plazoEntregaNumero": 4,
        "total": 439.01
    },
    {
        "costo": 993.01,
        "descripcion": "Andreani a domicilio",
        "id": 4065,
        "precio": 993.01,
        "plazoEntrega": "entre mañana y el jueves 07",
        "plazoEntregaNumero": 1,
        "total": 993.01
    },
    {
        "costo": 300,
        "descripcion": "Moto (Capital Federal).",
        "id": 3030,
        "precio": 0,
        "plazoEntrega": "hoy",
        "plazoEntregaNumero": 0,
        "total": 300,
        "horaActual": "2022-04-04 07:07:36"
    }
]
```



SQL, algunos ejemplos:



```sql
SELECT 
familias.largoMaximo,
familias.anchoMaximo,
familias.altoMaximo,
familias.pesoMaximo
FROM [NewBytes_DBF].[dbo].[pedclit]
LEFT JOIN [NewBytes_DBF].[dbo].[pedclil]
ON pedclit.cnumped = pedclil.cnumped and pedclit.cnumsuc = pedclil.cnumsuc
LEFT JOIN [NewBytes_DBF].dbo.[articulo] ON pedclil.ID_Articulo = articulo.ID_ARTICULO
LEFT JOIN [NewBytes_DBF].dbo.familias ON articulo.ID_FAMILIA = familias.ID_FAMILIA
```

---

```
SELECT *
FROM [NewBytes_DBF].[dbo].[pedclit]
LEFT JOIN NewBytes_DBF.dbo.pedclil ON pedclit.cnumped = pedclil.cnumped AND pedclit.cnumsuc = pedclil.cnumsuc
where pedclit.cnumped = '10217160' and pedclit.cnumsuc = '0002'
```



Si ejecutas esa query, vas a ver un pedido completo

que podes cotizar

Si lo llevo a la nomenclatura de las apis

las columnas llamadas cnumped son orderId o el numero de orde

y las columnas llamadas cnumsuc son branch
