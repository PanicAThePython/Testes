const axios = require('axios');
const Dev = require('../models/Dev');
const parseStringAsArray = require('../utils/parseStringAsArray');
//index - mostrar lista, show - mostra único, store - cria, update - atualiza, destroy - deleta
module.exports = {
    async index(request, response) { //busca todos os devs
        const devs = await Dev.find();
        return response.json(devs);
    },



    async store(request, response) { //cria um dev
        const { github_username, techs, latitude, longitude } = request.body;
    
        let dev = await Dev.findOne({github_username});

        if (!dev){
            const apiResponse = await axios.get(`https://api.github.com/users/${github_username}`);
        
            const { name = login, avatar_url, bio } = apiResponse.data;
            
            //if (!name) {
            //    name = apiResponse.login;
            //}
        
            const techsArray = parseStringAsArray(techs); //split tira a virgula e trim tira os espaços
        
            const location = {
                type: 'Point', 
                coordinates: [longitude, latitude],
            };
        
            dev = await Dev.create({
                github_username,
                name,
                avatar_url, 
                bio,
                techs: techsArray,
                location,
            });

        }

        
      
        return response.json(dev);
    }
};