/**
 * Created by elliot on 6/27/16.
 */



$( document ).ready(function() {
      $("#text").keyup(function (e) {
            if (e.keyCode == 13) {
        var input = $("#text").val();
        console.log(input);
        $( "#test" ).prepend("<p>"+input+"</p>");
        }
        });
    $("#button").click({'tag': 11}, function (e) {
        var input = $("#text").val();
        console.log(input);
        $( "#test" ).prepend("<p>"+input+"</p>");
    });
});
