const { Connection } = require('../database');

const mongoConnection = (req, res, next) => {
    Connection
        .then(() => next())
        .catch(err => next(err))
}

module.exports = mongoConnection;