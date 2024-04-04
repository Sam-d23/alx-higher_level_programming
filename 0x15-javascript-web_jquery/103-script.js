$(document).ready(function() {
    $("#btn_translate, #language_code").on('click keypress', function(event) {
        // Check if the click event or keypress event is from ENTER key
        if (event.type === 'click' || (event.type === 'keypress' && event.which === 13)) {
            // Get the language code entered by the user
            var languageCode = $("#language_code").val();

            // Make a GET request to fetch the translation
            $.get("https://www.fourtonfish.com/hellosalut/hello/", { lang: languageCode }, function(data) {
                // Update the content of DIV#hello with the fetched translation
                $("#hello").text(data.hello);
            });
        }
    });
});
