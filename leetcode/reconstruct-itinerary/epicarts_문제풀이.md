# 문제 주소
https://leetcode.com/problems/reconstruct-itinerary/submissions/

## 문제 접근 방법
1. 알파벳 순서로 먼저 가야하기 때문에 정렬을 해놓는다. 
2. 이때 dict형태로 그래프를 만든다.
3. 갈 수 있는 곳을 제일 먼저 가도록 한다. 
4. 한번 방문할때마다 딕셔너리를 딕셔너리에 있는 값을 pop시킨다.
5. 어디상 갈 수 있는 키값이 없으면 종료.