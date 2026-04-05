# Stack — Expedición

Tecnologías, versiones y dependencias clave del proyecto.

---

## Backend (api-rest-expedicion)

### Runtime
| Tecnología | Versión | Notas |
|-----------|---------|-------|
| PHP | 8.3 | Actualizado desde 8.0 (2026-04-05) |
| Apache | 2.4 | mod_rewrite, mpm_prefork |
| Docker | Ubuntu 22.04 | Actualizado desde 18.04 |
| Composer | 2.x | Package manager |

### Framework y librerías
| Dependencia | Versión | Uso |
|------------|---------|-----|
| slim/slim | 4.x | Micro-framework REST |
| pimple/pimple | 3.4 | Contenedor de DI |
| firebase/php-jwt | 5.3 | Generación/validación JWT |
| vlucas/phpdotenv | 5.3 | Variables de entorno |
| phpmailer/phpmailer | 6.6 | Envío de emails |
| phpoffice/phpspreadsheet | 1.23 | Exportación Excel |
| picqer/php-barcode-generator | 2.2 | Generación de códigos de barras |
| monolog/monolog | 2.2 | Logging estructurado |
| mercadopago/dx-php | 2.4 | Integración Mercado Pago |
| robmorgan/phinx | 0.12.7 | Migraciones de DB |

### Base de datos
| Tecnología | Versión | Notas |
|-----------|---------|-------|
| SQL Server | — | Remoto (190.210.23.108:1433) |
| ODBC Driver | 18 | ARM64, con OpenSSL SECLEVEL=0 |
| pdo_sqlsrv | PECL latest | Extensión PHP para SQL Server |
| Bases | NB_WEB, NEW_BYTES, NewBytes_DBF | Cross-database JOINs |

---

## Frontend (expedicion-web-app-v1)

### Runtime
| Tecnología | Versión | Notas |
|-----------|---------|-------|
| Node.js | 18+ | v25 requiere `--openssl-legacy-provider` |
| npm | 8+ | Package manager |
| PM2 | — | Process manager producción (cluster mode) |

### Framework y librerías
| Dependencia | Versión | Uso |
|------------|---------|-----|
| nuxt | 2.15.8 | Framework SSR/SPA |
| vue | 2.6.14 | Framework reactivo |
| ant-design-vue | 1.7.8 | Componentes UI |
| @nuxtjs/auth-next | 5.x | Autenticación JWT |
| @nuxtjs/axios | 5.13.6 | Cliente HTTP |
| vee-validate | 3.4.14 | Validación de formularios |
| chart.js | 3.8.0 | Gráficos dashboard |
| vue-chartjs | 4.1.1 | Wrapper Vue para Chart.js |
| firebase | 11.0.1 | Push notifications |
| v-mask | 2.3.0 | Máscaras de input |
| format-number | 3.0.0 | Formateo numérico (locale español) |
| @nuxtjs/moment | — | Fechas (locale español) |
| less | 4.1.3 | Preprocesador CSS |
| @nuxtjs/pwa | 3.3.5 | Soporte PWA (workbox disabled) |

### Linting y calidad
| Herramienta | Uso |
|------------|-----|
| eslint + eslint-plugin-vue | Linting JS/Vue |
| stylelint | Linting CSS/LESS |
| prettier | Formateo de código |
| commitlint | Conventional Commits |
| lint-staged | Pre-commit hooks |

---

## Servicios externos

| Servicio | URL base | Uso |
|---------|----------|-----|
| MS Envíos | `omega.ms-envio.lio.red` | Tracking, etiquetas ZPL, cotizaciones |
| MS Comprobantes | `comprobantes.lio.red` | Facturación, tipos de voucher, padrón AFIP |
| Postventa | `api.aftersale.lio.red` | Info de seriales, procesamiento de pases |
| Jira Support | `gamma.api.support.lio.red` | Reportes de soporte |
| Static CDN | `static.nb.com.ar` | Imágenes de productos |
| Firebase | Google FCM | Push notifications |

---

## Infraestructura

| Componente | Entorno | URL/Host |
|-----------|---------|----------|
| API (dev) | Local Docker | `localhost:8084/v1` |
| Frontend (dev) | Local Node | `localhost:4149` |
| API (gamma) | Staging | `api.warehouse.lio.red/v1` |
| API (prod) | Producción | `api2.warehouse.lio.red/v1` |
| SQL Server | Remoto | `190.210.23.108:1433` |

### CI/CD
- GitHub Actions: deploy automático a Gamma al mergear PR
- Post-deploy: PR automático Gamma → Development + Slack notification

---

## Ver también

- [[NB/expedicion/arquitectura|Arquitectura]] — Cómo se conectan estos componentes
- [[NB/expedicion/documentacion|Documentación]] — Setup y comandos
- [[NB/expedicion/contexto|Contexto]] — Visión general del proyecto
