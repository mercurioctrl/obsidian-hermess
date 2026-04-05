---
jira_key: "PED-889"
aliases: ["PED-889"]
summary: "API - SYNCUP - Enviar aviso con clientes que serán liberados el viernes (10 dias despues) cuando no tengan compras en los ultimos 180 dias"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-28 13:18"
updated: "2024-12-02 17:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-889"
---

# PED-889: API - SYNCUP - Enviar aviso con clientes que serán liberados el viernes (10 dias despues) cuando no tengan compras en los ultimos 180 dias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-28 13:18 |
| Actualizado | 2024-12-02 17:28 |
| Etiquetas | ninguna |
| Jira | [PED-889](https://bluinc.atlassian.net/browse/PED-889) |

## Relaciones

- **Padre:** [[PED-888]] Liberación de clientes automatica

## Descripcion

```
POST {{API_URL}}/v1/syncUp/inactiveClientNoticeSeller
```

```
{
  token: {token}
}
```

### **Lógica para el recurso de aviso**

#### **Query para asociar clientes con vendedores**

Si los clientes están vinculados a vendedores mediante una columna como `ID_VENDEDOR`:

```sql
SELECT 
c.ID_CLIENTE, c.ULTIMA_COMPRA, c.ID_VENDEDOR, v.EMAIL 
FROM [NewBytes_DBF].[dbo].[clientes] c 
JOIN [NewBytes_DBF].[dbo].[agentes] v 
ON c.ID_VENDEDOR = v.ID_VENDEDOR WHERE c.ULTIMA_COMPRA < DATEADD(DAY, -180, GETDATE()) 
ORDER BY c.ULTIMA_COMPRA DESC;
```

#### **Pasos en el Backend:**

- Ejecutar la consulta para obtener clientes inactivos y sus vendedores.


- Agrupar los clientes por vendedor (`ID_VENDEDOR`).


- Enviar un correo a cada vendedor con la lista de sus clientes inactivos.



### **Mensaje a enviar**

Asunto: 

```
✨ ¡Recupera a tus clientes inactivos y mantén su asignación contigo! 🚀
```

Enviaremos un mensaje del siguiente tipo

```
Hola [Nombre del Vendedor],

Queremos informarte que algunos de tus clientes asignados no han realizado compras en los últimos 180 días. Para garantizar que nuestros clientes reciban siempre el mejor servicio, existe una política de rotación que permite que estos clientes puedan ser reasignados en caso de inactividad.

💡 ¡Aún estás a tiempo!
Tienes 10 días para reactivar la relación con estos clientes y lograr una venta. Si logras una compra durante este período, el cliente seguirá asignado a ti.

Aquí tienes la lista de clientes asignados que están inactivos:

[Nombre del Cliente 1] – Última compra: [Fecha Última Compra]
[Nombre del Cliente 2] – Última compra: [Fecha Última Compra]
...
👉 Te invitamos a contactarlos, ofrecerles tus mejores productos o servicios, y ayudarlos a realizar una nueva compra.

⏰ Recuerda: Tienes hasta el [Fecha límite] para evitar la rotación de estos clientes.

Si necesitas apoyo o tienes alguna duda, estamos aquí para ayudarte. Escríbenos a [email de soporte] o contáctanos directamente.

¡Confiamos en tu capacidad para conectar con ellos y lograr grandes resultados! 💪

```
