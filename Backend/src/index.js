const express = require("express");
const rfs = require('rotating-file-stream')
const createError = require("http-errors");
const bodyParser = require("body-parser");
const helmet = require("helmet");
const morgan = require("morgan");
const path = require('path')
const cors = require("cors")
const fileUpload = require('express-fileupload');

require('dotenv').config()

// Files import
const mongoConnection = require('./middlewares/database');
const Middles = require('./middlewares/securityMiddle');
const routers = require("./routes");


// create a rotating write stream
var accessLogStream = rfs.createStream('http.log', {
    interval: '1d',
    path: path.join(__dirname, 'logs')
})
bodyEncoded = bodyParser.urlencoded({ extended: true })


const app = express();


// Middlewares
app.use(cors())
app.use(helmet());
app.use(express.urlencoded({ extended: true }));
app.use(morgan(process.env.DEV || "dev", { stream: accessLogStream }))
app.use(express.static(path.join(__dirname, "public")))
app.use((req, res, next) => (/^multipart\//i.test(req.get('Content-Type'))) ? next() : bodyEncoded(req, res, next))
app.use(bodyParser.json({ defer: true }));
app.use(mongoConnection)
app.use(fileUpload())
app.use(express.static('uploads')); 

// Routers
app.use("/v1/authentication", routers.Authentication)
app.use("/v1/video", Middles.authenticateToken, routers.crudVideos)


// Erro Middlewares
app.use((req, res, next) => next(createError(404)));
app.use(Middles.endPointError)

module.exports = app;