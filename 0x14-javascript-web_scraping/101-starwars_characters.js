#!/usr/bin/node

const rp = require('request-promise-native');

async function getFilmCharacters(url) {
    try {
        const response = await rp(url);
        const filmData = JSON.parse(response);
        const characters = filmData.characters;
        for (const characterUrl of characters) {
            const characterResponse = await rp(characterUrl);
            const characterData = JSON.parse(characterResponse);
            console.log(characterData.name);
        }
    } catch (error) {
        console.error(error);
    }
}

const filmId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;
getFilmCharacters(filmUrl);
