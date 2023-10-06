var mongoose = require('mongoose')
var Schema = mongoose.Schema // the structure of database
var ObjectId = mongoose.Schema.Types.ObjectId

var wishlist = new Schema({
    title: {type: String, default: "A wishlist"},
    products: [{type: ObjectId, ref:'Product'}] //ObjectId is has to be a mongo object, ref we link to Prodcut instance from the db
})

module.exports = mongoose.model('WishList',wishlist)