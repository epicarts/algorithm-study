# 문제 주소
* https://leetcode.com/problems/group-anagrams/

## 문제 접근 방법
* 각 문자 안에 들은 문자들을 정렬하여 키로 나타낼 수 있다. 'cba' 의 경우 'abc'가 키가 된다.
* 'abc'를 딕셔너리의 키로 쓴다. defaultdict를 이용하면 오류없이 키로 쉽게 저장할 수 있다.
