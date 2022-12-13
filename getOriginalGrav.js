const recent = flow.get("currentGrav");
flow.set("originalGrav", recent);
const newMsg = { payload: recent };
return msg;