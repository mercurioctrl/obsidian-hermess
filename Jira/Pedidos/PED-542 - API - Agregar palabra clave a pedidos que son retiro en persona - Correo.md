---
jira_key: "PED-542"
aliases: ["PED-542"]
summary: "API - Agregar palabra clave a pedidos que son retiro en persona - Correo inválido "
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-02-07 16:31"
updated: "2024-02-14 15:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-542"
---

# PED-542: API - Agregar palabra clave a pedidos que son retiro en persona - Correo inválido 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-07 16:31 |
| Actualizado | 2024-02-14 15:21 |
| Etiquetas | ninguna |
| Jira | [PED-542](https://bluinc.atlassian.net/browse/PED-542) |

## Relaciones

- **Padre:** [[PED-469]] SyncUps e Importaciones
- **blocks:** [[PED-515]] API - Feat - Agregar palabra clave de retiro al recorrer aquellos pedidos que son Retiro en persona y no lo tienen

## Descripcion

Al ejecutar la sincronización de confirmación de compra, surge un error indicando que el mensaje no puede ser enviado debido a que el correo es inválido.

```
{{API_URL}}/v1/syncUp/purchaseConfirmation
```

[adjunto]
Dato extra:
Esto podría deberse a que el sistema está buscando el correo en la tabla `NB_WEB.dbo.usuarios_nb`, sin embargo, se trata de un cliente que no tiene un usuario en NB. El correo se encuentra en la tabla `NewBytes_DBF.dbo.clientes.email`.Sería bueno considerar el caso.

---

Actualización 09/02/24
El correo llega correctamente, lo único que note es que no se está registrando el correo del destinatario en la base de datos

[adjunto]
Dato extra:

Esto puede deberse a que al momento de llamar el método que realiza la actualización del registro, no se le está enviando el email actualizado

```
$email = $userData->email_user ?? $userData->email_client;
$sent = $this->logSendEmail($order, $userData, $privateKey);
```
