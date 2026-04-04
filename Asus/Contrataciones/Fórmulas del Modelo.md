# Fórmulas del Modelo

## El problema central

Dado un **salario neto deseado** (lo que el empleado cobra en mano), calcular hacia atrás todo el costo para la agencia y la facturación al cliente.

## Fórmula del neto

```
Neto = Rem_total × (1 - 0,19) + NR_total × (1 - 0,02)
```

Donde:
- `Rem_total` = suma de todos los ítems remunerativos (bruto)
- `NR_total` = suma de todos los ítems no remunerativos
- `0,19` = deducciones del empleado sobre remunerativo (Jub 11% + PAMI 3% + OS 3% + Art.100 2%)
- `0,02` = deducciones del empleado sobre NR (solo Art.100 2%)

## Reverse-engineering: de neto a bruto

### Paso 1 — Calcular el bruto remunerativo necesario

```
Rem_total = (Neto - NR_total × 0,98) / 0,81
```

Los ítems NR son fijos por convenio ($40.000 + $60.000 con sus presentismos y antigüedades), así que `NR_total` es conocido.

### Paso 2 — Calcular el "A Cuenta Futuros Aumentos"

Todos los ítems remunerativos comparten un factor común:

```
factor = 1 + presentismo + antigüedad × años = 1 + 0,0833 + 0,01 × 1 = 1,0933
```

Entonces:
```
Rem_total = Básico × factor + A_Cuenta × factor

A_Cuenta = (Rem_total / factor) - Básico
         = (Rem_total - Básico × factor) / factor
```

### Fórmula completa del A Cuenta

```
A_Cuenta = ((Neto - NR_total × (1 - 0,02)) / (1 - 0,19) - Básico × factor) / factor
```

En la [[Calculadora Excel - Instrucciones|calculadora Excel]], esta fórmula está en la celda G11:

```excel
=((C5-(G14+G15+G16+G17+G18+G19)*(1-C21))/(1-C20)-C8*(1+C11+C12*C13))/(1+C11+C12*C13)
```

## Del bruto al costo total

### Gasto de la agencia (costo real)

```
Gasto = Rem_total × (1 + 0,27) + NR_total × (1 + 0,03)
      = Rem_total × 1,27 + NR_total × 1,03
```

### Fee de la agencia

```
Fee = Rem_total × 0,30 + NR_total × 0,27
```

Ver [[Coeficientes de Facturación]] para la descomposición de estos porcentajes.

### Facturación al cliente

```
Fact_sin_IVA = Rem_total × 1,57 + NR_total × 1,30
IVA = Fact_sin_IVA × 0,21
Total_cliente = Fact_sin_IVA × 1,21
```

## Verificaciones (deben dar exacto)

```
✓ Gasto + Fee = Facturación sin IVA
  (Rem × 1,27 + NR × 1,03) + (Rem × 0,30 + NR × 0,27) = Rem × 1,57 + NR × 1,30

✓ Coef_R = 1 + Contrib_R + Fee_R
  1,57 = 1 + 0,27 + 0,30

✓ Coef_NR = 1 + Contrib_NR + Fee_NR
  1,30 = 1 + 0,03 + 0,27
```

## Ejemplo numérico (Escenario 1: Neto $2.200.000)

```
NR_total = $109.330 (fijo por convenio)

Rem_total = ($2.200.000 - $109.330 × 0,98) / 0,81
          = ($2.200.000 - $107.143) / 0,81
          = $2.092.857 / 0,81
          = $2.815.228 (aprox.)

A_Cuenta = ($2.815.228 - $1.094.044 × 1,0933) / 1,0933
         = $1.480.938 (aprox.)

Gasto   = $2.815.228 × 1,27 + $109.330 × 1,03 = $3.394.002
Fee     = $2.815.228 × 0,30 + $109.330 × 0,27 = $804.651
Fact    = $3.394.002 + $804.651 = $4.198.654
Total   = $4.198.654 × 1,21 = $5.080.371
```

---

Ver también: [[Modelo de Liquidación CCT 130-75]] | [[Escenarios de Contratación]]

#contrataciones #formulas #calculo
