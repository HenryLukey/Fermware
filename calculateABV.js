// Check if there is an originalGravity in context
// If not then check if there is originalGravity in file
// If not then return payload of "Not configured"

const originalGravity = flow.get("originalGrav") || "";
let abvPercent = "Not yet calculated!";

if (originalGravity !== "") {
    let abv = ((originalGravity - parseFloat(msg.payload)) * 131.25);
    if (abv < 0) {
        abv = 0;
    }
    abv = abv.toFixed(2);
    abvPercent = abv + "%";
}

const newMsg = { payload: abvPercent };
return newMsg;