// http-service.js
require('whatwg-fetch');

const httpUrl = 'http://127.0.0.1:3200/product'
// const httpUrl = 'https://www.boredapi.com/api/activity/'

class HttpService {
     getProducts = () => { 
            fetch(httpUrl)
            .then(res => {
                return res.json()
            }).then(json =>{
                console.log(json)
            })
    }
}


module.exports = HttpService;
