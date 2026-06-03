---
tipo: estrategia
proyecto: LibreOpción
area: Inventario / Demanda
estado: a implementar
creado: 2026-06-02
tags:
  - libreopcion
  - aging
  - inventario
  - liquidacion
  - adquisicion
  - demanda
---

# 14 · Liquidación de Aging como Motor de Demanda

> [!danger] El dato
> **~50% (o más) del stock está envejecido**, y hoy **no hay mecanismo de liquidación**: la mercadería vieja queda en el catálogo al mismo precio hasta que alguien la compra. Como el capital no es el freno ([[13 - El Verdadero Cuello de Botella es la Demanda]]), el aging es el **único riesgo financiero real** — pero también una **mina de demanda sin explotar**.

## El reencuadre: el aging es munición de demanda

Necesitás **vender más** y tenés media bodega de stock que venderías feliz a **margen cero** (la alternativa es que se deprecie a la nada). Eso es **demanda inmediata, gatillable a voluntad**. La liability es el arma.

## Mecanismo: escalera de descuento automática por antigüedad

| Antigüedad | Acción (regla, no a mano) |
|---|---|
| 0–60 días | Precio normal (fresco) |
| 60 días | −5% |
| 90 días | −10% |
| 120 días | A costo |
| +150 días | Bajo costo + **sin interés agresivo** |

*(Valores de ejemplo — calibrar con la curva de depreciación real por categoría.)*

> [!tip] El "sin interés selectivo" sí tiene lugar — acá
> En stock fresco no se puede comer el costo de las cuotas (margen 17%, ver [[11 - Estrategia de Cuotas y Precio]]). Pero en **stock viejo conviene**: preferís moverlo con sin interés agresivo antes que comerte la caída de precio.

## 💡 El margen negativo es adquisición de clientes, no pérdida

Vender aging a pérdida ≈ **pagar para adquirir un cliente** (que después retenés con garantía + cuotas → LTV). Comparado con el CAC de los avisos (paid social convierte ~0), es **más barato y además mueve stock muerto**.

> [!success] Reciclar el presupuesto de paid social
> La plata que hoy se quema en IG/FB ads (12.495 visitas, 0 ventas) se "gasta" mejor como **descuento en stock viejo**: movés mercadería + adquirís cliente. **Mismo costo, doble beneficio.** → matar paid social ([[13 - El Verdadero Cuello de Botella es la Demanda]]) y redirigir.

## Guardrails

- Sección de **liquidación separada** y **por reglas** → no canibalizar stock fresco ni entrenar al cliente a esperar la oferta.
- Las ofertas profundas refuerzan el [[10 - Reposicionamiento - De Precio a Confianza|posicionamiento de confianza]] solo si mantienen **garantía** — liquidación ≠ "saldo trucho".

## Causa de raíz: comprar por demanda, no por olfato

50% de aging = selección de compra floja. **Cura del síntoma:** liquidar. **Cura de raíz:** usar el **evaluador de [[08 - Detección de Tendencias - Método y Herramientas]]** como filtro antes de importar. Sin esto, se liquida para siempre.

## Métrica

**Rotación de inventario / días de stock** por categoría — no la caja.

## Enlaces

- [[13 - El Verdadero Cuello de Botella es la Demanda]]
- [[11 - Estrategia de Cuotas y Precio]]
- [[08 - Detección de Tendencias - Método y Herramientas]]
- [[00 - Índice Gestión X]]
</content>
