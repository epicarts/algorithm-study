# 문제 주소
https://programmers.co.kr/learn/courses/30/lessons/42839

## 문제 접근 방법
1. itertools.permutations를 사용하여 모든 경우의 수(str형태)를 저장하였다. 1개일때, 2개일떄, n개일떄
2. 모든 str형태의 경우의 수를 int로 변환한 뒤, set을 이용해 중복을 제거하였다.
3. 구한 모든 경우의 수에 대해 소수판별을 하였다. (제곱근까지만 돌도록)
