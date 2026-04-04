# Coeficientes de Facturación

## Qué son los coeficientes

Los coeficientes determinan cuánto se le cobra al cliente por cada peso de salario bruto del empleado. Incluyen tanto el costo real del empleador (contribuciones patronales) como el margen/fee de la agencia.

## Descomposición

### Coeficiente Remunerativo: 1,57

```
1,57 = 1,00 (salario bruto)
     + 0,27 (contribuciones patronales: SUSS 18% + OS 6% + ART 3%)
     + 0,30 (fee de la agencia)
```

Es decir, por cada $1 de sueldo bruto remunerativo, al cliente se le cobra $1,57.

### Coeficiente No Remunerativo: 1,30

```
1,30 = 1,00 (importe bruto NR)
     + 0,03 (ART, única contribución sobre NR)
     + 0,27 (fee de la agencia)
```

Por cada $1 de concepto no remunerativo, al cliente se le cobra $1,30.

## Cómo se traduce en facturación

```
Facturación sin IVA = Σ(ítems remunerativos) × 1,57 + Σ(ítems NR) × 1,30
Facturación con IVA = Facturación sin IVA × 1,21
```

## Fee implícito de la agencia

| Tipo | Coeficiente | Contribuciones | Fee implícito |
|------|-------------|----------------|---------------|
| Remunerativo | 1,57 | 27% | **30%** |
| No Remunerativo | 1,30 | 3% | **27%** |

> [!tip] Verificación rápida
> Fee = Coeficiente - 1 - Contribuciones patronales
> - Fee rem = 1,57 - 1 - 0,27 = **0,30** (30%)
> - Fee NR = 1,30 - 1 - 0,03 = **0,27** (27%)

## Relación entre fee, gasto y facturación

```
Facturación sin IVA = Gasto de la agencia + Fee de la agencia
```

Donde:
- **Gasto** = Bruto + Contribuciones patronales = `Rem × 1,27 + NR × 1,03`
- **Fee** = `Rem × 0,30 + NR × 0,27`
- **Facturación** = `Rem × 1,57 + NR × 1,30`

Esta identidad se verifica en la [[Calculadora Excel - Instrucciones|calculadora Excel]] con las filas de verificación al final.

## Origen de estos coeficientes

Estos coeficientes fueron proporcionados por el cliente, que los tomó de una agencia anterior que le facturaba $2.200.000 + IVA. Se validó que la descomposición en contribuciones + fee es consistente con las alícuotas reales de cargas patronales argentinas para MiPyME comercio.

---

Ver también: [[Modelo de Liquidación CCT 130-75]] | [[Fórmulas del Modelo]]

#contrataciones #coeficientes #facturacion
