function solution(s, n) {
    var answer = '';
    let arr=s.split('');
    let up=[];
    let down=[];
    for (let i='a'.charCodeAt(0);i<='z'.charCodeAt(0);i++){
        down.push(String.fromCharCode(i));
    }
    for (let i='A'.charCodeAt(0);i<='Z'.charCodeAt(0);i++){
        up.push(String.fromCharCode(i));
    }
    
    arr.map((e,i)=>{
        if(down.includes(e)){
            let index =down.indexOf(e);
            answer+=down[(index+n)%26];
        }
        if(up.includes(e)){
            let index =up.indexOf(e);
            answer+=up[(index+n)%26];
        }
        if(e===' '){
            answer+=' ';
        }
    });
    
    
    return answer;
}