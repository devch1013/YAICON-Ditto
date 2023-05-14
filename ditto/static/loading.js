$(document).ready(function() {
    $('.loading').hide();
    $('#next').submit(function(){
        $('.loading').show();
        return true;
    });
});