# 문제 주소
https://www.acmicpc.net/problem/10871

## 문제 접근 방법
인풋값을 두개 받아들여 a는 최대 숫자 b는 b까지의 작은숫자를 받아내기 위한 설정값으로 생각하여 풀었다.

첫번째로는 1부터 a까지의 숫자 저장이다. 랜덤한 변수가 저장되게 설정을 하여 저장시킨뒤, 한번 출력을 해준다. 
그 후 b의 값까지의 작은숫자를 변수에서 찾아내 출력하였다.

### 코드
```javascript
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


```
### 시간복잡도


### 공간복잡도


