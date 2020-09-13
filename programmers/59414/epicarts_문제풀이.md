# 문제 주소
https://programmers.co.kr/learn/courses/30/lessons/59414

## 문제 접근 방법

### 테이블 정보
- ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블

### 문제 정리
- ANIMAL_INS 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디와 이름, 들어온 날짜를 조회하는 SQL문을 작성해주세요. 이때 결과는 아이디 순으로 조회해야 합니다.

### 해결방법
1. 2018-01-22 와 같은 순으로 조회되어야한다.
2. DATE_FORMAT을 이용한다. https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html
2. 아이디 순으로 정렬한다.