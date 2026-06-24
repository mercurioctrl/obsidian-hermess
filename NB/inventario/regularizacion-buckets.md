# Regularización — buckets de delta (cc4)

Clasificación de los items de cc4 con delta ≠ 0: si la **lógica los cierra** (confiar en el ledger de seriales + restaurar docs faltantes que aún tienen `pedprol`/venta) o si son **reales para recontar**. Método: identidad `delta = INB(ingreso) − HELD(stock) − OUT(salida)` vs el ledger de seriales. Ver [[modulo-regularizacion]]. Snapshot 2026-06-23.

> CSV completo (1.365 filas) fuera de la bóveda: `/Users/hermess/www/inventario/regularizacion_buckets_cc4.csv`

## Resumen

| bucket | items | u delta | qué hacer |
|---|--:|--:|---|
| auto_stock | 24 | 292 | **cerrar**: reconciliar stock↔serial (confiar ledger) — sin recuento |
| auto_con_doc | 62 | -1126 | **cerrar**: reconciliar stock + restaurar albprol/albclil (pedprol/venta existe) |
| casi_cero | 268 | 170 | ruido (|delta|≤2) — ignorar |
| recontar | 74 | 1073 | **RECUENTO FÍSICO** (ledger inconsistente) |
| revisar_legacy | 7 | -1943 | seriales sin albprol NI pedprol (legacy) — no recuperable por doc |
| revisar_doc | 502 | -46259 | revisión documental (sobre-doc / legacy sin serializar) |
| no_serializado | 428 | -1167339 | granel/servicio — lente columnas de stock |

**Auto-cerrables desde la lógica: 86 items** · **A recontar (físico): 74 items**

## Auto-cerrables — solo reconciliar stock↔serial

| itemId | SKU | título | delta | HELD |
|--:|---|---|--:|--:|
| 116467 | M022-10-000178 | ACCESORIOS EVGA BRACKET IO INTEL | 100 | -100 |
| 116343 | PVS48G320C6 | MEMORIA PATRIOT DDR4 8GB 3200MHZ | 50 | -50 |
| 104560 | IT-DSX | SOPORTE ADAPTADOR INTELAID PARA  | 15 | -15 |
| 117251 | 710425578687 | JUEGO PLAYSTATION PS5 GRAND THEF | 14 | -14 |
| 7425 | KB-PZX-KBBLUS-01 | TECLADO TT ESPORTS TECL MECHANIC | 12 | -13 |
| 119161 | NV-X120FWP | COOLER FAN 120mm ARGB PMW RAIDMA | 12 | -12 |
| 103768 | IT-DST | SOPORTE INTELAID PORTA NOTEBOOK  | 10 | -11 |
| 118224 | P400LP500GM28H | DISCO SSD PATRIOT P400 500 GB M. | 9 | -9 |
| 116938 | TN-2370 | BROTHER TONER TN2370 | 9 | -9 |
| 109025 | PVS48G360C8 | MEMORIA PATRIOT VIPER 4 STEEL SE | 8 | -8 |
| 115804 | AHV320-2TU31-CBK | DISCO EXTERNO ADATA HV320 2 TB 3 | 7 | -6 |
| 116344 | PVE2416G320C8 | MEMORIA PATRIOT DDR4 VIPER ELITE | 6 | -6 |
| 116357 | AD4S266664G19-SGN | MEMORIA ADATA SODIMM DDR4 4 GB 2 | 6 | -5 |
| 121519 | FE-SX19F2 | MONITOR SOLARMAX 18.5 VGA/HDMI N | 5 | -5 |
| 101703 | KVR24N17S8/8 | MEMORIA KINGSTON DDR4 8G SDRAM 2 | 4 | -4 |
| 118216 | PVV532G700C32K | MEMORIA PATRIOT VIPER VENOM DDR5 | 4 | -4 |
| 118534 | DKON2161ST-RUSPDMIWHHC2 | TECLADO MECANICO DUCKY ONE 3 MIN | 4 | -4 |
| 118929 | PVER516G60C42W | MEMORIA PATRIOT DDR5 VIPER ELITE | 4 | -5 |
| 118215 | PVV532G740C36K | MEMORIA PATRIOT VIPER VENOM DDR5 | 4 | -4 |
| 118537 | DKON2187-RESPDMAEGGC1 | Teclado Mecanico Ducky One 3 TKL | 3 | -3 |
| 118154 | 4250366851709 | GIGASET TELEFONO INALAMBRICO A17 | 3 | -3 |
| 118155 | 4250366851716 | GIGASET TELEFONO INALAMBRICO A17 | 3 | -3 |
| 118540 | DKON2167ST-RESPDABAAAC1 | TECLADO MECANICO DUCKY ONE 3 DAY | 3 | -3 |
| 118491 | TUF GAMING A620M-PLUS WIFI | MOTHER ASUS (AM5) TUF GAMING A62 | -3 | 3 |

## Auto-cerrables — reconciliar + restaurar doc

| itemId | SKU | título | delta | acción | pedprol |
|--:|---|---|--:|--:|--:|
| 170 | H500 | ATOMLUX ESTABILIZADOR ESTABILI | -907 | reconciliar-stock+restaurar-albprol(OC 1465u)+restaurar-albclil(verificar cobrada) | 1465 |
| 119724 | B550M K 1.0 | MOTHER GIGABYTE (AM4) B550M K | -196 | restaurar-albprol(OC 200u) | 200 |
| 5199 | O5150AMD | OUTLET AMD ATHLON 5150 1.6 GHB | -141 | restaurar-albprol(OC 155u) | 155 |
| 2983 | NDMP07B | PORTARETRATO DIGITAL NOVATECH  | -133 | reconciliar-stock+restaurar-albprol(OC 4u)+restaurar-albclil(verificar cobrada) | 4 |
| 104814 | 220-GA-0850 | FUENTE GAMER EVGA 850W SUPERNO | -110 | reconciliar-stock+restaurar-albprol(OC 2145u)+restaurar-albclil(verificar cobrada) | 2145 |
| 111539 | KVR26S19S6/4 | MEMORIA KINGSTON DDR4 SODIMM 4 | 100 | restaurar-albclil(verificar cobrada) | 150 |
| 101756 | GP-P650B | FUENTE GAMER GIGABYTE 650W 80  | 64 | reconciliar-stock+restaurar-albprol(OC 3180u)+restaurar-albclil(verificar cobrada) | 3180 |
| 119143 | 100-100001405WOF | PROCESADOR AMD (AM5) RYZEN 5 9 | 60 | reconciliar-stock+restaurar-albprol(OC 930u)+restaurar-albclil(verificar cobrada) | 930 |
| 103753 | CTB-800AP-LCD | LYONN UPS CTB-800AP LCD | -53 | restaurar-albprol(OC 527u) | 527 |
| 4504 | 31100061105 | GENIUS GRAPHIC TABLET EASYPEN  | -50 | reconciliar-stock+restaurar-albprol(OC 3660u)+restaurar-albclil(verificar cobrada) | 3660 |
| 119141 | 100-100001404WOF | PROCESADOR AMD (AM5) RYZEN 7 9 | 40 | reconciliar-stock+restaurar-albprol(OC 793u)+restaurar-albclil(verificar cobrada) | 793 |
| 118945 | B450M HDV R4.0 | MOTHER ASROCK (AM4) B450M HDV  | -39 | restaurar-albprol(OC 100u) | 100 |
| 2304 | SH-S203D/BEW | SAMSUNG DVD-RW SATA 20X MARFIL | -32 | reconciliar-stock+restaurar-albprol(OC 10u)+restaurar-albclil(verificar cobrada) | 10 |
| 109553 | GP-P850GM | FUENTE GAMER GIGABYTE 850W MOD | 31 | restaurar-albclil(verificar cobrada) | 1280 |
| 116738 | FQC-10553 | SOFTWARE MICROSOFT WINDOWS 11  | -30 | restaurar-albprol(OC 204u)+restaurar-albclil(verificar cobrada) | 204 |
| 104654 | PSD48G320081 | MEMORIA PATRIOT SIGNATURE LINE | 29 | reconciliar-stock+restaurar-albprol(OC 5500u)+restaurar-albclil(verificar cobrada) | 5500 |
| 108961 | 220-GA-0750 | FUENTE GAMER EVGA 750W SUPERNO | 28 | restaurar-albprol(OC 2018u)+restaurar-albclil(verificar cobrada) | 2018 |
| 117543 | NT01SA500-240-S3X | DISCO SSD NETAC SA500 2.5 SATA | 25 | reconciliar-stock+restaurar-albprol(OC 14400u)+restaurar-albclil(verificar cobrada) | 14400 |
| 104833 | ARXGU-80PBZ-650W | FUENTE GAMER AUREOX 650W BRONZ | 19 | reconciliar-stock+restaurar-albprol(OC 9004u)+restaurar-albclil(verificar cobrada) | 9004 |
| 104965 | GP-P750GM | FUENTE GAMER GIGABYTE 750W MOD | 16 | restaurar-albprol(OC 4460u)+restaurar-albclil(verificar cobrada) | 4460 |
| 117544 | NT01SA500-480-S3X | DISCO SSD NETAC SA500 2.5 SATA | 15 | reconciliar-stock+restaurar-albprol(OC 8000u)+restaurar-albclil(verificar cobrada) | 8000 |
| 117249 | 711719547624 | JUEGO PLAYSTATION HORIZON FORB | 14 | restaurar-albclil(verificar cobrada) | 14 |
| 102464 | ASU650SS-480GT-R | DISCO SSD ADATA SU650 2.5 480  | 14 | reconciliar-stock+restaurar-albprol(OC 5650u)+restaurar-albclil(verificar cobrada) | 5650 |
| 106746 | 100-100000063WOF | PROCESADOR AMD (AM4) RYZEN 7 5 | 13 | reconciliar-stock+restaurar-albclil(verificar cobrada) | 1044 |
| 117527 | G27F 2 AR | MONITOR GAMER GIGABYTE 27 G27F | -13 | restaurar-albprol(OC 132u)+restaurar-albclil(verificar cobrada) | 132 |
| 104473 | ASWORDFISH-500G-C | DISCO SSD ADATA 500 GB M.2 228 | 12 | reconciliar-stock+restaurar-albprol(OC 830u)+restaurar-albclil(verificar cobrada) | 830 |
| 101812 | GP-G750H | FUENTE GAMER GIGABYTE 750W 80  | 11 | reconciliar-stock+restaurar-albprol(OC 351u)+restaurar-albclil(verificar cobrada) | 351 |
| 6848 | SENTEY APHELION GS-3520 | MOUSE GAMER SENTEY APHELION GS | 9 | restaurar-albclil(verificar cobrada) | 60 |
| 104129 | PVB416G360C7K | MEMORIA PATRIOT VIPER 16 GB DD | 7 | restaurar-albclil(verificar cobrada) | 120 |
| 109350 | PVR416G360C8K | MEMORIA PATRIOT VIPER RGB 16 G | 6 | restaurar-albclil(verificar cobrada) | 110 |
| 116913 | G27FC A-SA | MONITOR GAMER GIGABYTE 27 G27F | 6 | restaurar-albclil(verificar cobrada) | 354 |
| 104806 | A520M DS3H | MOTHER GIGABYTE (AM4) A520M DS | 6 | restaurar-albclil(verificar cobrada) | 315 |
| 116766 | GV-R66EAGLE-8GD | PLACA DE VIDEO GIGABYTE RADEON | 6 | restaurar-albprol(OC 460u)+restaurar-albclil(verificar cobrada) | 460 |
| 119896 | DESIRE-500KS | LYONN UPS DESIRE-500KS | -6 | restaurar-albprol(OC 48u)+restaurar-albclil(verificar cobrada) | 48 |
| 1574 | OENDSL-A2 | OUTLET ROUTER ENCORE ADSL ENDS | -5 | reconciliar-stock+restaurar-albprol(OC 1u) | 1 |
| 116785 | B550 PHANTOM GAMING 4/AC | MOTHER ASROCK (AM4) B550 PHANT | 5 | restaurar-albprol(OC 172u)+restaurar-albclil(verificar cobrada) | 172 |
| 7677 |  | ELEPHONE TELEFONO P8000 4G SIL | 5 | restaurar-albprol(OC 95u)+restaurar-albclil(verificar cobrada) | 95 |
| 104141 | P300P512GM28US | DISCO SSD PATRIOT P300 512 GB  | 5 | restaurar-albclil(verificar cobrada) | 200 |
| 111411 | H510M H | MOTHER GIGABYTE (LGA1200) H510 | 5 | reconciliar-stock+restaurar-albprol(OC 3130u)+restaurar-albclil(verificar cobrada) | 3130 |
| 119104 | GS27F-SA | MONITOR GAMER GIGABYTE 27 GS27 | 5 | restaurar-albclil(verificar cobrada) | 460 |
| 103313 | AS40G-1TT-C | DISCO SSD ADATA 1 TB SPECTRIX  | 5 | restaurar-albclil(verificar cobrada) | 480 |
| 100865 | DT50/32GB | PEN DRIVE KINGSTON DT50/32GB | 5 | restaurar-albclil(verificar cobrada) | 151 |
| 109531 | ASX8100NP-1TT-C | DISCO SSD ADATA XPG 1 TB 8100  | -4 |  | 340 |
| 118745 | AX4U360016G18I-ST60 | MEMORIA ADATA DIMM XPG SPECTRI | 4 |  | 50 |
| 101962 | MO-IRS-WDOHBK-01 | MOUSE GAMER TT ESPORTS IRIS RG | 4 | restaurar-albclil(verificar cobrada) | 240 |
| 106801 | A520 AORUS ELITE | MOTHER GIGABYTE (AM4) A520 AOR | 4 |  | 100 |
| 6447 | BXP75-OR | FUENTE SENTEY 750W BXP75-OR OU | -4 | restaurar-albprol(OC 191u) | 191 |
| 117258 | WDS480G3G0A | DISCO SSD SATA 480GB WD GREEN | -4 | restaurar-albprol(OC 4040u)+restaurar-albclil(verificar cobrada) | 4040 |
| 117988 | B650 AORUS ELITE AX 1.1 | MOTHER GIGABYTE (AM5) B650 AOR | -4 | restaurar-albprol(OC 68u)+restaurar-albclil(verificar cobrada) | 68 |
| 119259 | GP-UD750GM PG5 | FUENTE GAMER GIGABYTE 750W PG5 | 4 | restaurar-albclil(verificar cobrada) | 710 |
| 121239 | DIR-822 | D-LINK ROUTER DIR-822  AC1200  | -4 | restaurar-albprol(OC 10u) | 10 |
| 115803 | ASU650SS-960GT-R | DISCO SSD ADATA SU650 2.5 960  | 3 | reconciliar-stock+restaurar-albprol(OC 3280u)+restaurar-albclil(verificar cobrada) | 3280 |
| 103236 | AORUS CV27F-SA | MONITOR GAMER GIGABYTE CURVO L | 3 | restaurar-albclil(verificar cobrada) | 78 |
| 109634 | 22015 | PARLANTE BARRA DE SONIDO TRUST | -3 |  | 150 |
| 117195 | PVSR416G360C0K | MEMORIA PATRIOT RGB 16GB 2X8 3 | 3 |  | 50 |
| 103818 | 22793 | MOUSE GAMER TRUST GAV JUNGLE G | 3 | restaurar-albprol(OC 260u)+restaurar-albclil(verificar cobrada) | 260 |
| 118806 | ARX420G | GABINETE GAMER AUREOX PHOBOS A | 3 |  | 552 |
| 103046 | JS00T5010K6 | MOCHILA JANSPORTS SUPERBREAK N | 3 |  | 9 |
| 118288 | H610M-HDV/M.2R2.0 | MOTHER ASROCK (LGA1700) H610M- | 3 | restaurar-albclil(verificar cobrada) | 200 |
| 121149 | SLEG-860-1000GCS | DISCO SSD 1TB ADATA LEGEND 860 | 3 |  | 600 |
| 111605 | GC1000 | TECLADO y MOUSE + PAD AUREOX L | 3 |  | 1000 |
| 100565 | 31731062100 | PARLANTE PORTATIL BLUETOOTH GE | 3 | restaurar-albprol(OC 592u)+restaurar-albclil(verificar cobrada) | 592 |

## Para recontar (físico) — ledger inconsistente

| itemId | SKU | título | delta | creados | presentes |
|--:|---|---|--:|--:|--:|
| 3497 | 31710037100 | AURICULAR + MIC HEADSET GENIUS H | -697 | 10509 | 1437 |
| 102462 | ASU650SS-120GT-R | DISCO SSD ADATA SU650 2.5 120 GB | 692 | 8392 | 479 |
| 103319 | SFX-GC783 | GABINETE SFX KIT 783 BLACK | 396 | 12324 | 4614 |
| 4999 | 31710011100 | AURICULAR + MIC HEADSET GENIUS H | -100 | 6534 | 188 |
| 102894 | SFX-GC782 | GABINETE SFX KIT 782 BLACK | -75 | 12263 | 5779 |
| 103837 | 21947 | MOUSE TRUST ZIVA | 73 | 2244 | 3 |
| 101260 | TR2-600NL2NC | FUENTE GAMER THERMALTAKE TR2 600 | 66 | 15560 | 49 |
| 6065 |  | MEMORIA NOVATECH DDR3 4GB 1600 M | 61 | 1722 | 530 |
| 103840 | 22051 | TECLADO TRUST ZIVA MEDIA ES | 52 | 801 | 5 |
| 101266 | TR2-500NL2NC | FUENTE GAMER THERMALTAKE TR2 500 | 51 | 12217 | 905 |
| 7666 | SFX-SC541A | GABINETE SFX KIT 541 BLACK PLUS  | 46 | 85 | 1 |
| 103041 | NEREID ARX 320G | GABINETE GAMER AUREOX NEREID ARX | 41 | 1644 | 7 |
| 116825 | 31300012401 | TECLADO USB GENIUS LUXEMATE 110  | 40 | 2000 | 0 |
| 103037 | FC-F50A | GABINETE OFFICE AUREOX 110S | 39 | 45 | 2 |
| 103424 | 31330003401 | TECLADO + MOUSE COMBO USB GENIUS | 39 | 7906 | 35 |
| 2233 | NOVATECH DDR 128MB 333 MHBOX | MEMORIA NOVATECH DDR 128 MB 333  | -30 | 32 | 5 |
| 102489 | SFX-GC785 | GABINETE SFX KIT 785 BLACK SLIM | 29 | 2535 | 2103 |
| 103042 | HYDRA ARX 330G | GABINETE GAMER AUREOX HYDRA ARX  | 29 | 15 | 0 |
| 103835 | 23270 | TECLADO Y MOUSE TRUST ZIVA MULTI | 29 | 578 | 0 |
| 106759 | 100000065BOX | PROCESADOR AMD (AM4) RYZEN 5 560 | 22 | 2771 | 8 |
| 104249 | CM-5832 | GABINETE KIT SOLARMAX CM-5832 | 21 | 5 | 0 |
| 104585 | 23278 | TECLADO TRUST MUTO SILENT ES | 20 | 653 | 4 |
| 103040 | ALBORYX ARX 310G | GABINETE GAMER AUREOX ALBORYX AR | 19 | 1062 | 2 |
| 102626 | F4-2133C15S-4GIS | MEMORIA GSKILL  AEGIS DDR4 4 GB  | 17 | 94 | 10 |
| 104836 | RZ01-03340100-R3U1 | MOUSE GAMER RAZER DEATHADDER V2  | 17 | 3507 | 19 |
| 101006 | A4U450 | GABINETE SFX RACKEABLE A4U450 SE | 15 | 1208 | 0 |
| 103607 | HEBE-ARX-340G | GABINETE GAMER AUREOX HEBE ARX 3 | 14 | 514 | 0 |
| 103168 | 31010105102 | MOUSE GENIUS DX-120 G5 WHITE USB | 13 | 13701 | 9 |
| 101400 | LC27F390FHLX | MONITOR SAMSUNG LED 27 CURVO F39 | 13 | 455 | 22 |
| 103039 | EUPHORY ARX 300G | GABINETE GAMER AUREOX EUPHORY AR | -12 | 799 | 1 |
| 100469 | KB-CPC-MBBRSP-01 | TECLADO GAMER TT ESPORTS COMBO C | 12 | 888 | 136 |
| 103097 | HS-SSD-C100 240G | DISCO SSD HIKVISION C100 2.5 240 | 10 | 150 | 0 |
| 113155 | PBE960GS25SSDR | DISCO SSD PATRIOT BURST ELITE SO | 10 | 4123 | 362 |
| 101950 | KB-GCK-PLBLSP-01 | TECLADO GAMER TT ESPORTS KNUCKER | 9 | 405 | 3 |
| 103312 | AS40G-512GT-C | M.2 ADATA 512 GB SPECTRIX XPG S4 | 9 | 905 | 4 |
| 106820 | PRIME A520M-K | MOTHER ASUS (AM4) PRIME A520M-K | 9 | 8119 | 445 |
| 103814 | 21843 | TECLADO GAMER TRUST THURA SEMI E | 8 | 387 | 60 |
| 104131 | PVB416G300C6K | MEMORIA PATRIOT VIPER 4 DDR4 16  | 7 | 61 | 1 |
| 100682 |  | TECLADO ELEPHONE ELEENTER GAME2  | 7 | 11 | 0 |
| 102623 | 31040063101 | MOUSE GAMER GX GAMING SCORPION M | 7 | 361 | 219 |
| 115245 | 834-W0-12SP | TECLADO GAMER EVGA Z12 RGB ESP | 7 | 1683 | 10 |
| 6145 |  | MEMORIA NOVATECH DDR3 8GB 1600 M | 6 | 594 | 287 |
| 104843 | 23712 | AURICULAR TRUST PRIMO TOUCH BT B | 6 | 1164 | 518 |
| 101306 | 31710025100 | AURICULAR + MIC HEADSET GENIUS H | 6 | 5766 | 92 |
| 100589 | CA-H442C-M8 | OUTLET GABINETE GAMER NZXT H440  | -5 | 1 | 0 |
| 6396 | 31100060102 | GENIUS GRAPHIC TABLET MOUSEPEN I | 5 | 3035 | 20 |
| 7421 | CA-N450W-W1 | OUTLET GABINETE GAMER NZXT NOCTI | 4 | 3 | 0 |
| 109304 | RZ01-03580100-R3U1 | MOUSE GAMER RAZER VIPER 8KHZ AMB | 4 | 1793 | 1 |
| 101660 | CH-9304011-NA | MOUSE GAMER CORSAIR SCIMITAR PRO | -3 | 222 | 1 |
| 104276 | P200S1TB25 | DISCO  SSD PATRIOT P200 SOLID 1  | 3 | 41 | 0 |
| 101708 | CA-H700W-BB | OUTLET GABINETE GAMER NZXT H700i | 3 | 3 | 0 |
| 104275 | PBU480GS25SSDR | DISCO SSD PATRIOT BURST SOLID 48 | 3 | 253 | 0 |
| 104326 | 22312 | TECLADO GAMER TRUST TECLADO+MOUS | 3 | 664 | 9 |
| 327 |  | MOUSE SOLTECH BOLITA SCROLL | -2 | 25 | 20 |
| 108991 | 31250012400 | APOYA MUÑECAS PAD TECLADO GENIUS | 2 | 2364 | 948 |
| 116356 | AUSDH32GUICL10A1-RA1 | MICRO SD ADATA  A1 DH CLASS 10 3 | 2 | 1450 | 96 |
| 104508 | DKSA11-USPDYNWO1 | SET 11 TECLAS DUCKY YELLOW PBT C | 2 | 62 | 34 |
| 109620 | 23825 | PARLANTE TRUST ZOWY MAX BLUETHOO | -1 | 165 | 0 |
| 5954 | MO-TRP-WDLOBK-06 | MOUSE GAMER TT ESPORTS THERON PL | -1 | 258 | 65 |
| 6627 | CA-H630F-W1 | GABINETE GAMER NZXT H630 WHITE | -1 | 2 | 0 |
| 104297 | KVR1333DN9/2G | OUTLET MEMORIA KINGSTON DDR3 CL9 | -1 | 2 | 2 |
| 109352 | PBE240GS25SSDR | DISCO SSD PATRIOT BURST ELITE SO | -1 | 21091 | 651 |
| 104504 | DKON1887-RUSPDZHBS | Teclado Mecanico Ducky One 2 TKL | 1 | 15 | 2 |
| 103821 | 21813 | MOUSE GAMER TRUST HERON RGB GXT  | -1 | 90 | 0 |
| 111409 | B550M DS3H 1.0 | MOTHER GIGABYTE (AM4) B550M DS3H | -1 | 1312 | 1 |
| 103038 | FC-F61A | GABINETE OFFICE AUREOX 130S | 1 | 31 | 0 |
| 104831 | ARXGP-600W | FUENTE GAMER AUREOX 600W PSU ARX | -1 | 6814 | 2364 |
| 101717 | RZ07-02270100-R3U1 | TECLADO KEYPAD GAMER RAZER TARTA | 1 | 288 | 0 |
| 104490 | DKON1787ST-RUSPDWWT1 | TECLADO GAMER DUCKY ONE 2 RGB TK | 1 | 5 | 0 |
| 119117 | NT01SA500-960-S3X | DISCO SSD NETAC SA500 2.5 SATA3  | 1 | 3601 | 794 |
| 100561 | 31040063103 | MOUSE GAMER GX GAMING SCORPION M | -1 | 244 | 36 |
| 104496 | DKON1967ST-RUSPDWWT1 | TECLADO GAMER DUCKY ONE 2 SF RGB | 1 | 16 | 0 |
| 102117 | F4-3000C16D-16GTZR | MEMORIA GSKILL TRIDENT DDR4 3000 | 1 | 115 | 0 |
| 117370 | 31330006402 | TECLADO + MOUSE COMBO USB GENIUS | 1 | 5400 | 1076 |

## Legacy sin doc recuperable (seriales sin albprol ni pedprol)

| itemId | SKU | título | delta |
|--:|---|---|--:|
| 2120 |  | ALPS FLOPPY 1.44 3 1/2 | -1376 |
| 104550 |  | MINI PC BRIX CELERON 240G 4GB | -321 |
| 116094 |  | PC MINI STX INTEL I5 8G 240G | -167 |
| 116095 |  | PC MINI STX INTEL i7 8G 240G | -50 |
| 2526 |  | LINKSYS PLACA RED PCMCIA WPC54G | -14 |
| 5475 |  | SOPORTE LUXA2 H5 CAR-MOUNT | -9 |
| 2062 | SMWVB | SOFTWARE MICROSOFT WINDOWS VISTA HOM | -6 |

## Notas
- **revisar_doc (502)** y **no_serializado (428, −1,17M concentrado en pocos como art 102157 ≈ −1M)**: no son recuento — legacy/granel, lente distinta.
- **cc11/cc9 quedan fuera**: no serializan ([[modulo-regularizacion]]).

## Estado de ejecución (2026-06-23)

- **`auto_stock` (24) APLICADOS en prod**: repuestos a Control (`nstock_ctrl`, 295 u) con línea en `registro_stock` (marcador "Regularizacion stock recuperable (seriales presentes)", agente Catriel, en lote). 22/24 a delta 0; 2 (115804, 116357) en delta 1 (recuperable capado a seriales).
- **`auto_con_doc` (62) NO se sostiene** — corrección: el cierre limpio por albprol (estilo 11568) es raro. Solo ~2 tienen `pedprol > albprol` (OC real sin documentar) y con delta positivo (sobre-corrigen al restaurar). Los ~35 "restaurar-albprol" tienen `pedprol ≤ albprol` → el gap son seriales SIN documento (legacy), no restaurable. **No tratar este bucket como auto-cerrable; re-clasificar.**

## Ver también
- [[modulo-regularizacion]] · [[inventario]] · [[changelog]]
