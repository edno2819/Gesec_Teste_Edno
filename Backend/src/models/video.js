const { Schema, model } = require('mongoose')

const videoSchema = new Schema({
    title: {
        type: String,
        required: true,
        unique: true,
        minLength: 2
    },
    thumbnail: {
        type: String,
        required: true,
        minLength: 2
    },
    video: {
        type: String,
        required: true,
        minLength: 2
    },
    description: {
        type: String,
        minLength: 2
    },
    createdAt: {
        type: Date,
        default: Date.now,
    },
    updatedAt: {
        type: Date,
        default: Date.now,
    },
})

module.exports = model('Video', videoSchema)