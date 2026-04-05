---
jira_key: "LIO-421"
aliases: ["LIO-421"]
summary: "API - Review - Al realizar una preguntas con el modelo deepseek (gpt anda bien) parece estar rompiendo el serializado de la respuesta"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-11 13:02"
updated: "2025-08-12 10:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-421"
---

# LIO-421: API - Review - Al realizar una preguntas con el modelo deepseek (gpt anda bien) parece estar rompiendo el serializado de la respuesta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-11 13:02 |
| Actualizado | 2025-08-12 10:40 |
| Etiquetas | ninguna |
| Jira | [LIO-421](https://bluinc.atlassian.net/browse/LIO-421) |

## Relaciones

- **Padre:** [[LIO-391]] Desarrollos IA para LIO (Aleph)

## Descripcion

[adjunto]
[link](https://gamma.libreopcion.com/procesador-amd-am4-ryzen-5-5600g-P573867?catalogue=1) 

```
curl 'https://gamma.api4.libreopcion.com/v4/aleph/answer' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjI2MTQzOTYsImF1ZCI6IjBmOGY2ZDk4NjhhYTYyYTgxMzVjNTI1MzIxOTcwMDFhMmI3YzU2OWQiLCJ1c2VyIjp7ImlkIjoyLCJlbWFpbCI6Imhlcm1lc3M4N0BnbWFpbC5jb20iLCJub21icmUiOiJDYXRyaWVsIE1lcmN1cmlvIiwicGVyZmlsIjoidmVuZGVkb3IiLCJkb2N1bWVudG8iOiIzMzQ1Nzk2MiIsInRlbGVmb25vIjoiNC02MzYtMzQwNiIsImRpcmVjY2lvbiI6eyJjYWxsZSI6Ik1lZGluYXMiLCJudW1lcm8iOiIzNTEyIiwicGlzbyI6IjEiLCJjYXNhQXB0byI6IjMifSwiY29kaWdvUG9zdGFsIjoiMTQwNyIsImF2YXRhciI6MTgsImNpdWRhZCI6eyJpZCI6MjA4MzIsIm5vbWJyZSI6IkNBQkEiLCJwcm92aW5jaWFJZCI6MX0sInByb3ZpbmNpYSI6eyJpZCI6MSwibm9tYnJlIjoiQ0FCQSIsInBhaXNJZCI6NywiY2l1ZGFkRGVmZWN0b0lkIjoyMDgzMn0sInBhaXMiOnsiaWQiOjcsIm5vbWJyZSI6IkFSR0VOVElOQSJ9LCJ0aWVuZGFJZCI6MjY4MDYsInZlbmRlZG9ySWQiOjIyLCJ0b2tlblYzIjoiZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SjFjM1ZoY21sdklqcDdJbWxrSWpveUxDSmxiV0ZwYkNJNkltaGxjbTFsYzNNNE4wQm5iV0ZwYkM1amIyMGlMQ0p1YjIxaWNtVWlPaUpEWVhSeWFXVnNJRTFsY21OMWNtbHZJaXdpY0dWeVptbHNJam9pZG1WdVpHVmtiM0lpTENKa2IyTjFiV1Z1ZEc4aU9pSXpNelExTnprMk1pSXNJblJsYkdWbWIyNXZJam9pTkMwMk16WXRNelF3TmlJc0ltUnBjbVZqWTJsdmJpSTZleUpqWVd4c1pTSTZJazFsWkdsdVlYTWlMQ0p1ZFcxbGNtOGlPaUl6TlRFeUlpd2ljR2x6YnlJNklqRWlMQ0pqWVhOaFFYQjBieUk2SWpNaWZTd2lZMjlrYVdkdlgzQnZjM1JoYkNJNklqRTBNRGNpTENKaGRtRjBZWElpT2pFNExDSmphWFZrWVdRaU9uc2lhV1FpT2pJd09ETXlMQ0p1YjIxaWNtVWlPaUpEUVVKQklpd2ljSEp2ZG1sdVkybGhYMmxrSWpveExDSjBiM1JoYkNJNk1IMHNJbkJ5YjNacGJtTnBZU0k2ZXlKcFpDSTZNU3dpYTJWNUlqb3hMQ0p1YjIxaWNtVWlPaUpEUVVKQklpd2ljR0ZwYzE5cFpDSTZOeXdpZEc5MFlXd2lPakFzSW1OcGRXUmhaRjlrWldabFkzUnZYMmxrSWpvd2ZTd2ljR0ZwY3lJNmV5SnBaQ0k2Tnl3aWJtOXRZbkpsSWpvaVFWSkhSVTVVU1U1Qklpd2lkRzkwWVd3aU9qQjlMQ0owYVdWdVpHRmZhV1FpT2pJMk9EQTJMQ0oyWlc1a1pXUnZjbDlwWkNJNk1qSXNJblJ2YTJWdVZqUWlPaUpHTXpVMlEwVTNPQzAxUXpjMExUUTFOekl0UWpCRlJDMDVNalpDTWpKQ1FVWTBORUVpTENKamIyUnBaMjlmY0c5emRHRnNYMlJsWm1GMWJIUWlPakUwTURjc0ltRmpkR2wyWlZkaGJHeGxkQ0k2Wm1Gc2MyVjlMQ0pwYzNNaU9pSnNhV0p5Wlc5d1kybHZiaTVqYjIwaUxDSmhkV1FpT2lKc2FXSnlaVzl3WTJsdmJpNWpiMjBpTENKcFlYUWlPakUzTkRrMk5UUXpPVFlzSW01aVppSTZNVGMwT1RZMU5ETTVObjAuaEo5T3htb2gwZVZjRFc2NFVDcFV2OFh0bkgwbHJoUk1neUN2X2U5REQ2QSIsImNvZGlnb1Bvc3RhbERlZmF1bHQiOjE0MDcsImFjdGl2ZVdhbGxldCI6ZmFsc2V9LCJpYXQiOjE3NDk2NTQzOTYsIm5iZiI6MTc0OTY1NDM5Nn0.Y-RXrK_nbDrtZQdDV6VjLs1BaXhXOddNOsye3Rq9bdA' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.libreopcion.com' \
  -H 'Referer: https://gamma.libreopcion.com/procesador-amd-am4-ryzen-5-5600g-P573867?catalogue=1' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"product_id":573867,"question":"es compatible con chipset B450 ?"}'

```

```
{
    "respuesta": "```json\n{\n  \"respuesta\": \"S\u00ed, es compatible con chipset B450.\",\n  \"confidence\": \"high\",\n  \"reliable\": true\n}\n```",
    "confidence": "medium",
    "reliable": true
}
```
