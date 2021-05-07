# 문제 주소
* https://leetcode.com/problems/combination-sum/

## 문제 접근 방법
* dfs 탈출조건은 값이 더 커지거나, 정답이 나오거나,
* 수열의 경우 모든것을 다 도는 방식으로 가능. 조합이기 때문에 i + 1이지만, 여기에서는 자기자신을 한번더 
포함시켜야 하기 때문에 i 를 다음 인덱스로 넘김. 
* path + [candidates[i]] 리스트 더하기 연산이 됨.
