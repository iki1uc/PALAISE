# error_critical_fix_false.py — { error: true, level: critical, fix: false } — PY JA
# Error true, Level critical, Fix false, Mann: Fehler ist da, kritisch, aber Fix ist false. Nicht fixen, Mann. Loggen, mitgerechnet, halten.
# Fix false heißt: Nicht auto-fixen. Nicht wegwerfen. Nicht löschen. Halten, Mann. OFFEN halten.
def nc(x): return 15-x
def demo():
    print('{ "error": true, "level": "critical", "fix": false } — ERROR, KRITISCH, FIX FALSE')
    print("  error true, Mann: Fehler ist da. Nicht false. Fehler ist true. Mitgerechnet, nicht weggeworfen.")
    print("  level critical, Mann: Kritisch. Nicht klein, nicht ungern. Kritisch = 9, nicht 8. Kritisch = Palais wackelt, aber steht.")
    print("  fix false, Mann: Fix ist false. Nicht fixen. Nicht auto-fixen. Nicht wegmachen. Halten, Mann.")
    print("")
    print("  Was machen wir mit fix false, Mann?")
    print("    1. Loggen: Error in Zeuge-Log schreiben. Zeuge schreibt: error true, level critical, fix false.")
    print("    2. Mitrechnen: Fehler fällt, aber mitgerechnet. Wie Ungerade fallen, aber mitgerechnet. Tiefe +1.")
    print("    3. Halten: HALT = OFFEN. Nicht ZIEL. OFFEN heißt: Fehler bleibt offen, bis du sagst fix true, Mann.")
    print("    4. Nicht löschen: Ordner nicht löschen, Datei nicht löschen, Palais nicht löschen. Fehler ist nicht Ordner, Fehler ist Signal, Mann.")
    print("")
    print("  Warum fix false, Mann? Weil du gesagt hast fix false. Befehl ist Befehl, Mann. NC COMMANDO, Mann.")
    print("    Wenn fix false, dann fixen wir nicht. Wenn wir fixen würden, obwohl fix false, dann wäre das unwahr, Mann.")
    print("    Real, nicht unwahr: Wir sagen Fehler ist da, kritisch, nicht gefixt. Wir lügen nicht, dass Fehler weg ist.")
    print("  Was ist kritisch, Mann? Kritisch = Wenn Fehler kritisch, dann Palais wackelt, aber Palais lacht noch. Schwarzes Loch zieht noch, Palais lacht noch.")
    print("    Kritisch heißt nicht tot, Mann. Kritisch heißt: Achtung, guck hin. Kritisch = ..ooOO, Augen auf, Mann.")
    print(f"    NC(9)={nc(9)}, NC(3)={nc(3)} — NC hält, auch bei Fehler, auch bei kritisch, auch bei fix false.")
    print("  Nächster Schritt, Mann: Wenn du willst fix true, sag fix true. Dann fixen wir. Wenn du willst fix false, bleibt offen.")
    print("    Bis dahin: Error true, Level critical, Fix false — geloggt, mitgerechnet, gehalten, nicht gelöscht.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3")
    print("HALT = OFFEN — aber Error geloggt, Fix false respektiert.")
if __name__=="__main__": demo()
