# Portal NBE

Portal B2B de autogestión para clientes mayoristas de **NB Electric (NBE)**, construido sobre la
API REST existente del grupo New Bytes. Reemplaza el pedido por WhatsApp/teléfono: el cliente
entra, ve su lista de precios con su bonificación, arma el pedido y lo confirma él mismo.

**Repo:** [New-Bytes/nbelectric-portal](https://github.com/New-Bytes/nbelectric-portal) (privado) — local en `~/portalNBE`
**Backend:** [New-Bytes/sitio-api-rest-v3](https://github.com/New-Bytes/sitio-api-rest-v3) — clonado en la carpeta, **fuera** de este repo
**API:** `https://api.nbe.com.ar/v1` (companyCode 9)
**Local:** `cd portal && npm run dev -- --port 3400`

## Notas

- [[stack|Stack y dependencias]]
- [[arquitectura|Arquitectura y patrones]]
- [[api-nbe|La API: endpoints y trampas]]
- [[contexto|Contexto y decisiones]]
- [[configuracion|Configuración: entorno, secciones, empresa]]
- [[marca|Marca: logo, paleta, tipografía]]
- [[estado|Estado: hecho, pendiente, bloqueado]]
- [[changelog|Changelog]]
- [[memoria|Memoria del proyecto]]

## En una línea

Login → catálogo con precios propios → carrito persistente → checkout con OC y cotización de
envío → seguimiento del pedido línea por línea. Más lista de precios con export, comprobantes,
compras frecuentes, sub-usuarios, direcciones y postventa de consulta.

## Riesgo abierto

`PedidoRepository::create()` de la API tiene almacén y sucursal **hardcodeados en 2 / '0002'**,
que son los de NB. El depósito de NBE es el 8. Verificar antes del primer pedido real — ver
[[estado#Bloqueado por backend]].

---
Última sincronización: 2026-09-05
