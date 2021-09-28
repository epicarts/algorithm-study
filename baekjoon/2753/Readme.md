백준 문제 풀이
=============
번호 2753
---------

> 주소 : https://www.acmicpc.net/problem/2753
> 언어 : JAVA 11

### 1. 문제 풀이
두개의 풀이 방식을 선택해서 속도를 비교해보고 싶었음.
 - 삼항 연산 방식
<pre>
<code>
System.out.println((A%4==0) ? (A%100!=0 || A%400 ==0 ? 1 : 0) : 0);
</code>
</pre>

 - 람다식
<pre>
<code>
if (IntStream.of(A).filter(i -> i % 4 == 0).filter(i -> i % 100 != 0 || i % 400 == 0).sum() > 0) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
</code>
</pre>


### 2. 속도 비교
- 절대적인 수치는 아니겠지만 구조가 복잡해서 인지 람다식이 미묘하게 더 느렸음. 
- 위가 람다, 아래가 삼항 연산

![김경한 아래가 일반 if 위에는 람다 if](https://user-images.githubusercontent.com/48428850/135041573-7a775237-4474-49b3-8a81-fae946f4fc90.png)

### 3. 참조링크
<https://khj93.tistory.com/entry/JAVA-%EB%9E%8C%EB%8B%A4%EC%8B%9DRambda%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B4%EA%B3%A0-%EC%82%AC%EC%9A%A9%EB%B2%95>
