#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

// Make a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Unexpected response:', response.statusCode);
  } else {
    try {
      const films = JSON.parse(body).results;
      let numMoviesWithWedge = 0;

      for (const film of films) {
        const characters = film.characters;
        if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
          numMoviesWithWedge++;
        }
      }

      console.log('Number of movies with Wedge Antilles:', numMoviesWithWedge);
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  }
});
