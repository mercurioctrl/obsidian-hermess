---
jira_key: "STASK-10"
aliases: ["STASK-10"]
summary: "API - Refactor - Correo \"ya disponible para retirar\" en pedidods pickUp autorizados"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-07 09:28"
updated: "2025-02-20 15:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-10"
---

# STASK-10: API - Refactor - Correo "ya disponible para retirar" en pedidods pickUp autorizados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-07 09:28 |
| Actualizado | 2025-02-20 15:28 |
| Etiquetas | ninguna |
| Jira | [STASK-10](https://bluinc.atlassian.net/browse/STASK-10) |

## Relaciones

- **Padre:** [[STASK-2]] Correos

## Descripcion

Lo que necesitamos es enviar un correo para los pedidos pickUp (retiros) una vez que los mismos ya están autorizados para notificar al cliente que ya puede retirarlo.

```
POST {API_URL}/v3/authorizedPickUpSentEmail
```

Para esto es posible que necesitemos crear una tabla que nos permita entender para que pedidos ya fue enviado el correo.. podríamos hacer algo como esto

```
SELECT TOP (1000) [id]
      ,[order]
      ,[branch]
      ,[clientId]
      ,[emailDestination]
      ,[sendEmail]
      ,[createdAt]
      ,[updatedAt]
  [NewBytes_DBF].[dbo].[authorizedPickUpSentEmail]
```

Para esto debemos tomar todos los pedidos **que son para retiro pickUp o en sucursal y tienen statusId ([NEW_BYTES].[dbo].[MS_VENTAS_REMITOS]) en cualquiera de los siguientes estados**

```
2 - Autorizados. Pendiente a despachar
4 - Armado Finalizado
11 - Serializado
10 - Parcialmente Serializado
```

## ¿De donde obtenemos los correo de destino?

Debemos enviarlo tanto al cliente, como a su vendedor para esto obtendremos los siguientes correos:

```
SELECT email, UserEmail, A.cemail
  FROM [NewBytes_DBF].[dbo].[clientes] C
  LEFT JOIN NB_WEB.dbo.usuarios_nb U ON U.codigoFP = C.ID_CLIENTE
  LEFT JOIN NewBytes_DBF.dbo.agentes A ON A.ID_VENDEDOR = C.ID_VENDEDOR
WHERE ID_CLIENTE = 31670
```

En principio serian como minimo esos tres:

Correo del cliente

Correo del usuario (a menos que estos primeros dos sean iguales)

Y el del vendedor

## Plantilla de envío de correo

**Asunto: **El pedido de RED EL THEAM SA (0002-10390710) ya se puede retirar

[adjunto]
Código de la plantilla (Como seguro la utilizaremos para varias coses, si aun no esta en este código, estaría bueno dejarla disponible para inyectarte cuerpo, titulo y demás):

```
<table align="center" cellpadding="0" cellspacing="0" width="600">
    <tbody>
        <tr>
            <td>
                <a href="https://www.nb.com.ar" style="outline: none; border: none" target="_blank"
                    rel="noreferrer"><img src="https://static.nb.com.ar/img/c91acf5da7caa25d791df1b87fdfa57d.jpg"
                        style="display: block; outline: none; border: none; width: 600px; height: 75px"
                        class="v1CToWUd"></a>
            </td>
        </tr>
        <tr>
            <td style="font-size: small; padding: 20px 10px 0px 10px; font-family: sans-serif">

                <table width="100%" cellspacing="0" cellpadding="0" border="0"
                    style="padding: 0 20px 0 0; text-align: center">
                    <tbody>
                        <tr>
                            <td style="font-family: Arial; font-size: 20px; color: #184bb5; font-weight: BOLD">El pedido
                                0002-10390710 ya se puede retirar</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td>

                <table width="100%" cellspacing="0" cellpadding="0" border="0" style="padding: 0 20px 0 0">
                    <tbody>
                        <tr>
                            <td height="15" style="font-size: 1px">&nbsp;</td>
                        </tr>
                        <tr>
                            <td height="25" style="font-size: 1px">
                                <hr style="border-top: dotted 1px #ccc; border-bottom: none">
                            </td>
                        </tr>
                        <tr>
                            <td height="15" style="font-size: 1px">&nbsp;</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td
                style="font-family: Arial; font-size: 14px; color: #666666; padding-bottom: 10px; line-height: 1.4; text-align: center">
                Ya fue auotorizado para su retiro por parte del cliente RED EL THEAM SA

            </td>
        </tr>



        <tr>
            <td>

                <table width="100%" cellspacing="0" cellpadding="0" border="0">
                    <tbody>
                        <tr>
                            <td
                                style="font-family: Arial;font-size: 14px;color: #666666;padding-bottom: 10px;line-height: 1.4;text-align: center;padding-top: 53px;">
                                Palabra clave:</td>
                        </tr>
                        <tr style="text-align: center">
                            <td
                                style="font-family: Arial; font-size: 18px; color: #184bb5; font-weight: normal; padding-bottom: 3px; line-height: 1.4">
                                ALMENDRA</td>
                        </tr>
                        <tr>
                            <td
                                style="font-family: Arial; font-size: 14px; color: #666666; padding-bottom: 10px; line-height: 1.4; text-align: center">
                                Utiliza la palabra clave para retirar/recibir tu compra.</td>
                        </tr>
                        <tr>

                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td>

                <table width="100%" cellspacing="0" cellpadding="0" border="0" style="padding: 0 20px 0 0">
                    <tbody>
                        <tr>
                            <td height="15" style="font-size: 1px">&nbsp;</td>
                        </tr>
                        <tr>
                            <td height="25" style="font-size: 1px">
                                <hr style="border-top: dotted 1px #ccc; border-bottom: none">
                            </td>
                        </tr>
                        <tr>
                            <td height="15" style="font-size: 1px">&nbsp;</td>
                        </tr>
                    </tbody>
                </table>

                <table width="100%" cellspacing="0" cellpadding="0" border="0" style="padding: 0 20px 0 0">
                    <tbody>
                        <tr>
                            <td height="25"
                                style="font-size: 11px; color: #999999; font-family: Arial; text-transform: uppercase; text-align: CENTER">
                                Av. Jujuy 1039 CABA C1229ABF | 4011-8800 | <a href="#v1">nb.com.ar</a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>
```
