// (Voltage.actual - 3)/(Voltage.max - Voltage.min) * 100 = % battery left
const batteryPercent = ((parseFloat(msg.payload) - 3) / (4.1 - 3) * 100).toFixed(0);
const newMsg = { payload: batteryPercent };
return newMsg;