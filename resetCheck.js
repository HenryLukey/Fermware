let enable = false;
const content = msg.payload.replace("\n", "");

if (content === "true" || content === "") {
    enable = true;
}

const newMsg = { enabled: enable };

return newMsg;