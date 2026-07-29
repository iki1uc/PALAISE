import { T6D } from "./TEM6D.js";
import DB from "./DB.universal";
import { UWM } from "./UTM.js";

export const PALAISE_TRUTHFLOW = {

  run(name){

    const human = DB.human[name];
    const universal = DB.universal[name];

    const truth = UWM.analyze(name, human, universal);

    const real = T6D.t[2];
    const drift = Math.abs(T6D.t[1] - T6D.t[2]);
    const stability = T6D.t[0] > T6D.t[2] ? "ALT-dominant" : "REAL-dominant";

    let epoche = "Unbekannt";
    if(real < 0.000050) epoche = "Paläozän";
    else if(real < 0.000040) epoche = "Eozän";
    else if(real < 0.000030) epoche = "Oligozän";

    const move = {
      order: "asc",
      filter: truth.delta > 0 ? "myth" : "truth",
      highlight: truth.delta,
      style: drift > 0.1 ? "neon-pulse" : "neon",
      mode: stability,
      epoche,
      state: "ACTIVE"
    };

    const respo = {
      name,
      mythLevel: truth.mythLevel,
      missingTruth: truth.delta,
      drift,
      stability,
      epoche,
      status: "TRUTHFLOW 6D ACTIVE"
    };

    return { truth, move, respo };
  }
};
