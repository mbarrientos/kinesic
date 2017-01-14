/* Add your custom JavaScript code */

$("#bio-link").click(function(event) {
    event.preventDefault();
    $('html, body').animate({
        scrollTop: $("#bio").offset().top
    }, 500);
});

$("#player-link").click(function(event) {
    event.preventDefault();
    $('html, body').animate({
        scrollTop: $("#player").offset().top
    }, 500);
});

$("#gallery-link").click(function(event) {
    event.preventDefault();
    $('html, body').animate({
        scrollTop: $("#gallery").offset().top
    }, 500);
});