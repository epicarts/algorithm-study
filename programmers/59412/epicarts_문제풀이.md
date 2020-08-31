# 문제 주소
https://programmers.co.kr/learn/courses/30/lessons/59412

## 문제 접근 방법
1. SELECT: HOUR 컬럼은 HOUR(DATETIME) 이렇게 쓸경우 시간만 추출되는데 이를 HOUR 로 선언하였다. COUNT로 개수를 뽑아내었다.
2. WHERE: 9:00 부터 19:59 까지 시간 중에서,
3. GORUP BY: SELCET 에서 만든 HOUR으로 그룹을 나누고,
4. ORDER BY: HOUR을 오름차순으로 정렬 후 조회하였다.