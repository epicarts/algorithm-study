function solution(s){
    var answer = true;
    
    var p= s.match(/p/ig);
    var y=s.match(/y/ig);

    if(p.length==y.length){
        answer=true;
    }
    else{
        answer=false;
    }
    console.log(p);
    console.log(y);


   return answer;
}