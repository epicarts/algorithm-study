# 문제 주소
https://programmers.co.kr/learn/courses/30/lessons/59041

## 문제 접근 방법
1. FROM: ANIMAL_INS 테이블에서
2. WHERE: 이름이 NULL 이 아닌 것들을 고르는데,
3. GORUP BY: 공톡적인 NAME 끼리 묶어서
4. HAVING: 그룹중에서 2 이상인 것들을 뽑아서,
5. SELECT: NAME 컬럼과 COUNT 라는 컬럼을 만드는데, COUNT 컬럼은 HAVING 에서 추출한 NAME 2 이상인 개수만 추출한다.
6. ORDER BY: 오름차순으로 이름을 정렬한다.
