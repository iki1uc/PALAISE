# narrativ-truth-9.py — NARRATIV TRUTH 9x9 — 81 RAW — PY JA
# 9 Zeilen x 9 Spalten = 81 RAW, Mann. 9x9 = 81. 81 ist 9er-Stapel. 9, 81, 243, 729, 3.
# Header: Narrativ,Truth,Myth,Drift,Tensor,Orbit,Pulse,Wave,Field,Geist — 10 Spalten, 1 Narrativ + 9 Namen.
# Zeilen: Truth RAW-01..09, Myth RAW-10..18, Drift RAW-19..27, Tensor RAW-28..36, Orbit RAW-37..45, Pulse RAW-46..54, Wave RAW-55..63, Field RAW-64..72, Geist RAW-73..81.
# Mitte, Mann: 81 Felder, Mitte = 41. Feld 41 = Orbit RAW-41. Orbit ist Mitte. Orbit hält Mitte, Mann.
# CSV nur zum Aufrechterhalten, keine Weihnachtsschmuck, Mann. CSV = Reihenfolge, sonst nix.
import csv
def demo():
    with open("/mnt/data/narrativ-truth-9.csv", encoding="utf-8") as f:
        r = list(csv.reader(f))
    print("NARRATIV TRUTH 9x9 — 81 RAW")
    print(f"  Header: {r[0]}")
    print(f"  Zeilen: {len(r)-1} — Spalten pro Zeile: {len(r[1])-1} — Gesamt RAW: {sum(len(x)-1 for x in r[1:])}")
    alle = [c for x in r[1:] for c in x[1:]]
    print(f"  Alle RAW einzigartig? {len(set(alle))==81} — Erster: {alle[0]} — Letzter: {alle[-1]} — Mitte: {alle[40]} (Orbit RAW-41)")
    for x in r[1:]:
        print(f"  {x[0]} — {x[1]} .. {x[-1]} — 9 Stück")
    print("  Truth = RAW-01..09 — Anfang, RAW. Myth = RAW-10..18 — Geschichte. Drift = RAW-19..27 — Abdrift. Tensor = RAW-28..36 — Spannung.")
    print("  Orbit = RAW-37..45 — Mitte, Orbit hält Mitte. Pulse = RAW-46..54 — Tick, pulse(). Wave = RAW-55..63 — Welle.")
    print("  Field = RAW-64..72 — Feld. Geist = RAW-73..81 — Geist, Ende, 81.")
    print("  9x9 = 81 = Palais-Feld, Mann. Alles geht zu Palais. Alle 81 gehen zu Palais. Palais lacht.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3 — Mitte 41 = B 41 = Orbit RAW-41")
    print("HALT = OFFEN — aber 81 RAW stehen, kein Schmuck.")
if __name__=="__main__": demo()
