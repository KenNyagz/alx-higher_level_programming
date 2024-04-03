$(document).ready(function() {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    let movies = data.results;
    let $listMovies = $('ul#list_movies');
          
    $.each(movies, function(index, movie) {
      let $li = $('<li>').text(movie.title);
      $listMovies.append($li);
    });
  });
});
