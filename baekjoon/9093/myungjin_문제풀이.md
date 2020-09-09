# 문제 주소
---
https://www.acmicpc.net/problem/9093

## 문제 접근 방법
- 지금까지 배운 자료구조를 이용하여 최대한 공간복잡도(?)를 줄이려고 노력하였다.

    *현재 링크드리스트와 스택가지 공부했다*

- array를 사용하지 않고 stack형태의 list의 구조로 사용한 이유는 잉여 메모리를 줄이려고 했기 때문이다.

## 전체 함수 구조

---

### main

```
1. [입력] : test case 
2. test case만큼 [반복]
    1. [입력] : a string
    2. 입력받은 string을 거꾸로 출력
```

### 입력받은 string을 거꾸로 출력(함수명 : print_reverse_word)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/946f2a74-60a6-44e2-9d64-ecb3a808419b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/946f2a74-60a6-44e2-9d64-ecb3a808419b/Untitled.png)

```
1. 글자를 하나씩 읽음
    1. 글자가 문자일때(공백이 아닐때)
        - 해당 글자를 stack의 형태의 리스트에 push
    2. 글자가 공백일때
        - stack의 형태의 리스트에 있는 내용을 pop하며 출력
```

## 필요한 데이터 형

---

### 문자를 담는 노드

```c
typedef struct s_node
{
    char data;
    struct s_node *prev;
}   t_node;
```

### stack의 top을 가리키는 노드

```c
typedef struct s_word
{
    t_node *top;
}
```

# 결과

---

생각보다 효율적이지 않은 부분이 많은 듯 하다... 😭

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ac17b965-647f-4cbb-b606-c6f67535bb2a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ac17b965-647f-4cbb-b606-c6f67535bb2a/Untitled.png)

# 풀이

---

- 지금까지 배운 자료구조를 이용하여 최대한 공간복잡도(?)를 줄이려고 노력하였다.

    *현재 링크드리스트와 스택가지 공부했다*

- array를 사용하지 않고 stack형태의 list의 구조로 사용한 이유는 잉여 메모리를 줄이려고 했기 때문이다.

## 전체 함수 구조

---

### main

```
1. [입력] : test case 
2. test case만큼 [반복]
    1. [입력] : a string
    2. 입력받은 string을 거꾸로 출력
```

### 입력받은 string을 거꾸로 출력(함수명 : print_reverse_word)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/946f2a74-60a6-44e2-9d64-ecb3a808419b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/946f2a74-60a6-44e2-9d64-ecb3a808419b/Untitled.png)

```
1. 글자를 하나씩 읽음
    1. 글자가 문자일때(공백이 아닐때)
        - 해당 글자를 stack의 형태의 리스트에 push
    2. 글자가 공백일때
        - stack의 형태의 리스트에 있는 내용을 pop하며 출력
```

## 필요한 데이터 형

---

### 문자를 담는 노드

```c
typedef struct s_node
{
    char data;
    struct s_node *prev;
}   t_node;
```

### stack의 top을 가리키는 노드

```c
typedef struct s_word
{
    t_node *top;
}
```

# 결과

---

생각보다 효율적이지 않은 부분이 많은 듯 하다... 😭

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ac17b965-647f-4cbb-b606-c6f67535bb2a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ac17b965-647f-4cbb-b606-c6f67535bb2a/Untitled.png)
