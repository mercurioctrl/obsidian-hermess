---
jira_key: "PEGA-58"
aliases: ["PEGA-58"]
summary: "APP - Review - Revisar porque no puede compilar en remote gamma"
status: "Gamma"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-01-17 07:43"
updated: "2023-01-31 16:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-58"
---

# PEGA-58: APP - Review - Revisar porque no puede compilar en remote gamma

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-17 07:43 |
| Actualizado | 2023-01-31 16:46 |
| Etiquetas | ninguna |
| Jira | [PEGA-58](https://bluinc.atlassian.net/browse/PEGA-58) |

## Relaciones

- **Padre:** [[PEGA-1]] Bases y repositorios

## Descripcion

Haciendo uso de las credenciales ssh se debe verificar el error que arroja al intentar ejecutar el comando ‘npm ci’

Para llegar hasta el directorio, una vez dentro del directorio se debe dirigir a

```
cd /var/www/gamma_pega/precios-gamer-v1-web-app/app/
```

Se debe mantener el puerto `2536`

El mismo ya esta vinculado a la URL [https://gamma.preciosgamer.com](https://gamma.preciosgamer.com)



El error que estoy recibiendo es el siguiente:

```
npm ERR! code 1
npm ERR! path /var/www/pega/precios-gamer-v1-web-app/app/node_modules/sharp
npm ERR! command failed
npm ERR! command sh -c (node install/libvips && node install/dll-copy && prebuild-install) || (node install/can-compile && node-gyp rebuild && node install/dll-copy)
npm ERR! sharp: Please see https://sharp.pixelplumbing.com/install for required dependencies
npm ERR! sharp: Installation error: Expected Node.js version >=14.15.0 but found 12.22.5

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/hermess/.npm/_logs/2023-01-23T10_02_42_113Z-debug.log
```
