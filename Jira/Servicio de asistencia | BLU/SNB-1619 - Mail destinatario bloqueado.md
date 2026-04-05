---
jira_key: "SNB-1619"
aliases: ["SNB-1619"]
summary: "Mail destinatario bloqueado"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Pedidos Jira"
created: "2024-03-11 09:39"
updated: "2024-03-19 14:09"
labels: ["blitz_test", "bugfix"]
jira_url: "https://bluinc.atlassian.net/browse/SNB-1619"
---

# SNB-1619: Mail destinatario bloqueado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Pedidos Jira |
| Creado | 2024-03-11 09:39 |
| Actualizado | 2024-03-19 14:09 |
| Etiquetas | blitz_test, bugfix |
| Jira | [SNB-1619](https://bluinc.atlassian.net/browse/SNB-1619) |

## Relaciones

*Sin relaciones*

## Descripcion

Me viene rechazado el mail. Es una cuenta a la que reporto semanalmente una marca:

This is the mail system at host box.lio.red.

I'm sorry to have to inform you that your message could not
be delivered to one or more recipients. It's attached below.

For further assistance, please send mail to postmaster.

If you do so, please include this problem report. You can
delete your own text from the attached returned message.

                   The mail system

<wlin@evga.com>: host d290004a.ess.barracudanetworks.com[209.222.82.253] said:
    550 permanent failure for one or more recipients (wlin@evga.com:blocked)
    (in reply to end of DATA command)


Reporting-MTA: dns; box.lio.red
X-Postfix-Queue-ID: 08FB6120751
X-Postfix-Sender: rfc822; galo@nb.com.ar
Arrival-Date: Mon, 11 Mar 2024 09:34:57 -0300 (-03)

Final-Recipient: rfc822; wlin@evga.com
Original-Recipient: rfc822;wlin@evga.com
Action: failed
Status: 5.0.0
Remote-MTA: dns; d290004a.ess.barracudanetworks.com
Diagnostic-Code: smtp; 550 permanent failure for one or more recipients
    (wlin@evga.com:blocked)

Usuario: galo
