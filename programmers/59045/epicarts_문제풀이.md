# 문제 주소
https://programmers.co.kr/learn/courses/30/lessons/59045

## 문제 접근 방법

### 테이블 정보
- ANIMAL_OUTS 테이블은 입양보낸 동물의 정보를 담은 테이블
- ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블

### 문제 정리
- 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.
- 보호소에 나갈 당시에 중성화 수술된 동물들을 찾으면 되는 문제입니다.

### 해결방법
1. 보호소에 나간 친구들을 조회, 그리고 보호소 안에 중성화가 안되어있던 친구들을 조회하는 쿼리를 먼저 작성합니다. 

```sql
SELECT AO.ANIMAL_ID, AO.ANIMAL_TYPE , AO.NAME, AO.SEX_UPON_OUTCOME, AI.SEX_UPON_INTAKE
FROM ANIMAL_OUTS AO 
LEFT JOIN ANIMAL_INS AI ON AO.ANIMAL_ID = AI.ANIMAL_ID
WHERE AI.SEX_UPON_INTAKE LIKE 'Intact%' 
ORDER BY AI.ANIMAL_ID
```

ANIMAL_ID	ANIMAL_TYPE	NAME	SEX_UPON_OUTCOME	SEX_UPON_INTAKE
A378353	Dog	Lyla	            Intact Female	    Intact Female
A379998	Dog	Disciple	        Intact Male	Intact Male
A382192	Dog	Maxwell 2	        Neutered Male	    Intact Male
A410330	Dog	Chewy	            Spayed Female	    Intact Female

2. 보호소 밖으로 나간 친구들을 중에 중성화하는 동물들을 조회하는 쿼리를 추가하여 작성합니다.

AND ( AO.SEX_UPON_OUTCOME LIKE 'Spayed%' OR AO.SEX_UPON_OUTCOME LIKE 'Neutered%')
