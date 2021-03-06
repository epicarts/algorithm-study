# 문제 주소
* https://leetcode.com/problems/longest-palindromic-substring

## 문제 접근 방법
1. 홀수 펠린드롬과, 짝수 펠린드롬을 왼쪽에서부터 슬라이딩 윈도우로 찾는다.
2. 최대 값까지 돌아야한다. (1일때, 펠린드롭 길이가 최대일때는 예외)
3. expand에서 좌우로 한칸씩 늘려가면서 검사를 한다.
4. max 에 key값으로 len을 주면, len의 길이를 토대로 문자열만 리턴 시킬 수 있다.

