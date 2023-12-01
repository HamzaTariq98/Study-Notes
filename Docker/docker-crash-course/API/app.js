const express = require('express')
const cors = require('cors')

const app = express()

app.use(cors())

app.get('/', (req, res) => {
  res.json([
    {
      "id":"1",
      "title":"Book Review: The Bear & The Nightingale"
    },
    {
      "id":"888asda8",
      "title":"Game Review: Pokemon Brillian Diamondsadfasdfasdf"
    },
    {
      "id":"3",
      "title":"Show Review: Alice in Borderland"
    },
    {
      "id":"hamza",
      "title":"AAAAAAAAAAAAAAAAAH"
    }   

  ])
})

app.listen(4000, () => {
  console.log('listening for requests on port 4000')
})