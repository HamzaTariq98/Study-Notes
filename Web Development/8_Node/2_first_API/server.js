var express = require('express')
var bodyparser = require('body-parser')
var app = express()



var ingredients = [
    {
        'id':1,
        'text': 'Eggs',
    },
    {
        'id':2,
        'text': 'Milk',
    },
    {
        'id':3,
        'text': 'Meat',
    },
    {
        'id':4,
        'text': 'Flour',
    }
]

var id = 4

// Body-parser middleware, middleware like a filter for the GET request to pass through before it get to us

app.use(bodyparser.json())
app.use(bodyparser.urlencoded({ extended: false }))

app.get('/ingredients',function(request,response){
    response.send(ingredients)
})

app.post('/ingredients',function(req,res){
    id +=1
    var ingredient = req.body
    if(!ingredient || ingredient.text===""){
        res.status(500).send({error:'your ingredient must have text'})
    } else{
        ingredients.push({'id':id,'text':ingredient.text})
        res.status(200).send(ingredients)
    }
})

app.put('/ingredients/:ingredientId', function(req,res){
    var ingredientId = parseInt(req.params.ingredientId)
    var index = ingredients.findIndex(item => item.id === ingredientId)
    
    if (index === -1){ 
        res.status(404).send({error:'id '+ingredientId+' is not in ingredient list'})
    }

    var text = req.body.text
    
    if (!text || text === ""){
        res.status(500).send({error:'your ingredient must have text'})
    }

    ingredients[index].text = text
    res.status(200).send(ingredients)
})


app.delete('/ingredients/:ingredientId', function(req,res){
    var ingredientId = parseInt(req.params.ingredientId)
    var index = ingredients.findIndex(item => item.id === ingredientId)
    
    if (index === -1){ 
        res.status(404).send({error:'id '+ingredientId+' is not in ingredient list'})
    }
    
    ingredients.splice(index, 1); // Remove 1 element at the found index
    res.status(200).send(ingredients);
})

app.listen(3000,function(){
    console.log('First API running on port 3000')
})