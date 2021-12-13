const express = require('express')
const axios = require('axios')

const PORT = 3000

const app = express()

app.use(express.urlencoded({
    extended: false
}))
app.use(express.json())

app.post('/', async (req, res) => {
    const { word, type } = req.body

    let baseUrl = ""

    switch(type) {
        case "p":
            baseUrl = "http://localhost:3001"
            break;
        case "f":
            baseUrl = "http://localhost:3002"
            break;
        case "l":
            baseUrl = "http://localhost:3003"
            break;
        default:
            res.send({
                error: "Not found"
            })
            break;
    }
    
    try {
        const response = await axios.post(`${baseUrl}/${type}`, { word })
        res.send(response.data)
    } catch(err) {
        res.send(err)
    }
})

app.listen(PORT, () => {
    console.log(`Server listening at port: ${PORT}`)
})