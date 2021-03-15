# 문제 주소
https://leetcode.com/problems/remove-duplicate-letters/

## 문제 접근 방법
1. Counter를 이용하여 모든 값들의 개수를 센다.
2. 일단 스택에 넣고 본다.
3. c가 먼저 들어갔고, 다음 숫자로 b가 나왔다고 가정. 만약 c의 카운트가 0이면 c는 계속 유지된 상태로 b가 들어감
4. c의 카운터가 1이면, 다음에 넣으면 되므로, 기존의 c를 제거. => 넣음. 
5. while인 이유 [c, d]가 있고 둘의 카운트가 1개 이상씩 있을때 b가 온다면, stack 전체를 pop 해야하기 떄문.
  