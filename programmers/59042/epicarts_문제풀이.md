# 문제 주소
https://programmers.co.kr/learn/courses/30/lessons/59042

## 문제 접근 방법

### 테이블 정보
- ANIMAL_OUTS 테이블은 입양보낸 동물의 정보를 담은 테이블
- ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블


### 문제 정리
- ANIMAL_OUTS 테이블의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID의 외래 키이다.
- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
- 즉, ANIMAL_OUTS에 기록은 있으나, ANIMAL_INS에는 기록이 없음. 유실된 데이터를 찾아아야함.

### 해결방법
- 두개의 테이블을 조인하였을 때, ANIMAL_INS에는 없는 동물들을 ANIMAL_OUTS에서 찾으면 댐.
- SELECT : ANIMAL_OUTS에 데이터가 있으므로, AO를 조회해야함.
- FROM: ANIMAL_OUTS을 기준 테이블로 놓고(왼쪽에 위치).
- LEFT JOIN: 왼쪽에 있는 테이블(ANIMAL_OUTS)과 겹친 테이블(ANIMAL_OUTS과 ANIMAL_INS의 교집합)을 조회함. 
- 여기까지 진행했을 경우 ANIMA_INS와 ANIMAL_OUTS 의 아이디의 교집합 및  ANIMAL_OUTS에 만 있는 값이 생기게됨. 
- WHERE: 둘이서 JOIN 되기 전에 WHERE 조건을 이용해 ANIMAL_INS 아이디가 NULL 인 것만 조회함. 즉, ANIMAL_INS의 ID가 없는, ANIMAL_OUTS만 조회 됨.
