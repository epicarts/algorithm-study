# 문제 주소
https://leetcode.com/problems/most-common-word/

## 문제 접근 방법
1. 정규식으로 띄어쓰기 단위로 단어문자만 남겨놓음. 소문자로 변경후 공백을 기준으로 split.
2. banned가 있ㅇ다면 words리스트에 넣지 않음.
3. collections를 사용하여 단어를 딕셔너리로 개수르 ㄹ셈.
4. 이후 가장 count가 큰 값을 반환.
 
