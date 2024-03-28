#!/usr/bin/node
const request = require('request');

async function fetchCharacters(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(error || new Error(`Failed to fetch characters from ${url}`));
      } else {
        resolve(JSON.parse(body).characters);
      }
    });
  });
}

async function printCharacters(characters) {
  for (const character of characters) {
    try {
      const response = await fetchCharacters(character);
      console.log(JSON.parse(response).name);
    } catch (error) {
      console.error(error);
    }
  }
}

(async () => {
  try {
    const filmId = process.argv[2];
    const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;
    const characters = await fetchCharacters(filmUrl);
    await printCharacters(characters);
  } catch (error) {
    console.error(error);
  }
})();
