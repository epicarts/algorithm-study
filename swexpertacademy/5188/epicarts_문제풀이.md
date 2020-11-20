# 문제 주소
https://swexpertacademy.com/
5188문제 - 최소

## 문제 접근 방법
- 왼쪽에서 시작하여 오른쪽, 혹은 아래로만 움직인다.
- dfs함수를 만들어 하나씩 방문을 한다.
- 먼저 dfs 들어갔을떄, 이 배열이 마지막인지 아닌지 검사를 한다. 또한 시간 단축을 위해 기존의 저장된 값이 있을경우 가차없이 반환한다.
- 방향을 한칸씩 증가시키는데 이떄 for range 문을 이용한다. 이떄 의 range 값은 방향의 개수이다.(아래 오른쪽 range(2))
- 배열에서 배열크기를 초과할 경우 dfs로 들어가지 않고, 초과되지 않을경우 계속해서 들어가게 된다.

## 참고코
- https://tothefullest08.github.io/php/2020/02/03/Cleancode17-dip/
- https://rhdtka21.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-SW-Expert-Academy-%EC%B5%9C%EC%86%8C%ED%95%A9
