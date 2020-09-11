# algorithm-study
> 알고리즘 스터디를 위한 저장소입니다.

## Programming Language 
* Java, C++, Python, JavaScript, SQL

## 알고리즘 사이트
* **baekjoon**: https://www.acmicpc.net/
* **programmers**: https://programmers.co.kr/learn/challenges
* **hackerrank**: https://www.hackerrank.com/
* **leetcode**: https://leetcode.com/
* **codeground**: https://www.codeground.org/about
* **synap**: http://euler.synap.co.kr/
* **topcoder**: https://www.topcoder.com/
* **algospot**: https://algospot.com/judge/problem/list/
* **swexpertacademy**: https://www.swexpertacademy.com/main/main.do
* **geeksforgeeks**: https://www.geeksforgeeks.org/
* **codeforces**: http://codeforces.com

## 폴더 구조
* 폴더 구조는 다음과 같다. 
    * 사이트 폴더 - 문제 폴더 - 소스코드 및 풀이방법 파일
        * 예) ```baekjoon ```폴더 -> ```1000``` 폴더 -> ```epicarts.py``` , ```epicarts_풀이방법.md```
    * 사이트 폴더: 누구나 사이트를 알아볼 수 있게 영어로 작성한다.
        * 예) ```baekjoon```, ```programmers```, ```codeground```
    * 문제 폴더: 숫자를 우선적으로 작성, 숫자가 없다면 영어로 작성한다.
        * ```1000```, ```1234```
    * 소스코드: 자신의 ```이름``` 혹은 ```아이디``` 뒤에 ```.확장자명```으로 작성한다.
        * ```epicarts.py```, ```epicarts.java```, ```epicarts.cpp```
    * 풀이방법: 자신의 ```이름``` 혹은 ```아이디``` 뒤에 ```.풀이방법.md``` 로 작성한다.
        * ```epicarts_풀이방법.md```


## Commit Rule
* Commit Rule은 다음을 참고한다
    * 브런치 생성: ```자기이름(혹은 아이디)_사이트_문제번호```
        * 예) ```epicarts_baekjoon_1000```를 브런치 이름으로 한다.
    * ```commit message```는 자유롭게 한다.

## ```파일이름.md``` Rule
* 각 문제별 ```파일이름.md``` Rule은  다음을 참고한다
    * **문제 주소**, **문제 접근 방법** 를 작성한다.
    * **문제 접근 방법** 은 되도록이면 구체적으로 작성한다.
    
## PullRequest(PR) Rule
* PR rule은 다음을 참고한다
    * 최소 2명이상 리뷰가 달릴 경우에 ```PR Merge```가 가능하다.
    * ```Pull request``` 제목 및 내용은 자유롭게 한다.
    * ```Merge``` 버튼은 2명이상이 리뷰 comment를 남겼을 때, 마지막 리뷰어가 누르는 것으로 한다. 단, 질문을 남겼을 경우 질문에 대한 답을 받고 ```Merge``` 해야한다.

## 스터디 Rule
> 일주일에 최소 한번이상 **Commit**하는 것을 규칙으로 한다.
* 개인이 할 일
    * 이론 정리   
        * 알고리즘 이론 내용을 간단히 정리한다.
    * 문제 풀이
        * 알고리즘 문제를 푼다.
        * 각자가 해당 코드의 좋은 예제를 찾아서 분석한다.
        * 각 문제 폴더 마다 ```파일이름.md``` Rule에 맞게 작성한다.
    * 공유 및 피드백
        1. 각자가 푼 문제에 대한 코드를 **브런치**를 따서 github에 push한 후 pull request를 날린다.
        2. 상대방의 코드를 확인한 후 **리뷰나 피드백**을 작성하면 된다.
        3. 만약 리뷰나 피드백할 의견이 없을 경우 **approve** 기능을 사용해 승인해주면 된다. 
        3. 두개 이상의 리뷰어가 **approve** 혹은 **리뷰나 피드백**을 작성하였을 경우, 해당하는 **브런치**를 ```Merge```한다.
* 스터디 모임에서 할 일
    * 이론 정리 공유
    * 문제를 풀 때 발생한 **리뷰 및 피드백** 에 대해 논의
    * 좋은 코드에 대한 분석 공유
    * 문제 및 스터디에 대한 회고

## 여기까지 읽었는데 커밋 방법을 잘 모르겠다면..
* 간단하게 [블로그](https://epicarts.tistory.com/98)를 참고하여 처음 연습해보기 바란다.

## 참고 사이트
* https://gmlwjd9405.github.io/2018/05/14/how-to-study-algorithms.html
* https://github.com/TheCopiens/algorithm-study
* https://github.com/WeareSoft/algorithm-study
