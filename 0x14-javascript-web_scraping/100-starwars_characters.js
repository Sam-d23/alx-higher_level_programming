#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request.get(apiUrl + movieId, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    return;
  }

  try {
    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, function (error, response, body) {
        if (error) {
          console.error('Error:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Request failed with status code:', response.statusCode);
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
