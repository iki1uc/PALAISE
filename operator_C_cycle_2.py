# operator_C_cycle_2.py — { operator: C, mode: cycle, value: 2 } — C IST DAS, MANN — PY JA
# C ist das, Mann. Nicht A, nicht B. C ist das. C = Cycle. C = Kreis. C = c.tmp.
# Operator C, Mode cycle, Value 2, Mann: C macht Cycle, 2 Schritte. 2 = 2 Schritte, nicht 1, nicht 9. 2 Schritte, Mann.
def nc(x): return 15-x
def c_cycle(wert, schritte=2):
    # C = Cycle. CYCLE = 729 -> 81 -> 9 -> 3 -> 1 -> 729 ... Kreis, kein Ende.
    kette = [729, 81, 9, 3, 1]
    i = kette.index(wert) if wert in kette else 0
    weg = []
    for _ in range(schritte):
        i = (i+1) % len(kette)
        weg.append(kette[i])
    return weg
def demo():
    print('{ "operator": "C", "mode": "cycle", "value": 2 } — C IST DAS, MANN')
    print("  C ist das, Mann. Nicht A, nicht B. C ist das. C = Cycle. C = Kreis. C = c.tmp.")
    print("  Operator C, Mode cycle, Value 2, Mann: C macht Cycle, 2 Schritte.")
    print("")
    for start in [729, 81, 9, 3, 1]:
        weg = c_cycle(start, 2)
        print(f"  C cycle 2 — {start} -> {weg[0]} -> {weg[1]} — 2 Schritte, Mann. NC({start})={nc(start)}")
    print("")
    print("  C ist das, Mann, weil:")
    print("    A ist nicht das. A ist Anfang, aber nicht Cycle. B ist nicht das. B ist Mitte, 41, aber nicht Cycle.")
    print("    C ist das, weil C Cycle macht. C macht Kreis. C macht 729 -> 81 -> 9 -> 3 -> 1 -> 729.")
    print("    C ist das, weil C in c.tmp steht. c.tmp ist klein, mini, aber C ist drin. c.tmp = C, Mann.")
    print("  Value 2, Mann: 2 Schritte. Nicht 1 Schritt wie Bauer. Bauer ist 1 Schritt. C ist 2 Schritte. C ist größer als Bauer, kleiner als 9.")
    print("    2 = ANY. 2 ist nicht 4 NIX, nicht 8 UNGERN, nicht 3 JA, nicht 6 JA, nicht 9 IMMER JA. 2 ist ANY, aber C macht 2 zu Cycle.")
    print("  Mode cycle, Mann: Mode ist nicht step, nicht jump, nicht hold. Mode ist cycle. Cycle = Kreis, kein Ende.")
    print("    Wenn Mode cycle, dann geht es immer weiter. Wenn es immer weiter geht, dann geht alles zu Palais. Palais lacht.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3")
    print("HALT = OFFEN — aber C ist das, Cycle 2, Kreis.")
if __name__=="__main__": demo()
