#!/usr/bin/env python3
"""Genera cube-data.js para Cubo-Datos-LibreOpcion.html desde los CSV de meses/.

Uso:  cd "Libre Opcion/Gestion X" && python3 gen-cube-data.py

Salida: cube-data.js con 4 consts:
  MONTHS  -> ['YYYY-MM', ...]
  SKUS    -> { sku: [detalle, categoria, marca] }   (1 entrada por SKU único)
  FACTS   -> [[mes, sku, cantidad, venta, costo, renta], ...]   (producto × mes; item-group)
  OPS     -> [[mes, pago, envio, vendedor, ordenes, venta, renta], ...]  (pre-agregado; grilla)

Notas:
  - Productos (item-group) y Operaciones (grilla) NO se pueden cruzar: distinto grano, sin clave común.
  - Valores en u$s. Las líneas "COSTO FINANCIERO" (ingreso de cuotas) y "TRANSPORTE/FLETE"
    (costo del envío gratis) NO son productos: se etiquetan como categoría "· ..." y marca "—".
  - Encoding mixto: se intenta UTF-8 y se cae a latin-1.
"""
import csv, glob, re, json, io, os
from collections import defaultdict

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meses")

def read_rows(fn):
    data = open(fn, "rb").read()
    try: txt = data.decode("utf-8")
    except UnicodeDecodeError: txt = data.decode("latin-1")
    return list(csv.DictReader(io.StringIO(txt)))

def num(s):
    try: return float((s or "").strip())
    except: return 0.0

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

# (keyword, marca). Orden = prioridad: sub-marcas y específicas primero. Primer match gana.
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
    toks = set(re.findall(r"[A-Z0-9\.\-]+", d))   # tokens para evitar falsos positivos (LG, WD, HP...)
    for kw, br in BRANDS:
        if (" " in kw and kw in d) or (" " not in kw and kw in toks): return br
    return "Otras"

# --- Productos (item-group consolidado) ---
SKUS, FACTS = {}, []
for r in read_rows(os.path.join(BASE, "item-group_consolidado_2025-06_2026-05.csv")):
    sku = r["ID"].strip()
    det = re.sub(r"\s+", " ", r["Detalle"].strip())[:54]
    if sku not in SKUS:
        SKUS[sku] = [det, categoria(r["Detalle"]), marca(r["Detalle"])]
    FACTS.append([r["Mes"], sku, round(num(r["Cantidad"])), round(num(r["Venta"])),
                  round(num(r["Costo"])), round(num(r["Renta"]))])

# --- Operaciones (grillas, pre-agregado por mes×pago×envio×vendedor) ---
agg = defaultdict(lambda: [0, 0.0, 0.0])  # ordenes, venta, renta
for fn in glob.glob(os.path.join(BASE, "grilla_*.csv")):
    m = re.search(r"grilla_(\d{2})-(\d{4})", os.path.basename(fn))
    if not m: continue
    mes = f"{m.group(2)}-{m.group(1)}"
    for r in read_rows(fn):
        pago = (r.get("Pago") or "").strip() or "(s/d)"
        envio = (r.get("Envio") or "").strip() or "(s/d)"
        vend = (r.get("Vendedor") or "").strip() or "(s/d)"
        k = (mes, pago, envio, vend)
        agg[k][0] += 1; agg[k][1] += num(r.get("Venta")); agg[k][2] += num(r.get("Renta"))
OPS = [[k[0], k[1], k[2], k[3], v[0], round(v[1]), round(v[2])] for k, v in agg.items()]
MONTHS = sorted({f[0] for f in FACTS})

out_path = os.path.join(os.path.dirname(BASE), "cube-data.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("// Datos del cubo — item-group (productos, con MARCA) + grilla (operaciones)\n")
    f.write("// Generado por gen-cube-data.py — NO editar a mano.\n")
    f.write(f"const MONTHS={json.dumps(MONTHS)};\n")
    f.write(f"const SKUS={json.dumps(SKUS, ensure_ascii=False)};\n")
    f.write(f"const FACTS={json.dumps(FACTS, ensure_ascii=False)};\n")
    f.write(f"const OPS={json.dumps(OPS, ensure_ascii=False)};\n")

print(f"OK -> {out_path}  ({len(SKUS)} SKUs, {len(FACTS)} facts, {len(OPS)} ops, {len(MONTHS)} meses)")
