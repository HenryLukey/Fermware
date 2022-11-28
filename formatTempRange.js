const max = parseInt(flow.get("maxTemp"));
let min = parseInt(flow.get("minTemp"));

if (min > max) {
    min = max - 1;
}
const toWrite = `${min},${max}`;

const newMsg = { payload: toWrite };

return newMsg;