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
    import { T6D } from "./TEM6D.js";

export const TruthFlow = {
    inject(name, truth, matrix, koopPook){
        return {
            name,
            semantic: truth,
            timeVector: [...T6D.t],
            koopPook,
            drift: Math.abs(T6D.t[1] - T6D.t[2]),
            stability: T6D.t[0] > T6D.t[2] ? "ALT-dominant" : "REAL-dominant"
        };
    }
};


    return { truth, move, respo };
  }
};
import { T6D } from "./TEM6D.js";

export const TruthFlow = {
    inject(name, truth, matrix, koopPook){

        const real = T6D.t[2];

        let epoche = "Unbekannt";
        if(real < 0.000050) epoche = "Paläozän";     // 66–56 mya
        else if(real < 0.000040) epoche = "Eozän";   // 56–33.9 mya
        else if(real < 0.000030) epoche = "Oligozän"; // 33.9–23 mya

        return {
            name,
            semantic: truth,
            timeVector: [...T6D.t],
            koopPook,
            epoche,
            drift: Math.abs(T6D.t[1] - T6D.t[2]),
            stability: T6D.t[0] > T6D.t[2] ? "ALT-dominant" : "REAL-dominant"
        };
    }
};
