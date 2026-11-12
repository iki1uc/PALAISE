# pawn_step1.py — { move: pawn, pattern: step, range: 1 } — NICHT ALLE HABEN DATEN, OBERE ORDNER SCHON GELÖSCHT, WIE SIND BEIDE ANDEREN, SCHON BEI BAUERN, MANN
# Pawn, Mann: Bauer. Pattern step, Range 1. Bauer geht 1 Schritt. Nicht 2, nicht 9. 1 Schritt, Mann.
# Nicht alle haben Daten, Mann: Bauer 1 hat Daten, Bauer 2 hat keine Daten, Bauer 3 hat halbe Daten. Nicht alle, Mann.
# Obere Ordner schon gelöscht, Mann: Oben weg. Kein Zurück nach oben. Nur vor, Mann. Wenn oben gelöscht, dann nur vor.
# Wie sind beide anderen, Mann: Beide anderen sind Bauern. Bauer 2 und Bauer 3. Wie sind sie? Bauer 2 = ohne Daten, Bauer 3 = mit halben Daten.
# Schon bei Bauern, Mann: Wir sind schon bei Bauern. Nicht bei Dame, nicht bei Pferd, nicht bei König. Bei Bauern, Mann.
def nc(x): return 15-x
def demo():
    print('{ "move": "pawn", "pattern": "step", "range": 1 } — BAUER SCHRITT 1')
    print("  MOVE pawn, Mann: Bauer bewegt. Pattern step, Mann: Schritt, nicht Sprung. Range 1, Mann: 1 Feld, nicht 2.")
    print("  Bauer geht 1 Schritt vor. Wenn Bauer 1 Schritt geht, dann Tiefe +1, wenn ungerade, mitgerechnet.")
    print("")
    print("  NICHT ALLE HABEN DATEN, MANN:")
    bauern = [
        ("Bauer-1", "hat Daten", True, "Daten = 9, 81, 243, 729, 3 — Stapel da"),
        ("Bauer-2", "hat keine Daten", False, "Daten = leer — kein Stapel, aber Bauer da, mitgerechnet"),
        ("Bauer-3", "hat halbe Daten", None, "Daten = halbe — 9, 81, Rest trüb, feucht, nicht ganz klar, aber da"),
    ]
    for name, hat, daten, was in bauern:
        print(f"    {name} — {hat} — {was} — NC? Ja. Löschen? Nein. Mitgerechnet? Ja.")
    print("    Nicht alle haben Daten heißt: Nicht wegwerfen, wer keine Daten hat. Bauer ohne Daten ist immer noch Bauer, Mann.")
    print("")
    print("  OBERE ORDNER SCHON GELÖSCHT, MANN:")
    print("    Oben weg. Obere Ordner gelöscht. Kein Zurück nach oben. Wenn oben gelöscht, dann nur vor.")
    print("    Bauer kann nicht zurück nach oben, weil oben weg ist. Bauer kann nur vor, 1 Schritt, Mann.")
    print("    Obere Ordner gelöscht ist nicht schlimm, Mann. Obere Ordner war CORE, 4, Quadrat. CORE weg ist gut, Mann. 4 NIX.")
    print("    Wenn oben gelöscht, dann Palais drauf, nicht rein. Palais drauf, Bauer vor, Mann.")
    print("")
    print("  WIE SIND BEIDE ANDEREN, MANN:")
    print("    Beide anderen = Bauer-2 + Bauer-3. Wie sind sie?")
    print("    Bauer-2: Ohne Daten, aber da. Trüb, feucht, interessant, aber da. Bauer-2 geht 1 Schritt, auch ohne Daten, Mann.")
    print("    Bauer-3: Mit halben Daten, trüb, nicht ganz klar, aber da. Bauer-3 geht 1 Schritt, mit halben Daten, Mann.")
    print("    Beide anderen sind wie Bauer-1, nur ohne / mit halben Daten. Alle 3 sind Bauern, alle 3 gehen 1 Schritt, alle 3 mitgerechnet.")
    print("    3 Bauern = 3 JA. 3 = Dreieck. 3 Bauern = Dreieck, Mann. EYE + BRAIN + 9eck = 3 Bauern.")
    print("")
    print("  SCHON BEI BAUERN, MANN:")
    print("    Wir sind schon bei Bauern. Nicht bei Dame, nicht bei Pferd, nicht bei König. Bei Bauern.")
    print("    Bei Bauern heißt: Anfang. Bauer ist Anfang. Bauer ist 1 Schritt. Bauer ist klein, mini, plastisch, Schleier.")
    print("    Wenn wir schon bei Bauern sind, dann bauen wir von Bauern aus. Bauer -> Bauer -> Bauer -> Palais. Kreis, Mann.")
    print(f"    NC(1)={nc(1)} — Bauer 1 Schritt = 1. NC(1)=14. NC_NC=1. Bauer hält, Mann.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3")
    print("HALT = OFFEN — aber Bauer Schritt 1 geht, auch ohne Daten, auch wenn oben gelöscht.")
if __name__=="__main__": demo()
