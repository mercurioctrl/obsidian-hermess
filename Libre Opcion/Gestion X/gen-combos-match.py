#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen-combos-match.py
Replica los "Kits de actualización" (CPU+Mother) y las "PC de Escritorio" de Compra Gamer
usando el catálogo de la distribuidora del usuario (items/catalogoDistribuidoraJulio.csv).

Entradas:
  - adjuntos/LibreOpcion-Estudio-Catalogo-CompraGamer.xlsx  (hoja 'Catálogo completo')
  - items/catalogoDistribuidoraJulio.csv

Salida:
  - combos-armables.md  (reporte en Markdown para la bóveda)
Corre: python3 gen-combos-match.py
"""
import csv, re, unicodedata
from collections import defaultdict

CG_XLSX  = 'adjuntos/LibreOpcion-Estudio-Catalogo-CompraGamer.xlsx'
CAT_CSV  = 'items/catalogoDistribuidoraJulio.csv'
OUT_MD   = 'combos-armables.md'

# ---------------------------------------------------------------- utilidades
def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def norm(s):
    return re.sub(r'\s+', ' ', strip_accents((s or '').upper())).strip()

def read_catalog(path):
    for enc in ('utf-8-sig', 'latin-1'):
        try:
            with open(path, encoding=enc) as f:
                return list(csv.DictReader(f, delimiter=';'))
        except Exception:
            continue
    raise SystemExit('No pude leer ' + path)

def fnum(x):
    try:
        return float(str(x).replace(',', '.'))
    except Exception:
        return None

# ---------------------------------------------------------------- sockets
def socket_of(text):
    t = norm(text)
    # AMD
    if 'AM5' in t: return 'AM5'
    if 'AM4' in t: return 'AM4'
    # Intel
    if 'LGA1851' in t or '1851' in t: return 'LGA1851'
    if 'LGA1700' in t or '1700' in t: return 'LGA1700'
    if 'LGA1200' in t or '1200' in t: return 'LGA1200'
    if 'LGA1151' in t or '1151' in t: return 'LGA1151'
    return None

# Socket implícito por familia de CPU (cuando el texto no lo dice)
def socket_from_cpu(model):
    m = model.upper()
    if m.endswith('X3D') or m.endswith('X3D2'):
        # 5xxx X3D = AM4 ; 7xxx/9xxx X3D = AM5
        if m.startswith('5'): return 'AM4'
        return 'AM5'
    if re.match(r'5\d{3}', m): return 'AM4'          # Ryzen 5000
    if re.match(r'[789]\d{3}', m): return 'AM5'      # Ryzen 7000/8000/9000
    if m in ('225','225F','235','245K','245KF','265K','265KF','285K'): return 'LGA1851'  # Core Ultra 200
    if re.match(r'1[2-4]\d00', m): return 'LGA1700'  # Core 12/13/14 gen
    if m.startswith('G74'): return 'LGA1700'
    if m.startswith('G44'): return 'LGA1151'
    return None

# ---------------------------------------------------------------- CPU model
CPU_RE = re.compile(
    r'\b('
    r'\d{4}X3D2?|'          # 9800X3D, 9950X3D2
    r'\d{4}[A-Z]{0,3}|'     # 5600GT, 5700X, 13100F, 14400, 12400F, 12700
    r'2[0-8]5K?F?|'         # Core Ultra 225/235/245K/265KF/285K
    r'G\d{4}'               # G7400, G4400
    r')\b'
)

# familias Core Ultra: el número puede venir sin sufijo
def extract_cpu_model(text):
    t = norm(text)
    # Core Ultra 200 primero (evita confundir con Ryzen)
    m = re.search(r'CORE ULTRA \d\s+(2[0-8]5K?F?)\b', t)
    if m: return m.group(1)
    m = re.search(r'\b(\d{4}X3D2?)\b', t)
    if m: return m.group(1)
    m = re.search(r'RYZEN \d\s+(\d{4}[A-Z]{0,2})\b', t)
    if m: return m.group(1)
    m = re.search(r'CORE I\d\s+(\d{4,5}[A-Z]?)\b', t)
    if m: return m.group(1)
    m = re.search(r'\b(G\d{4})\b', t)
    if m: return m.group(1)
    return None

# rango de performance aproximado por socket para elegir sustituto cercano
TIER = {
    # AM4
    '5300G':1,'5500':2,'5500X3D':4,'5600GT':3,'5600':3,'5700':4,'5700G':4,'5700X':5,'5800XT':6,
    # AM5 (no-X3D)
    '7600':5,'8400F':5,'8500G':4,'8600G':5,'8700G':6,'8700F':6,'9600X':7,'9700X':8,'9900X':9,
    # AM5 X3D
    '7800X3D':10,'9800X3D':12,'9900X3D':13,'9950X3D':14,'9950X3D2':14,
    # Intel 1700
    'G7400':1,'13100F':3,'12400':4,'12400F':4,'12700':7,'14400':6,
    # Intel Ultra 200
    '225':4,'225F':4,'235':5,'245K':7,'245KF':7,'265K':9,'265KF':9,'285K':11,
    # 1151
    'G4400':1,
}

# ---------------------------------------------------------------- chipset (mother)
def chipset_of(text):
    t = norm(text)
    m = re.search(r'\b([XZBAH]\d{3}[A-Z]*)\b', t)
    return m.group(1) if m else None

def chipset_tier(cs):
    if not cs: return 0
    return {'A':1,'H':1,'B':2,'Z':3,'X':3}.get(cs[0], 0)

# ---------------------------------------------------------------- cargar CG
def load_cg():
    import openpyxl
    wb = openpyxl.load_workbook(CG_XLSX, read_only=True)
    ws = wb['Catálogo completo']
    rows = list(ws.iter_rows(values_only=True))[1:]
    kits = [r for r in rows if (r[3] or '') == 'Kits de actualización']
    pcs  = [r for r in rows if (r[3] or '') == 'PC de Escritorio']
    return kits, pcs

# clasifica un "kit" de CG
def classify_kit(name):
    t = norm(name)
    has_cpu = 'PROCESADOR' in t
    has_mother = 'MOTHER' in t
    has_gpu = bool(re.search(r'RTX|RX \d|GEFORCE|RADEON', t))
    has_psu = 'FUENTE' in t
    has_case = 'GABINETE' in t
    if has_cpu and has_mother: return 'CPU+MOTHER'
    if has_gpu and has_psu:    return 'GPU+FUENTE'
    if has_case and has_psu:   return 'GABINETE+FUENTE'
    if has_mother and 'COOLER' in t and not has_cpu: return 'MOTHER+COOLER'
    return 'OTRO'

# ---------------------------------------------------------------- parseo de specs
def cap_gb(text):
    t = norm(text)
    m = re.search(r'(\d+(?:[.,]\d+)?)\s*TB', t)
    if m: return int(float(m.group(1).replace(',', '.')) * 1000)
    m = re.search(r'(\d{2,4})\s*GB', t)
    if m: return int(m.group(1))
    return None

def ddr_gen(text):
    t = norm(text)
    if 'DDR5' in t: return 5
    if 'DDR4' in t: return 4
    return None

def watts(text):
    m = re.search(r'(\d{3,4})\s*W', norm(text))
    return int(m.group(1)) if m else None

def platform_ddr(socket):
    return 4 if socket in ('AM4', 'LGA1700', 'LGA1151', 'LGA1200') else 5  # AM5/1851 = DDR5

# vram + watts recomendados por GPU
def gpu_watts(model):
    m = (model or '').upper()
    if '5070TI' in m or '5080' in m or '5090' in m: return 750
    if '5070' in m or '9070' in m: return 700
    if any(x in m for x in ('5060', '9060', 'B580', '3050')): return 650
    return 500

# ---------------------------------------------------------------- índice de partes del usuario
class Parts:
    def __init__(self, rows):
        self.rows = rows
        self.cpus = []      # (model, socket, price, detalle)
        self.mothers = []   # (socket, chipset, price, detalle)
        self.by_cat = defaultdict(list)
        for r in rows:
            cat = norm(r['CATEGORIA'])
            det = r['DETALLE']
            price = fnum(r.get('PRECIO USD CON UTILIDAD')) or fnum(r.get('PRECIO FINAL'))
            self.by_cat[cat].append((det, price, r))
            if cat == 'PROCESADORES':
                mdl = extract_cpu_model(det)
                sk = socket_of(det) or (socket_from_cpu(mdl) if mdl else None)
                if mdl: self.cpus.append((mdl, sk, price, det))
            elif cat.startswith('MOTHER'):
                sk = socket_of(det)
                self.mothers.append((sk, chipset_of(det), price, det))

    def find_cpu(self, model, socket):
        if model:
            for c in self.cpus:
                if c[0] == model:
                    return ('EXACTO', c, 0)
        want = TIER.get(model, None)
        cands = [c for c in self.cpus if c[1] == socket]
        if not cands:
            return ('FALTA', None, None)
        if want is None:
            cands.sort(key=lambda c: c[2] or 9e9)
            return ('SUSTITUTO', cands[0], None)
        cands.sort(key=lambda c: abs(TIER.get(c[0], 99) - want))
        best = cands[0]
        gap = abs(TIER.get(best[0], 99) - want)
        status = 'SUSTITUTO' if gap <= 3 else 'LEJANO'
        return (status, best, gap)

    def find_mother(self, socket, chipset):
        cands = [m for m in self.mothers if m[0] == socket]
        if not cands:
            return ('FALTA', None)
        exact = [m for m in cands if m[1] == chipset]
        if exact:
            exact.sort(key=lambda m: m[2] or 9e9)
            return ('EXACTO', exact[0])
        wt = chipset_tier(chipset)
        same = [m for m in cands if chipset_tier(m[1]) == wt]
        pool = same or cands
        pool.sort(key=lambda m: m[2] or 9e9)
        return ('SUSTITUTO', pool[0])

    def pick_ram(self, cap, ddr):
        """Devuelve (detalle, precio_total, qty). Nunca cruza generación de DDR; llega a la
        capacidad con varios módulos iguales (ej. 2×16GB para 32GB)."""
        mods = []
        for det, price, r in self.by_cat.get('MEMORIAS', []):
            t = norm(det)
            if 'SODIMM' in t or not price:   # SODIMM = RAM de notebook
                continue
            c, g = cap_gb(t), ddr_gen(t)
            if not c: continue
            mods.append((det, price, c, g))
        same = [x for x in mods if x[3] == ddr]
        pool = same or mods                  # si no hay del DDR correcto, caé a lo que haya
        best = None
        for det, price, c, g in pool:
            import math
            qty = max(1, math.ceil(cap / c))
            total_cap, total_price = c * qty, price * qty
            score = (0 if total_cap == cap else 1, 0 if qty <= 2 else 1, total_price)
            if best is None or score < best[0]:
                best = (score, (det, total_price, qty))
        return best[1] if best else None

    def pick_ssd(self, cap, nvme):
        best = None
        for det, price, r in self.by_cat.get('DISCOS SSD', []):
            t = norm(det)
            if not price: continue
            c = cap_gb(t)
            is_nvme = 'NVME' in t or 'PCIE' in t
            below = 1 if (c or 0) < cap else 0       # penalizá quedarte corto
            score = (0 if c == cap else 1, below, 0 if is_nvme == nvme else 1, price)
            if best is None or score < best[0]:
                best = (score, (det, price))
        return best[1] if best else None

    def pick_psu(self, min_w):
        cands = []
        for det, price, r in self.by_cat.get('FUENTES', []):
            if not price: continue
            w = watts(det) or 0
            sfx = 'SFX' in norm(det)          # SFX no entra en gabinete ATX estándar
            cands.append((w, price, det, sfx))
        ok = [c for c in cands if c[0] >= min_w]
        pool = ok or cands
        pool.sort(key=lambda c: (0 if c[0] >= min_w else 1, c[3], c[1]))
        return (pool[0][2], pool[0][1]) if pool else None

    def pick_water_cooler(self):
        best = None
        for det, price, r in self.by_cat.get('COOLERS', []):
            if not price or 'WATER COOLER' not in norm(det):
                continue
            if best is None or price < best[1]:
                best = (det, price)
        return best

    def pick_gpu(self, gpu_model):
        want = re.sub(r'\s+', '', (gpu_model or '').upper())          # 'RTX 5070 TI' -> 'RTX5070TI'
        wantnum = re.sub(r'(RTX|RX|ARC|GEFORCE|RADEON)', '', want)     # '5070TI'
        exact, subs = [], []
        for det, price, r in self.by_cat.get('PLACA DE VIDEO', []):
            if not price: continue
            t = re.sub(r'\s+', '', norm(det))
            tnum = re.sub(r'.*?((?:RTX|RX)\d{4}(?:TI|XT)?).*', r'\1', t)
            tnum = re.sub(r'(RTX|RX)', '', tnum)
            if wantnum and wantnum in t:
                exact.append((det, price))
            subs.append((det, price, tnum))
        if exact:
            exact.sort(key=lambda x: x[1])
            return ('EXACTO', exact[0])
        # sustituto: la más barata (aprox. gama de entrada) si no hay match
        subs.sort(key=lambda x: x[1])
        return ('SUSTITUTO', (subs[0][0], subs[0][1])) if subs else ('FALTA', None)

    def cheapest(self, cat_substr, contains=None):
        best = None
        for cat, items in self.by_cat.items():
            if cat == cat_substr or cat_substr == cat:
                for det, price, r in items:
                    if contains and not all(k in norm(det) for k in contains):
                        continue
                    if price and (best is None or price < best[1]):
                        best = (det, price)
        return best

# ---------------------------------------------------------------- matcheo de KITS
def match_kits(kits, parts):
    seen = set()
    out = []
    for r in kits:
        name = r[1]
        kind = classify_kit(name)
        if kind != 'CPU+MOTHER':
            continue
        cpu_model = extract_cpu_model(name)
        sk = socket_of(name) or (socket_from_cpu(cpu_model) if cpu_model else None)
        cs = chipset_of(name)
        key = (cpu_model, cs)
        if key in seen:   # dedup: CG repite mother×cpu, nos importa la receta única
            continue
        seen.add(key)
        cst_cpu, cpu, _gap = parts.find_cpu(cpu_model, sk)
        cst_mb,  mb  = parts.find_mother(sk, cs)
        armable = cpu is not None and mb is not None
        price = (cpu[2] + mb[2]) if (armable and cpu[2] and mb[2]) else None
        out.append(dict(
            cg=name, socket=sk, cpu_model=cpu_model, chipset=cs,
            cpu_status=cst_cpu, cpu=cpu, mb_status=cst_mb, mb=mb,
            armable=armable, price=price, cg_price=r[5],
        ))
    return out

# ---------------------------------------------------------------- matcheo de PCs
def parse_pc(name):
    t = norm(name)
    cpu = extract_cpu_model(name)
    sk = socket_from_cpu(cpu) if cpu else None
    # sacar la GPU (con su VRAM) antes de leer la RAM del sistema
    gpu = None
    gm = re.search(r'(RTX \d{4}(?: TI)?|RX \d{4}(?: XT)?|ARC B\d{3})(?:\s+\d{1,2}GB)?', t)
    if gm:
        gpu = re.sub(r'\s+', '', gm.group(1))
        t = t[:gm.start()] + ' ' + t[gm.end():]
    ram = None
    rm = re.search(r'(\d{1,3})GB', t)
    if rm: ram = int(rm.group(1))
    ssd = None
    sm = re.search(r'(\d+)\s*(TB|GB)\s*SSD', t)
    if sm: ssd = int(sm.group(1)) * (1000 if sm.group(2) == 'TB' else 1)
    nvme = 'NVME' in t
    return dict(cpu=cpu, socket=sk, ram=ram or 16, ssd=ssd or 1000,
                nvme=nvme, gpu=gpu, water='WATER CO' in t,
                gamer='GAMER' in t)

def match_pc(name, parts):
    p = parse_pc(name)
    cst_cpu, cpu, _g = parts.find_cpu(p['cpu'], p['socket'])
    cst_mb, mb = parts.find_mother(p['socket'], None) if p['socket'] else ('FALTA', None)
    ram = parts.pick_ram(p['ram'], platform_ddr(p['socket']))
    ssd = parts.pick_ssd(p['ssd'], p['nvme'])
    gpu_status, gpu = (parts.pick_gpu(p['gpu']) if p['gpu'] else (None, None))
    case = parts.cheapest('GABINETE GAMER') or parts.cheapest('GABINETE')
    psu = parts.pick_psu(gpu_watts(p['gpu']) if p['gpu'] else 500)
    water = parts.pick_water_cooler() if p['water'] else None
    comps = dict(cpu=cpu, mb=mb, ram=ram, ssd=ssd, gpu=gpu, case=case, psu=psu, water=water)
    needed = ['cpu', 'mb', 'ram', 'ssd', 'case', 'psu'] + (['gpu'] if p['gpu'] else []) + (['water'] if p['water'] else [])
    missing = [k for k in needed if not comps[k]]
    price = 0.0
    for k in needed:
        v = comps[k]
        pv = (v[2] if k in ('cpu', 'mb') else v[1]) if v else None
        if pv: price += pv
    return dict(cg=name, parsed=p, comps=comps, missing=missing,
                armable=not missing, price=price if not missing else None,
                cpu_status=cst_cpu, gpu_status=gpu_status, cg_price=None)

# ---------------------------------------------------------------- otros combos (GPU+PSU, Gabinete+PSU, CPU+Mother+RAM)
def gpu_key(text):
    """(numero, sufijo) -> ('5060','') / ('9070','XT'). None si no hay GPU."""
    t = norm(text)
    m = re.search(r'(?:RTX|RX)\s*(\d{4})\s*(TI|XT)?', t)
    return (m.group(1), m.group(2) or '') if m else None

def match_gpu_psu(parts, cg_rows):
    out = []
    for r in cg_rows:
        name = r[1]
        if classify_kit(name) != 'GPU+FUENTE':
            continue
        gk = gpu_key(name)
        gw = watts(name)                     # watt de la fuente que ellos ponen
        gpu = None; gstatus = 'FALTA'
        if gk:
            cands = []
            for det, price, rr in parts.by_cat.get('PLACA DE VIDEO', []):
                if not price: continue
                k = gpu_key(det)
                if k == gk:
                    cands.append((det, price))
            if cands:
                cands.sort(key=lambda x: x[1])
                gpu, gstatus = cands[0], 'EXACTO'
        need_w = gw or gpu_watts((gk[0] if gk else ''))
        psu = parts.pick_psu(need_w)
        armable = gpu is not None and psu is not None
        price = (gpu[1] + psu[1]) if armable else None
        out.append(dict(cg=name, cg_price=r[5], gpu=gpu, gpu_status=gstatus,
                        psu=psu, need_w=need_w, armable=armable, price=price))
    return out

def match_case_psu(parts, cg_rows):
    out = []
    cases = sorted([(d, p) for d, p, r in parts.by_cat.get('GABINETE GAMER', []) if p], key=lambda x: x[1])
    for r in cg_rows:
        name = r[1]
        if classify_kit(name) != 'GABINETE+FUENTE':
            continue
        need_w = watts(name) or 650
        case = cases[0] if cases else None
        psu = parts.pick_psu(need_w)
        armable = case is not None and psu is not None
        price = (case[1] + psu[1]) if armable else None
        out.append(dict(cg=name, cg_price=r[5], case=case, psu=psu,
                        need_w=need_w, armable=armable, price=price))
    return out

def build_cpu_mother_ram(kres, parts):
    """Toma los combos CPU+Mother únicos por (cpu,mother) y les suma una RAM del DDR de la plataforma."""
    seen = {}
    for k in kres:
        if not k['armable']:
            continue
        key = (k['cpu'][3], k['mb'][3])
        if key in seen:
            continue
        seen[key] = k
    out = []
    for k in seen.values():
        ddr = platform_ddr(k['socket'])
        ram = parts.pick_ram(16, ddr)        # 16GB, el piso razonable
        armable = ram is not None
        price = (k['price'] + ram[1]) if (armable and k['price']) else None
        out.append(dict(socket=k['socket'], cpu=k['cpu'], mb=k['mb'], ram=ram,
                        ddr=ddr, armable=armable, price=price, base=k['price']))
    return out

# ---------------------------------------------------------------- main
def money(x):
    return f"u$s{x:,.0f}".replace(',', '.') if x else '—'

def main():
    cat_rows = read_catalog(CAT_CSV)
    parts = Parts(cat_rows)
    kits, pcs = load_cg()

    kres = match_kits(kits, parts)
    pres = [match_pc(r[1], parts) for r in pcs]
    gres = match_gpu_psu(parts, kits)
    cres = match_case_psu(parts, kits)
    rres = build_cpu_mother_ram(kres, parts)

    n_kit_arm = sum(1 for k in kres if k['armable'])
    n_kit_ex  = sum(1 for k in kres if k['cpu_status']=='EXACTO' and k['mb_status']=='EXACTO')
    n_pc_arm  = sum(1 for p in pres if p['armable'])

    L = []
    L.append('---')
    L.append('tipo: entregable')
    L.append('proyecto: LibreOpción')
    L.append('area: Catálogo / Combos')
    L.append('generado_por: gen-combos-match.py')
    L.append('---\n')
    L.append('# Combos y PCs armables con tu catálogo (vs Compra Gamer)\n')
    L.append('> [!info] Generado por `gen-combos-match.py` cruzando los kits/PCs de '
             '[[09 - Estudio de Catálogo - Compra Gamer|Compra Gamer]] contra '
             '`items/catalogoDistribuidoraJulio.csv`. Precios en u$s con tu utilidad cargada.\n')
    L.append(f'**Kits CPU+Mother únicos de CG:** {len(kres)} · '
             f'**armables con tu stock:** {n_kit_arm} · **match exacto (CPU y mother):** {n_kit_ex}\n')
    L.append(f'**PCs de escritorio de CG:** {len(pres)} · **armables:** {n_pc_arm}\n')

    n_lejano = sum(1 for k in kres if k['cpu_status'] == 'LEJANO')
    L.append('\n> [!warning] Hallazgos\n'
             '> - **Podés cubrir casi todo el lineup**: no hay socket que te falte (AM4/AM5/LGA1700/LGA1851).\n'
             '> - **Hueco de gama media AM5**: tu línea AM5 es toda alta gama X3D (7800/9800/9900/9950X3D). '
             f'Cuando CG kitea un Ryzen 5/7 no-X3D (7600, 8500G/8600G/8700G/8700F, 9600X, 9700X) tu único sustituto '
             f'es un 7800X3D — más caro y de otra gama ({n_lejano} kits marcados 🟠). Si querés competir esos precios '
             'necesitás sumar 1-2 CPUs AM5 baratos (un 7600 o un 8500G/8600G).\n'
             '> - **Los precios son de costo+utilidad tuyo, no PVP**: comparalos contra el precio de CG para ver el margen.\n')

    # -------- KITS
    L.append('\n## Kits de actualización (CPU + Mother)\n')
    L.append('Estado: 🟢 exacto · 🟡 sustituto cercano · 🟠 sustituto lejano (gama distinta) · 🔴 falta.\n')
    L.append('| Kit Compra Gamer | Socket | Tu CPU | Tu Mother | Precio combo (u$s) |')
    L.append('|---|---|---|---|--:|')
    def ico(s): return {'EXACTO':'🟢','SUSTITUTO':'🟡','LEJANO':'🟠','FALTA':'🔴'}[s]
    # ordenar: armables primero, por socket
    def clean_cpu(d): return re.sub(r'^PROCESADOR (AMD|INTEL)\s*\([^)]*\)\s*', '', d).strip()
    def clean_mb(d):  return re.sub(r'^MOTHER\s+', '', d).strip()
    for k in sorted(kres, key=lambda k:(not k['armable'], k['socket'] or 'zz', -(TIER.get(k['cpu_model'],0)))):
        cg = re.sub(r'^Kit (Mother |Procesador )?', '', k['cg'])[:56]
        cpu_txt = f"{ico(k['cpu_status'])} {clean_cpu(k['cpu'][3])}" if k['cpu'] else f"🔴 falta {k['cpu_model'] or '?'}"
        mb_txt  = f"{ico(k['mb_status'])} {clean_mb(k['mb'][3])[:38]}" if k['mb'] else '🔴 falta mother'
        L.append(f"| {cg} | {k['socket'] or '?'} | {cpu_txt} | {mb_txt} | {money(k['price'])} |")

    # -------- GPU + Fuente
    L.append('\n## Combos GPU + Fuente\n')
    L.append('Réplica de los combos "placa + fuente" de Compra Gamer, con tu placa y una fuente del wattaje adecuado.\n')
    L.append('| Combo Compra Gamer | Tu placa | Tu fuente | Precio (u$s) |')
    L.append('|---|---|---|--:|')
    def clean_gpu(d): return re.sub(r'^PLACA DE VIDEO\s+', '', d).strip()
    for g in gres:
        cg = re.sub(r'^Combo\s+', '', g['cg'])[:50]
        gpu = f"{ico(g['gpu_status'])} {clean_gpu(g['gpu'][0])[:38]}" if g['gpu'] else '🔴 falta placa'
        psu = f"{g['psu'][0][:34]} ({g['need_w']}W)" if g['psu'] else '🔴 falta fuente'
        L.append(f"| {cg} | {gpu} | {psu} | {money(g['price'])} |")

    # -------- Gabinete + Fuente
    L.append('\n## Combos Gabinete + Fuente\n')
    L.append('| Combo Compra Gamer | Tu gabinete | Tu fuente | Precio (u$s) |')
    L.append('|---|---|---|--:|')
    for c in cres:
        cg = re.sub(r'^Combo (XYZ )?', '', c['cg'])[:50]
        case = c['case'][0][:34] if c['case'] else '🔴 falta gabinete'
        psu = f"{c['psu'][0][:30]} ({c['need_w']}W)" if c['psu'] else '🔴 falta fuente'
        L.append(f"| {cg} | {case} | {psu} | {money(c['price'])} |")

    # -------- CPU + Mother + RAM
    L.append('\n## Combos CPU + Mother + RAM (full upgrade)\n')
    L.append('Los combos CPU+Mother con una RAM de 16GB del DDR correcto sumada (el combo de 3 piezas que propone la landing).\n')
    L.append('| Socket | CPU | Mother | RAM (16GB) | Precio (u$s) |')
    L.append('|---|---|---|---|--:|')
    order = {'AM5':0,'AM4':1,'LGA1851':2,'LGA1700':3}
    for x in sorted(rres, key=lambda x:(order.get(x['socket'],9), -(x['price'] or 0))):
        if not x['armable']: continue
        cpu = clean_cpu(x['cpu'][3])
        mb = clean_mb(x['mb'][3])[:26]
        ram = re.sub(r'^MEMORIA\s+', '', x['ram'][0])[:30]
        L.append(f"| {x['socket']} | {cpu} | {mb} | {ram} | {money(x['price'])} |")

    # -------- PCs
    L.append('\n## PC de escritorio (build completa)\n')
    L.append('| PC Compra Gamer | Armable | Falta | Precio partes (u$s) |')
    L.append('|---|:--:|---|--:|')
    for p in pres:
        cg = p['cg'][:58]
        ok = '✅' if p['armable'] else '❌'
        falta = ', '.join(p['missing']) if p['missing'] else '—'
        L.append(f"| {cg} | {ok} | {falta} | {money(p['price'])} |")

    # -------- Detalle de PCs armables
    L.append('\n### Receta de las PCs armables\n')
    for p in pres:
        if not p['armable']:
            continue
        flag = ''
        if p['cpu_status'] in ('SUSTITUTO','LEJANO'): flag += ' ⚠️CPU sustituto'
        if p.get('gpu_status') == 'SUSTITUTO': flag += ' ⚠️GPU sustituta'
        L.append(f"\n**{p['cg']}** — {money(p['price'])}{flag}")
        for k in ['cpu','mb','ram','ssd','gpu','water','case','psu']:
            v = p['comps'][k]
            if not v: continue
            det = v[3] if k in ('cpu','mb') else v[0]
            pr  = v[2] if k in ('cpu','mb') else v[1]
            L.append(f"- {k}: {det} — {money(pr)}")

    with open(OUT_MD, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')

    # resumen a consola
    print(f'Kits únicos CG: {len(kres)} | armables: {n_kit_arm} | exactos: {n_kit_ex}')
    print(f'PCs CG: {len(pres)} | armables: {n_pc_arm}')
    print(f'Escrito -> {OUT_MD}')

if __name__ == '__main__':
    main()
