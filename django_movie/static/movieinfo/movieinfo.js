//
// $(".mybutton a").click(function () {
//     $(".mybutton a").css("background", "url(btn-bg2.png)");
//     $(".mybutton a").css("background-size", "cover");
//     $(this).css("background", "url(btn-bg1.png)");
//     $(this).css("background-size", "cover");
// });
$(".setTime").click(function (){
   localStorage.clear();
   const date = $(".dateTime").val();
   const movieName = $(".MovieTitle").text();
   const timeValue = $(this).find((".timeValue")).text();
   localStorage.setItem("MovieTime", timeValue);
   localStorage.setItem("MovieName", movieName);
   localStorage.setItem("MovieDate", date);
});