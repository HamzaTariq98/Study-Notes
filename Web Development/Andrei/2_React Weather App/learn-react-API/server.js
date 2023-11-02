const mongoose = require('mongoose')
const express = require('express')
var bodyParser = require('body-parser')
const cors = require('cors');
const axios = require('axios');

const deffaultCard = require('./deffaultWeather')


const db = mongoose.connect('mongodb://127.0.0.1:27017/weather-users')

const app = express()
app.use(bodyParser.json())
app.use(cors());

let Schema = mongoose.Schema // the structure of database

let user = new Schema({
    email: String,
    locations: [String]
})

User = mongoose.model('User',user)



const fetchCardsData = async (locations) => {

    
    if (locations.length > 0){

    const apiKey = 'b3d41e2b4d9646dc9b4163603232710';
    let cardsObject = []
    
    for (const location of locations) {

        if (location !== 'Select Location'){
            try {
                let apiUrl = `https://api.weatherapi.com/v1/forecast.json?key=${apiKey}&q=${location}&days=6`;
                const response = await axios.get(apiUrl);
                newLocationName = response.data.location.name + '/'+ response.data.location.country
                if (newLocationName.length >30){
                    newLocationName = response.data.location.name
                }
                let cardObject = {
                    locationName: newLocationName,
                    days: [
                        {
                            day: 'Today',
                            weather: response.data.current.condition.icon,
                            tempreture: Math.round(response.data.current.temp_c)
                        },
                        {
                            day: response.data.forecast.forecastday[0].date,
                            weather: response.data.forecast.forecastday[0].day.condition.icon,
                            tempreture: Math.round(response.data.forecast.forecastday[0].day.avgtemp_c)
                        },
                        {
                            day: response.data.forecast.forecastday[1].date,
                            weather: response.data.forecast.forecastday[1].day.condition.icon,
                            tempreture: Math.round(response.data.forecast.forecastday[1].day.avgtemp_c)
                        },
                        {
                            day: response.data.forecast.forecastday[2].date,
                            weather: response.data.forecast.forecastday[2].day.condition.icon,
                            tempreture: Math.round(response.data.forecast.forecastday[2].day.avgtemp_c)
                        },
                        {
                            day: response.data.forecast.forecastday[3].date,
                            weather: response.data.forecast.forecastday[3].day.condition.icon,
                            tempreture: Math.round(response.data.forecast.forecastday[3].day.avgtemp_c)
                        },
                        {
                            day: response.data.forecast.forecastday[4].date,
                            weather: response.data.forecast.forecastday[4].day.condition.icon,
                            tempreture: Math.round(response.data.forecast.forecastday[4].day.avgtemp_c)
                        },
                        {
                            day: response.data.forecast.forecastday[5].date,
                            weather: response.data.forecast.forecastday[5].day.condition.icon,
                            tempreture: Math.round(response.data.forecast.forecastday[5].day.avgtemp_c)
                        }
                    ]
                }
                cardsObject.push(cardObject);
    
                } catch (error) {
                cardsObject.push(deffaultCard);
                    }
        } else {
            cardsObject.push(deffaultCard)
        }

    };
    return cardsObject
    
    }

    else {
        return []
        }
  };


  app.get('/get/ip/address', function (req, res) {
    userIp = req.socket.remoteAddress
    res.send('ip'+userIp)
})


app.get('/add/:email',async function(req,res){
    

    const userEmail = req.params.email
    console.log('user ip: ',userEmail)
    const existingUser = await User.findOne({ email: userEmail });
    if (existingUser) {
        console.log("just an old user :)");

        cardsData = await fetchCardsData(existingUser.locations)
        res.send(cardsData);
    } else {
        const newUser = new User({
            email: userEmail,
            locations: [],
    });
    const savedUser = await newUser.save();
    console.log('new user added')
    res.send([]);
    }

})


app.get('/addNewCard/:email',async function(req,res){
    const user = await User.findOne({ email: req.params.email });
    user.locations.push('Select Location');
    await user.save();
    res.send(`new card added for user ${req.params.email}`)
})


app.get('/removeCard/:email/:index',async function(req,res){
    const email = req.params.email
    const index = parseInt(req.params.index)
    console.log(email,index)
    const user = await User.findOne({ email: email });
    user.locations.splice(index, 1);
    await user.save();
    res.send(`card ${index} was removed from email: ${email}`)
})


app.get('/removeCard/:email/:index/:newLocationName',async function(req,res){
    const email = req.params.email
    const index = parseInt(req.params.index)
    const newLocationName = req.params.newLocationName

    const user = await User.findOne({ email: email });
    user.locations[index] = newLocationName;
    await user.save();
    res.send(`card ${index} name was changed for: ${newLocationName}`)
})


app.listen('3005',function(){
    console.log('weather API running on 127.0.0.1:3005')
} )
