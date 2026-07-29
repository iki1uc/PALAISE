import { NC_HUB_ALL } from "./NC_HUB_ALL.js";
import { T6D } from "./TEM6D.js";

export function PALAISE_TIME(name){

    const hub = NC_HUB_ALL();

    const D0 = hub.hub6D.D0;
    const D1 = hub.hub6D.D1;
    const D2 = hub.hub6D.D2;

    let epoche = "Unbekannt";
    if(D2 < 0.000050) epoche = "Paläozän";
    else if(D2 < 0.000040) epoche = "Eozän";
    else if(D2 < 0.000030) epoche = "Oligozän";

    const drift = Math.abs(D1 - D2);

    return {
        name,
        epoche,
        time6d: {
            vector: [D0, D1, D2],
            projected: T6D.project()
        },
        drift,
        stability: D0 > D2 ? "ALT-dominant" : "REAL-dominant"
    };
}
