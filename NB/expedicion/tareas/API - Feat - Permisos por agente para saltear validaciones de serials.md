# API - Feat - Permisos por agente para saltear validaciones de serials

**Proyecto:** [[NB/expedicion/expedicion|Expedición]]
**Estado:** Pendiente
**Fecha:** 2026-04-06

---

## Descripción

Crear 3 permisos en la tabla `permisos_agente` que permitan a un agente/usuario saltear las validaciones de producto al cargar serials en órdenes de proveedores:

1. **Saltear validación de barcode** (ean, upc, isbn, gtin)
2. **Saltear validación de medidas** (weightAverage, lengthAverage, widthAverage, highAverage)
3. **Saltear validación de unidades por paquete** (packagePerUnit / PPU)

### Comportamiento actual

- `VALIDATE_MEASURES` (.env) → controla validación de medidas
- `VALIDATE_PACKAGEPERUNIT` (.env) → controla validación de PPU
- `hasBarcode` → **siempre se ejecuta**, no tiene toggle

### Comportamiento esperado

- Los flags de `.env` siguen funcionando como **fallback global** (si `.env` dice `false`, no se valida para nadie)
- Si `.env` dice `true` (o no está definido), se validan las 3 cosas **excepto** si el agente tiene el permiso correspondiente en `permisos_agente`
- Es decir: el permiso por agente **pisa** la configuración del `.env` cuando el agente lo tiene asignado

### Lógica de prioridad

```
Si .env = false → NO validar (para todos)
Si .env = true (o default):
    Si agente tiene permiso → NO validar (solo para ese agente)
    Si agente NO tiene permiso → VALIDAR
```

## Criterios de aceptación

- [ ] Crear 3 registros de permisos nuevos en la tabla `permisos_agente` (o migración)
- [ ] Modificar `ProvidersOrderSerial.php` para consultar permisos del agente antes de validar
- [ ] Si el agente tiene permiso de saltear barcode → no ejecutar `hasBarcode`
- [ ] Si el agente tiene permiso de saltear medidas → no ejecutar `hasMeasures` (independiente del .env)
- [ ] Si el agente tiene permiso de saltear PPU → no ejecutar `hasPpu` (independiente del .env)
- [ ] Los flags de `.env` siguen funcionando como fallback global
- [ ] No romper el flujo actual para agentes sin permisos especiales

## Notas técnicas

### Archivos involucrados

- `api-rest-expedicion/app/src/Controller/Providers/ProvidersOrderSerial.php` (líneas 42-61) — lógica principal de validación
- `api-rest-expedicion/app/src/Service/Providers/ProvidersService.php` — `hasBarcode()` (L291), `hasMeasures()` (L310), `hasPpu()`
- `api-rest-expedicion/app/src/Repository/Providers/ProvidersRepository.php` — queries SQL Server

### Validaciones actuales

| Validación | Qué revisa | Tabla |
|---|---|---|
| `hasBarcode` | ean, upc, isbn, gtin ≠ null (al menos 1) | `[NewBytes_DBF].[dbo].[articulo]` |
| `hasMeasures` | weightAverage, lengthAverage, widthAverage, highAverage ≠ null | `[NewBytes_DBF].[dbo].[articulo]` |
| `hasPpu` | packagePerUnit ≠ null | `[NewBytes_DBF].[dbo].[articulo]` |

### Consideraciones

- Obtener el agente/usuario desde el request (middleware de auth o token)
- Consultar `permisos_agente` para ese usuario y verificar si tiene los permisos de bypass
- Posiblemente crear un servicio o método que encapsule la consulta de permisos

## Ver también

- [[NB/expedicion/arquitectura|Arquitectura]]
- [[NB/expedicion/documentacion|Documentación]]
