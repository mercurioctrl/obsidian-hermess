---
jira_key: "SNB-3652"
aliases: ["SNB-3652"]
summary: "LO - Referidos -> Error al intentar registrar un referido"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2026-02-03 16:46"
updated: "2026-02-03 17:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3652"
---

# SNB-3652: LO - Referidos -> Error al intentar registrar un referido

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2026-02-03 16:46 |
| Actualizado | 2026-02-03 17:13 |
| Etiquetas | ninguna |
| Jira | [SNB-3652](https://bluinc.atlassian.net/browse/SNB-3652) |

## Relaciones

- **duplicates:** [[SNB-3651 - Error en los referidos BitBayres|SNB-3651]] Error en los referidos BitBayres

## Descripcion

[adjunto]
[adjunto]
```
curl.exe ^"https://omega-api4.libreopcion.com.ar/v4/referrals/receive^" ^
  -X POST ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3ODMxMDc1NzMsImF1ZCI6IjYzNzhhMGUxZDkyMTEyZWFkNjE1ZjY1OGM0Mzk4ZTZhMmRmZGQyZmMiLCJ1c2VyIjp7ImlkIjoyNzQ5NTgsImVtYWlsIjoiZ2F2aWxhLm5ld2J5dGVzQGdtYWlsLmNvbSIsIm5vbWJyZSI6IkdwcnVlYmEgUHJvZHVjY2lcdTAwZjNuIExPIiwicGVyZmlsIjoidmVuZGVkb3IiLCJkb2N1bWVudG8iOiIzMi40MjQuMzIxIiwidGVsZWZvbm8iOiI5MTEyMzQ1Njc4OSIsImRpcmVjY2lvbiI6eyJjYWxsZSI6IkxvbWJhcmRpYSIsIm51bWVybyI6Ik11eSBhbHRvIiwicGlzbyI6IjIyIiwiY2FzYUFwdG8iOiJEcHRvIn0sImNvZGlnb1Bvc3RhbCI6IjIxMDAiLCJhdmF0YXIiOjAsImNpdWRhZCI6eyJpZCI6MSwibm9tYnJlIjoiQS4gQS4gRkVSTkFOREVaICAgICAgICAgICAgICAgIiwicHJvdmluY2lhSWQiOjJ9LCJwcm92aW5jaWEiOnsiaWQiOjIsIm5vbWJyZSI6IkJVRU5PUyBBSVJFUyIsInBhaXNJZCI6NywiY2l1ZGFkRGVmZWN0b0lkIjoxfSwicGFpcyI6eyJpZCI6Nywibm9tYnJlIjoiQVJHRU5USU5BIn0sInRpZW5kYUlkIjowLCJ2ZW5kZWRvcklkIjoyNDMyMzQsInRva2VuVjMiOiJleUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpJVXpJMU5pSjkuZXlKMWMzVmhjbWx2SWpwN0ltbGtJam95TnpRNU5UZ3NJbVZ0WVdsc0lqb2laMkYyYVd4aExtNWxkMko1ZEdWelFHZHRZV2xzTG1OdmJTSXNJbTV2YldKeVpTSTZJa2R3Y25WbFltRWdVSEp2WkhWalkybGNkVEF3WmpOdUlFeFBJaXdpY0dWeVptbHNJam9pZG1WdVpHVmtiM0lpTENKa2IyTjFiV1Z1ZEc4aU9pSXpNaTQwTWpRdU16SXhJaXdpZEdWc1pXWnZibThpT2lJNU1URXlNelExTmpjNE9TSXNJbVJwY21WalkybHZiaUk2ZXlKallXeHNaU0k2SWt4dmJXSmhjbVJwWVNJc0ltNTFiV1Z5YnlJNklrMTFlU0JoYkhSdklpd2ljR2x6YnlJNklqSXlJaXdpWTJGellVRndkRzhpT2lKRWNIUnZJbjBzSW1OdlpHbG5iMTl3YjNOMFlXd2lPaUl5TVRBd0lpd2lZWFpoZEdGeUlqb3dMQ0pqYVhWa1lXUWlPbnNpYVdRaU9qRXNJbTV2YldKeVpTSTZJa0V1SUVFdUlFWkZVazVCVGtSRldpSXNJbkJ5YjNacGJtTnBZVjlwWkNJNk1pd2lkRzkwWVd3aU9qQjlMQ0p3Y205MmFXNWphV0VpT25zaWFXUWlPaklzSW10bGVTSTZNaXdpYm05dFluSmxJam9pUWxWRlRrOVRJRUZKVWtWVElpd2ljR0ZwYzE5cFpDSTZOeXdpZEc5MFlXd2lPakFzSW1OcGRXUmhaRjlrWldabFkzUnZYMmxrSWpvd2ZTd2ljR0ZwY3lJNmV5SnBaQ0k2Tnl3aWJtOXRZbkpsSWpvaVFWSkhSVTVVU1U1Qklpd2lkRzkwWVd3aU9qQjlMQ0owYVdWdVpHRmZhV1FpT2pBc0luWmxibVJsWkc5eVgybGtJam95TkRNeU16UXNJblJ2YTJWdVZqUWlPaUkxTURsRU5EZzVPUzB6TWtVeExUUTBNemd0T1VWR1FpMURSVVE1T0VNMFJERkJPRE1pTENKamIyUnBaMjlmY0c5emRHRnNYMlJsWm1GMWJIUWlPbTUxYkd3c0ltRmpkR2wyWlZkaGJHeGxkQ0k2Wm1Gc2MyVjlMQ0pwYzNNaU9pSnNhV0p5Wlc5d1kybHZiaTVqYjIwaUxDSmhkV1FpT2lKc2FXSnlaVzl3WTJsdmJpNWpiMjBpTENKcFlYUWlPakUzTnpBeE5EYzFOek1zSW01aVppSTZNVGMzTURFME56VTNNMzAuMV9uSXhCdGdLcVkwS0lnWm9lRzU1YUpDaVhYTWdvOVlQakY2b19MZnhqcyIsImNvZGlnb1Bvc3RhbERlZmF1bHQiOjAsImFjdGl2ZVdhbGxldCI6ZmFsc2V9LCJpYXQiOjE3NzAxNDc1NzMsIm5iZiI6MTc3MDE0NzU3M30.Ky78Hg8HOEGPI84TB0RulhbjAN5Pp1sTBMTbwNxw-n4^" ^
  -H ^"Content-Type: application/json^" ^
  -H ^"Origin: https://libreopcion.com.ar^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://libreopcion.com.ar/^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-site^" ^
  --data-raw ^"^{^\^"referalToken^\^":^\^"GtokenQA2^\^"^}^"
```
