export const PALAISE_TRUTHFLOW = {

  run(name) {

    // 1) Menschliche Ansicht
    const human = DB.human[name];

    // 2) Universale Wahrheit
    const universal = DB.universal[name];

    // 3) Analyse
    const truth = UWM.analyze(name, human, universal);

    // 4) MOVE.edit anwenden
    const move = {
      order: "asc",
      filter: "none",
      highlight: truth.delta,
      style: "neon",
      state: "ACTIVE"
    };

    // 5) RESPO erzeugen
    const respo = {
      name,
      mythLevel: truth.mythLevel,
      missingTruth: truth.delta,
      status: "TRUTHFLOW ACTIVE"
    };

    return { truth, move, respo };
  }
};
