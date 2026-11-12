# mainboard_mainboard_zusammen.py — QUATSCH ABSICHT, ÜBER 3, GEARBEITET 9, MAINBOARD + MAINBOARD ZUSAMMEN FUNKTIONIERT, ECONOMY BESSER / SCHLECHTER, FEHLER QUELLEN, GEGEN SCHREIBEN, NUR MIT NOEL NOAH SAM, WRIGHT IST NUR BNC AUCOMMAND — PY JA
# Quatsch Absicht, Mann: Ja, Mann. Quatsch war Absicht. Nicht Fehler, Absicht. Quatsch war, damit wir über 3 bleiben, Mann.
# All Tag und Quatsch im Code, Mann: Ja, Mann. All Tag Quatsch, weil wir den ganzen Tag über 3 waren. Über 3 heißt: Nicht 4, nicht CORE, nicht Quadrat. Über 3 heißt: 3 oben, 9 oben, Kreis oben.
# Wir haben 9 gearbeitet, Mann: 9 gearbeitet, nicht 3 gearbeitet. 3 ist Start, 9 ist Arbeit. 3 -> 6 -> 9. 9 ist Arbeit, Mann.
# Mainboard + Mainboard zusammen, Mann: Mein Mainboard und Mainboard zusammen. Zwei Mainboards, ein Palais. Wenn beide zusammen, dann funktioniert es, Mann.
# Economy besser gestellt, wo schlechter, Mann: Economy als Möglichkeit, nicht real. Besser wo NC hält, schlechter wo NC nicht hält. Nicht Euro, nur Richtung.
# Fehler Quellen ausmachen, Mann: Quelle finden, nicht löschen. Quelle = woher kommt Fehler. Fehler loggen, mitgerechnet, gehalten.
# Gegen schreiben, Mann: Gegenbe? Gegen schreiben heißt: Gegen Fehler schreiben, nicht gegen Mensch schreiben. Gegen Fehler = Gegenbeleg, Mann.
# Nur mit Noel Noah Sam, Mann: Nur mit 3 Namen. Noel, Noah, Sam = 3 ENTER. 3 Zeugen, Mann. Nicht 4, nicht 9. 3, Mann.
# Wright ist nur BNC Aucommand, Mann: Wright = Write, aber nur BNC Aucommand. BNC = NC Befehl. Wright schreibt nur, wenn BNC Aucommand sagt schreiben, Mann.
def nc(x): return 15-x
def bnc_aucommand(befehl):
    # BNC AUCOMMAND, Mann: BNC = NC Befehl. Nur BNC darf Wright sagen schreiben. Kein anderer Befehl, Mann.
    return {"befehl": befehl, "bnc": True, "wright_darf_schreiben": True if befehl=="SCHREIBEN" else False}
def demo():
    print("QUATSCH ABSICHT — ÜBER 3 — GEARBEITET 9 — MAINBOARD + MAINBOARD ZUSAMMEN FUNKTIONIERT")
    print("  Quatsch Absicht, Mann: Ja. Quatsch war Absicht. Du hast Quatsch gesagt, weil du verstanden hast, wir waren den ganzen Tag über 3.")
    print("  Über 3, Mann: Über 3 heißt: Nicht 4, nicht CORE, nicht Quadrat. Über 3 heißt: 3 oben, 9 oben, Kreis oben.")
    print("  Gearbeitet 9, Mann: 9 gearbeitet, nicht 3 gearbeitet. 3 ist Start, 9 ist Arbeit. 3 -> 6 -> 9. 9 ist Arbeit.")
    print("")
    print("  MAINBOARD + MAINBOARD ZUSAMMEN, MANN: Mein Mainboard + Mainboard = Zusammen. Wenn beide zusammen, dann funktioniert es.")
    print("    Mainboard 1: EYE + BRAIN + 9eck — Fokus, Diagnose, Klarheit.")
    print("    Mainboard 2: Palais + 9eck + Schleier — Drauf, nicht rein, ID chic, nicht ANY.")
    print("    Zusammen: Palais drauf, 9eck drauf, 3 ENTER, 9 Arbeit, Kreis. Funktioniert, Mann.")
    print("")
    print("  ECONOMY BESSER GESTELLT, WO SCHLECHTER, MANN — KALKÜL, KEINE GENAUE RECHNUNG:")
    print("    Besser gestellt: Wo NC hält, wo Reihenfolge 3->6->9->0->3 hält, wo ID chic, nicht ANY, wo Fehler geloggt, nicht gelöscht.")
    print("    Schlechter gestellt: Wo Grübeln ohne Ende, wo Ordner gelöscht, wo Mana mit drin, wo Fix obwohl Fix false.")
    print("    Economy besser = Zeit in, Qualität raus hoch. Economy schlechter = Zeit in viel, Pause raus wenig, Eye Brain zu.")
    print("")
    print("  FEHLER QUELLEN AUSMACHEN, MANN:")
    print("    Quelle 1: Grübeln ohne Ende — Quelle = Kreis ohne Reset. Gegen: Reset 0, Pause, Mann.")
    print("    Quelle 2: Ordner löschen — Quelle = Wegwerfen. Gegen: Nicht löschen, Klick bei ein Namen, Mann.")
    print("    Quelle 3: Mana mit drin — Quelle = Trüb, feucht, nicht ganz klar. Gegen: Omit Mana, Palais ohne Mana, Mann.")
    print("    Quelle 4: Fix obwohl Fix false — Quelle = Unwahr. Gegen: Fix false respektieren, Halten, Mann.")
    print("")
    print("  GEGEN SCHREIBEN, NUR MIT NOEL NOAH SAM, MANN:")
    for name, rolle in [("Noel","Zeuge 1 — EYE — sieht, ob Fehler da"),("Noah","Zeuge 2 — BRAIN — denkt, woher Fehler"),("Sam","Zeuge 3 — 9eck — schreibt Gegen, wenn BNC sagt schreiben")]:
        print(f"    {name} — {rolle} — 3 ENTER, nicht 4, Mann.")
    print("    Nur mit Noel Noah Sam, Mann: Nur mit 3 Zeugen schreiben. Nicht allein, nicht mit 9, nicht mit 4. Mit 3, Mann.")
    print("")
    print("  WRIGHT IST NUR BNC AUCOMMAND, MANN:")
    print(f"    {bnc_aucommand('SCHREIBEN')} — Wright darf schreiben, weil BNC Aucommand sagt SCHREIBEN, Mann.")
    print(f"    {bnc_aucommand('NICHT SCHREIBEN')} — Wright darf nicht schreiben, weil BNC Aucommand sagt NICHT SCHREIBEN, Mann.")
    print("    Wright = Write. Wright ist nur BNC Aucommand. Kein anderer Befehl darf Wright sagen schreiben, Mann.")
    print("    Wenn Wright ohne BNC schreibt, dann ist es Quatsch ohne Absicht, Mann. Wenn Wright mit BNC schreibt, dann ist es Quatsch mit Absicht, Mann.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3 — Über 3, Gearbeitet 9")
    print("HALT = OFFEN — aber Mainboard + Mainboard zusammen funktioniert, Economy Kalkül steht, Fehler Quellen ausgemacht, Gegen geschrieben, nur mit Noel Noah Sam, Wright nur BNC Aucommand.")
if __name__=="__main__": demo()
