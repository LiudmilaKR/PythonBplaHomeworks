const express = require("express");
const arDrone = require("ar-drone");

const app = express();
const drone1 = arDrone.createClient();
const drone2 = arDrone.createClient({ ip: '192.168.1.2' });

app.get("/:droneId/takeoff", (req, res) => {
    const droneId = req.params.droneId;
    console.log(`Запрос на взлет для Дрона ${droneId}`);
    if (droneId == 1) drone1.takeoff();
    else if (droneId == 2) drone2.takeoff();
    res.json({ status: `Дрон ${droneId} взлетел` });
});

app.get("/:droneId/land", (req, res) => {
    const droneId = req.params.droneId;
    console.log(`Запрос на приземление Дрона ${droneId}`);
    if (droneId == 1) drone1.land();
    else if (droneId == 2) drone2.land();
    res.json({ status: `Дрон ${droneId} приземлился` });
});

app.listen(3001, () => {
    console.log("Сервер запущен!")
});

