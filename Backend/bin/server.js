const app = require('../src/index')
const server = require('http').Server(app)
const log4js = require("log4js");


log4js.configure({
  appenders: { cheese: { type: "file", filename: "logs/cheese.log" } },
  categories: { default: { appenders: ["cheese"], level: process.env.LEVEL_LOG || "error" } },
});

//useDatabase(HOSTMONGO, MONGOBD);


// LINK TO SERVICES
const PORT = process.env.PORT || 3000
const HOST = process.env.HOST || 'localhost'
ports = `
------------------- ROUTERS -----------------------------
Api in            = http://${HOST}:${PORT}
MongoDb in        = http://${HOST}:27017/
Storage Files in  = http://${HOST}:9001/login
---------------------------------------------------------
`
// console.log(process.env)

server.listen(PORT, () => console.log(ports));
