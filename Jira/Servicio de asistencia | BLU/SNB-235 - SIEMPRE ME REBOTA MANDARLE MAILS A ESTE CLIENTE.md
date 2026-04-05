---
jira_key: "SNB-235"
aliases: ["SNB-235"]
summary: "SIEMPRE ME REBOTA MANDARLE MAILS A ESTE CLIENTE"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Andrea  Altamiranda"
created: "2022-08-09 07:49"
updated: "2022-08-11 09:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-235"
---

# SNB-235: SIEMPRE ME REBOTA MANDARLE MAILS A ESTE CLIENTE

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Andrea  Altamiranda |
| Creado | 2022-08-09 07:49 |
| Actualizado | 2022-08-11 09:48 |
| Etiquetas | ninguna |
| Jira | [SNB-235](https://bluinc.atlassian.net/browse/SNB-235) |

## Relaciones

*Sin relaciones*

## Descripcion

```
--------------------------------------------------------------------------
MDaemon Delivery Status Notification - http://www.altn.com/dsn
--------------------------------------------------------------------------

The attached message had TEMPORARY non-fatal delivery errors.

--------------------------------------------------------------------------
THIS IS A WARNING MESSAGE ONLY - YOU DO NOT NEED TO RESEND YOUR MESSAGE
--------------------------------------------------------------------------

MDaemon is configured to automatically retry delivery at configured
intervals.  Subsequent attempts to deliver this message are pending.

Failed address: aablin@tvpublica.com.ar

--- Session Transcript ---
 Tue 2022-08-09 07:47:31: Session 733250; child 0002
 Tue 2022-08-09 07:47:31: Parsing message <xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\pd90001015916.msg>
 Tue 2022-08-09 07:47:31: *  From: aaltamiranda@nb.com.ar
 Tue 2022-08-09 07:47:31: *  To: aablin@tvpublica.com.ar
 Tue 2022-08-09 07:47:31: *  Subject: DISCO NAS
 Tue 2022-08-09 07:47:31: *  Size (bytes): 8303
 Tue 2022-08-09 07:47:31: *  Message-ID: <1e8f77fc-2276-b80e-1ad5-18381c52d093@nb.com.ar>
 Tue 2022-08-09 07:47:31: Attempting SMTP connection to [tvpublica.com.ar]
 Tue 2022-08-09 07:47:31: Resolving MX records for [tvpublica.com.ar] (DNS Server: 190.2.57.1)...
 Tue 2022-08-09 07:47:31: *  P=010 S=000 D=tvpublica.com.ar TTL=(60) MX=[host213.181-15-247.tvpublica.com.ar]
 Tue 2022-08-09 07:47:31: Attempting SMTP connection to [host213.181-15-247.tvpublica.com.ar:25]
 Tue 2022-08-09 07:47:31: Resolving A record for [host213.181-15-247.tvpublica.com.ar] (DNS Server: 190.2.57.1)...
 Tue 2022-08-09 07:47:31: *  D=host213.181-15-247.tvpublica.com.ar TTL=(60) A=[181.15.247.213]
 Tue 2022-08-09 07:47:31: Attempting SMTP connection to [181.15.247.213:25]
 Tue 2022-08-09 07:47:31: Waiting for socket connection...
 Tue 2022-08-09 07:47:31: *  Connection established (192.168.0.15:60296 -> 181.15.247.213:25)
 Tue 2022-08-09 07:47:31: Waiting for protocol to start...
 Tue 2022-08-09 07:47:32: <-- 220 proxmoxmail.rtanet.com.ar Correo
 Tue 2022-08-09 07:47:32: --> EHLO new-bytes.local
 Tue 2022-08-09 07:47:32: <-- 250-proxmoxmail.rtanet.com.ar
 Tue 2022-08-09 07:47:32: <-- 250-PIPELINING
 Tue 2022-08-09 07:47:32: <-- 250-SIZE 20485760
 Tue 2022-08-09 07:47:32: <-- 250-VRFY
 Tue 2022-08-09 07:47:32: <-- 250-ETRN
 Tue 2022-08-09 07:47:32: <-- 250-ENHANCEDSTATUSCODES
 Tue 2022-08-09 07:47:32: <-- 250-8BITMIME
 Tue 2022-08-09 07:47:32: <-- 250-SMTPUTF8
 Tue 2022-08-09 07:47:32: <-- 250 CHUNKING
 Tue 2022-08-09 07:47:32: --> MAIL From:<aaltamiranda@nb.com.ar> SIZE=8303
 Tue 2022-08-09 07:47:32: <-- 250 2.1.0 Ok
 Tue 2022-08-09 07:47:32: --> RCPT To:<aablin@tvpublica.com.ar>
 Tue 2022-08-09 07:47:32: <-- 450 4.7.25 Client host rejected: cannot find your hostname, [190.104.194.67]
 Tue 2022-08-09 07:47:32: --> QUIT
 Tue 2022-08-09 07:47:32: <-- 221 2.0.0 Bye
 Tue 2022-08-09 07:47:32: This message is 0 days old; it has 2 days left to get delivered
--- End Transcript ---

```
