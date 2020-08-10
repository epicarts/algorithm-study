var a = prompt('입력');
var b = prompt('입력');

var arrNumber = new Array();
var printNumber = new Array();

while(arrNumber.length < a) {
    var n = rand(a); 
    if(!arrNumber.includes(n)){
      arrNumber.push(n);
    }
}

document.write(arrNumber.join(' '));

function rand(a) {
    return Math.floor(Math.random()*a)+1
}
document.write('<br>');


for(i=0;i<arrNumber.length;i++){
    if(arrNumber[i] < b){
        printNumber.push(arrNumber[i]);
    }
}
document.write(printNumber.join(' '));


