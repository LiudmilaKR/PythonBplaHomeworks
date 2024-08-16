const express = require("express");
const app = express();
const PORT = 3001;

app.get("/time", (req, res) => {
    const currentTime = new Date();
    console.log(currentTime);
    console.log(currentTime.getDate());
    console.log(currentTime.getFullYear());
    res.json(currentTime)
});

app.listen(PORT, () => {
    console.log("Сервер запущен!")
});