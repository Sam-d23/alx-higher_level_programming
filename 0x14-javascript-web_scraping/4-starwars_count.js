#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred while making the request:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to fetch movie details. Status code:', response.statusCode);
  } else {
    const filmsData = JSON.parse(body).results;
    const wedgeAntillesMovies = filmsData.filter(movie => movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log('Number of movies with Wedge Antilles:', wedgeAntillesMovies.length);
  }
});
