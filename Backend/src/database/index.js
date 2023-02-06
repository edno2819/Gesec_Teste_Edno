const mongoose = require("mongoose");


const options = {
    dbName: process.env.MONGO_DATABASE,
    connectTimeoutMS: 1000,
};

const connect = mongoose.connect(process.env.MONGO_URL, options)

mongoose.connection.on("error", () => {
    console.error(`Mongo not connected!`);
});
mongoose.connection.on("connected", () => {
    console.warn(`Mongo connected!`);
});
mongoose.connection.on("disconnected", () => {
    console.error(`Mongo disconnected!`);
});

exports.Video = require("../models/video.js");
exports.User = require("../models/user.js")

exports.Connection = connect;