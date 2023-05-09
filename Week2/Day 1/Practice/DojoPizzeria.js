function pizzaOven(crustType,sauceType,cheeses,toppings){
    var pizza={};
    pizza.crustType=crustType;
    pizza.sauceType=sauceType;
    pizza.cheeses=cheeses;
    pizza.toppings=toppings;
    console.log(pizza)
    return pizza
}

var pizzaA = pizzaOven("deep dish","traditional","mozzarella",["pepperoni", "sausage"])
console.log(pizzaA)

function pizzaOven(crustType,sauceType,cheeses,toppings){
    var pizza={};
    pizza.crustType=crustType;
    pizza.sauceType=sauceType;
    pizza.cheeses=cheeses;
    pizza.toppings=toppings;
    return pizza
}

var pizza1 = pizzaOven("hand tossed","marinara",["mozzarella", "feta"],["mushrooms", "olives", "onions"])
console.log(pizza1);


var pizza2 =  pizzaOven("fine","rosé","mozzarella",["basilico", "olives", "tomato"]);
console.log(pizza2);

var pizza3 =  pizzaOven("double","blache","gruyere","olive oil");
console.log(pizza3);

var pizza = {
    "crustType": ["hand tossed", "fine", "double"],
    "sauceType": ["marinara", "rosé", "blache"],
    "cheeses": ["mozzarella", "feta", "gruyere"],
    "toppings": ["mushrooms", "olives", "onions", "olive oil", "basilico", "tomato"],
};

    var crustType = ["hand tossed", "fine", "double"];
    var sauceType = ["marinara", "rosé", "blache"];
    var cheeses = ["mozzarella", "feta", "gruyere"];
    var toppings = ["mushrooms", "olives", "onions", "olive oil", "basilico", "tomato"];


function random(element) {
    var x = Math.random()*element.length-1;
    // console.log(x);
    var number = Math.ceil(x);

    // console.log(element.length);
    console.log(number)
    return number;
    
}



function randomPizza() {
    var pizzaR = {};
    pizzaR.crustType = crustType[random(crustType)];
    pizzaR.sauceType = sauceType[random(sauceType)];
    pizzaR.cheeses = cheeses[random(cheeses)];
    pizzaR.toppings = toppings[random(toppings)];
    // console.log(pizzaR);
    return pizzaR;
}
var resulat = randomPizza();
console.log(resulat)