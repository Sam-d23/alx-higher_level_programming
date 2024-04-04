$(document).ready(function(){
    // Fetch character name from the provided URL
    $.getJSON("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data){
        // Display the character name in the HTML tag with id "character"
        $("#character").text("Character Name: " + data.name);
    });
});
