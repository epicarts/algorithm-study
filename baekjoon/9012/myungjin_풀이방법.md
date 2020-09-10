# 문제 주소
https://www.acmicpc.net/problem/9012

## 문제 접근 방법

- 지금까지 배운 자료구조를 이용하여 최대한 공간복잡도(?)를 줄이려고 노력하였다.

    *현재 링크드리스트와 스택가지 공부했다*

- 9093번 문제 풀고 푸니까 매우 easy함 (비슷한 부분이 꽤있음)
- 때문에 대충 설계하고 코드로 짰다..

## 전체 함수 구조

### main

```
1. [입력] : test case 
2. test case만큼 [반복]
    1. [입력] : a string
    2. 괄호가 vsp 인지 확인하는 함수
			- vsp면 "YES" 출력
			- 아니면 "NO" 출력
```
### 괄호가 vsp 인지 확인하는 함수
```
1. [반복] 입력받은 문자를 한글자씩 읽음
    1. 문자가 '('이면
        - stack에 push
    2. 문자가 ')'이면
        1. 만약 stack 리스트에 아무것도 없는경우
            - over pop (return 0)
        2. stack 리스트에 내용이 존재하는 경우
            - stack에 pop
    3. 둘다 아니면
        - 무시
2. stack list가 비워져 있는 경우
    - 모든 stack이 정상적으로 빠져나간 것이므로  (return 1)
3. stack list에 노드가 남아있는 경우
    - 괄호가 제대로 안닫친게 있으므로 (return 0)
```

## 필요한 데이터 형

---

### 문자를 담는 노드

```c
typedef struct s_parenthesis
{
    struct s_parenthesis *prev;
}   t_parenthesis;
```

### stack의 top을 가리키는 노드

```c
typedef struct s_stack
{
    t_parenthesis *top;
}   t_stack;
```
## code
https://github.com/jungmyungjin/algorithm_baekjoon/blob/master/9012_parenthesis/main.c

## 결과
- 메모리 1116 KB
- 시간 0 ms
- 코드 길이 2064 B

무난하게 한것 같다 😁
