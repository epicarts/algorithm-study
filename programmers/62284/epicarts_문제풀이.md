# 문제 주소
https://programmers.co.kr/learn/courses/30/lessons/62284

## 문제 접근 방법

### 테이블 정보
- CART_PRODUCTS 테이블은 장바구니에 담긴 상품 정보를 담은 테이블입니다

### 문제 정리
- 데이터 분석 팀에서는 우유(Milk)와 요거트(Yogurt)를 동시에 구입한 장바구니가 있는지 알아보려 합니다. 우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회하는 SQL 문을 작성해주세요. 이때 결과는 장바구니의 아이디 순으로 나와야 합니다.

### 해결방법
1. 먼저 WHERE 을 사용해, 우유와 요거트를 먼저 조회한다.

```
CART_ID	    NAME
286	        Milk
286	        Yogurt
287	        Milk
448	        Milk
448	        Yogurt
578	        Milk
578	        Yogurt
636	        Milk
789	        Yogurt
830	        Yogurt
977	        Milk
977	        Yogurt
996	        Milk
1034    	Yogurt
1048    	Milk
1048    	Yogurt
```

2. CART_ID로 NAME을 카운트해서 묶어서 조회해보자.

```sql
SELECT CART_ID, COUNT(NAME)
FROM CART_PRODUCTS
WHERE NAME IN ('Milk', 'Yogurt') 
GROUP BY CART_ID
ORDER BY CART_ID
```

```
CART_ID	COUNT(NAME)
286	    2
287	    1
448	    3
578	    3
636	    1
789	    2
830	    3
977	    2
996	    1
1034	1
1048	3
```

3. 이제 COUNT가 2 이상인 값을 조회하면 될 듯하다. 하지만 잘 보면 이상한 점이 있다. 우리는 MILK, YOGURT를 WHERE 조건문을 이용해 조회했다. 
합이 3개 인것들도 있는데, 우유2개 요거트 1개 일 수도 있지만, 우유 3개 일 수도 있다.

4. 이름의 중복을 제거하자.

```sql
SELECT CART_ID, COUNT(DISTINCT NAME)
FROM CART_PRODUCTS
WHERE NAME IN ('Milk', 'Yogurt') 
GROUP BY CART_ID
ORDER BY CART_ID
```

```
CART_ID	COUNT(DISTINCT NAME)
286	    2
287	    1
448	    2
578	    2
636	    1
789	    1
830	    1
977	    2
996	    1
1034	1
1048	2
```


3. 그룹 조건과 HAVING 을 이용해서 조회한다.

4. 마지막으로 CART_ID 순으로 정렬한다.
