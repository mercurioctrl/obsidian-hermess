#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen-ventas-forecast.py
Lee items/ventas-por-sku-2026.csv (ventas por SKU × mes, ene–jun 2026, sacadas del
reporte benefits-report.php de gestion.saftel.com) y emite ventas-data.js con:
  - MONTHS / FMONTHS           meses históricos y proyectados
  - MONTHLY                    totales por mes (venta, costo, ganancia, unidades, skus)
  - CATMONTH / BRANDMONTH      venta y unidades por categoría/marca × mes
  - SKUS                       serie mensual por SKU (qty, venta, costo, ganancia)
  - FORECAST                   proyección de compra 6 meses adelante por SKU
  - FTOTALS                    totales de compra proyectada por mes
Consumido por Ventas-y-Proyeccion-LibreOpcion.html.
Corre: python3 gen-ventas-forecast.py
"""
import csv, re, json, math, os
from collections import defaultdict

SRC = 'items/ventas-por-sku-2026.csv'
OUT = 'ventas-data.js'
MONTHS = ['2026-01', '2026-02', '2026-03', '2026-04', '2026-05', '2026-06']
FMONTHS = ['2026-07', '2026-08', '2026-09', '2026-10', '2026-11', '2026-12']
MLABEL = {'2026-01':'Ene','2026-02':'Feb','2026-03':'Mar','2026-04':'Abr','2026-05':'May','2026-06':'Jun',
          '2026-07':'Jul','2026-08':'Ago','2026-09':'Sep','2026-10':'Oct','2026-11':'Nov','2026-12':'Dic'}

# ------------------------------------------------ categoría / marca (consistente con gen-cube-data.py)
def categoria(d):
    d = d.upper()
    if "COSTO FINANCIERO" in d: return "· Financiero"
    if "TRANSPORTE" in d or "FLETE" in d: return "· Envío (costo)"
    rules = [
        ("CPU", ["PROCESADOR", "RYZEN", "CORE I"]),
        ("GPU", ["PLACA DE VIDEO", "GEFORCE", "RADEON", "RTX", "GTX"]),
        ("Motherboard", ["MOTHER"]), ("RAM", ["MEMORIA", "DDR5", "DDR4 "]),
        ("Storage", ["SSD", "NVME", "DISCO", "RIGIDO", "M.2", "SOLIDO"]),
        ("PSU/Fuente", ["FUENTE"]), ("Gabinete", ["GABINETE"]),
        ("Cooling", ["COOLER", "REFRIGERA", "DISIPADOR", "VENTILADOR", "WATER"]),
        ("Monitor", ["MONITOR"]), ("Notebook", ["NOTEBOOK", "NETBOOK"]),
        ("UPS/Energia", ["UPS", "ESTABILIZADOR"]),
        ("Perifericos", ["TECLADO", "MOUSE", "AURICULAR", "HEADSET", "PARLANTE", "MICROFONO", "WEBCAM", "COMBO", "GAMEPAD", "JOYSTICK", "MOUSEPAD"]),
        ("Silla", ["SILLA"]), ("Redes", ["ROUTER", "SWITCH", "ACCESS POINT", "REPETIDOR", "ANTENA"]),
        ("Accesorios", ["CABLE", "ADAPTADOR", "HUB", "SOPORTE", "PASTA", "CARGADOR"]),
        ("Impresion", ["IMPRESORA", "TONER", "CARTUCHO"]),
    ]
    for name, kws in rules:
        if any(k in d for k in kws): return name
    return "Otros"

BRANDS = [
    ("ROG","ASUS"),("TUF","ASUS"),("ASUS","ASUS"),("AORUS","GIGABYTE"),("GIGABYTE","GIGABYTE"),
    ("ASROCK","ASROCK"),("MSI","MSI"),("ZOTAC","ZOTAC"),("SAPPHIRE","SAPPHIRE"),
    ("POWER COLOR","POWERCOLOR"),("POWERCOLOR","POWERCOLOR"),("GAINWARD","GAINWARD"),("PALIT","PALIT"),
    ("PNY","PNY"),("XFX","XFX"),("EVGA","EVGA"),("BIOSTAR","BIOSTAR"),
    ("XPG","ADATA"),("ADATA","ADATA"),("FURY","KINGSTON"),("KINGSTON","KINGSTON"),("CORSAIR","CORSAIR"),
    ("VIPER","PATRIOT"),("PATRIOT","PATRIOT"),("NETAC","NETAC"),("TEAMGROUP","TEAMGROUP"),
    ("CRUCIAL","CRUCIAL"),("G.SKILL","G.SKILL"),("GSKILL","G.SKILL"),
    ("WESTERN DIGITAL","WD"),("WD","WD"),("SEAGATE","SEAGATE"),("LEXAR","LEXAR"),
    ("KINGSPEC","KINGSPEC"),("GIGASTONE","GIGASTONE"),("MARKVISION","MARKVISION"),
    ("RYZEN","AMD"),("AMD","AMD"),("CORE I","INTEL"),("INTEL","INTEL"),
    ("COOLER MASTER","COOLER MASTER"),("COOLERMASTER","COOLER MASTER"),("DEEPCOOL","DEEPCOOL"),
    ("THERMALTAKE","THERMALTAKE"),("THERMALRIGHT","THERMALRIGHT"),("NOCTUA","NOCTUA"),("BE QUIET","BE QUIET"),
    ("NZXT","NZXT"),("LIAN LI","LIAN LI"),("ANTEC","ANTEC"),("AEROCOOL","AEROCOOL"),("GAMEMAX","GAMEMAX"),
    ("SEASONIC","SEASONIC"),("SENTEY","SENTEY"),("AUREOX","AUREOX"),("REDRAGON","REDRAGON"),("HYPERX","HYPERX"),
    ("LOGITECH","LOGITECH"),("GENIUS","GENIUS"),("TRUST","TRUST"),("RAZER","RAZER"),
    ("NOGANET","NOGA"),("NOGA","NOGA"),("KLIPXTREME","KLIPXTREME"),("KLIP","KLIPXTREME"),
    ("AOC","AOC"),("PHILIPS","PHILIPS"),("VIEWSONIC","VIEWSONIC"),("LG","LG"),("SAMSUNG","SAMSUNG"),
    ("LENOVO","LENOVO"),("PREDATOR","ACER"),("ACER","ACER"),("BROTHER","BROTHER"),("HP","HP"),("DELL","DELL"),
    ("TP-LINK","TP-LINK"),("TPLINK","TP-LINK"),("MERCUSYS","MERCUSYS"),("NEXXT","NEXXT"),
    ("D-LINK","D-LINK"),("TENDA","TENDA"),("UBIQUITI","UBIQUITI"),("UNIFI","UBIQUITI"),
    ("LYONN","LYONN"),("XIAOMI","XIAOMI"),("HUNNOX","HUNNOX"),
]
def marca(det):
    d = det.upper()
    if "COSTO FINANCIERO" in d or "TRANSPORTE" in d or "FLETE" in d: return "—"
    toks = set(re.findall(r"[A-Z0-9\.\-]+", d))
    for kw, br in BRANDS:
        if (" " in kw and kw in d) or (" " not in kw and kw in toks): return br
    return "Otras"

def f(x):
    try: return float(str(x).replace(',', ''))
    except: return 0.0

# ------------------------------------------------ leer y agregar
def read():
    for enc in ('utf-8-sig', 'utf-8', 'latin-1'):
        try:
            with open(SRC, encoding=enc) as fh:
                return list(csv.DictReader(fh))
        except Exception:
            continue
    raise SystemExit('No pude leer ' + SRC)

rows = read()
mi = {m: i for i, m in enumerate(MONTHS)}

# sku[id] = {det,cat,marca,prov, qty[6], ven[6], cos[6], gan[6], costU(último)}
sku = {}
for r in rows:
    m = r['MES']
    if m not in mi: continue
    i = mi[m]
    _id = r['ID'].strip()
    det = re.sub(r'\s+', ' ', r['DETALLE'].strip())
    if _id not in sku:
        sku[_id] = dict(det=det, cat=categoria(det), mar=marca(det), prov=r['PROVEEDOR'].strip(),
                        qty=[0.0]*6, ven=[0.0]*6, cos=[0.0]*6, gan=[0.0]*6, costU=0.0)
    s = sku[_id]
    s['qty'][i] += f(r['CANTIDAD'])
    s['ven'][i] += f(r['VENTA_TOTAL'])
    s['cos'][i] += f(r['COSTO_TOTAL'])
    s['gan'][i] += f(r['GANANCIA'])
    if f(r['COSTO_U']) > 0: s['costU'] = f(r['COSTO_U'])   # último costo unit conocido
    if len(det) > len(s['det']): s['det'] = det

# ------------------------------------------------ totales por mes
MONTHLY = []
for i, m in enumerate(MONTHS):
    ven = sum(s['ven'][i] for s in sku.values())
    cos = sum(s['cos'][i] for s in sku.values())
    gan = sum(s['gan'][i] for s in sku.values())
    uni = sum(s['qty'][i] for s in sku.values())
    nsk = sum(1 for s in sku.values() if s['qty'][i] > 0)
    MONTHLY.append(dict(mes=m, label=MLABEL[m], venta=round(ven), costo=round(cos),
                        ganancia=round(gan), unidades=round(uni), skus=nsk,
                        margen=round(gan/ven*100, 1) if ven else 0))

# categoría/marca × mes (venta y unidades)
def dim_month(keyfn):
    agg = defaultdict(lambda: dict(ven=[0.0]*6, qty=[0.0]*6))
    for s in sku.values():
        k = keyfn(s)
        for i in range(6):
            agg[k]['ven'][i] += s['ven'][i]
            agg[k]['qty'][i] += s['qty'][i]
    out = []
    for k, v in agg.items():
        out.append(dict(key=k, ven=[round(x) for x in v['ven']], qty=[round(x) for x in v['qty']],
                        total=round(sum(v['ven']))))
    out.sort(key=lambda x: -x['total'])
    return out

CATMONTH = dim_month(lambda s: s['cat'])
BRANDMONTH = dim_month(lambda s: s['mar'])

# ------------------------------------------------ tabla de SKUs
SKUS = []
for _id, s in sku.items():
    tv = sum(s['ven']); tq = sum(s['qty']); tg = sum(s['gan'])
    SKUS.append(dict(id=_id, det=s['det'][:60], cat=s['cat'], mar=s['mar'], prov=s['prov'],
                     qty=[round(x, 1) for x in s['qty']], ven=[round(x) for x in s['ven']],
                     gan=[round(x) for x in s['gan']], costU=round(s['costU'], 2),
                     tv=round(tv), tq=round(tq, 1), tg=round(tg),
                     mrg=round(tg/tv*100, 1) if tv else 0))
SKUS.sort(key=lambda x: -x['tv'])

# ------------------------------------------------ PROYECCIÓN DE COMPRA (6 meses adelante)
# Crecimiento mensual por categoría (compound), anclado al último trimestre, amortiguado y acotado.
def cat_growth():
    g = {}
    for c in CATMONTH:
        q = c['qty']
        prim = sum(q[0:3]) / 3.0 or 0.0     # ene-mar
        ult = sum(q[3:6]) / 3.0 or 0.0      # abr-jun
        if prim > 0 and ult > 0:
            gm = (ult / prim) ** (1/3.0)     # crecimiento mensual compuesto
        else:
            gm = 1.0
        g[c['key']] = min(1.15, max(0.90, gm))   # acotar ±(15/10)% mensual
    return g
CATG = cat_growth()

NONPROD = {'· Financiero', '· Envío (costo)'}
FORECAST = []
for s in SKUS:
    if s['cat'] in NONPROD:                 # transporte/financiero no se "compran"
        continue
    q = sku[s['id']]['qty']
    last3 = q[3], q[4], q[5]                 # abr, may, jun
    # base = promedio ponderado del último trimestre (peso 1·2·3 hacia jun)
    base = (1*last3[0] + 2*last3[1] + 3*last3[2]) / 6.0
    sold_months = sum(1 for x in q if x > 0)
    if base <= 0 or sold_months < 2:        # ruido: descartar SKUs sin recurrencia
        continue
    g = CATG.get(s['cat'], 1.0)
    proj = [base * (g ** k) for k in range(1, 7)]    # jul..dic
    units = [max(0, math.ceil(p - 1e-9)) for p in proj]
    total_u = sum(units)
    cu = s['costU'] or (sum(sku[s['id']]['cos']) / (sum(q) or 1))
    cost_m = [round(u * cu) for u in units]
    trend = 'up' if g > 1.03 else ('down' if g < 0.97 else 'flat')
    FORECAST.append(dict(id=s['id'], det=s['det'], cat=s['cat'], mar=s['mar'], prov=s['prov'],
                         hist=[round(x, 1) for x in q], base=round(base, 1), g=round(g, 3),
                         trend=trend, units=units, total=total_u, costU=round(cu, 2),
                         costM=cost_m, costTot=round(sum(cost_m))))
FORECAST.sort(key=lambda x: -x['costTot'])

# totales de compra proyectada por mes
FTOTALS = []
for k in range(6):
    u = sum(x['units'][k] for x in FORECAST)
    c = sum(x['costM'][k] for x in FORECAST)
    FTOTALS.append(dict(mes=FMONTHS[k], label=MLABEL[FMONTHS[k]], unidades=u, costo=c))

# compra proyectada agrupada por MARCA (6 meses sumados)
_fb = defaultdict(lambda: dict(skus=0, unidades=0, costo=0, um=[0]*6))
for x in FORECAST:
    b = _fb[x['mar']]
    b['skus'] += 1
    b['unidades'] += x['total']
    b['costo'] += x['costTot']
    for k in range(6):
        b['um'][k] += x['units'][k]
FBRAND = [dict(marca=k, skus=v['skus'], unidades=v['unidades'], costo=v['costo'], um=v['um'])
          for k, v in _fb.items()]
FBRAND.sort(key=lambda x: -x['costo'])

# ------------------------------------------------ escribir JS
def js(name, obj):
    return f'const {name} = {json.dumps(obj, ensure_ascii=False)};\n'

with open(OUT, 'w', encoding='utf-8') as out:
    out.write('// Generado por gen-ventas-forecast.py — NO editar a mano.\n')
    out.write('// Fuente: items/ventas-por-sku-2026.csv (reporte benefits-report.php, ene–jun 2026).\n')
    out.write(js('MONTHS', MONTHS))
    out.write(js('FMONTHS', FMONTHS))
    out.write(js('MLABEL', MLABEL))
    out.write(js('MONTHLY', MONTHLY))
    out.write(js('CATMONTH', CATMONTH))
    out.write(js('BRANDMONTH', BRANDMONTH))
    out.write(js('SKUS', SKUS))
    out.write(js('FORECAST', FORECAST))
    out.write(js('FTOTALS', FTOTALS))
    out.write(js('FBRAND', FBRAND))

# resumen consola
print(f'SKUs únicos: {len(SKUS)} | en proyección: {len(FORECAST)}')
print('Venta por mes:', ' '.join(f"{m['label']} {m['venta']//1000}k" for m in MONTHLY))
print('Compra proyectada u$s/mes:', ' '.join(f"{t['label']} {t['costo']//1000}k" for t in FTOTALS))
print(f'Compra total 6m: u$s {sum(t["costo"] for t in FTOTALS):,.0f}')
print(f'-> {OUT}')
