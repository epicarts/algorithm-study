function solution(s){
    var answer = true;

    var p=s.match(/p/ig);
    var y=s.match(/y/ig);
    if(p==null){
        p=0;
    }
    if(y==null){
        y=0;
    }
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