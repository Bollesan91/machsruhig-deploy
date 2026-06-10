# -*- coding: utf-8 -*-
# Generator: Bundesland-Vergleichsdaten fuer /bestattungskosten-nach-bundesland
# Rechnet EXAKT wie tools/bestattungskosten-rechner (per-Item-Rundung, Default-State):
#   Default-State: sargQualitaet=mittel, grabGrab=Einzelgrab, KEINE Extras
#   (aufbahrung/trauerfeier/blumenschmuck/grabstein/traueranzeige = false)
#   Grabpflege inklusive (wie Tool-Default-Output).
# Quelle: tools/bestattungskosten-rechner/index.html (REGIONAL_MULTIPLIERS, KOSTENMODELL)
# jround = JS Math.round (half-up), NICHT Python round() (banker's rounding).
import math

def jround(x):
    return int(math.floor(x + 0.5))

MULT = {
    'Baden-Wuerttemberg': 1.20, 'Bayern': 1.22, 'Berlin': 1.15, 'Brandenburg': 0.80,
    'Bremen': 1.05, 'Hamburg': 1.20, 'Hessen': 1.15, 'Mecklenburg-Vorpommern': 0.78,
    'Niedersachsen': 1.02, 'Nordrhein-Westfalen': 1.05, 'Rheinland-Pfalz': 0.95,
    'Saarland': 0.90, 'Sachsen': 0.82, 'Sachsen-Anhalt': 0.78, 'Schleswig-Holstein': 0.95,
    'Thueringen': 0.80
}

FEUER = [(1800,3200),(600,1800),(300,550),(50,150),(80,400),(300,1500),(250,600)]
FEUER_GP = (40,150,10)
ERD = [(2000,3500),(800,2200),(600,2800),(300,800)]
ERD_GP = (80,250,20)

def total(items, gp, m):
    mn = sum(jround(a*m) for a,b in items) + jround(gp[0]*m)*gp[2]
    mx = sum(jround(b*m) for a,b in items) + jround(gp[1]*m)*gp[2]
    return mn, mx

def r50(x):  # auf 50 EUR runden fuer "ca."-Darstellung
    return int(jround(x/50.0)*50)

def de(n):
    return '{:,}'.format(n).replace(',', '.')

rows = []
for bl, m in MULT.items():
    rows.append((bl, m, total(FEUER, FEUER_GP, m), total(ERD, ERD_GP, m)))
rows.sort(key=lambda r: (-r[1], r[0]))

print('%-22s %5s  %-20s %-20s' % ('Bundesland','Idx','Feuer ca.','Erd ca.'))
for bl,m,f,e in rows:
    print('%-22s %5d  %7s-%-8s %7s-%-8s' % (bl, jround(m*100), de(r50(f[0])), de(r50(f[1])), de(r50(e[0])), de(r50(e[1]))))

by, mv = MULT['Bayern'], MULT['Mecklenburg-Vorpommern']
fby, fmv = total(FEUER,FEUER_GP,by), total(FEUER,FEUER_GP,mv)
eby, emv = total(ERD,ERD_GP,by), total(ERD,ERD_GP,mv)
print('\n--- Headline-Claims ---')
print('Faktor-Verhaeltnis BY/MV: %.4f => +%.1f %%' % (by/mv, (by/mv-1)*100))
print('Feuer BY ca. %s-%s | MV ca. %s-%s' % (de(r50(fby[0])),de(r50(fby[1])),de(r50(fmv[0])),de(r50(fmv[1]))))
print('Erd   BY ca. %s-%s | MV ca. %s-%s' % (de(r50(eby[0])),de(r50(eby[1])),de(r50(emv[0])),de(r50(emv[1]))))
print('Erd-Mitte BY %d vs MV %d => Diff %d EUR (+%.0f%%)' % (
    (eby[0]+eby[1])//2,(emv[0]+emv[1])//2,(eby[0]+eby[1])//2-(emv[0]+emv[1])//2,
    ((eby[0]+eby[1])/(emv[0]+emv[1])-1)*100))
# Spanne aller 16
allf = [total(FEUER,FEUER_GP,m) for m in MULT.values()]
print('Feuer guenstigste-Mitte %d (MV/ST) ... teuerste-Mitte %d (BY)' % (
    min((a+b)//2 for a,b in allf), max((a+b)//2 for a,b in allf)))
