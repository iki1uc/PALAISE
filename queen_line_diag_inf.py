# queen_line_diag_inf.py — { move: queen, pattern: line+diag, range: inf } — DAME, MANN — PY JA
# Dame, Mann: Queen. Pattern line+diag, Range inf. Dame geht Linie + Diagonale, unendlich im Modell, bis Rand im Feld, Mann.
# Bauer war 1 Schritt. C war 2 Schritte Cycle. Dame ist inf Schritte. Dame ist größer als Bauer, größer als C, Mann.
# Aber inf ist Modell, Mann. Nicht real unendlich. Im 9x9 Feld ist inf = bis Rand. Rand = 9. 9x9 = 81. Dame geht bis 9, Mann.
def nc(x): return 15-x
def demo():
    print('{ "move": "queen", "pattern": "line+diag", "range": "inf" } — DAME, MANN')
    print("  MOVE queen, Mann: Dame bewegt. Nicht Bauer, nicht C. Dame.")
    print("  PATTERN line+diag, Mann: Linie + Diagonale. Linie = gerade, Diagonale = schräg. Beides, Mann.")
    print("  RANGE inf, Mann: Unendlich im Modell. Im Feld 9x9 = bis Rand. Rand = 9. Inf = bis 9, Mann.")
    print("")
    print("  Dame von Mitte 41 aus, Mann: Mitte = 41, Orbit RAW-41, B 41.")
    print("    Linie oben: 41 -> 32 -> 23 -> 14 -> 5 — bis Rand oben, 4 Schritte, Mann.")
    print("    Linie unten: 41 -> 50 -> 59 -> 68 -> 77 — bis Rand unten, 4 Schritte, Mann.")
    print("    Linie links: 41 -> 40 -> 39 -> 38 -> 37 — bis Rand links, 4 Schritte, Mann.")
    print("    Linie rechts: 41 -> 42 -> 43 -> 44 -> 45 — bis Rand rechts, 4 Schritte, Mann.")
    print("    Diag oben-links: 41 -> 31 -> 21 -> 11 -> 1 — bis Ecke, 4 Schritte, Mann.")
    print("    Diag oben-rechts: 41 -> 33 -> 25 -> 17 -> 9 — bis Ecke, 4 Schritte, Mann.")
    print("    Diag unten-links: 41 -> 49 -> 57 -> 65 -> 73 — bis Ecke, 4 Schritte, Mann.")
    print("    Diag unten-rechts: 41 -> 51 -> 61 -> 71 -> 81 — bis Ecke, 4 Schritte, Mann.")
    print("    8 Richtungen, Mann. 8 = 2x4, ungern, aber Dame geht 8 Richtungen, weil Dame alles kann, Mann.")
    print("")
    print("  Bauer vs C vs Dame, Mann:")
    print("    Bauer: move pawn, pattern step, range 1 — 1 Schritt, klein, mini, Anfang.")
    print("    C: operator C, mode cycle, value 2 — 2 Schritte, Cycle, Kreis.")
    print("    Dame: move queen, pattern line+diag, range inf — bis Rand, 8 Richtungen, alles, Mann.")
    print("    Bauer ist klein, C ist Kreis, Dame ist alles, Mann. Dame ist nicht besser, Dame ist nur weiter, Mann.")
    print("  Dame ist nicht CORE, Mann. Dame ist 9eck, Palais. Dame geht zu Palais, wie alles zu Palais geht.")
    print(f"    NC(9)={nc(9)}, NC(41)={nc(41)} — NC hält, auch bei Dame, auch bei inf, Mann.")
    print("  Inf ist Modell, Mann. Nicht real unendlich. Im Feld ist inf = bis Rand. Rand ist 9. 9 ist IMMER JA.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3 — Mitte 41 = Dame Start")
    print("HALT = OFFEN — aber Dame geht line+diag, bis Rand, 8 Richtungen.")
if __name__=="__main__": demo()
