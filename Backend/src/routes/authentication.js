const router = require("express").Router();
const bcrypt = require("bcrypt")
const jwt = require("jsonwebtoken")
const createError = require("http-errors");

const { User } = require("../database");


router
    .route("/register")
    .post((req, res, next) => Promise.resolve()
        .then(() => bcrypt.hash(req.body.password, 10))
        .then(passwordHashed => {
            new User({ ...req.body, password: passwordHashed }).save()
            .then(() => res.status(201).json({ message: `User created` }))
            .catch((err) => next(err))
        })
        .catch((err) => next(err)))



router
    .route("/login")
    .post((req, res, next) => Promise.resolve()
        .then(() => User.findOne({ user: req.body.user }))
        .then(data => {
            data ? bcrypt.compare(req.body.password, data.password)
                .then(passwordHash => {
                    var token = {
                        accessToken: jwt.sign({
                            user: data.user,
                        }, process.env.ACCESS_TOKEN)
                    }
                    passwordHash ? res.status(201).json(token) : next(createError(401))
                }) : next(createError(401))
        })
        .catch((err) => next(err)))



module.exports = router