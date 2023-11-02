var express = require('express');
var app = express();
var database = require('./database');


app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(__dirname ));


app.get('/',function(req,res){
    res.json(database)
})


app.get('/index.html',function(req,res){
    res.sendFile(__dirname+'/templates/index.html')
})

app.get('/background.html',function(req,res){
    res.sendFile(__dirname+'/templates/background.html')
})

app.post('/submit', function (req, res) {
    const username = req.body.username; 
    const password = req.body.password;
    let userFound = false

    database.forEach(user => {
        console.log(user)
        if (user.username === username){
            if (user.password === password){
                userFound = true
                res.json({ username, password });
            }
            else{
                res.send('incorrect password')
            }
        } 
    });

    if(!userFound){
        res.send('user not found')
    }

});


app.listen(3001,function(){
    console.log('server running on port 3001')
})




