$(document).ready(function(){
    var results = $(".results").attr('data-result').split(',');
    console.log(results);
    if (results[0] == -1){
        console.log("too low");
        $(".results").html("<h1>Too Low!</h1>");
        $(".results").addClass("redalert");
    } else if (results[0] == 1) {
        console.log("too high");
        $(".results").html("<h1>Too High!</h1>");
        $(".results").addClass("redalert");
    } else if(results[0] == 2){
        console.log("Correct!");
        $(".results").addClass("greenalert");
        $(".results").html("<h1>" + results[1] + " was the number!</h1>");
        $(".results").append("<a href='/reset'><button>Play again!</button></a>")
        $("form").css("display","none");
    } else {
        console.log("Default");
        $(".results").html("");
    }
});
