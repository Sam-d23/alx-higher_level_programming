$(document).ready(function(){
    // Fetch movie titles from the provided URL
    $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data){
        // Iterate over each movie and append its title to the unordered list
        $.each(data.results, function(index, movie){
            $("#list_movies").append("<li>" + movie.title + "</li>");
        });
    });
});
