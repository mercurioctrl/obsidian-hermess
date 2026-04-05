---
jira_key: "LIO-34"
aliases: ["LIO-34"]
summary: "API - Feat - Crear formularios de registro especifico para empresas e individuos "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-10 10:26"
updated: "2025-05-15 17:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-34"
---

# LIO-34: API - Feat - Crear formularios de registro especifico para empresas e individuos 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-10 10:26 |
| Actualizado | 2025-05-15 17:13 |
| Etiquetas | ninguna |
| Jira | [LIO-34](https://bluinc.atlassian.net/browse/LIO-34) |

## Relaciones

- **Padre:** [[LIO-11]] Proceso de registro sencillo para los vendedores/Compradores
- **blocks:** [[LIO-36]] APP - Refactor - Desconectar registro del sitio legacy para migrar 
- **relates to:** [[LIO-46]] API - Refactor - Crear formularios de registro especifico para empresas e individuos - Añadir razón social
- **relates to:** [[LIO-354]] API - Oportunidad de mejora - Registro de usuarios -> Acortar nombre de usuario

## Descripcion

Crearemos el recurso necesario para poder utilizar el formulario de registro simplificado 

- [https://beta.vender.libreopcion.com/registro/registroEmpresa](https://beta.vender.libreopcion.com/registro/registroEmpresa)


- [https://beta.vender.libreopcion.com/registro/registroPersona](https://beta.vender.libreopcion.com/registro/registroPersona)


- [link](https://www.libreopcion.com/registro) 



```
POST {{API_URL}}/auth/register
```

Carga util:

```
[
  {
    mail: correo@gmail.com,
    fullName: Nombre completo,
    document: 20-03948576-0,
    password:
  }
]
```

```
SELECT  
      [usuarioID]
      ,[nombre]
      ,[uri]
      ,[email]
      ,[activo]
  FROM [LO].[dbo].[vendedores]
```

```
SELECT TOP (1000) [id]
      ,[activo]
      ,[perfil]
      ,[fechaAlta]
      ,[nombre]
      ,[password]
      ,[correo]
  FROM [LO].[dbo].[usuarios]
```

Se debe validar que no este dado de alta el correo. 

Si es un individuo que el DNI tenga la cantidad correcta de caracteres y no este cargado.

Si es un empresa que el CUIT tenga la cantidad correcta de caracteres y no este cargado.
