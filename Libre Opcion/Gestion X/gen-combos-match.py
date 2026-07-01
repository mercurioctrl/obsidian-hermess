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
                    return ('EXACTO', c)
        # sustituto: mismo socket, tier más cercano
        want = TIER.get(model, None)
        cands = [c for c in self.cpus if c[1] == socket]
        if not cands:
            return ('FALTA', None)
        if want is None:
            cands.sort(key=lambda c: c[2] or 9e9)
            return ('SUSTITUTO', cands[0])
        cands.sort(key=lambda c: abs(TIER.get(c[0], 99) - want))
        return ('SUSTITUTO', cands[0])

    def find_mother(self, socket, chipset, prefer='cheap'):
        cands = [m for m in self.mothers if m[0] == socket]
        if not cands:
            return ('FALTA', None)
        # exacto por chipset
        exact = [m for m in cands if m[1] == chipset]
        if exact:
            exact.sort(key=lambda m: m[2] or 9e9)
            return ('EXACTO', exact[0])
        # mismo tier de chipset
        wt = chipset_tier(chipset)
        same = [m for m in cands if chipset_tier(m[1]) == wt]
        pool = same or cands
        pool.sort(key=lambda m: m[2] or 9e9)
        return ('SUSTITUTO', pool[0])

    def cheapest(self, cat_substr, contains=None):
        best = None
        for cat, items in self.by_cat.items():
            if cat_substr in cat:
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
        cst_cpu, cpu = parts.find_cpu(cpu_model, sk)
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
    ram = None
    m = re.search(r'(\d{1,2})GB(?!\s*(?:RTX|RX))', t)
    # RAM: primer "NGB" que no sea de la placa; heurística: el que sigue al patrón del build
    rams = re.findall(r'(\d{1,2})GB', t)
    ssd = None
    m = re.search(r'(\d+(?:TB|GB)) SSD', t)
    if m: ssd = m.group(1)
    gpu = None
    m = re.search(r'(RTX \d{4}(?: TI)?|RX \d{4}(?: XT)?|ARC B\d{3})', t)
    if m: gpu = m.group(1)
    return dict(cpu=cpu, socket=sk, ram=rams, ssd=ssd, gpu=gpu, gamer='GAMER' in t)

def match_pc(name, parts):
    p = parse_pc(name)
    cst_cpu, cpu = parts.find_cpu(p['cpu'], p['socket'])
    cst_mb, mb = parts.find_mother(p['socket'], None) if p['socket'] else ('FALTA', None)
    ssd = None
    if p['ssd']:
        want = p['ssd'].replace('TB','000GB') if p['ssd'].endswith('TB') else p['ssd']
        ssd = parts.cheapest('DISCOS SSD', contains=[p['ssd'].replace('TB',' TB') if False else p['ssd'][:-2]])
    if ssd is None:
        ssd = parts.cheapest('DISCOS SSD')
    ram = parts.cheapest('MEMORIAS')
    gpu = None
    if p['gpu']:
        toks = p['gpu'].split()
        gpu = parts.cheapest('PLACA DE VIDEO', contains=[toks[-1]])
        if gpu is None:
            gpu = parts.cheapest('PLACA DE VIDEO')
    case = parts.cheapest('GABINETE')
    psu = parts.cheapest('FUENTES')
    comps = dict(cpu=cpu, mb=mb, ram=ram, ssd=ssd, gpu=gpu, case=case, psu=psu)
    needed = ['cpu','mb','ram','ssd','case','psu'] + (['gpu'] if p['gpu'] else [])
    missing = [k for k in needed if not comps[k]]
    price = 0.0
    for k in needed:
        v = comps[k]
        pv = (v[2] if k in ('cpu','mb') else v[1]) if v else None
        if pv: price += pv
    return dict(cg=name, parsed=p, comps=comps, missing=missing,
                armable=not missing, price=price if not missing else None,
                cpu_status=cst_cpu, cg_price=None)

# ---------------------------------------------------------------- main
def money(x):
    return f"u$s{x:,.0f}".replace(',', '.') if x else '—'

def main():
    cat_rows = read_catalog(CAT_CSV)
    parts = Parts(cat_rows)
    kits, pcs = load_cg()

    kres = match_kits(kits, parts)
    pres = [match_pc(r[1], parts) for r in pcs]

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

    # -------- KITS
    L.append('\n## Kits de actualización (CPU + Mother)\n')
    L.append('Estado: 🟢 exacto · 🟡 sustituto (misma familia/socket) · 🔴 falta la pieza.\n')
    L.append('| Kit Compra Gamer | Socket | Tu CPU | Tu Mother | Precio combo (u$s) |')
    L.append('|---|---|---|---|--:|')
    def ico(s): return {'EXACTO':'🟢','SUSTITUTO':'🟡','FALTA':'🔴'}[s]
    # ordenar: armables primero, por socket
    for k in sorted(kres, key=lambda k:(not k['armable'], k['socket'] or 'zz', -(TIER.get(k['cpu_model'],0)))):
        cg = re.sub(r'^Kit (Mother |Procesador )?', '', k['cg'])[:60]
        cpu_txt = f"{ico(k['cpu_status'])} {k['cpu'][3][:34]}" if k['cpu'] else f"🔴 falta {k['cpu_model'] or '?'}"
        mb_txt  = f"{ico(k['mb_status'])} {k['mb'][3][:34]}" if k['mb'] else '🔴 falta mother'
        L.append(f"| {cg} | {k['socket'] or '?'} | {cpu_txt} | {mb_txt} | {money(k['price'])} |")

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
        L.append(f"\n**{p['cg']}** — {money(p['price'])}")
        for k in ['cpu','mb','ram','ssd','gpu','case','psu']:
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
