# Kanban – Catriel (General)

## Por hacer
- Responderle a [[Ana]] (Anabel) el formulario sobre su música: https://forms.gle/kfmR3MhrWDV3mgED9
- Daily: Preguntarle a [[Ezequiel Manzano|Ezequiel]] "cómo descargo las facturas de facturu".
- Revisar errores de carga FC Solytec 49503 (Carla Carpinteri - NB): ![[captura_nb_1.jpg]] ![[captura_nb_2.jpg]] [[factura_solytec_nb.pdf]]
  - No trae percepciones (AFIP no las levanta, exige PDF físico).
  - IVA precargado en 10% en lugar de 10,5%.
  - Falla al aplicar descuento del 5% (da error por total distinto). Nota: Si se cambia manual el IVA a 10,5% el IVA da bien, pero sigue sin aplicar el descuento (quizás ya está precalculado).
- Probar la carga de ítems de NB en el módulo de compras.
- Pagar deuda AFIP (VEP de autónomos / multa que mandó Cristina). Vencimiento: 03/06/2026.
- Linkear el chat en la app.
- Comprar la mesada (Lavadero).
- Subir el arreglo de [[Franco Callipo|Franco]] para Libre Opción.
- Descargar lo de Play Console para la app de Libre Opción.
- Poner en un stored procedure para [[Sebastian Fontan|Seba]] las actualizaciones de ST_GANANCIA_ESTIPULADA_ARTICULOS:
  ```sql
  UPDATE A SET PORC_GANAN_ESTIPLO = (PORC_GANAN_ESTIP3+PORC_GANAN_ESTIP4)
  FROM [NEW_BYTES].[dbo].[ST_GANANCIA_ESTIPULADA_ARTICULOS] A
  LEFT JOIN NewBytes_DBF.dbo.articulo B ON B.cRef = A.ID_ARTICULO
  WHERE ((PORC_GANAN_ESTIP3+PORC_GANAN_ESTIP4) <> PORC_GANAN_ESTIPLO ) and companyCode =4;

  UPDATE A SET PORC_GANAN_ESTIPLO1 = 5
  FROM [NEW_BYTES].[dbo].[ST_GANANCIA_ESTIPULADA_ARTICULOS] A
  LEFT JOIN NewBytes_DBF.dbo.articulo B ON B.cRef = A.ID_ARTICULO
  WHERE ((PORC_GANAN_ESTIP3+PORC_GANAN_ESTIP4) = PORC_GANAN_ESTIPLO ) AND PORC_GANAN_ESTIPLO1 = 0 and companyCode =4;
  ```

## Bloqueos / Esperando OK

## En curso

## Listo
- Resolver SLI.
- Mandarle mensaje o mail a Seba por el tema de Bulli.
- Arreglar el tema de Bulli (pedido por Seba).
- Aplicar cambios en el módulo de préstamos de capital según la captura enviada: ![[prestamos_captura.jpg]]
- Arreglar a Sebastián el módulo de "préstamos de capital".
- Hacer lo de LASET del ECCN.
- Hacer el banner del Pacman para Libre Opción.
- Daily: Hablar de SLI con Ezequiel y Marbe.
- Daily: Preguntarle a Ezequiel si arregló la meet con Postventa.
- Seguimiento Ezequiel (Postventa): Ver si pudo replicar con el cliente dónde falla el flujo.
- Confirmar call de arquitectura sobre módulo Crypto.
- Asignar/agregar historia de categorías de Libre Opción a Franco.
- Dar OK a Ema para crear manualmente las líneas de caja/banco (caso cobro 3 métodos).
- Pagarle la tarjeta a mi papá.
- Responder preguntas a Marbe sobre PED-1360.
- Reiniciar el servidor de Gamma (Marbe).
- Bug FACTURU multi-producto resuelto (Ezequiel).

## Ver también
- [[Bily/Inicio|Inicio de Bily]]
