$(document).ready(function(){
    // Add event listener to the div with id "toggle_header"
    $("#toggle_header").click(function(){
        // Toggle the class "red" and "green" on the header element
        $("header").toggleClass("red green");
    });
});
