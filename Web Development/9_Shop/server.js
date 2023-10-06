var express = require('express')
var bodyParser = require('body-parser')
var mongoos = require('mongoose')

var app = express()
var db = mongoos.connect('mongodb://127.0.0.1:27017/shop-database')

var Product = require('./model/product')
var WishList = require('./model/wishlist')

app.use(bodyParser.json())


/////////////////////     Product    //////////////////////

app.get('/product',async function(req,res){

    try{
    res.send(await Product.find({}))
    } catch (error){
        res.status(500).send({ error: 'Unable to fetch' });
    }

})

app.get('/product/:id',async function(req,res){
    var id = req.params.id;
    try{
    res.send(await Product.find({}))
    } catch (error){
        res.status(500).send({ error: 'Unable to fetch' });
    }

})

app.post('/product',async function(req,res){
    var product = new Product()

    console.log(req.body)

    if (!req.body.title || !req.body.price){
        res.status(500).send({"err":'make sure yr product is as below:',"correctFormat":{
            "title": "String",
            "price": "Number"
        }})
    }
    product.title = req.body.title
    product.price = req.body.price

    try{
    savedProduct = await product.save()
    res.send(savedProduct)

    } catch(err){
        res.status(500).send({ error: 'File was not saved' });
    }
})




app.delete('/product',async function(req,res){
    var products = await Product.deleteMany({})
    var products = await Product.find({})
    res.send(products)
})



/////////////////////     WishList    //////////////////////

app.get('/wishlist',async function(req,res){
    res.send(await WishList.find({}))
})


app.post('/wishlist',async function(req,res){
    var wishlist = new WishList()
    wishlist.title = req.body.title
    res.send(await wishlist.save())
})


app.put('/wishlist/product/add',async function(req,res){
    try{
        my_product = await Product.findOne({_id:req.body.productId})
        res.send(my_product)
    } catch(error){
        res.status(500).send({ error: 'Product ID was not found' });
    }
    
})




app.listen(3000,function(){
    console.log("Shop's API running on 127.0.0.1:3000")
})
