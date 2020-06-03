$(document).ready(function () {
    console.log('jQuery started')
    $(".image").click(function () {
        var img = $(this);
        var src = img.attr('style')
        src = src.substring(16)
        src = src.slice(0,-218)
        $("body").append("<div class='popup'>"+
           "<div class='popup_bg'>"+
           "<img src='"+src+"' class='popup_img' />"+
           "</div>");
        $(".popup").fadeIn(800);
        $(".popup_bg").click(function(){
            $(".popup").fadeOut(800);
            setTimeout(function(){
                $(".popup").remove();
            })
        })
    })
})