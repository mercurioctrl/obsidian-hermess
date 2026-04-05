---
jira_key: "BLUWEB-25"
summary: "API - Feat - Agregar objeto users para consultar informacion del usuario logueado"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-14 13:08"
updated: "2025-05-16 17:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-25"
---

# BLUWEB-25: API - Feat - Agregar objeto users para consultar informacion del usuario logueado

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-14 13:08 |
| Actualizado | 2025-05-16 17:11 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-25](https://bluinc.atlassian.net/browse/BLUWEB-25) |

## Descripción

```
GET {API_URL}/user
```

```
{
  "id": 1,
  "first_name": "Juan",
  "last_name": "Pérez",
  "email": "juan@example.com",
  "role": "staff",
  "job_title": "Ventas",
  "phone": "1123456789",
  "whatsapp": "1123456789",
  "cbu": "2850590940090412345671",
  "alias": "juan.cuenta.banco",
  "status": "active"
}

```

### Response 401 – Token inválido o ausente

```
{
  "error": "Unauthenticated"
}
```

### Criterios de aceptación

- El endpoint `GET /user` responde solo si el token es válido


- La respuesta incluye todos los campos visibles del usuario


- El usuario debe estar `active`, de lo contrario devuelve 403


- El endpoint es usable desde el frontend para obtener datos del perfil actual
