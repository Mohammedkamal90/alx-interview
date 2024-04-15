#!/usr/bin/node

const request = require('request');

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

// Check if the movie ID is provided
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// API endpoint for fetching movie details
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to make HTTP GET request to the API
const fetchData = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(`Failed to fetch data. Status: ${response.statusCode}`);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

// Function to fetch character names and print them
const fetchAndPrintCharacterNames = async () => {
  try {
    const movieDetails = await fetchData(apiUrl);
    const charactersUrls = movieDetails.characters;
    const characterPromises = charactersUrls.map(characterUrl => fetchData(characterUrl));
    const characterDetails = await Promise.all(characterPromises);
    const characterNames = characterDetails.map(character => character.name);
    console.log(characterNames.join('\n'));
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
};

// Call the function to fetch and print character names
fetchAndPrintCharacterNames();
