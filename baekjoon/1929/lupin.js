var a = prompt('입력');
var b = prompt('입력');

var results = new Array();



function getPrimeNumber(){

for (let i = a; i<=b;i++){
    if (a<0){break;}
    let isPrmeNumber = true;
    for(let j=a; j<b;j++){
        if(i&j===0){
            isPrimeNumber=false;
        }
    }
    if(isPrimeNumber){
        results.push(i);
    }
}
return results;
}