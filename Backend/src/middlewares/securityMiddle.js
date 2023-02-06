const createError = require('http-errors');
const jwt = require('jsonwebtoken')
const logger = require("log4js").getLogger("aplication");


const ACCESS_TOKEN = process.env.ACCESS_TOKEN


function authenticateToken(req, res, next) {
    const authHeader = req.headers.authorization
    const token = authHeader && authHeader.split(' ')[1]
    if (token == null) return next(createError(401))
    jwt.verify(token, ACCESS_TOKEN, (err, decoded) => {
        if (err) return next(createError(403))
        return  next()
    })
}


function endPointError(err, req, res, next) {
    if (err.name && err.name === "ValidationError") {
        res.status(406).json(err)
    }
    else if ((err.status === 404) || (err.name === "CastError")) {
        res.status(404).json({
            url: req.originalUrl,
            error: { message: 'Not found' }
        })
    } else if ((err.status === 11000) || (err.name === "CastError")) {
        res.status(404).json({
            url: req.originalUrl,
            error: { message: 'Duplicate key not allowed' }
        })
    } else {
        logger.error(err);
        res.status(err.status || 500).json({
            url: req.originalUrl,
            error: { message: 'Not informed' }
        })
    }
}


module.exports = {
    endPointError,
    authenticateToken,
}

