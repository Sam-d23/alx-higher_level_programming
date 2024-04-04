$(document).ready(function(){
    // Add event listener to the div with id "update_header"
    $("#update_header").click(function(){
        // Update the text of the header element to "New Header!!!"
        $("header").text("New Header!!!");
    });
});
