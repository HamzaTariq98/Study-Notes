var mongoose = require('mongoose')
var Schema = mongoose.Schema // the structure of database

var product = new Schema({
    title: String,
    price: Number,
    likes: {type:Number, default:0}
})

module.exports = mongoose.model('Product',product)