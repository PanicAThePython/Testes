const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const routes = require('./routes');

const app = express();
mongoose.connect('mongodb+srv://PanicAThePython:248703@cluster0-ufc8f.mongodb.net/week10?retryWrites=true&w=majority', {
    useUnifiedTopology: true,
    useNewUrlParser: true,
});
app.use(cors());
app.use(express.json()); //mostra pro express que estamos usando json, ele n interpreta sozinho
app.use(routes);//vem dps do aviso que é json


app.listen(3333);

