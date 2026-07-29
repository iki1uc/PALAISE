export function PALAISE_raw_6D(canvasId, truth){
    const c = document.getElementById(canvasId);
    const ctx = c.getContext("2d");

    const { ALT, GHOST, REAL } = truth.time6d.vector;
    const epoche = truth.epoche; // hinzugefügt

    ctx.clearRect(0,0,c.width,c.height);

    ctx.fillStyle = "#0f0";
    ctx.fillText("ALT: " + ALT.toFixed(6), 20, 40);
    ctx.fillText("GHOST: " + GHOST.toFixed(6), 20, 80);
    ctx.fillText("REAL: " + REAL.toFixed(6), 20, 120);

    ctx.fillStyle = "#6cf";
    ctx.fillText("Projected: " + truth.time6d.projected.toFixed(6), 20, 160);

    ctx.fillStyle = "#fc0";
    ctx.fillText("Epoche: " + epoche, 20, 200);
}
<canvas id="hud6d" width="400" height="240"></canvas>

<script type="module">
import { PALAISE_RESPO } from "./PALAISE.RESPO.js";
import { PALAISE_raw_6D } from "./PALAISE.raw.js";

async function runHUD(){
    const truth = await PALAISE_RESPO.truth("BEN");
    PALAISE_raw_6D("hud6d", truth);
}
setInterval(runHUD, 200);
</script>
