백준 문제 풀이
=============
번호 1110
---------

> 주소 : https://www.acmicpc.net/problem/1110 <br>
> 언어 : JAVA 11

<br>

## 1. 문제
<br>

### 문제
***
0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

### 입력
***
첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.

### 출력
***
첫째 줄에 N의 사이클 길이를 출력한다.
![image](https://user-images.githubusercontent.com/48428850/136309336-4add19a0-4d6b-4710-9cd6-d634693caf50.png)



## 2. 문제 풀기전 알고리즘 생각
```
26이 주어졌을때
n : 26    a : 2 , b : 6   temp : 2 + 6
"b" + "temp에서 1의 자리" => nextNum : 68

nextNum : 68   a : 6 , b : 8   temp : 6 + 8
"b" + "temp에서 1의 자리" => nextNum : 84

nextNum : 84   a : 8 , b : 4   temp : 8 + 4
"b" + "temp에서 1의 자리" => nextNum : 42

nextNum : 42   a : 4 , b : 2   temp : 4 + 2
"b" + "temp에서 1의 자리" => nextNum : 26


"횟수 : 4"

```

## 3. 문제 풀이방식

#### 3-1. 문자열과 정수를 활용한 방법(제일 길고 복잡)

파일 이름 : num1110.java

<pre>
<code>
    if(num<10) {
			str = "0"+ Integer.toString(num);
		} else {
			str = Integer.toString(num);
		}
		while(true) {
			
			a = Integer.parseInt(str.substring(0,1));
			b = Integer.parseInt(str.substring(1,2));
			
			if(a+b<10) {
				temp = "0"+ Integer.toString(a+b);
			} else {
				temp = Integer.toString(a+b);
			}
			str = Integer.toString(b) + temp.substring(1,2);
			
			i++;
			if(Integer.parseInt(str) == num) {
				System.out.println(i);
				break;
			} 
		}
</code>
</pre>

#### 3-2. 나누기와 나머지 연산자를 활용한 처리

파일 이름 : num1110_using_restOp.java

<pre>
<code>
    while(true) {
			if(calnum <10) {
				a = 0;
				b = calnum;
			} else {
				a = calnum / 10;
				b = calnum % 10;
			}
			calnum = a+b;
			i++;
			calnum = b*10 + calnum%10;
			if(calnum == num) {
				System.out.println(i);
				break;
			}
		}
</code>
</pre>

#### 3-3. 나누기와 나머지 연산자를 활용한 처리(발전 버전)
 
파일 이름 : num1110_using_restOp_better.java

<pre>
<code>
    while (true) {
			calnum = (calnum % 10) * 10 + (calnum / 10 + calnum % 10) % 10;
			i++;
			if (calnum == num) {
				System.out.println(i);
				break;
			}
		}
</code>
</pre>

## 4. 문제 소감

- 코드를 하나씩 발전 시켜가는 것에 성취감을 느꼈음. 버전 업이랄까
