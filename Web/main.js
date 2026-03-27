function message(){
    alert("Hello from Mwega");
}

var fnumber, snumber, sumnumbers ;
function add(fnumber, snumber){
    sumnumbers =fnumber + snumber;
    return sumnumbers;
};

function changeText()
{
    var btn= document.getElementById("myBtn");
    var span= document.getElementById("output");
    var textbox= document.getElementById("textbox");

   textbox.style.color= "red"
}