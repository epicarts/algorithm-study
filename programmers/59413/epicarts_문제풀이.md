# 문제 주소
https://programmers.co.kr/learn/courses/30/lessons/59413

## 문제 접근 방법
- 잘 모르겠다. 프로그래머스 질문하기에 있는 답을 보고 제출하였다. 


```sql
SET @HOUR := -1;
```
@HOUR 에 -1이라는 값을 넣는다. 마치 변수 대입하듯이 생각하면 된다.

```sql
SELECT @HOUR := @HOUR + 1 AS HOUR, (
```
@HOUR의 값을 하나씩 증가시킨다. 컬럼 이름은 `HOUR` 이다.
처음 선언한 `@HOUR := -1` 과 `+ 1` 에 의해 `0` 부터 시작한다.


```sql
(
    SELECT COUNT(*) 
    FROM ANIMAL_OUTS 
    WHERE HOUR(DATETIME) = @HOUR
) AS COUNT
```

`( 생략 ) AS COUNT` 이므로 컬럼이름은 `COUNT`이다.
`()`를 보면 
1. SELECT: COUNT(*) 카운트 개수를 센다.
2. FROM: ANIMAL_OUTS 라는 테이블에서
3. WHERE: DATETIME의 컬럼을 시간으로 변환한 값을 `@HOUR`과 비교하는 조건문.

WHERE 이 없을경우 전체 행을 조회한다. 그러나 `WHERE`에 `@HOUR`이 라는 조건문이 있기 떄문에, `@HOUR`의 값에 맞는 조건을 가져온다. 

가령, `@HOUR = 13`일경우 DATETIME이 13인 있는 모든 조건들의 개수를 카운트한다.

```SQL
FROM ANIMAL_OUTS 
GROUP BY HOUR 
```
이를 HOUR 로 집계를 할 경우, 프로그래머스 테스트 실행창에서는 HOUR은 0 ~ 99까지 순서대로 행들이 생긴다.

```SQL
HAVING HOUR BETWEEN 0 AND 23
```
0 ~ 99 까지의 HOUR 컬럼들을 0 ~ 23까지만 출력하도록 한다.


## 회고
- 0 ~ 99까지 모든 컬럼을 조회한 뒤 이를 다시 HAVING절로 범위를 조건을 나누는건 별로 내키지 않는다.