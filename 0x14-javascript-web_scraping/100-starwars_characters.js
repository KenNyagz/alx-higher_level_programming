#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(url, (err, response, body) => {
  if (err) { return; }

  const films = JSON.parse(body);
  films.characters.forEach((characterUrl) => {
    request.get(characterUrl, (err, resp, body) => {
      if (err) { return; }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
  /* console.log(films.characters.length); */
});
