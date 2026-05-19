# Stack — CashBox Cobros

## Backend (`api-rest-cobros`)
| Tecnología | Versión | Uso |
|---|---|---|
| PHP | 8.2 | Runtime |
| Slim 4 | ^4.x | Framework HTTP |
| Pimple | ^3.x | DI Container |
| pdo_sqlsrv | latest | Driver SQL Server |
| ODBC Driver 18 | 18.x | Microsoft SQL Server |
| Monolog | ^2.x | Logging |
| Firebase JWT | ^6.x | Auth tokens |
| PHPSpreadsheet | ^1.x | Export Excel |
| Phinx | ^0.12 | Migraciones DB |
| PHPUnit | ^9.x | Testing |

## Frontend (`cobros-web-app-v1`)
| Tecnología | Versión | Uso |
|---|---|---|
| Nuxt | 2.x | SSR framework |
| Vue | 2.x | UI framework |
| Ant Design Vue | 1.x | Componentes UI |
| Vuex | 3.x | Estado global |
| @nuxtjs/axios | latest | HTTP client |
| @nuxtjs/auth-next | latest | Autenticación JWT |
| vee-validate | 3.x | Validación de formularios |
| chart.js | 3.x | Gráficos |
| LESS | — | Estilos |
| ESLint + Prettier | — | Linting |
| PM2 | — | Process manager (cluster mode) |
| Node | 18.x | Runtime (con --openssl-legacy-provider) |

## Infraestructura
| Servicio | Descripción |
|---|---|
| SQL Server | BD principal (cross-database: NB_WEB, NEW_BYTES, NewBytes_DBF) |
| Docker | Dev environment del backend |
| GitHub | New-Bytes/api-rest-cobros + New-Bytes/cobros-web-app-v1 |

## URLs producción
- Frontend: `https://caja.saftel.com`
- Backend API: `https://api.cashbox.lio.red/v1`

## Ver también
- [[arquitectura]] · [[contexto]]
