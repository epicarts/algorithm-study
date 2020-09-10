var a = prompt('입력');

var arrNumber = new Array();

while(arrNumber.length < a) {
    var n = rand(a); 
    if(!arrNumber.includes(n)){
      arrNumber.push(n);
    }
}


function rand(a) {
    return Math.floor(Math.random()*a)+1
}
document.write('<br>');

arrNumber.sort(function(a,b){
    return a-b;
});

