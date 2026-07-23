# Módulo Clientes — distribuidores, resellers y contactos

Los "clientes" del ERP son la tabla `clientes`. Históricamente = **distribuidores**; desde 2026-07 se distinguen por **tipo** y se suman **contactos** de resellers. Controllers: `ClienteController`, `ContactoController`, `ImportacionContactosController`.

## Tipos de cliente (`clientes.tipo`)

- Columna `tipo` con default **`distribuidor`** (mig `0021`). En la práctica todo cliente creado por el ERP quedaba como `distribuidor` porque `ClienteController@store` **no valida ni expone `tipo`**.
- Nuevo valor **`reseller`**: lo crean automáticamente el importador de contactos (`firstOrCreate ['nombre','tipo'=>'reseller']`).
- El listado `/clientes` tiene **pestañas** distribuidor / reseller. El botón "Importar contactos" solo aparece en la pestaña reseller.
- Índices `clientes(tipo, pais)` → mig `0050`.

## Contactos (mig `0049`, tabla `contactos`)

- `Contacto`: `cliente_id`, `email` (idempotente por `cliente_id + email`). Modelo + `ContactoResource`.
- CRUD por `apiResource('contactos')`. **Sección propia** en el ERP: `/contactos` (`pages/contactos/index.vue`) + entrada en `utils/secciones.ts` (permiso `VER_SECCION_*`, ver [[permisos-secciones]]).

## Importación de contactos por bloques — `/clientes/importar-contactos`

`ImportacionContactosController` carga un Excel con **bloques de columnas repetidos por país** (estructura del archivo real `files/Emi Calendario.xlsx`, hoja **"LISTA MAILS CLIENTES"**).

- `POST /importaciones-contactos/parsear` → guarda en `storage/local/importaciones_contactos/{uuid}.{ext}`, devuelve headers + filas (preview).
- `POST /importaciones-contactos` → confirma. Cada **bloque** = `{col_cliente, col_mail, pais}` (o `cliente_fijo` para el bloque "Partners NVIDIA", solo mail). Crea clientes `reseller` + contactos.
- **Carry-forward** del nombre de cliente: si la celda CLIENTE viene vacía, reutiliza el último nombre no vacío del bloque (maneja celdas combinadas/agrupadas). Emails inválidos / filas sin cliente → omitidos con motivo.
- UI en 3 pasos: archivo → configurar bloques (dropdowns de columnas + preview de 8 filas) → resultado (creados / ya existían / omitidos). Bloques por defecto calzan con `Emi Calendario.xlsx`.
- **PhpSpreadsheet ya está instalado** en el container (para `.xlsx`); igual hay fallback a CSV. (Contrasta con [[modulos/productos|el importador de catálogo]], donde antes no estaba.)

## Cuenta corriente / línea de crédito / notas de crédito

Cada cliente tiene cuenta corriente, línea de crédito con historial y notas de crédito. Ver [[arquitectura#Módulo Cuenta Corriente|arquitectura]].

## Ver también

- [[modulos/resellers]] — resellers live desde partpicker (distinto: no toca DB)
- [[contexto]] · [[arquitectura]] · [[gigaErp]]
