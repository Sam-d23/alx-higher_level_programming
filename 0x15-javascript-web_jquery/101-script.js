$(document).ready(function() {
    // Add event listener for adding an item
    $("#add_item").click(function() {
        $("<li>").text("Item").appendTo("ul.my_list");
    });

    // Add event listener for removing the last item
    $("#remove_item").click(function() {
        $("ul.my_list li:last-child").remove();
    });

    // Add event listener for clearing the list
    $("#clear_list").click(function() {
        $("ul.my_list").empty();
    });
});
