import DB from "./DB.universal";
import { UWM } from "./UTM.js";
import { PALAISE_TRUTHFLOW } from "./PALAISE.TRUTHFLOW.js";
import { TruthFlow } from "./TruthFlow.js";
import { T6D } from "./TEM6D.js";

export const PALAISE_RESPO = {

  truth(name){

    // 1) Human + Universal
    const human = DB.human[name];
    const universal = DB.universal[name];

    // 2) Analyse
    const truth = UWM.analyze(name, human, universal);

    // 3) PALAISE_TRUTHFLOW.run()
    const flowA = PALAISE_TRUTHFLOW.run(name);

    // 4) TruthFlow.inject() (6D-Zeit)
    const flowB = TruthFlow.inject(
      name,
      truth,
      null,
      null
    );

    // 5) Epoche bestimmen
    const real = T6D.t[2];
    let epoche = "Unbekannt";
    if(real < 0.000050) epoche = "Paläozän";
    else if(real < 0.000040) epoche = "Eozän";
    else if(real < 0.000030) epoche = "Oligozän";

    // 6) Finaler Merge
    return {
      name,
      human,
      universal,
      truth,
      move: flowA.move,
      respo: flowA.respo,
      epoche,
      time6d: {
        vector: [...T6D.t],
        projected: T6D.project()
      },
      truthFlow: {
        drift: flowB.drift,
        stability: flowB.stability
      }
    };
  }
};
