---
jira_key: "PED-1286"
aliases: ["PED-1286"]
summary: "API - Research - Clientes reactivados ¿cual es la mejor forma de obtener esta métrica?"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-26 08:54"
updated: "2026-02-03 17:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1286"
---

# PED-1286: API - Research - Clientes reactivados ¿cual es la mejor forma de obtener esta métrica?

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-26 08:54 |
| Actualizado | 2026-02-03 17:53 |
| Etiquetas | ninguna |
| Jira | [PED-1286](https://bluinc.atlassian.net/browse/PED-1286) |

## Relaciones

- **Padre:** [[PED-299 - Objetivos y Desafios|PED-299]] Objetivos y Desafios
- **has action item:** [[PED-1293 - API - Feat - Clientes Reactivados Vs Clientes reactivados objetivo|PED-1293]] API - Feat - Clientes Reactivados Vs Clientes reactivados objetivo

## Descripcion

Con los datos disponibles en las bases de datos, se debe realizar una propuesta para entender cual es la mejor forma de saber que clientes fueron reactivados agrupando por vendedor



**Propuesta**:

Crear un endpoint que retorne la cantidad de clientes reactivados agrupados por vendedor, permitiendo identificar qué vendedores están recuperando clientes inactivos.



**Definiciones:**

**Cliente Inactivo: **Cliente cuya última compra (ULTIMA_COMPRA) fue hace más de 3 meses desde la fecha de análisis.

**Cliente Reactivado:** Cliente que cumple ambas condiciones:

- Estuvo inactivo (sin compras en los últimos 3 meses antes de la venta)


- Realizó una compra confirmada (albclit) en el período de análisis





**Vendedor de Reactivación:**

El vendedor que realizó la venta que reactivó al cliente (albclit.ID_VENDEDOR), no necesariamente el vendedor asignado al cliente.

**Endpoint**

```
GET /v1/objectives/reactivatedClients
```



**Criterio de Inactividad:**

Un cliente se considera inactivo si su ULTIMA_COMPRA es menor o igual a 3 meses antes de la fecha del albarán que lo reactivó.

`cliente.ULTIMA_COMPRA <= DATEADD(month, -3, albclit.dfecalb)`



**Criterio de Reactivación:**

El albarán debe estar dentro del período de análisis especificado por months o between.



**Agrupación:**

Los resultados se agrupan por vendedor (alb.ID_VENDEDOR), contando clientes únicos reactivados.

**Respuesta Exitosa (HTTP 200)**

```json
{
  "response": [
    {
      "sellerId": 5,
      "sellerDescription": "Juan Pérez",
      "reactivatedClients": 15
    },
    {
      "sellerId": 8,
      "sellerDescription": "María González",
      "reactivatedClients": 12
    }
  ],
  "pagination": {
    "total": 50,
    "current": 1,
    "pageSize": 100
  }
}
```



**Campos de Respuesta**

**sellerId**

- Tipo: integer


- Descripción: ID del vendedor



**sellerDescription**

- Tipo: string


- Descripción: Nombre completo del vendedor (apellido + nombre)



**reactivatedClients**

- Tipo: integer


- Descripción: Cantidad de clientes únicos reactivados por el vendedor en el período





**Consulta base.**

```sql
SELECT a.ID_VENDEDOR                     as sellerId,
       CONCAT(a.capeage, ' ', a.cnbrage) as sellerDescription,
       COUNT(DISTINCT alb.ID_CLIENTE)    as reactivatedClients
FROM [NewBytes_DBF].[dbo].[albclit] alb
         INNER JOIN [NewBytes_DBF].[dbo].[clientes] c
                    ON c.ID_CLIENTE = alb.ID_CLIENTE
         INNER JOIN [NewBytes_DBF].[dbo].[agentes] a
                    ON a.ID_VENDEDOR = alb.ID_VENDEDOR
         LEFT JOIN [NewBytes_DBF].[dbo].[albclil] detail
                   ON detail.cnumalb = alb.cnumalb
                       AND detail.cnumsuc = alb.cnumsuc
WHERE
  -- Cliente estaba inactivo
    c.ULTIMA_COMPRA <= DATEADD(month, -3, alb.dfecalb)
  --  período de análisis
  AND alb.dfecalb >= DATEADD(month, -3, GETDATE())

GROUP BY a.ID_VENDEDOR, a.capeage, a.cnbrage
ORDER BY 3 desc
OFFSET 0 ROWS FETCH NEXT 100 ROWS ONLY

```
