백준 문제 풀이
=============
번호 2753
---------

> 주소 : https://www.acmicpc.net/problem/14681 <br>
> 언어 : JAVA 11

### 1. 문제 풀이

단순 문제로 if에 대한 처리를 삼항 연산자를 사용한 checkDimension 메소드를 만들어 해결함

<pre>
<code>
static public int checkDimension(int a,int b) {
		return (a>0 && b>0) ? 1 : ((a<0 && b>0) ? 2 : ((a<0 && b<0) ? 3 : 4));
	}
</code>
</pre>
