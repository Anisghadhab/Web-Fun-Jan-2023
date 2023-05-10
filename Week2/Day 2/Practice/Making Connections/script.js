var Request = document.querySelector(".requests");
var Propic1 = document.querySelector("#PROPIC1");
var Propic2 = document.querySelector("#PROPIC2");

var x = -1;
function decrease1() {
    Request.innerText = 2 + x + "Connection Requests";
    x--;
    Propic1.remove();
}

function decrease2() {
    Request.innerText = 2 + x + "Connection Requests";
    x--;
    Propic2.remove();
}


var Connections = document.querySelector("#connections");
var Prof1 = document.querySelector("#prof1");
var Prof2 = document.querySelector("#prof2");
var Prof3 = document.querySelector("#prof3");
var Prof4 = document.querySelector("#prof4");



var y = 1;
function increase(elm1,elm2) {
    elm1.innerText = y + 500 + "Connetions";
    y++;
    elm2.remove();
    
} 
function dec(elm){
    elm.remove();
} 

var Change = document.querySelector('#Name');
function change(){
    Change.innerText='Anis Ghadhab';
}
