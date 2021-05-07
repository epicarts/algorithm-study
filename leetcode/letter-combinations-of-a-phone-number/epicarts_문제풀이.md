# 문제 주소
* https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## 문제 접근 방법
1. 키와 알파벳을 dict형태로 저장을 한다.
2. dfs에서 모든 그래프를 탐색하도록한다. 탈출조건은 n가지 조합을 찾아내었을떄 이다. digits 의 길이.
3. "23" 일경우 처음에는 2, 다음에는 3을 찾아야한다. 인덱스 접근 방법으로 index변수를 사용하여 한단계 아래마다 i + 1 한다.
 