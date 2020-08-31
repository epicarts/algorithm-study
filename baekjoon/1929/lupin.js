
var n = 3;
var m = 16;

function getPrimeNumber() {  

    var results = [];   
    
    for ( i = n; i <= m; i++) {


       var isPrimeNumber = true; 
       for (j = 2; j < i; j++) { 
      
         if (i % j === 0) {   
   
           isPrimeNumber = false;       
         }     
       }      
       if (isPrimeNumber==true) {
         results.push(i);
       }
    } return results;
  }
getPrimeNumber();
