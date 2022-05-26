$(".myTicketsButton").click(function() {
    $("#DIV_13").css("display", "none");
    $("#DIV_256").css("display", "block");
    $("#DIV_241").css("display", "none");
    $(".profileButton").css("background", "transparent");
    $(".myTicketsButton").css("background", "rgb(238, 45, 55) none repeat scroll 0% 0% / auto padding-box border-box");
});
$(".profileButton").click(function() {
    $("#DIV_13").css("display", "block");
    $("#DIV_256").css("display", "none");
    $("#DIV_241").css("display", "none");
    $(".myTicketsButton").css("background", "transparent");
    $(".profileButton").css("background", "rgb(238, 45, 55) none repeat scroll 0% 0% / auto padding-box border-box");
});

$(".actually").click(function() {
    $("#DIV_241").css("display", "none");
    $("#cardWrap").css("display", "block");
    $(".booked").css("background", "transparent");
    $(".archive").css("background", "transparent");
    $(".actually").css("background", "rgb(238, 45, 55) none repeat scroll 0% 0% / auto padding-box border-box");
});
$(".booked").click(function() {
    $("#cardWrap").css("display", "block");
    $("#DIV_241").css("display", "none");
    $(".actually").css("background", "transparent");
    $(".archive").css("background", "transparent");
    $(".booked").css("background", "rgb(238, 45, 55) none repeat scroll 0% 0% / auto padding-box border-box");
});
$(".archive").click(function() {
    $("#cardWrap").css("display", "block");
    $("#DIV_241").css("display", "none");
    $(".actually").css("background", "transparent");
    $(".booked").css("background", "transparent");
    $(".archive").css("background", "rgb(238, 45, 55) none repeat scroll 0% 0% / auto padding-box border-box");
});