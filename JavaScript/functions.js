var x= 20;
var y= 30;

//function definition
function add_numbers(x, y){
    sum= x + y;
    return sum;
}

//calling the function
console.log(add_numbers(x,y));

var sum= 0;
var last= 50;

function sum_numbers(){
    for (var i= 0; i< last; i++);
    sum= sum+ i;

    return sum;
}

console.log(sum_numbers)
