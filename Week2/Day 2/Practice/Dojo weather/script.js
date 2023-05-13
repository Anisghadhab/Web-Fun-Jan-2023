function signal() {
    alert('Loading weather report...')
}

var cookies = document.querySelector('.cookies');
function dis() {
    cookies.remove()
}




var arrRightf = ["", "65°", "66°", "61°", "70°"];
var arrLeftf = ["", "75°", "80°", "69°", "78°"];
var arrRightd = ["", "18°", "19°", "16°", "21°"];
var arrLeftd = ["", "24°", "27°", "21°", "26°"];
var left1 = document.querySelector(".left1")
var left2 = document.querySelector(".left2")

function change() {
    if (left1.innerText == "24°") {
        for (var i = 1; i < 5; i++) {

            (document.querySelector(".right" + i)).innerText = arrRightf[i];
            console.log(document.querySelector(".right" + i));
            (document.querySelector(".left" + i)).innerText = arrLeftf[i];
            console.log(document.querySelector(".left" + i));
        }
    }
    else if (left1.innerText == "75°") {
        for (var i = 1; i < 5; i++) {
            (document.querySelector(".right" + i)).innerText = arrRightd[i];
            (document.querySelector(".left" + i)).innerText = arrLeftd[i];

        }
    }
}