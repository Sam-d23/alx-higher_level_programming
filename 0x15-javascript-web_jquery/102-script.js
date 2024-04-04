$(document).ready(function() {
    $("#btn_translate").click(function() {
        // Get the language code entered by the user
        var languageCode = $("#language_code").val();

        // Make a GET request to fetch the translation
        $.get("https://www.fourtonfish.com/hellosalut/hello/", { lang: languageCode }, function(data) {
            // Update the content of DIV#hello with the fetched translation
            $("#hello").text(data.hello);
        });
    });
});
