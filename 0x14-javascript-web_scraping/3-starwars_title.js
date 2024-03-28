#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred while making the request:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to fetch movie details. Status code:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    console.log('Title:', movieData.title);
  }
});
