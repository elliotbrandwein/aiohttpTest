/**
 * Created by elliot on 6/27/16.
 */

$( document ).ready(function() {
  // Handler for .ready() called.
});

function Send() {
    var input = $("#text").val();
    console.log(input);
    $( "#test" ).prepend("<p>"+input+"</p>");
}

