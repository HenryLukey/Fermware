const stripped = msg.payload.replace("\n", "");

flow.set("originalGrav", stripped);

const enableBtn = false;

if (stripped === "") {
    const enableBtn = true;
}

const newMsg = { payload: stripped, enable: enableBtn }

return newMsg;