# 문제 주소
https://leetcode.com/problems/number-of-islands/submissions/

## 문제 접근 방법
1. 기본적으로 모든 0,0 부터 n,n까지 배열의 반복문을 돈다.
2. 만약 섬일 경우 섬을 dfs로 전체 탐색을 진행한다. 섬을 방문했다는 증거로 1이 아닌 다른 값으로 바꾼다.
