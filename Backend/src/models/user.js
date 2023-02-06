const { Schema, model } = require('mongoose')


const userSchema = new Schema({
    user: {
        type: String,
        required: true,
        unique: true,
        minLength: 2
    },
    password: {
        type: String,
        required: true,
        minLength: 2
    },
})

module.exports = model('User', userSchema)