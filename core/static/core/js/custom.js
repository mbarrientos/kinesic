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
        scrollTop: $("#player").offset().top - 70
    }, 500);
});