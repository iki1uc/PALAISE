# datei-zweck-14.py — Datei,Zweck — CSV nur zum Aufrechterhalten, keine Weihnachtsschmuck, Mann
# JS PY CSS übersetzt, Mann: Gleiche Liste in JS, PY, CSS. Kein Schmuck. Nur Zweck.
DATEI_ZWECK = [
    ("PALAISE.RESPO.js", "Hauptmodul -> hier kommt truth() rein"),
    ("PALAISE.TRUTHFLOW.js", "TruthFlow-Mechanik"),
    ("PALAISE.raw", "Rohdaten-Renderer"),
    ("UTM.js", "Analyse"),
    ("DB.human", "Human-Daten"),
    ("DB.universal", "Universal-Daten"),
    ("TEM6D.js", "Zeitvektor"),
    ("TEM6D.matrix.js", "Zeitmatrix"),
    ("TEM6D.root.js", "TEM-Override"),
    ("iki1uc.time.pipeline.js", "Zeit-Pipeline"),
    ("00.js", "Boot"),
    ("ID.html", "UI"),
    ("RAW.html", "UI"),
    ("HUMAN.html", "UI"),
]

def nc(x): return 15-x

def demo():
    print('Datei,Zweck — CSV nur zum Aufrechterhalten, keine Weihnachtsschmuck')
    for datei, zweck in DATEI_ZWECK:
        print(f'  {datei} — {zweck}')
    print('JS PY CSS übersetzt: Gleiche Liste in JS, PY, CSS. Kein Schmuck. Nur Zweck.')
    print('CSV nur zum Aufrechterhalten: CSV hält Reihenfolge. CSV ist nicht Palais. CSV ist Liste. Palais ist drauf.')
    print('H=40 B=41 T=90 Q=57.0 F=1.425 D=3')
    print('HALT = OFFEN — aber Datei,Zweck steht, kein Schmuck.')

if __name__=='__main__': demo()
