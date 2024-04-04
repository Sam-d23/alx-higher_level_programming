$(document).ready(function(){
    // Fetch the translation of "hello" in French
    $.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data){
        // Display the translation in the <div id="hello"></div> element
        $("#hello").text(data.hello);
    });
});
